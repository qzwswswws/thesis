# 基于 AI 协同的硕士学位论文撰写项目

这是一个利用 Antigravity (AI) 与用户深度协同完成的硕士论文项目。本项目通过结构化的目录管理和标准化的 AI 交互协议，实现从原始实验数据到高质量 LaTeX 文稿的高效转化。

## 目录结构概览

```bash
thesis/
├── 00_AI_Management/       # AI 协作中枢（协议、提示词、进度看板）
├── 01_Thesis_LaTeX/        # 核心活跃区（LaTeX 源码、生成的 PDF）
├── 02_Source_Material/     # 原始素材（开题报告、算法脚本、实验数据）
├── 03_Literature/          # 参考资料库
├── 04_Appendix/            # 附录内容
├── 05_Defense_Slides/      # 答辩幻灯片
└── 99_Archive/             # 历史归档区（AI 默认忽略，保持工作区清爽）
```

## 核心协作流程

### 1. 文献调研 (Research)
*   **原则**: 严禁 AI 幻想文献。
*   **流程**: AI 发现知识缺口 -> 提示用户使用 **Undermind** 调研 -> 用户将结果存入 `00_AI_Management/Input_Buffer` -> AI 提取并撰写文献综述。

### 2. 撰写与起草 (Drafting)
*   **输入**: 基于 `02_Source_Material` 中的原始逻辑。
*   **输出**: 初稿生成于 `00_AI_Management/Output_Drafts` 或直接更新 `01_Thesis_LaTeX/data/`。

### 3. 科研绘图 (Plotting)
*   **TikZ 优先**: 对于神经网络架构和逻辑流程图，优先使用原生 TikZ/LaTeX 渲染以保证极高的学术标准（如 `EdgeMIFormer` 架构与 `KD蒸馏` 框架均采用该方案无损矢量化）。
*   **外部生成**: 复杂示意图由用户利用外部 AI 生成后，再由本项目 AI 进行 LaTeX 适配。

## 🏆 项目里程碑 (Project Milestones)

- **[2026-03] 起步与技术基础**：确立了 AI 协同库的运行法则，并完成了 `第 1/2 章`（研究背景、脑电原理、EdgeMIFormer 理论推导与边缘部署基础）的 LaTeX 收口与编译。
- **[2026-03] 硬件端落地**：完成 `第 3 章` 的第一轮正规起草，涵盖了基于 RK3568 与 KS1092 的便携式双通道脑电采集硬件系统的拓扑设计、固件协议与上位机打通。
- **[2026-03] 算法端落地**：完成 `第 4 章` 起草，不仅将线上实验室拉回的 `04_Algorithm_Workbench` CSV 性能落地为学术图表，更严丝合缝地论证了低通道约束下的性能断崖、任务二次收束策略与 KD 蒸馏补偿机制的数学逻辑。
- **[2026-03] 系统集成**：完成 `第 5 章` 初稿，撰写了基于 BLE 的通信实时性打标与软硬协同方案评估体系。

## 快速开始

1.  **唤醒 AI**: “阅读 `00_AI_Management/Prompt_Library/Master_Prompt.md` 并汇报当前进度”。
2.  **获取支持**: 将外部信息（如网页摘要、Undermind 结果）放入 `00_AI_Management/Input_Buffer` 后，告知 AI “处理输入缓存”。
3.  **检查质量**: 每次大幅修改后运行 `01_Thesis_LaTeX/makepdf.bat`。

---
*注：本项目不仅是论文的仓库，更是人机协同撰写的方法论实践。*
