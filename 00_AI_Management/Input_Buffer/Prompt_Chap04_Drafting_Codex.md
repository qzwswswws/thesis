---
type: Codex_Drafting_Prompt
status: Active
target: 01_Thesis_LaTeX/data/chap04.tex (或实验章 chap05.tex)
---

# 🤖 致 Codex 的第 4/5 章算法实验起草指令 (Chapter 4/5 Drafting Prompt)

**背景 (Context):**
我们在另一台设备上已经完成了算法侧的基线复核与核心的“通道退化 (Channel Degradation)”离线实验，并将所有源数据、CSV 与退化曲线图 `degradation_curve_4class.png` 置入了本地仓库。现由你接手，将其转化为符合由 `nudtpaper` 模板驱动的 LaTeX 毕业论文正文。

## 📥 必须读取的输入物 (Required Inputs)
1. `02_Source_Material/04_Algorithm_Workbench/docs/Experiment_Results_Overall_Summary.md` (最核心的结论摘要，包含准确率、参数量、Kappa值等)
2. `02_Source_Material/04_Algorithm_Workbench/results/degradation_4class.csv` (若需要读入具体原始数据填表)

## 🎯 你的具体输出任务 (Actionable Tasks)

### 任务一：起草“边缘侧通道退化与基线对比”正文 (Drafting LaTeX Text)
在 `chap04.tex` (或对应的实验章) 中撰写以下小节：
- **基线模型性能对比**：绘制基于 BCI Competition IV 2a 数据集的 LaTeX 性能对比表格（如基准 `EEGConformer` 与其他模型的分类准确率 `Acc` 与 `Kappa`）。
- **通道数量对解码性能的非线性影响 (通道剥夺实验)**：用严谨的学术语言描述从 21导联 $\rightarrow$ 8导联 $\rightarrow$ 3导联 $\rightarrow$ 2导联的准确率暴跌现象。
- **引用图表**：使用 `\begin{figure}` 插入 `02_Source_Material/04_Algorithm_Workbench/figures/degradation_curve_4class.png`，配以深度的中英文 caption 分析，指出“由于纯深度学习在极端低通道下丧失空间分辨率，物理天花板显现”。

### 任务二：论证模型复杂度与边缘部署可行性 (Model Efficiency Argument)
- 将 `Experiment_Results_Overall_Summary.md` 中的模型大小 (Size) 与参数量提取出来。
- 撰写一段论述：说明虽然 2 导联下绝对精度受损，但极低的参数量使得模型可以在诸如 RK3568 等 NPU / MCU 端全动态运行，为“交互式闭环”留出了算力冗余。

### 任务三：为缺失插图撰写生成提示词 (Banano / Midjourney Prompts)
为了丰富第 4 章的视觉表达，若你认为文中仍缺少**算法网络架构图 (例如 EdgeMIFormer 的结构)** 或 **人机闭环交互系统概念图**：
- **严格禁止**尝试输出大段复杂的 TikZ / Mermaid 代码（极易翻车报错）。
- **请输出纯文本提示词 (Banano Prompts)**：在你的回复末尾，用独立的 Markdown 代码块，为人类作者（USER）提供 1-2 条用于在 Banano / Midjourney 绘画机器人生成高质量学术架构图的英文提示词。
- **提示词撰写标准**：必须符合扁平化科技插画风格。例如：
  `A high-tech flat vector illustration of an electroencephalography (EEG) brain-computer interface algorithm architecture, showing data flow from 2-channel sensors to a lightweight transformer neural network ... clean background, academic paper style, blue and cyan color palette, isometric layout --ar 16:9`

---

**⚠️ 执行守则 (Execution Rules):**
1. 保持严谨客观的工程学术文风（参考 `Writing_Quality_Standards.md`）。
2. 不要编造未出现在 CSV 里的假数据。
3. 请直接在本会话中回复撰写好的 LaTeX 代码片段与 Banano 提示词，并在完成后更新 `_AI_SYNC_BOARD.md` 的状态。
