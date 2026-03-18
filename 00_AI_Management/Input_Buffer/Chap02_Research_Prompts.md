# 第 2 章技术基础调研方案 (Undermind Prompts)

基于第 4 章 EdgeMIFormer 的算法设计，第 2 章需要构建以下四个技术支柱的理论基础。请将以下提示词（建议使用英文以获得全球高质量文献）投入 Undermind 进行调研。

---

## 知识簇 1：运动想象脑电信号基础 (EEG/MI Basis)
**重点**: 关注 C3/C4 通道的生理意义及 mu/beta 节律。

> **Undermind Prompt**: 
> "Research the neurophysiological basis of Motor Imagery (MI) EEG signals, specifically focusing on Event-Related Desynchronization (ERD) and Synchronization (ERS) in the Mu (8-13Hz) and Beta (13-30Hz) frequency bands over the C3, C4, and Cz channels. Find seminal and recent papers (2018-2024) discussing the spatial-temporal characteristics of MI signals for BCI systems."

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

## 知识簇 4：边缘端深度学习 optimization (Edge AI & Quantization)
**重点**: 为第 3、4 章的量化和 NPU 部署提供理论依据。

> **Undermind Prompt**: 
> "Investigate hardware-aware optimization techniques for deploying deep learning models on edge devices (e.g., ARM-based NPUs like RK3568). Focus on Post-Training Quantization (PTQ), weight pruning, and the trade-offs between model compression (8-bit quantization) and decoding accuracy in Brain-Computer Interface applications."

---

## 操作说明
1. 请在 Undermind 中分别运行上述 4 个提示词。
2. 将生成的报告（网页链接或导出的 Markdown/Text）反馈给我。
3. 我将分析报告并指定 3-5 篇核心文献用于深入阅读。
