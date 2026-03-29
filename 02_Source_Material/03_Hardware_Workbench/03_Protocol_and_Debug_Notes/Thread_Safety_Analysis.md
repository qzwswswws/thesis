# 固件崩溃问题分析

## 问题现象
- 上位机发送控制指令时固件崩溃
- LED指示灯卡在亮或灭状态（系统停止响应）

## 根本原因分析

### 1. **BLE回调上下文问题** ⚠️ 严重

**问题**：
- `nus_recv_cb()` 在BLE协议栈的回调中执行
- 在Zephyr中，BLE回调可能在**中断上下文**或**BLE工作队列**中执行
- 这是**非线程安全**的上下文，不能执行阻塞操作

**证据**：
```c
// main.c:233
static void nus_recv_cb(struct bt_conn *conn, const void *data, uint16_t len, void *ctx)
{
    // ... 直接调用命令处理函数
    handle_gain_command(cmd, cmd_len);  // ❌ 可能包含阻塞操作
}
```

### 2. **阻塞操作导致崩溃** ⚠️ 严重

**问题**：
在 `ks1092_write_reg()` 中使用了 `k_msleep(10)`，这在中断上下文中是**禁止的**：

```c
// ks1092.c:108-111
cs_low();
k_msleep(10);           // ❌ 中断上下文中不能休眠！
int ret = spi_write(...);
k_msleep(10);           // ❌ 中断上下文中不能休眠！
cs_high();
```

**影响**：
- 如果BLE回调在中断上下文中执行，调用 `k_msleep()` 会导致：
  - 看门狗超时（watchdog timeout）
  - 系统死锁
  - LED停止闪烁（系统停止响应）

### 3. **线程竞争条件** ⚠️ 中等

**问题**：
- `iir_filter_set_mode()` 直接修改 `filter_config[]` 数组（无锁）
- 主循环在 `ks_filter()` 中读取 `filter_config[]`
- 如果BLE回调和主循环同时访问，可能造成：
  - 数据不一致
  - 读取到部分更新的数据

```c
// iir_filter.c:139-140 (无锁访问)
filter_config[channel].mode = mode;        // 写入
filter_config[channel].enabled = enable;   // 写入

// main.c:395-396 (主循环读取)
float ch0_f = ks_filter((float)sample.ch0);  // 读取 filter_config[0]
float ch1_f = ks_filter1((float)sample.ch1); // 读取 filter_config[1]
```

### 4. **SPI操作安全性** ⚠️ 中等

**问题**：
- SPI写入操作可能需要获取SPI总线锁
- 在中断上下文中执行SPI操作可能导致死锁

## 解决方案

### 方案1：使用工作队列（推荐）✅

**原理**：
- 将命令处理从BLE回调延迟到工作队列
- 工作队列在系统工作队列线程中执行，可以安全地调用 `k_msleep()` 和SPI操作

**实现步骤**：
1. 在BLE回调中只保存命令数据到队列/缓冲区
2. 提交工作项到系统工作队列
3. 在工作队列的处理函数中执行实际的命令处理

### 方案2：使用互斥锁保护共享状态 ✅

**原理**：
- 使用 `k_mutex` 保护 `filter_config[]` 数组
- 确保读写操作的原子性

**实现步骤**：
1. 在 `iir_filter_set_mode()` 和 `iir_filter_get_mode()` 中加锁
2. 在 `ks_filter()` 和 `ks_filter1()` 中加锁读取
3. 注意：锁的粒度要小，避免长时间持有锁影响实时性

### 方案3：原子操作（仅适用于简单状态）⚠️

**适用场景**：
- 如果 `filter_config` 结构体足够小（通常<=8字节），可以使用原子操作
- 但 `filter_mode_t` 和 `bool` 组合可能不适合原子操作

## 推荐实现方案

**组合使用方案1和方案2**：
1. **工作队列**：解决阻塞操作问题
2. **互斥锁**：解决线程竞争问题

这样既能保证系统稳定性，又能保证数据一致性。
