# NeuraMeter 蓝牙数据传输协议说明

本文档详细说明了 NeuraMeter (脑电 EEG + 脉搏血氧 MAX30102) 设备与上位机（PC/移动端）之间的蓝牙通信协议。请使用本指南来开发兼容的其他上位机软件。

## 1. 基础蓝牙服务信息

NeuraMeter 采用 **Nordic UART Service (NUS)** 进行数据透传。

* **Service UUID**: `6e400001-b5a3-f393-e0a9-e50e24dcca9e`
* **RX Characteristic (PC -> 设备，写入)**: `6e400002-b5a3-f393-e0a9-e50e24dcca9e` (Write / Write Without Response)
* **TX Characteristic (设备 -> PC，通知)**: `6e400003-b5a3-f393-e0a9-e50e24dcca9e` (Notify)

> **注意**：上位机连接后，必须首先订阅 TX 通道的 `Notify` 才能接收到设备主动上传的数据。

---

## 2. 数据解析总则（TX 通道数据）

设备通过 TX 通道发送的数据分为 **两类**：
1. **二进制 EEG 连续数据帧**：包含高频采集的脑电波形数据。
2. **ASCII 文本消息**：包含命令执行的回应（ACK）、心率/血氧数据的上报、错误信息（ERR）等。

为解决粘包和类型冲突，协议在二进制帧的头部增加了一个固定魔数字节 `0xE0`。
**上位机解析的第一步逻辑**：检查收到的数据包的首个字节：
* 如果 `Packet[0] == 0xE0`：这是一个**二进制 EEG 数据帧**。
* 如果 `Packet[0]` 是 ASCII 可打印字符（如 `'A'`，即 `0x41`）：这是一个**ASCII 文本消息**。

---

## 3. 二进制 EEG 数据帧格式

当 `Packet[0] == 0xE0` 时，整个 Packet 的二进制结构如下（所有多字节整数均采用 **小端序 Little-Endian**）：

| 字段 | 长度 (Bytes) | 数据类型 | 说明 |
| :--- | :--- | :--- | :--- |
| **Magic** | 1 | `uint8_t` | 固定标识符：`0xE0` |
| **Sequence ID** | 2 | `uint16_t` | 包序号（0~65535 自增），用于上位机检测是否丢包 |
| **Sample Count (N)**| 1 | `uint8_t` | 本包内包含的 EEG 采样点集合数量，范围通常在 1~20 之间（由 MTU 决定）|
| **Samples Array** | N × 8 | 结构体数组 | 包含 N 个采样点数据的数组 |

### 采样点 (Sample) 数据格式（长度 8 字节）
每个 Sample 包含了两个通道的 ADC 值及时间戳：
| 字段 | 长度 (Bytes) | 数据类型 | 说明 |
| :--- | :--- | :--- | :--- |
| **Channel 0 ADC** | 2 | `int16_t` | 通道 0 原始 ADC 值 |
| **Channel 1 ADC** | 2 | `int16_t` | 通道 1 原始 ADC 值 |
| **Timestamp** | 4 | `uint32_t` | 设备端的内部系统时间戳（时钟滴答数） |

> **提示**：计算 EEG 数据帧总体预期长度的公式为：`4 + N * 8` 字节。上位机解析时，请先校验 `Packet.length >= 4`，读取 N 后再校验 `Packet.length >= 4 + N * 8`，以防越界。

---

## 4. ASCII 文本消息格式

非二进制的数据包为 UTF-8 编码的纯文本字符串，通常以 `ACK ` 或 `ERR ` 开头。

### 4.1 生理信号 (心率/血氧) 解析
心率/血氧数据由 MAX30102 提供，该模块约每 4 秒生成一次结果，会以文本格式主动上报。
* **报文格式**: `ACK HR <HeartRate> <SpO2> <HR_Valid> <SpO2_Valid>`
* **各字段含义**（以空格分隔）：
  * `<HeartRate>`: 心率值，单位 BPM（整数）
  * `<SpO2>`: 血氧饱和度，单位 %（整数）
  * `<HR_Valid>`: 心率值是否有效（1 为有效，0 为无效）
  * `<SpO2_Valid>`: 血氧值是否有效（1 为有效，0 为无效）
* **示例**: `ACK HR 75 98 1 1` 表示有效心率 75 BPM，有效血氧 98%。

### 4.2 电极脱落状态解析
当 EEG 芯片检测到电极触点状态发生变化时，会主动上报：
* **报文格式**: `ACK LDF <status>`
* **各字段含义**:
  * `<status>`: `1` 表示电极已脱落 (Lead-off)，`0` 表示电极接触正常。
* **示例**: `ACK LDF 1`

### 4.3 其他命令回执
* `ACK GAIN ...` : 回复增益查询或设置成功。
* `ACK FILTER ...` : 回复滤波配置查询或设置成功。
* `ACK STATUS ...`: 回复设备运行状态。
* `ERR <reason>`: 命令执行失败或无法识别命令。

---

## 5. 上位机发送命令（RX 通道数据）

上位机可通过写入 ASCII 文本的形式向设备发送控制命令：

| 命令分类 | 字符串形式 | 示例 / 说明 |
| :--- | :--- | :--- |
| **设置后端增益** | `GAIN <ch0> <ch1>` | `GAIN 540 1020` (各通道可接受值：360, 540...等)|
| **查询当前增益** | `QUERY GAIN` | 设备将回复 `ACK GAIN ...` |
| **设置滤波器** | `FILTER <ch> <mode> <en>` | `FILTER 0 3 1` (ch: 0或1; mode: 0~3; en: 1启用/0禁用)|
| **查询滤波配置** | `QUERY FILTER` | 设备将回复 `ACK FILTER ...` |
| **查询状态参数** | `QUERY STATUS` | 查询当前运行状态 |
| **查询硬件状态** | `QUERY STATS` | 查询底层统计信息 |
| **清空硬件缓存** | `CLEAR BUFFER` | 丢弃当前设备内的缓存数据 |
| **复位KS1092** | `RESET KS1092` | 重新对脑电前端芯片下发复位执行序列 |
| **主动查询心率** | `QUERY HR` | 设备将回复最新的 `ACK HR ...` |

## 6. 上位机解析伪代码参考

```python
def parse_bluetooth_packet(packet_bytes):
    if len(packet_bytes) == 0:
        return
        
    if packet_bytes[0] == 0xE0:
        # 1. 校验是 EEG 的二进制帧
        if len(packet_bytes) < 4:
            return  # 包不完整
            
        seq_id = struct.unpack('<H', packet_bytes[1:3])[0]
        count = packet_bytes[3]
        expected_len = 4 + count * 8
        
        if len(packet_bytes) >= expected_len:
            offset = 4
            for i in range(count):
                ch0, ch1, ts = struct.unpack('<hhI', packet_bytes[offset:offset+8])
                offset += 8
                # 抛出处理这一个 sample: handle_eeg_sample(ch0, ch1, ts)
    else:
        # 2. 文本消息帧
        text = packet_bytes.decode('utf-8').strip()
        
        if text.startswith("ACK HR "):
            # 处理心跳血氧  例如："ACK HR 75 98 1 1"
            parts = text[7:].split()
            if len(parts) >= 4:
                hr = int(parts[0])
                spo2 = int(parts[1])
                hr_valid = bool(int(parts[2]))
                spo2_valid = bool(int(parts[3]))
                # 抛出处理生理数据: handle_hr_spo2(hr, spo2, hr_valid, spo2_valid)
                
        elif text.startswith("ACK LDF "):
            # 处理电极脱离探测
            status = int(text[8:])
            is_lead_off = (status != 0)
            # handle_lead_off(is_lead_off)
            
        elif text.startswith("ACK ") or text.startswith("ERR "):
            # 记录处理其余普通的 ACK 返回与 INFO
            print("Command Response: ", text)
```
