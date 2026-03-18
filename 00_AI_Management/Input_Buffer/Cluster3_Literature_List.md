# Cluster 3: 高效局部注意力机制文献精筛名单 (Efficient & Local Attention)

**调研目标**: 系统回顾将自注意力计算复杂度从 $O(N^2)$ 降至线性 $O(N)$ 的高效 Transformer 架构及局部注意力机制（如 Swin Transformer），并重点关注其在高频时间序列或生物医学信号（尤其是脑机接口系统）实时推理中的应用。

---

## 一、核心推荐：EdgeMIFormer 的最强理论印证 (3 篇必读)

这三篇文章是与我们“第 4 章：轻量化脑电部署”重叠度最高的，建议**直接下载 PDF 全文**：

1. **[Wan23] A Novel Algorithmic Structure of EEG Channel Attention Combined With Swin Transformer for Motor Patterns Classification (2023)**
   - **下载链接**: [IEEE page](https://ieeexplore.ieee.org/document/10190140/)
   - **入选理由**: 本文直接将 **Swin 风格的窗口注意力** 引入 EEG 运动模式分类。这与我们 EdgeMIFormer 的滑动局部窗口设计高度一致，是极其罕见且对口的硬件友好设计。

2. **[Hua23b] An improved model using convolutional sliding window-attention network for motor imagery EEG classification (2023)**
   - **下载链接**: [Frontiers article](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1204385/full) · [PDF](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1204385/pdf)
   - **入选理由**: 直接针对 MI EEG 的**滑动窗口注意力**论文。这篇对于我们论述“局部窗口比全局注意力更擅长提取时空特征”非常关键。

3. **[Keu24] Compact convolutional transformer for subject-independent motor imagery EEG-based BCIs (2024)**
   - **下载链接**: [Nature article](https://www.nature.com/articles/s41598-024-73755-4) · [PDF](https://www.nature.com/articles/s41598-024-73755-4.pdf)
   - **入选理由**: 极其契合“端侧部署”角度的最新顶刊文章。虽然其降低计算量的方式可能不完是 $O(N)$，但其**紧凑型（Compact）架构**和跨被试性能对后续我们做对比实验很有帮助。

---

## 二、端侧真实部署基准 (Edge Deployment Evidence) (2 篇必读)

我们第 3、4 章的痛点就是板端推理（RK3568），这两篇虽然未必是 MI，但提供了不可多得的**部署落地论据**，值得下载核心章节参考性能数据：

4. **[Bus24] Reducing False Alarms in Wearable Seizure Detection With EEGformer: A Compact Transformer Model for MCUs (2024)**
   - **下载链接**: [Author PDF](https://iris.polito.it/bitstream/11583/2996576/1/Reducing_False_Alarms_in_Wearable_Seizure_Detection_With_EEGformer_A_Compact_Transformer_Model_for_MCUs.pdf)
   - **入选理由**: 本篇提供了罕见的**在 MCU 级别设备上部署 Transformer 的真实延迟和能耗数据**！可用于支撑为何我们要量化到 8-bit 及在端侧运行的合理性。

5. **[Yao22] A CNN-Transformer Deep Learning Model for Real-time Sleep Stage Classification in an Energy-Constrained Wireless Device (2022)**
   - **下载链接**: [arXiv PDF](https://www.medrxiv.org/content/10.1101/2022.11.21.22282544v1.full.pdf)
   - **入选理由**: 提供了低功耗无线设备（如 NPU）部署脑电 Transformer 的论证，强化算法必须硬件化。

---

## 三、方法论基石与 Baseline (Foundational Mechanism) (按需引述)

这部分只需放入参考文献列表中进行理论撑腰，且 `[Son22]` 极有可能成为我们实验章节的对比模型（Baseline）。

6. **[Son22] EEG Conformer: Convolutional Transformer for EEG Decoding and Visualization (2022)**
   - **入选理由**: 700+ 引用的 EEG Transformer 开拓性神作之一，大概率会作为我们的 Baseline 被写进文章里。
   - **下载链接**: [Author PDF](https://bingchuanliu.github.io/assets/pdf/song_tnsre.pdf)

7. **[Liu21b] Swin Transformer: Hierarchical Vision Transformer using Shifted Windows (ICCV 2021)**
   - **入选理由**: 我们阐述局部窗口注意力机制降低计算复杂度时，必须引用的“万恶之源”，29000+ 引用基石。
   - **下载链接**: [Open access PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.pdf)

8. **[Bel20] Longformer: The Long-Document Transformer (2020)**
   - **入选理由**: 将自注意力计算复杂度从 $O(N^2)$ 降到 $O(N)$ 的 NLP 经典论文，解释局部性原理。

9. **[Den23] Hierarchical Transformer for Motor Imagery-Based Brain Computer Interface (2023)**
   - **入选理由**: 探讨了将长序列分解为局部特征的层级化方法。
