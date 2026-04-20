# 第1章-第2章图片台账（2026-04-16）

## 用途

这份台账用于快速定位第 1 章与第 2 章当前正在使用的图片，避免后续在以下操作中出现混乱：

- 调整图片大小
- 挪动图片所属章节
- 删除或替换图片
- 修改图号、图注、引用来源
- 排查“图已删但正文还在引用”或“图片已存在但未编译显示”的问题

建议后续每次改图时，优先先看本表，再改 `chap01.tex` / `chap02.tex`。

## 当前正在使用的图片

| 章 | 图号 | 文件 | 当前插入位置 | 当前尺寸 | 图注 | 主要作用 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 第1章 | 图1.1 | `01_Thesis_LaTeX/figures/C1-1_BCI_system_and_apps.png` | `chap01.tex` 第 1.1 节开头 | `0.75\textwidth` | EEG-BCI系统的基本组成与典型应用场景示意 | 用于绪论起势，说明 EEG-BCI 的基本组成与应用价值 | `gu2021eeg` |
| 第1章 | 图1.2 | `01_Thesis_LaTeX/figures/C1-4_BCI_modes_and_metrics.png` | `chap01.tex` 第 1.1 节评价协议讨论后 | `0.8\linewidth` | 不同脑机接口使用模式下的系统组织差异 | 支撑“评价指标与使用模式相关，不能只看单一离线分数” | `Tho14` |
| 第1章 | 图1.3 | `01_Thesis_LaTeX/figures/C1-2_EEG_acquisition_block_diagram.png` | `chap01.tex` 第 1.2.1 节 | `0.88\linewidth` | 脑电采集设备的一般组成框图 | 用于系统与采集链路综述，承接后续硬件实现 | `He20` |
| 第1章 | 图1.4 | `01_Thesis_LaTeX/figures/C1-8_Edge_BCI_Prototype.png` | `chap01.tex` 第 1.2.3 节 | `\textwidth` | 基于嵌入式节点的轻量脑机接口原型与卷积网络部署示意 | 用于说明边缘节点与系统链路协同探索 | `Ene23` |
| 第1章 | 图1.5 | `01_Thesis_LaTeX/figures/C1-3_EEGNet_architecture.png` | `chap01.tex` 第 1.3.3 节前后（方法线） | `0.75\linewidth` | EEGNet 紧凑卷积结构示意 | 用于方法演进中展示紧凑 CNN 路线 | `lawhern2018eegnet` |
| 第1章 | 图1.6 | `01_Thesis_LaTeX/figures/C1-5_EEG_Conformer_architecture.png` | `chap01.tex` 第 1.3.3 节 | `0.92\linewidth` | EEG Conformer 卷积与自注意力协同解码的框架示意图 | 用于引出后续第 4 章自注意力主线 | `songEEG2022` |
| 第2章 | 图2.1 | `01_Thesis_LaTeX/figures/C1-7_ERD_ERS_topomap.png` | `chap02.tex` 第 2.1 节运动想象脑电信号特性 | `0.75\textwidth` | 不同运动想象类别下 ERD/ERS 现象的头皮地形分布示意 | 用于说明 MI 的生理基础与感觉运动区节律变化 | `Pfu06` |

## 已停用 / 已移除图片

| 状态 | 文件 | 原用途 | 当前情况 | 备注 |
| --- | --- | --- | --- | --- |
| 已移除 | `01_Thesis_LaTeX/figures/C1-6_Pseudo_Online_framework.png` | 伪在线评估框架图 | 已从正文删除，不再用于第 1 章 | 用户明确要求删除，后续不要误加回 |
| 注释占位 | `org_structure`（无实际文件引用） | 论文技术路线与组织结构 | `chap01.tex` 中仍保留注释式占位 | 若后续真要加技术路线图，需要新建真实文件并解除注释 |

## 当前图号与用途速览

- 图1.1：BCI 系统与应用总览
- 图1.2：BCI 使用模式与评价差异
- 图1.3：脑电采集设备组成
- 图1.4：嵌入式边缘原型
- 图1.5：EEGNet 结构
- 图1.6：EEG Conformer 结构
- 图2.1：MI 条件下 ERD/ERS 地形图

## 后续改图注意事项

1. 如果移动图片所属章节，必须同时检查：
   - `chap01.tex` / `chap02.tex` 中的 `\includegraphics`
   - 图注中的图号表述是否仍自然
   - 正文前后承接句是否仍成立

2. 如果更换文件名，必须同步修改：
   - `\includegraphics{...}`
   - 本台账中的路径记录

3. 如果删除图片，必须同步检查：
   - `\ref{...}` 是否仍存在
   - 与该图配套的说明段落是否仍保留

4. 如果只调整图片大小，优先先改：
   - `width=...`
   - 不要随意改 `label`
   - 不要误动图注中的引用来源

5. 若后续需要继续补图，优先考虑：
   - 第 1 章：wearable 形态/真实应用约束类图
   - 第 2 章：MI 生理机制、节律与频带特性类图
   - 避免重复添加系统框图

