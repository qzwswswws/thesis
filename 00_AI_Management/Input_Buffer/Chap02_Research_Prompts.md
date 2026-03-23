# 第 2 章技术基础调研方案 (Undermind Prompts)

基于第 4 章 EdgeMIFormer 的算法设计，第 2 章需要构建以下四个技术支柱的理论基础。请将以下提示词（建议使用英文以获得全球高质量文献）投入 Undermind 进行调研。

---

## 知识簇 1：运动想象脑电信号基础 (EEG/MI Basis)
**重点**: 关注 C3/C4 通道的生理意义及 mu/beta 节律。

> **Undermind Prompt**: 
> "Prioritize human MI EEG physiology studies that explain C3/C4/Cz sensorimotor rhythms, Mu/Beta (8-13 Hz / 13-30 Hz), and ERD/ERS timing patterns with quantitative evidence. Allow decoding/modeling papers only when they report explicit channel, band, or time-window effects that can justify model design constraints. Keep classic left/right hand MI as the primary protocol. Include foot/tongue/multiclass MI only as secondary evidence when sensorimotor interpretation is directly transferable. Use healthy adults as the default evidence base; include stroke/ALS/rehab/patient cohorts as supporting evidence only, and explicitly mark transferability risk due to altered ERD/ERS magnitude or lateralization. When evidence conflicts, prioritize controlled physiology/protocol studies for mechanism claims, while retaining benchmark-dataset papers for engineering implications if their quantitative evidence is explicit. Prefer peer-reviewed papers from 2018-2026 and include seminal earlier works only if canonical."

---

## 知识簇 2：Transformer 在 EEG 领域的演进 (Transformer for EEG)
**重点**: 从 CNN (EEGNet) 到 Conformer 的演进，以及典型架构瓶颈。

> **Undermind Prompt**: 
> "Survey the evolution of deep learning architectures for EEG classification, starting from CNN-based models like EEGNet to Transformer-based architectures such as EEG-Conformer and Vision Transformer (ViT) adaptations. Highlight the strengths and limitations of global self-attention when applied to non-stationary EEG time series."

---

## 知识簇 3：高效/局部自注意力机制 (Efficient & Local Attention)
**重点**: 这是 EdgeMIFormer 的核心理论来源。

> **Undermind Prompt**: 
> "Systematically review efficient Transformer architectures and local self-attention mechanisms (e.g., Swin Transformer's window attention, Longformer, or local window sliding attention) that reduce computational complexity from O(N^2) to linear O(N). Focus on their applications in high-frequency time-series or biomedical signal processing where real-time inference is critical."

---

## 知识簇 4A：边缘端模型压缩与量化 (Edge AI Compression & Quantization)
**重点**: 为第 3、4 章的量化、剪枝和精度-延迟-能耗权衡提供理论依据。

> **Undermind Prompt**:
> "Review hardware-aware optimization techniques for EEG or Brain-Computer Interface deep models, with emphasis on post-training quantization (PTQ), quantization-aware training (QAT), structured and unstructured pruning, mixed precision (INT8/INT16), and knowledge distillation. Prioritize studies that report explicit accuracy-latency-memory-energy trade-offs. For each paper, extract: task, dataset, hardware platform, baseline FP32 accuracy, optimized-model accuracy, latency, model size, energy or power if reported, and the deployment toolchain. Be strict about separating direct EEG/BCI evidence from only partially transferable time-series or biomedical-signal evidence. Prefer peer-reviewed papers from 2018-2026 and include canonical earlier papers only if still widely cited."

---

## 知识簇 4B：边缘硬件平台与 RK3568 部署证据 (Edge Deployment Platforms)
**重点**: 为 RK3568 / RKNN / NPU 部署叙述提供更直接的工程依据。

> **Undermind Prompt**:
> "Investigate on-device deployment evidence for transformer-like or temporal deep models on edge hardware platforms relevant to this thesis, especially RK3568, RKNN, ARM-based NPUs, embedded Linux SBCs, and comparable low-power inference devices. Prioritize studies or technical reports with measured latency, memory footprint, throughput, power, or energy results. If direct EEG/BCI evidence is limited, include the closest transferable biomedical or high-frequency time-series deployments and explicitly assess transferability risk to motor-imagery EEG decoding. For each source, report: hardware, runtime/toolchain, numeric deployment results, model type, input characteristics, and why the evidence is or is not directly usable in a thesis chapter on edge deployment."

---

## 知识簇 1B（可选）：运动想象生理尾部补强 (MI Physiology Tail-End Support)
**重点**: 补足当前 `2.1` 中仍偏 provisional 的反馈、训练、beta rebound 与大样本个体差异问题。

> **Undermind Prompt**:
> "Conduct a targeted follow-up review on unresolved motor imagery EEG physiology questions that remain after the core C3/C4/Cz and Mu/Beta literature review. Focus specifically on: (1) whether feedback or short-term training changes hemispheric asymmetry or ERD strength, (2) how reliable beta rebound is in hand MI compared with foot or mixed-task paradigms, and (3) large-sample evidence on user variability beyond simple left-right averages. Return only papers that provide explicit quantitative findings and clearly state whether each paper is suitable as primary evidence, secondary support, or discussion-only context for a master's thesis section on MI EEG physiology."

---

## 操作说明
1. 当前推荐优先运行：`知识簇 4A` → `知识簇 4B`。
2. 若需要继续补强第 2 章 `2.1` 的论证边界，再运行 `知识簇 1B`。
3. `知识簇 2` 与 `知识簇 3` 当前已基本够用，除非要补反证或新增专题，否则可暂缓。
4. 将生成的报告（网页链接或导出的 Markdown/Text）反馈给我。
5. 我将分析报告并指定 3-5 篇核心文献用于深入阅读或直接转写入正文。
