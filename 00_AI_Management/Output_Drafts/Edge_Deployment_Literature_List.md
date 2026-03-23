# 边缘部署与量化剪枝高优文献下载清单
*(专供直接支撑第 3 章“硬件部署”与第 4 章“算法压缩”设计)*

根据 Undermind 审查的 `Hardware_aware_EEG_BCI_model_optimization_evidence_report.md`，筛选出 **8篇** 最具代表性的研究。其中 1-5 篇为建议**无脑拉取全文 (Must Download)**的绝对核心，6-8篇为供对比论证的**次级支撑文献 (Secondary Contrast)**。

## 📥 Top 5 核心必读全文 (Must Download & Parse)
*(强烈建议下载 PDF 并通过 AI 直接精读这 5 篇的所有图表和数学推理部分)*

### 1. [Wan22] MI-BMInet: An Efficient Convolutional Neural Network for Motor Imagery Brain–Machine Interfaces With EEG Channel Selection
- **全文本价值 (为何须下载原文)**：需提取他们是怎么推导 INT8 定点量化公式的，以及他们如何记录 PULP MCU 的 2.95ms 推理延迟。这为第 4 章的 INT8 量化章节提供了可以直接套用的理论架构。
- **推荐等级**: ⭐️⭐️⭐️⭐️⭐️ (最高优先)

### 2. [Sch20] Q-EEGNet: an Energy-Efficient 8-bit Quantized Parallel EEGNet Implementation for Edge Motor-Imagery Brain-Machine Interfaces
- **全文本价值 (为何须下载原文)**：需抄录其底层针对边缘设备的 8-bit 并行化加速结构。它能极大地丰富第 3/4 章中“如何将原始浮点网络压缩入 MCU SRAM”的物理逻辑说明。
- **推荐等级**: ⭐️⭐️⭐️⭐️⭐️ 

### 3. [Wan20] An Accurate EEGNet-based Motor-Imagery Brain–Computer Interface for Low-Power Edge Computing
- **全文本价值 (为何须下载原文)**：这篇文章在 Cortex-M4F 和 M7 (极弱算力核心) 上跑通了脑电深度解码，它的 15 倍降内存方案是您论文里“在 RK3568/单片机环境证明端侧可行性”的基底参考。
- **推荐等级**: ⭐️⭐️⭐️⭐️⭐️ 

### 4. [Ene23] Low-power EEGNet-based Brain-Computer Interface implemented on an Arduino Nano 33 Sense
- **全文本价值 (为何须下载原文)**：最新的 2023 年成果。它用的是最廉价的商用微控制器（Arduino Nano 33 Sense），并应用了 PTQ (训练后量化)。非常适合作为您第 5 章做功耗/延迟对标 Baseline。
- **推荐等级**: ⭐️⭐️⭐️⭐️

### 5. [Tra23] TinyML for EEG Decoding on Microcontrollers
- **全文本价值 (为何须下载原文)**：在极端的 256KB SRAM 以下内存做架构搜索（NAS）。这给第 4 章提供了宏观的架构设计背书——“为什么 EdgeMIFormer 是这样设计的，因为只有这样才放得进 MCU”。
- **推荐等级**: ⭐️⭐️⭐️⭐️

---

## 🔬 对比与迁移备用库 (Secondary Contrast)
*(仅作为综述或实验对比时引用，不需要深抠其底层实现代码，能看到摘要/结论即可)*

### 6. [Bek24] On Optimizing Deep Neural Networks Inference on CPUs for Brain-Computer Interfaces using Inference Engines
- **说明**：重点对标 ONNX Runtime, TVM 等推理引擎的加速倍率。如果项目最终落地瑞芯微 RK3568 NPU，这篇是极好的“算法编译流派”引库支撑，但不需要深究它如何做训练。

### 7. [Hua24] Enhancing Low-Density EEG-Based Brain-Computer Interfacing With Similarity-Keeping Knowledge Distillation
- **说明**：这是一篇知识蒸馏（KD）用于弥补通道减少带来精度下降的文章。在论述“降本增效只靠量化剪枝不够”时，可用这篇论文佐证使用多通道向少通道映射的前沿方案。

### 8. [Pac24] Design and Evaluation of CPU-, GPU-, and FPGA-Based Deployment of a CNN for Motor Imagery Classification in Brain-Computer Interfaces
- **说明**：提供了 CPU、嵌入式 GPU 和 FPGA 的全平台横向对比数据（如 FPGA 功耗降低 89%）。直接将其摘出作为第 3 章硬件选型的一节佐证材料即可，无需通读。
