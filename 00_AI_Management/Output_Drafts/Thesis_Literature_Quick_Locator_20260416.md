# Thesis 文献快速定位索引 20260416

## 用途
这份索引用于后续 AI 或人工写作时，快速判断：

- 哪些资料是 `综述 / memo / evidence report`
- 哪些资料有 `本地原文 pdf`
- 哪些论文只在 `开题报告` 或 `zyf 模板论文` 的参考文献中出现
- 在**没有原文**的情况下，现有信息到底有多丰富，能否先支撑安全写作

## 当前快照

- 综述型 / 调研型 / evidence 型 `md`：`28` 份
- 本地 `pdf`（`03_Literature` + `00_AI_Management/Input_Buffer`，排除模板图和封面）：`50` 份
- `nudtpaper-zyf` 模板论文 `refs.bib` 文献池：`328` 条
- 开题报告参考文献来源：`开题报告最终版.docx` 内嵌 `EndNote` 记录，可提取题名、年份、作者、部分 DOI/期刊信息

## 可用性分级

- `有本地原文`：本地存在可直接打开的 `pdf`
- `仅综述/备忘`：没有原文，但有较完整的总结、证据抽取或阅读记录
- `仅 EndNote 元数据`：没有原文，但 `docx` 中嵌有题名、作者、年份、部分来源信息
- `仅 bib 条目`：没有原文，但有结构化书目信息，适合机器检索

## 信息丰富度说明

- `高`：足以直接支撑安全写作，通常包含原文或较系统的证据总结
- `中`：足以做定位和初步概括，但关键判断最好回原文
- `低`：只适合做线索，不宜直接承担论文核心判断

---

## A. 高价值综述 / 调研 / 备忘型 MD

| 类别 | 文件 | 路径 | 原文状态 | 信息丰富度 | 简要概括 |
|---|---|---|---|---|---|
| 可穿戴 EEG 景观 | `Wearable_EEG_thesis_intro_landscape.md` | `00_AI_Management/Input_Buffer/` | 仅综述/备忘 | 高 | 面向绪论写作的 wearable EEG 现状景观，已按形态、应用和证据强弱整理。 |
| 真实应用约束 | `Wearable_EEG_design_constraints_memo.md` | `00_AI_Management/Input_Buffer/` | 仅综述/备忘 | 高 | 讨论为什么真实应用下难以继续沿用高密度有线配置，适合支撑 `1.1/1.2/1.4`。 |
| 大预训练 EEG | `Large_pretrained_EEG_for_wearable_BCI_memo.md` | `00_AI_Management/Input_Buffer/` | 仅综述/备忘 | 高 | 讨论 EEG foundation / large pretraining 的价值与边界，尤其是对 wearable / low-channel / interactive 系统的失配。 |
| trial 波动 | `MI_BCI_local_temporal_variability_memo.md` | `00_AI_Management/Input_Buffer/MI_Paper_Knowledge_Clusters_20260414/...` | 仅综述/备忘 | 中-高 | 关注 local temporal variability、trial quality 与非平稳性。 |
| trial 波动原文阅读 | `MI_BCI_Local_Temporal_Variability_Original_Papers_Review.md` | `00_AI_Management/Input_Buffer/MI_Paper_Knowledge_Clusters_20260414/...` | 仅综述/备忘 | 高 | 对相关原文的定向阅读记录，适合支撑第 1 章“共性问题”。 |
| 冷启动判定 | `MI_EEG_cold_start_decision_memo.md` | `00_AI_Management/Input_Buffer/MI_Paper_Knowledge_Clusters_20260414/...` | 仅综述/备忘 | 高 | 专门讨论冷启动、离线评价与真实使用错位。 |
| 参数适配原文 | `MI_EEG_Parameter_Adaptation_Original_Papers_Reading.md` | `00_AI_Management/Input_Buffer/MI_Paper_Knowledge_Clusters_20260414/...` | 仅综述/备忘 | 高 | 面向在线适配与参数更新的原文阅读摘要。 |
| 在线适配备忘 | `Online_MI_EEG_parameter_adaptation_memo.md` | `00_AI_Management/Input_Buffer/MI_Paper_Knowledge_Clusters_20260414/...` | 仅综述/备忘 | 高 | 在线适配与 lightweight calibration 的综合备忘。 |
| 在线适配 Codex 读书稿 | `Online_MI_EEG_Parameter_Adaptation_Memo_Codex_Reading.md` | `00_AI_Management/Input_Buffer/MI_Paper_Knowledge_Clusters_20260414/...` | 仅综述/备忘 | 中-高 | 更偏写作服务型摘要，可直接转为绪论/展望段落。 |
| 论文-知识簇映射 | `MI_Paper_Clusters_Thesis_Mapping_20260414.md` | `00_AI_Management/Output_Drafts/` | 仅综述/备忘 | 高 | 说明各知识簇服务哪一章、哪类论点、哪些可写成主张。 |
| 全文统稿总评 | `Thesis_Global_Review_20260415.md` | `00_AI_Management/Output_Drafts/` | 仅综述/备忘 | 高 | 从全文角度评估各章问题、证据强度和后续工作优先级。 |
| 边缘部署文献清单 | `Edge_Deployment_Literature_List.md` | `00_AI_Management/Output_Drafts/` | 仅综述/备忘 | 中-高 | 边缘部署方向的候选论文列表，适合快速找 K4 相关文献。 |
| 新报告下载优先级 | `New_Report_Fulltext_Download_Priority.md` | `00_AI_Management/Output_Drafts/` | 仅综述/备忘 | 中 | 标记哪些文献值得优先补全文。 |
| 生理证据报告 | `MI_EEG_sensorimotor_physiology_evidence_report.md` | `03_Literature/K1_MI_Physiology/` | 仅综述/备忘 | 高 | 感觉运动节律、ERD/ERS、C3/C4 等生理基础证据。 |
| 生理后续补证 | `MI_Physiology_Followup_Evidence_Report.md` | `03_Literature/K1_MI_Physiology/` | 仅综述/备忘 | 高 | 对 MI 生理文献的补充与更细化的证据整理。 |
| Cluster 3 列表 | `Cluster3_Literature_List.md` | `03_Literature/K3_Efficient_Local_Attention/` | 仅综述/备忘 | 中 | 自注意力/局部注意力分支的文献目录。 |
| RK3568 证据报告 | `RK3568_Edge_Deployment_Evidence_Report.md` | `03_Literature/K4A_Edge_Compression_Quantization/` | 仅综述/备忘 | 高 | 板端部署、量化和嵌入式推理的论据汇总。 |
| RK3568 与时序模型 | `Edge_deployment_evidence_for_RK3568_and_temporal_models.md` | `03_Literature/K4B_Edge_Deployment_Platforms/` | 仅综述/备忘 | 高 | 端侧板卡与时序模型部署证据，适合第 4/5 章。 |

> 使用建议：如果后续 AI 需要先“搭框架再回原文”，优先从本节开始；如果需要写 `1.1`，优先看前三份；如果需要写在线/适配，优先看冷启动与参数适配系列。

---

## B. 本地 PDF 原文文件

### B1. `03_Literature` 中已归档原文

| 文件 | 路径 | 类型 | 原文状态 | 信息丰富度 | 简要概括 |
|---|---|---|---|---|---|
| `Bla22.pdf` | `03_Literature/K1_MI_Physiology/` | 原文/待核 | 有本地原文 | 高 | MI 生理或相关基础论文，建议结合 evidence report 再判具体定位。 |
| `full-paper_873.pdf` | `03_Literature/K1_MI_Physiology/` | 原文/待核 | 有本地原文 | 中 | 命名较弱，需打开确认具体论文。 |
| `Mu and beta rhythm topographies during motor imagery and actual movements.pdf` | `03_Literature/K1_MI_Physiology/` | 原文 | 有本地原文 | 高 | MI 中 mu/beta 节律拓扑，适合生理基础部分。 |
| `Pfu06.pdf` | `03_Literature/K1_MI_Physiology/` | 原文 | 有本地原文 | 高 | Pfurtscheller 相关 MI / BCI 基础。 |
| `Pfu97.pdf` | `03_Literature/K1_MI_Physiology/` | 原文 | 有本地原文 | 高 | 早期反馈训练 / SMR 可分辨性的重要依据。 |
| `ACNN-TransformerDeepLearningModelfor.pdf` | `03_Literature/K2_Transformer_for_EEG/` | 原文 | 有本地原文 | 高 | EEG Transformer 方向候选。 |
| `EEGConformerConvolutionalTransformer.pdf` | `03_Literature/K2_Transformer_for_EEG/` | 原文 | 有本地原文 | 高 | EEG Conformer 原文，已多次用于第 1/4 章。 |
| `Hierarchical_Transformer_for_Motor_Imagery-Based_Brain_Computer_Interface.pdf` | `03_Literature/K2_Transformer_for_EEG/` | 原文 | 有本地原文 | 高 | 层级 Transformer for MI-BCI。 |
| `AnimprovedmodelusingconvolutionalslidingwindowattentionnetworkformotorimageryEEGclassification2023.pdf` | `03_Literature/K3_Efficient_Local_Attention/` | 原文 | 有本地原文 | 高 | 卷积+滑窗注意力，和当前方法线相关。 |
| `A_Novel_Algorithmic_Structure_of_EEG_Channel_Attention_Combined_With_Swin_Transformer_for_Motor_Patterns_Classification.pdf` | `03_Literature/K3_Efficient_Local_Attention/` | 原文 | 有本地原文 | 高 | 通道注意力 + Swin Transformer，适合方法现状。 |
| `Compactconvolutionaltransformer.pdf` | `03_Literature/K3_Efficient_Local_Attention/` | 原文 | 有本地原文 | 高 | 紧凑卷积 Transformer，适合端侧友好路线。 |
| `Efficient_Transformers_for_EEG_real_time_inference_report.pdf` | `03_Literature/K3_Efficient_Local_Attention/` | 报告型 PDF | 有本地原文 | 中-高 | 更像汇总/报告，不是单篇正式原文。 |
| `Bia24.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | On-device learning / wearable MI。 |
| `EdgeDL2020_cameraReady.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 会议原文 | 有本地原文 | 高 | 边缘部署方向会议论文。 |
| `electronics-13-01646.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | `Pac24`，CPU/GPU/FPGA 部署对比。 |
| `Engineering_Village_detailed_3-23-2026_83337224.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 数据库导出 | 有本地文件但不算原文 | 低-中 | 更像检索元数据，不宜当论文原文使用。 |
| `Low-power_EEGNet-based_Brain-Computer_Interface_implemented_on_an_Arduino_Nano_33_Sense.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | Arduino Nano 33 Sense 上的低功耗 EEGNet。 |
| `MI-BMInet_An_Efficient_Convolutional_Neural_Network_for_Motor_Imagery_BrainMachine_Interfaces_With_EEG_Channel_Selection.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | MI-BMInet，通道选择+高效 CNN。 |
| `Reducing_False_Alarms_in_Wearable_Seizure_Detection_With_EEGformer_A_Compact_Transformer_Model_for_MCUs.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | EEGformer / MCU / wearable seizure。 |
| `TinyEEGConformer_An_Attention-Based_EEG_Decoding_Model_for_Embedded_Systems.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | TinyEEGConformer，嵌入式注意力模型。 |
| `Wan20.pdf` | `03_Literature/K4A_Edge_Compression_Quantization/` | 原文 | 有本地原文 | 高 | EEGNet-based MI BCI for low-power edge computing。 |

### B2. `MI_Paper_Knowledge_Clusters_20260414` 中的本地 PDF

| 文件 | 知识簇 | 原文状态 | 信息丰富度 | 简要概括 |
|---|---|---|---|---|
| `2512.15941v1.pdf` | Local Temporal Variability | 有本地原文 | 中 | 预印本，需结合摘要判断具体主题。 |
| `Cho18.pdf` | Local Temporal Variability | 有本地原文 | 高 | 与 MI / trial variability 相关。 |
| `Ger16.pdf` | Local Temporal Variability | 有本地原文 | 高 | 适合支撑用户学习 / 训练差异。 |
| `Grosse-Wentrup_2012_J._Neural_Eng._9_046001.pdf` | Local Temporal Variability | 有本地原文 | 高 | 经典 MI / BCI 理论与表现差异文献。 |
| `Kra08b.pdf` | Local Temporal Variability | 有本地原文 | 高 | MI/BCI 表现与状态差异线索。 |
| `Nan21.pdf` | Local Temporal Variability | 有本地原文 | 中-高 | 可支撑非平稳或评价问题。 |
| `NIPS-2007-invariant-common-spatial-patterns-alleviating-nonstationarities-in-brain-computer-interfacing-Paper.pdf` | Local Temporal Variability | 有本地原文 | 高 | 非平稳性、ICSP。 |
| `Prediction_of_Motor_Imagery_Performance_based_on_Pre-Trial_Spatio-Spectral_Alertness_Features.pdf` | Local Temporal Variability | 有本地原文 | 高 | 预 trial alertness 与 MI 表现。 |
| `Sag15.pdf` | Local Temporal Variability | 有本地原文 | 中-高 | 需结合 reading memo 确定精确作用。 |
| `Thomas_2013_J._Neural_Eng._10_031001.pdf` | Local Temporal Variability | 有本地原文 | 高 | BCI performance / evaluation 相关。 |
| `Zho16.pdf` | Local Temporal Variability | 有本地原文 | 中-高 | 适合支撑试次质量 / 非平稳问题。 |
| `Bro24_Data_Leakage_Translational_EEG.pdf` | Cold Start Evaluation | 有本地原文 | 高 | 数据泄漏与 translational EEG 评价陷阱。 |
| `Car23_Pseudo_Online_Framework_BCI_Evaluation.pdf` | Cold Start Evaluation | 有本地原文 | 高 | 伪在线评估框架，极适合绪论与第 5 章。 |
| `Kam21_Data_Partitioning_CrossParticipant_EEG.pdf` | Cold Start Evaluation | 有本地原文 | 高 | 数据划分与跨被试评价问题。 |
| `Per18b_Data_Sample_Dependence_BCI_Evaluation.pdf` | Cold Start Evaluation | 有本地原文 | 高 | sample dependence 与 BCI evaluation。 |
| `Tho14_BCI_Performance_Measurement_Tutorial.pdf` | Cold Start Evaluation | 有本地原文 | 高 | BCI performance measurement tutorial。 |
| `Var16_CV_Caveats_Brain_Decoders.pdf` | Cold Start Evaluation | 有本地原文 | 高 | 交叉验证陷阱。 |
| `Wim23_Online_TTA_MI.pdf` | Cold Start Evaluation / Parameter Adaptation | 有本地原文 | 高 | 在线 test-time adaptation for MI。 |
| `Wim25b_Fine_Tuning_Strategies_Continual_Online_MI.pdf` | Cold Start Evaluation / Parameter Adaptation | 有本地原文 | 高 | 持续在线 fine-tuning 策略。 |
| `Bou21_Guidelines_TL_MI_Detection.pdf` | Cold Start Alignment | 有本地原文 | 高 | transfer learning 指南。 |
| `He18_Euclidean_Alignment_TL_BCI.pdf` | Cold Start Alignment | 有本地原文 | 高 | Euclidean Alignment 经典文献。 |
| `Jun24_EA_Deep_Learning_EEG_Decoding.pdf` | Cold Start Alignment | 有本地原文 | 高 | EA 与深度 EEG decoding。 |
| `Rod19_Riemannian_Procrustes_Analysis.pdf` | Cold Start Alignment | 有本地原文 | 高 | Riemannian/Procrustes 线。 |
| `Wu25_Revisiting_Euclidean_Alignment.pdf` | Cold Start Alignment | 有本地原文 | 高 | 重新审视 Euclidean Alignment。 |
| `Che25b_Rapid_Training_BCI_Decoders.pdf` | Parameter Adaptation | 有本地原文 | 高 | 快速训练 / rapid calibration。 |
| `Sha24_Evaluating_Fast_Adaptability_BCI.pdf` | Parameter Adaptation | 有本地原文 | 高 | fast adaptability 评价。 |
| `Zha20b_Adaptive_Transfer_Learning_Deep_CNN.pdf` | Parameter Adaptation | 有本地原文 | 高 | adaptive transfer learning。 |

> 使用建议：如果后续 AI 需要“回原文支撑绪论方法学边界”，本节 B2 是目前最值得优先读的一组。

---

## C. 开题报告引用论文池

### 来源说明

- 文件：`00_AI_Management/Input_Buffer/开题报告最终版.docx`
- 形式：`EndNote` 内嵌记录
- 特点：没有逐篇原文，但通常包含 `题名 + 作者 + 年份 + 期刊/出版社 + 有时含 DOI`
- 适合用途：快速追溯“开题时已经看过哪些方向”；不适合在**未回原文**的情况下直接承担强结论

### 当前已能稳定抽取的高相关条目

| 题名 | 年份 | 本地原文 | 信息丰富度 | 简要概括 |
|---|---:|---|---|---|
| 面向脑机接口的脑电采集设备硬件系统综述 | 2020 | 未检出本地 pdf | 高 | 脑电采集硬件链路综述，已进入当前 thesis `refs.bib`。 |
| 脑电信号采集系统设计及在脑—机接口中的应用研究 | 2006 | 未检出本地 pdf | 中-高 | 偏硬件/采集系统硕士论文。 |
| Electrophysiological Correlates of Change Detection during Delayed Matching Task: A Comparison of Different References | 2017 | 未检出本地 pdf | 中-高 | 参考方式比较，可支撑参考电极讨论。 |
| A CMOS IC for portable EEG acquisition systems | 1998 | 未检出本地 pdf | 高 | 便携 EEG 采集芯片经典工作。 |
| Miniaturization for wearable EEG systems: recording hardware and data processing | 2022 | 未检出本地 pdf | 高 | wearable EEG 小型化与数据处理协同。 |
| Design of EEG data acquisition system based on Raspberry Pi 3 for acute ischemic stroke identification | 2018 | 未检出本地 pdf | 中 | Raspberry Pi 采集平台，偏系统实现。 |
| A review of critical challenges in MI-BCI: From conventional to deep learning methods | 2023 | 未检出本地 pdf | 高 | MI-BCI 挑战综述。 |
| A Design of EEGNet based Inference Processor for Pattern Recognition of EEG using FPGA | 2020 | 未检出本地 pdf | 中-高 | FPGA 上的 EEGNet 推理处理器。 |
| Overview of the EEG-Based Classification of Motor Imagery Activities Using Machine Learning Methods and Inference Acceleration with FPGA-Based Cards | 2022 | 未检出本地 pdf | 中-高 | MI 分类方法与 FPGA 加速综述。 |
| A Unified Novel Neural Network Approach and a Prototype Hardware Implementation for Ultra-Low Power EEG Classification | 2019 | 未检出本地 pdf | 中-高 | 超低功耗 EEG 分类原型。 |
| Motor imagery and direct brain-computer communication | 2001 | 未检出本地 pdf | 中 | MI-BCI 早期重要文献。 |
| Recent trends in EEG based Motor Imagery Signal Analysis and Recognition: A comprehensive review | 2023 | 未检出本地 pdf | 高 | MI 信号分析与识别综述。 |
| Deep learning for motor imagery EEG-based classification: A review | 2021 | 未检出本地 pdf | 高 | MI 深度学习综述。 |
| EEGNet: A Compact Convolutional Network for EEG-based Brain-Computer Interfaces | 2018 | 未检出本地 pdf | 高 | EEGNet 经典原文，当前只用了其结构图，建议后续补全文。 |
| Deep learning with convolutional neural networks for EEG decoding and visualization | 2017 | 未检出本地 pdf | 高 | Schirrmeister 经典 CNN 论文。 |
| EEG Conformer: Convolutional Transformer for EEG Decoding and Visualization | 2023 | 有本地原文 | 高 | 本地见 `03_Literature/K2_Transformer_for_EEG/EEGConformerConvolutionalTransformer.pdf`。 |
| Attention is All you Need | 2017 | 未检出本地 pdf | 高 | Transformer 原始方法来源。 |
| Adaptive feature extraction in EEG-based motor imagery BCI: tracking mental fatigue | 2019 | 未检出本地 pdf | 中-高 | fatigue / MI 自适应特征提取。 |
| EEG-Based Spatio–Temporal Convolutional Neural Network for Driver Fatigue Evaluation | 2019 | 未检出本地 pdf | 中 | 驾驶疲劳 EEG CNN。 |
| Continuous EEG Decoding of Pilots’ Mental States Using Multiple Feature Block-Based Convolutional Neural Network | 2020 | 未检出本地 pdf | 中 | pilots mental state / continuous EEG decoding。 |
| A cross-attention swin transformer network for EEG-based subject-independent cognitive load assessment | 2024 | 未检出本地 pdf | 中-高 | cross-attention Swin Transformer for EEG cognitive load。 |

> 使用建议：对这部分文献，后续 AI 若要真正写入正文，应优先检查是否已有本地全文；没有全文时，可先据 EndNote 元数据做定位，但不要直接用来支撑强判断。

---

## D. `nudtpaper-zyf` 模板论文参考文献池

### 来源说明

- 机器可读主源：`99_Archive/Format_Templates/nudtpaper-zyf/nudtpaper-zyf/ref/refs.bib`
- 条目数：`328`
- 特点：书目信息完整，适合机器直接检索；但多数条目当前 thesis 下**没有对应原文**

### 推荐用法

1. 如果后续 AI 只需要找“某一方向有哪些经典文献”，先查这个 `refs.bib`
2. 如果需要真正写正文，优先去本地 `pdf` 或已有 `memo/review`
3. 如果某条只存在于 `refs.bib`，可先当线索，不要直接上强结论

### 与当前 thesis 关系最强的代表性条目

| 键 | 题名 | 年份 | 本地原文 | 信息丰富度 | 简要概括 |
|---|---|---:|---|---|---|
| `chaudhary2016brain` | Brain--computer interfaces for communication and rehabilitation | 2016 | 未检出本地 pdf | 中 | BCI communication / rehabilitation 综述。 |
| `farwell1988talking` | Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials | 1988 | 未检出本地 pdf | 中 | P300/BCI 经典论文。 |
| `pfurtscheller1999event` | Event-related EEG/MEG synchronization and desynchronization: basic principles | 1999 | 未检出本地 pdf | 中 | ERD/ERS 基础。 |
| `lotte2018review` | A review of classification algorithms for EEG-based brain-computer interfaces | 2018 | 未检出本地 pdf | 高 | EEG-BCI 分类算法综述。 |
| `blankertz2008berlin` | The Berlin Brain-Computer Interface: Accurate performance from first-session in BCI-naive subjects | 2008 | 未检出本地 pdf | 中-高 | first-session / BCI-naive 重要依据。 |
| `schirrmeister2017deep` | Deep learning with convolutional neural networks for EEG decoding and visualization | 2017 | 未检出本地 pdf | 高 | CNN for EEG 经典。 |
| `lawhern2018eegnet` | EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces | 2018 | 未检出本地 pdf | 高 | EEGNet 经典。 |
| `ang2012filter` | Filter bank common spatial pattern algorithm on BCI competition IV datasets 2a and 2b | 2012 | 未检出本地 pdf | 中-高 | FBCSP 经典。 |
| `xie_transformer-based_2022` | A transformer-based approach combining deep learning network and spatial-temporal information for raw EEG | 2022 | 未检出本地 pdf | 中 | EEG Transformer 早期线索之一。 |
| `song2022eeg` / `songEEG2022` | EEG conformer: Convolutional transformer for EEG decoding and visualization | 2022 | 有本地原文 | 高 | 本地见 `03_Literature/K2_Transformer_for_EEG/EEGConformerConvolutionalTransformer.pdf`。 |
| `kwon2019subject` | Subject-independent brain--computer interfaces based on deep convolutional neural networks | 2019 | 未检出本地 pdf | 中 | cross-subject CNN。 |
| `mihajlovic2014wearable` | Wearable, wireless EEG solutions and applications? | 2014 | 未检出本地 pdf | 中 | wearable EEG 早期综述线索。 |
| `wan2021review` | A review on transfer learning in EEG signal analysis | 2021 | 未检出本地 pdf | 中-高 | EEG transfer learning 综述。 |
| `campbell2010neurophone` | NeuroPhone: brain-mobile phone interface using a wireless EEG headset | 2010 | 未检出本地 pdf | 中 | 早期移动 BCI 例子。 |
| `mahmood2019fully` | Fully portable and wireless universal brain-machine interfaces enabled by flexible scalp electronics and deep learning algorithm | 2019 | 未检出本地 pdf | 中-高 | 便携无线 BCI / flexible scalp electronics。 |

> 备注：`refs.bib` 是一个非常有价值的“线索池”，但它更适合机器搜题名、作者、年份，而不是直接拿来写作。

---

## E. 后续 AI 使用建议

### 1. 如果要写第 1 章研究背景与现状

优先顺序：

1. `Wearable_EEG_thesis_intro_landscape.md`
2. `Wearable_EEG_design_constraints_memo.md`
3. `Large_pretrained_EEG_for_wearable_BCI_memo.md`
4. `03_Literature/K1_*` 生理 evidence report
5. 如需强证据，再回本地 `pdf`

### 2. 如果要写第 4 / 5 章端侧部署与在线实现

优先顺序：

1. `RK3568_Edge_Deployment_Evidence_Report.md`
2. `Edge_deployment_evidence_for_RK3568_and_temporal_models.md`
3. `K4A_Edge_Compression_Quantization/` 下本地 `pdf`
4. 开题报告中的边缘部署 / FPGA / processor 线索

### 3. 如果要写冷启动、在线校准、伪在线/在线评价

优先顺序：

1. `MI_EEG_cold_start_decision_memo.md`
2. `Online_MI_EEG_parameter_adaptation_memo.md`
3. B2 中的 `Car23 / Tho14 / Wim23 / Wim25b / He18 / Bou21 / Wu25`

### 4. 如果只有 bibliographic 线索，没有原文

- `开题报告最终版.docx`：优先级高于普通文本摘抄，因为它含 EndNote 元数据
- `nudtpaper-zyf/ref/refs.bib`：适合机器检索，不适合直接承担论文核心判断

---

## F. 最短机器提示

如果后续要让 AI 直接用这份索引，可以这样提示：

> 先读 `Thesis_Literature_Quick_Locator_20260416.md`，按“综述 md -> 本地 pdf -> 开题报告 EndNote -> zyf refs.bib”顺序定位证据。优先使用本地原文和高信息丰富度 memo；对于只有 EndNote 或 bib 的条目，只作为检索线索，不直接支撑强判断。

