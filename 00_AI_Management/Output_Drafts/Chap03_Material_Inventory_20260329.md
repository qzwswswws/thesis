# 第三章材料整理清单（基于 2026-03-29 已归档硬件资料）

## 1. 总体结论

截至目前，第三章所需材料已经从“仅靠源码可写”提升到“具备电路、PCB、BOM、协议和界面证据，可正式起草硬件系统章节”。原先暂存于 `00_AI_Management/Input_Buffer` 的主要硬件资料现已归整到 `02_Source_Material/03_Hardware_Workbench/`。

尤其是以下几类关键材料已经补齐：

- 原理图
- PCB 顶底层图
- 3D 结构预览
- 局部电路图（前端、主控）
- BOM 器件清单
- BLE 协议说明
- 上位机界面截图

这意味着第三章中的以下部分都已经具备较好的写作基础：

- 硬件系统总体架构设计
- 核心硬件电路设计
- 接口协议设计
- 固件程序开发与流程设计
- 上位机软件设计

## 2. 当前已收集材料总表

### 2.1 硬件设计类

- [SCH_Schematic1_2026-03-29.pdf](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/Schematics/SCH_Schematic1_2026-03-29.pdf)
  - 整机原理图
  - 用途：第三章“核心硬件电路设计”的主证据

- [Front_End_Schematic.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/Schematics/Crops/Front_End_Schematic.png)
  - 分辨率：`1428 x 689`
  - 推测为脑电前端局部原理图或截图
  - 用途：可作为“脑电采集前端电路”配图候选

- [Main_Control_Schematic.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/Schematics/Crops/Main_Control_Schematic.png)
  - 分辨率：`1394 x 641`
  - 推测为主控/无线/电源相关局部图
  - 用途：可作为“主控与无线传输电路”配图候选

- [PCB_Top_View.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/PCB_Top_View.png)
  - 分辨率：`465 x 261`
  - 用途：可作为 PCB 总览图，但分辨率偏低

- [PCB_Bottom_View.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/PCB_Bottom_View.png)
  - 分辨率：`501 x 311`
  - 用途：可作为 PCB 总览图，但分辨率偏低

- [3D_Top_View.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/3D_Models/3D_Top_View.png)
  - 分辨率：`897 x 567`
  - 用途：整机结构展示

- [3D_Bottom_View.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/3D_Models/3D_Bottom_View.png)
  - 分辨率：`882 x 510`
  - 用途：整机结构展示

- [PCB_Board_3D_Model.step](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/3D_Models/PCB_Board_3D_Model.step)
  - 用途：后续如需导出更高质量结构图，可以继续利用

- [PCB_PCB1_2026-03-29.zip](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/06_Imported_Packages/PCB_PCB1_2026-03-29.zip)
  - 包内导出内容已解压到：
    - [PCB_Top_Reference_Designators.pdf](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/Auto_Annotation/PCB_Top_Reference_Designators.pdf)
    - [PCB_Bottom_Reference_Designators.pdf](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/Auto_Annotation/PCB_Bottom_Reference_Designators.pdf)
  - 用途：可用于定位器件编号与版图说明

### 2.2 器件与选型类

- [BOM_Board1_PCB1_2026-03-29.xlsx](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/05_Component_Lists/BOM_Board1_PCB1_2026-03-29.xlsx)
  - 用途：第三章“关键器件选型”和“系统组成说明”的重要证据
  - 当前已能确认的关键器件包括：
    - `KS1092` 脑电前端
    - `NRF52832-QFAA-R` 主控与 BLE SoC
    - `RT9193-33GB-MS` 稳压器
    - `SLM4054` 充电管理
    - `TYPEC-304S-ACP16` Type-C 接口
    - `32MHz` 高频晶振
    - `32.768kHz` 低频晶振
    - `AFC01-S07FCA-00` FPC 连接器
    - `1.25-5P` / `1.25-2P` 接插件
    - `RFANT3216120A5T` 射频相关器件

- [Datasheet-KS109X-V1.1.4(2025A).pdf](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/02_Datasheets/Datasheet-KS109X-V1.1.4(2025A).pdf)
  - 用途：补充 KS1092 芯片说明与论文中的器件背景描述

- [datasheet-NRF52832.PDF](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/02_Datasheets/datasheet-NRF52832.PDF)
  - 用途：补充主控与 BLE 平台说明

### 2.3 协议与软件类

- [BLE_Protocol.md](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/03_Protocol_and_Debug_Notes/BLE_Protocol.md)
  - 用途：第三章“接口协议设计”的核心材料
  - 已明确内容包括：
    - NUS Service UUID
    - RX/TX Characteristic UUID
    - `0xE0` EEG 二进制帧魔数
    - 小端序传输
    - `ACK HR` / `ACK LDF` 文本消息
    - `GAIN / QUERY / FILTER / STATUS / STATS / RESET / QUERY HR` 命令体系

- [Desktop_UI_Screenshot.png](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/04_UI_Assets/Desktop_UI_Screenshot.png)
  - 分辨率：`1920 x 1140`
  - 用途：第三章“上位机软件设计”主配图

- [BLE_Throughput_Issue_Analysis.md](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/03_Protocol_and_Debug_Notes/BLE_Throughput_Issue_Analysis.md)
  - 用途：可提炼为“系统联调与速率优化分析”材料

- [Thread_Safety_Analysis.md](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/03_Protocol_and_Debug_Notes/Thread_Safety_Analysis.md)
  - 用途：可提炼为“固件线程安全设计”或“实现细节优化”说明

- [Solution_Implementation.md](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/03_Protocol_and_Debug_Notes/Solution_Implementation.md)
  - 用途：可提炼为“命令处理与线程同步优化”补充说明

## 3. 对第三章各小节的支撑关系

### 3.1 硬件系统总体架构设计

当前可直接使用的材料：

- `swkd` 源码中的系统模块信息
- 原理图 PDF
- `Front_End_Schematic.png`
- `Main_Control_Schematic.png`
- PCB 顶底层截图
- 3D 预览图

可写内容：

- 系统由脑电采集前端、主控与无线传输模块、电源管理模块、上位机软件组成
- 双通道 EEG 与 BLE 传输构成核心主线
- 系统同时具备基础生理信号采集扩展能力

### 3.2 核心硬件电路设计

当前可直接使用的材料：

- 原理图 PDF
- 前端局部图
- 主控局部图
- BOM
- KS1092 与 nRF52832 数据手册

可重点展开：

- KS1092 前端作用与双通道脑电采集链路
- nRF52832 主控的采样、控制与无线通信职责
- 供电与充电器件
- 晶振与接口配置
- Type-C 与外设连接形式

### 3.3 固件程序开发与流程设计

当前可直接使用的材料：

- `swkd/neurameter` 固件源码
- `THREAD_SAFETY_ANALYSIS.md`
- `SOLUTION_IMPLEMENTATION.md`
- `速率问题分析.md`

可重点展开：

- Zephyr 固件架构
- 500 Hz 双通道采样流程
- 环形缓冲区与 BLE 分帧传输
- 可配置增益与滤波
- 工作队列与线程安全优化

### 3.4 接口协议与上位机设计

当前可直接使用的材料：

- `BLE_Protocol.md`
- `swkd/nearalQT` 上位机源码
- 界面截图

可重点展开：

- NUS 服务与特征值设计
- EEG 数据帧与命令交互协议
- 上位机数据解析与可视化功能
- 实时波形、频带能量与设备状态界面

## 4. 目前最有价值的新增材料

如果只从“这次新增以后，第三章被明显补强了什么”来看，最关键的是以下五项：

1. `BOM_Board1_PCB1_2026-03-29.xlsx`
   - 让器件选型不再停留在源码推断层面

2. `SCH_Schematic1_2026-03-29.pdf`
   - 让电路设计章节真正有了硬件原始依据

3. `Front_End_Schematic.png`
   - 很适合单独支撑“脑电前端电路设计”小节

4. `Main_Control_Schematic.png`
   - 很适合单独支撑“主控与无线通信电路设计”小节

5. `3D_PCB1_2026-03-29.step`
   - 后续如果需要更高质量展示结构设计，潜力很高

## 5. 当前仍需注意的边界

### 5.1 还不宜直接写成定论的部分

- `MAX30102` 是否直接焊接在主板上，目前不能只凭源码下结论。
  - 原因：源码中存在心率血氧模块，但当前 BOM 共享字符串里未直接看到 `MAX30102` 字样。
  - 更稳妥的写法应是：
    - 系统支持基于 `MAX30102` 的心率/血氧采集扩展
    - 待结合原理图页和实物连接方式进一步确认其集成形式

- PCB 尺寸、板厚、层数等结构参数，目前材料中还未直接提取。
  - 若正文需要精确参数，最好后续从 EDA 中补一份尺寸信息。

### 5.2 当前图像分辨率需注意的部分

- `PCB_Top_View.png` 和 `PCB_Bottom_View.png` 分辨率偏低
  - 可以用于内部整理与草稿
  - 若正式进论文，建议后续导出更高清版本

## 6. 建议的论文配图方案

### 6.1 可直接考虑放入第三章的图片

- 图 3-1：系统总体架构图
  - 需要后续手工绘制或从现有材料整理

- 图 3-2：脑电前端电路图
  - 候选：`Front_End_Schematic.png`

- 图 3-3：主控与无线传输电路图
  - 候选：`Main_Control_Schematic.png`

- 图 3-4：PCB 三维结构图
  - 候选：`3D_Top_View.png` + `3D_Bottom_View.png`

- 图 3-5：上位机界面图
  - 候选：`Desktop_UI_Screenshot.png`

### 6.2 更适合做辅助说明或附录的图片

- PCB 顶底层总览图
- PCB 自动位号图 PDF

## 7. 对后续写作的直接建议

基于当前材料，第三章已经可以进入正式写作阶段，而且建议采用以下策略：

- 先以“便携式双通道脑电采集与无线传输系统”为主线
- 将心率/血氧采集写成系统扩展能力或辅助生理信号模块
- 把 `BOM + 原理图 + 源码 + 协议文档` 结合起来写，不再单靠源码推断
- 在未确认 `MAX30102` 物理集成方式前，避免写成“主板集成式血氧模块”这类过满表述

## 8. 现阶段仍建议补充的材料

虽然第三章已经可以写，但若想让这一章更完整，还建议补以下内容：

- 实物照片
- 佩戴状态图
- 板子尺寸信息
- 电池型号与容量
- 如方便，导出更高分辨率 PCB 顶底图

## 9. 最终判断

这批新增材料是有效且关键的，已经足以支持第三章起稿，并且能把原本偏“源码说明”的内容，升级成更标准的“硬件系统设计与实现”章节。

下一步最合理的动作就是：

- 先据此起草 `chap03.tex`
- 将暂时缺少精确参数的位置留为可后补项
- 等后续若补来实物照片和尺寸，再做第二轮增强
