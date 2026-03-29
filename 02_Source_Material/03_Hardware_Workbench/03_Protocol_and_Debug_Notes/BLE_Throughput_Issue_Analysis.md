# BLE数据传输速率问题分析

## 问题现象

### Qt应用端（每秒帧数）
- **实际帧率**：5-15帧/秒
- **预期帧率**：
  - MTU=23时：250帧/秒（每帧2样本，500Hz采样率）
  - MTU=247时：50帧/秒（每帧10样本，500Hz采样率）
- **帧率损失**：约95-98%

### 固件端（RTT日志）
- **采样正常**：500Hz采样率正常
- **NUS错误**：`NUSerr:NM=0 IV=57 OT=0`
  - `IV=57`：57次 `-EINVAL` 错误（notify未启用或连接问题）
  - `NM=0`：无内存错误（TX buffer未满）
- **MTU状态**：**未看到 "MTU updated" 日志**，说明MTU交换未成功
- **批次大小**：可能仍在使用默认值（2或3）

## 根本原因分析

### 1. MTU交换未成功 ⚠️ **关键问题**
- **Qt端**：移除了 `requestMtu(247)` 调用（因为API不可用）
- **结果**：MTU仍为默认23字节
- **影响**：只能发送小数据包（19字节/帧，2样本/帧）

### 2. Notify可能未正确启用 ⚠️ **关键问题**
- **固件端**：57次 `-EINVAL` 错误
- **可能原因**：
  - Qt端notify订阅失败
  - 订阅时机不对（在服务发现完成前）
  - 描述符写入失败

### 3. 数据传输瓶颈
- **当前状态**：即使MTU=23，也应该有250帧/秒
- **实际状态**：只有5-15帧/秒
- **说明**：主要问题不在MTU大小，而在notify或连接状态

## 解决方案

### 方案1：修复Notify订阅（优先）

#### 检查点1：确认notify订阅成功
在 `blerx.cpp` 的 `subscribeNotifications()` 中添加确认：

```cpp
void BleReceiver::subscribeNotifications()
{
    if (m_service) {
        const auto chars = m_service->characteristics();
        for (const auto &c : chars) {
            if (c.uuid() == m_txUuid) {
                m_notifyChar = c;
                auto desc = c.descriptor(QBluetoothUuid::DescriptorType::ClientCharacteristicConfiguration);
                if (desc.isValid()) {
                    // 检查是否已启用
                    QLowEnergyDescriptor::DescriptorType type = desc.type();
                    qDebug() << "Writing notify descriptor, current value:" << desc.value().toHex();
                    
                    m_service->writeDescriptor(desc, QByteArray::fromHex("0100")); // enable notify
                    emit statusMessage(QStringLiteral("已订阅 NUS 通知"));
                    qDebug() << "Notify descriptor write requested";
                } else {
                    qDebug() << "ERROR: Notify descriptor not found!";
                    emit statusMessage(QStringLiteral("错误：未找到通知描述符"));
                }
                break;
            }
        }
    }
}
```

#### 检查点2：监听描述符写入结果
添加描述符写入完成的信号处理：

```cpp
connect(m_service, &QLowEnergyService::descriptorWritten,
        this, [this](const QLowEnergyDescriptor &desc, const QByteArray &value) {
    qDebug() << "Descriptor written:" << desc.uuid().toString() 
             << "value:" << value.toHex();
    if (desc.uuid() == QBluetoothUuid::DescriptorType::ClientCharacteristicConfiguration) {
        emit statusMessage(QStringLiteral("通知已启用"));
    }
});
```

### 方案2：尝试其他方式请求MTU

#### 选项A：使用Qt 6的API（如果可用）
```cpp
#if QT_VERSION >= QT_VERSION_CHECK(6, 2, 0)
    // Qt 6.2+ 可能有不同的API
    if (m_controller->mtu() < 247) {
        // 尝试其他方式
    }
#endif
```

#### 选项B：在服务发现后延迟请求
```cpp
void BleReceiver::onServiceStateChanged(QLowEnergyService::ServiceState state)
{
    if (state == QLowEnergyService::ServiceDiscovered && svc == m_service) {
        emit statusMessage(QStringLiteral("NUS 服务已就绪，订阅通知"));
        subscribeNotifications();
        
        // 延迟后检查MTU
        QTimer::singleShot(500, this, [this]() {
            int currentMtu = m_controller->mtu();
            qDebug() << "Current MTU:" << currentMtu;
            if (currentMtu < 100) {
                emit statusMessage(QStringLiteral("警告：MTU较小(%1)，可能影响传输速率").arg(currentMtu));
            }
        });
    }
}
```

### 方案3：固件端优化（临时方案）

如果MTU交换无法成功，可以：
1. **降低批次大小到2**（确保不超过23字节MTU）
2. **增加发送频率**（减少延迟）

在 `main.c` 中确保：
```c
// 连接时初始化为2
nus_batch_size = 2;  // 确保不超过MTU=23的限制

// 如果MTU回调未触发，保持批次大小为2
```

## 诊断步骤

### 1. 检查Notify状态
- [ ] Qt端日志是否显示"已订阅 NUS 通知"？
- [ ] 是否有描述符写入成功的日志？
- [ ] 固件端 `-EINVAL` 错误是否减少？

### 2. 检查MTU状态
- [ ] Qt端是否收到 `mtuChanged` 信号？
- [ ] 固件端RTT日志是否有 "MTU updated" 消息？
- [ ] 当前MTU值是多少？

### 3. 检查数据传输
- [ ] 固件端统计：`NUSerr:NM=X IV=Y OT=Z` 中IV是否减少？
- [ ] Qt端帧率是否提升？
- [ ] 数据是否连续（无长时间间隔）？

## 预期结果

### 修复后应该看到：
1. **固件端**：
   - `MTU updated: TX=247 RX=247, batch_size=10`（如果MTU交换成功）
   - 或 `NUSerr:NM=0 IV=0 OT=0`（notify正常）
   - 发送频率：50帧/秒（MTU=247）或250帧/秒（MTU=23）

2. **Qt端**：
   - `MTU已更新: 247`（如果MTU交换成功）
   - `[BLE] parseFrame avg X ms over 50-250 frames in 1000 ms`
   - 连续的数据接收，无长时间间隔

## 临时解决方案

如果无法立即修复，可以：
1. **接受低帧率**：5-15帧/秒可能足够某些应用
2. **降低采样率**：从500Hz降到250Hz，减少数据量
3. **使用固定批次大小2**：确保不超过MTU限制

