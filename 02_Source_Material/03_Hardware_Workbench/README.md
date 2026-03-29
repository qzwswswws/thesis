# Hardware Workbench

本目录用于集中存放第三章相关的硬件源码、设计导出物、器件清单、协议说明和界面素材，避免长期资料继续堆积在 `00_AI_Management/Input_Buffer` 中。

## 目录结构

- `swkd/`
  - 固件与上位机源码仓库

- `01_Design_Exports/`
  - `Schematics/`
    - 整机原理图导出
    - `Crops/` 中存放脑电前端、主控等局部截图
  - `PCB_Layout/`
    - PCB 顶底层截图
    - `Auto_Annotation/` 中存放自动位号图 PDF
  - `3D_Models/`
    - 3D 预览图
    - STEP 三维模型

- `02_Datasheets/`
  - 关键芯片数据手册

- `03_Protocol_and_Debug_Notes/`
  - BLE 协议说明
  - 吞吐、线程安全与实现优化记录

- `04_UI_Assets/`
  - 上位机界面截图

- `05_Component_Lists/`
  - BOM 与器件清单

- `06_Imported_Packages/`
  - 原始压缩包等导入文件

## 当前核心文件

- 原理图：[`01_Design_Exports/Schematics/SCH_Schematic1_2026-03-29.pdf`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/Schematics/SCH_Schematic1_2026-03-29.pdf)
- 前端局部图：[`01_Design_Exports/Schematics/Crops/Front_End_Schematic.png`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/Schematics/Crops/Front_End_Schematic.png)
- 主控局部图：[`01_Design_Exports/Schematics/Crops/Main_Control_Schematic.png`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/Schematics/Crops/Main_Control_Schematic.png)
- PCB 顶层图：[`01_Design_Exports/PCB_Layout/PCB_Top_View.png`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/PCB_Top_View.png)
- PCB 底层图：[`01_Design_Exports/PCB_Layout/PCB_Bottom_View.png`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/PCB_Bottom_View.png)
- 自动位号图：[`01_Design_Exports/PCB_Layout/Auto_Annotation/PCB_Top_Reference_Designators.pdf`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/Auto_Annotation/PCB_Top_Reference_Designators.pdf) ，[`01_Design_Exports/PCB_Layout/Auto_Annotation/PCB_Bottom_Reference_Designators.pdf`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/PCB_Layout/Auto_Annotation/PCB_Bottom_Reference_Designators.pdf)
- 3D 模型：[`01_Design_Exports/3D_Models/PCB_Board_3D_Model.step`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/01_Design_Exports/3D_Models/PCB_Board_3D_Model.step)
- BOM：[`05_Component_Lists/BOM_Board1_PCB1_2026-03-29.xlsx`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/05_Component_Lists/BOM_Board1_PCB1_2026-03-29.xlsx)
- 协议说明：[`03_Protocol_and_Debug_Notes/BLE_Protocol.md`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/03_Protocol_and_Debug_Notes/BLE_Protocol.md)
- 界面截图：[`04_UI_Assets/Desktop_UI_Screenshot.png`](/C:/Users/qzwsw/Documents/thesis/02_Source_Material/03_Hardware_Workbench/04_UI_Assets/Desktop_UI_Screenshot.png)
