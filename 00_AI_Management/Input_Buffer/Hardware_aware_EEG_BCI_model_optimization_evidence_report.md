# Hardware aware EEG BCI model optimization evidence report

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [1. Primary deployment evidence](#primary-deployment-evidence)
  - [Fast view](#fast-view)
  - [Direct MI papers with measured hardware or runtime evidence](#direct-mi-papers-with-measured-hardware-or-runtime-evidence)
  - [\[Wan22\]](#wan22)
  - [\[Sch20\]](#sch20)
  - [\[Wan20\]](#wan20)
  - [\[Ene23\]](#ene23)
  - [\[Bia24\]](#bia24)
  - [\[Pac24\]](#pac24)
  - [\[Bek24\]](#bek24)
  - [\[Fen22b\]](#fen22b)
  - [\[Mwa23\]](#mwa23)
  - [Direct MI optimization papers with weak or partial deployment reporting](#direct-mi-optimization-papers-with-weak-or-partial-deployment-reporting)
  - [\[Asa25\]](#asa25)
  - [\[Tra23\]](#tra23)
  - [\[Ing20\]](#ing20)
  - [\[Vis21\]](#vis21)
  - [\[Zha22\]](#zha22)
  - [\[Hua24\]](#hua24)
- [2. Secondary transferable evidence](#secondary-transferable-evidence)
  - [Fast view](#fast-view-1)
  - [\[Tru18\]](#tru18)
  - [\[R22\]](#r22)
  - [\[Liu20b\]](#liu20b)
  - [\[Zan21\]](#zan21)
  - [\[Bus24\]](#bus24)
  - [\[Ing23\]](#ing23)
  - [\[Kav23\]](#kav23)
  - [\[Bha25\]](#bha25)
  - [\[Xin24\]](#xin24)
- [3. Optimization methods summary](#optimization-methods-summary)
  - [Method-level takeaways](#method-level-takeaways)
- [4. Platform summary](#platform-summary)
  - [Platform-level takeaways](#platform-level-takeaways)
- [5. Unresolved gaps for this thesis](#unresolved-gaps-for-this-thesis)
- [Ranked top-10 reading list](#ranked-top-10-reading-list)
- [Five papers most useful for direct use in Chapters 3 and 4](#five-papers-most-useful-for-direct-use-in-chapters-3-and-4)
- [Recommended citation strategy for a master’s thesis](#recommended-citation-strategy-for-a-masters-thesis)
- [Explicit warnings about overclaiming](#explicit-warnings-about-overclaiming)
- [References](#references)

Hardware-aware EEG/BCI model optimization evidence report

Audit scope: direct evidence is restricted to deep motor imagery EEG and near-real-time BCI decoding. Non-MI EEG papers are included only when they provide concrete hardware or deployment lessons that plausibly transfer to deployable MI decoders. NR means not reported in the project metadata available for this audit. Bibliographic records below reproduce the project library metadata, which in some cases abbreviates author lists.

## 1. Primary deployment evidence

### Fast view

| Paper | Main contribution | Platform | Strongest reported deployment result | Audit label |
|:---|:---|:---|:---|:---|
| \[Wan22\] | Efficient MI CNN with channel selection and INT8 quantization | PULP MCU | 2.95 ms and 30 μJ per inference at 82.51% | Primary evidence |
| \[Sch20\] | EEGNet INT8 quantization and parallel hardware-aware implementation | Mr. Wolf PULP SoC | 5.82 ms and 0.627 mJ per inference | Primary evidence |
| \[Wan20\] | EEGNet scaling with downsampling, channel selection, shorter windows | Cortex-M4F and M7 | 101 ms and 4.28 mJ on M4F, 44 ms and 18.1 mJ on M7 | Primary evidence |
| \[Ene23\] | EEGNet PTQ on Arduino-class MCU | Arduino Nano 33 Sense, Cortex-M4F | 137 ms and 2.55 mJ per inference | Primary evidence |
| \[Bia24\] | On-device adaptation for wearable MI BCI | GAP9 PULP processor | 14.9 ms and 0.76 mJ per inference, 20 μs update time | Primary evidence |
| \[Asa25\] | Tiny attention model for embedded MI decoding | Arm Cortex-M | 79.63% with 37,135 parameters and 145 kB | Primary support |
| \[Tra23\] | NAS under MCU memory and latency constraints | MCU target under 256 KB SRAM | ≈20× lower inference memory and up to 1.7× latency speedup | Primary support |
| \[Pac24\] | CPU vs GPU vs FPGA deployment comparison for MI CNN | CPU, embedded GPU, FPGA | FPGA up to 89% lower power than CPU and 98% lower memory footprint | Primary evidence |
| \[Bek24\] | Runtime-engine optimization for BCI inference on CPUs | CPU with ONNX Runtime, OpenVINO, TVM | 5 to 6× average speedup vs PyTorch | Primary evidence |
| \[Fen22b\] | Model-compressed EEGNet accelerator | FPGA plus 65 nm CMOS synthesis | 24.4 ms and 0.267 mJ per inference | Primary evidence |
| \[Mwa23\] | Jetson TX2 MI deployment with channel selection | NVIDIA Jetson TX2 | 48.7 ms average latency | Primary evidence with lower transferability |
| \[Ing20\] | Canonical embedded-friendly MI backbone | Embedded-oriented design | 77.35% group accuracy and 83.84% subject-tuned accuracy | Primary support |
| \[Vis21\] | Magnitude pruning for MI CNN | No hardware measurement reported | 90% sparsity and 4.77× compression with 0.02 pp loss | Primary support |
| \[Zha22\] | Neuron pruning for MI CNN | No hardware measurement reported | 50% model-size reduction and 67.09% compute saving | Primary support |
| \[Hua24\] | KD for low-density MI EEG | No hardware measurement reported | Accuracy gains for low-density montages across models | Primary support |

### Direct MI papers with measured hardware or runtime evidence

### \[Wan22\]

- Paper ID: \[Wan22\]
- Bibliographic record: Xiaying Wang, …, and L. Benini. *MI-BMInet: An Efficient Convolutional Neural Network for Motor Imagery Brain–Machine Interfaces With EEG Channel Selection*. IEEE Sensors Journal, 2022, pp. 8835-8847.
- Task: 2-class MI EEG classification for embedded BMI, with channel-reduction emphasis.
- Model type: Efficient CNN named MI-BMInet.
- Optimization technique: Compact architecture, automatic channel selection, INT8 quantization of weights and activations.
- Hardware platform: Leading-edge parallel ultra-low-power PULP MCUs.
- Runtime and deployment toolchain: Embedded deployment on PULP MCU platform. Exact software stack NR.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: 82.51% for the final two-class solution.
- Latency: 2.95 ms per inference.
- Memory and model size: Uses 6.4× fewer EEG channels than the reference setting. Full memory figure NR in abstract.
- Power and energy: 30 μJ per inference.
- Transferability to deployable MI-EEG decoding: Very high. This is the cleanest direct match to a thesis centered on low-power embedded MI decoding \[Wan22\].
- Evidence label: Primary evidence.

### \[Sch20\]

- Paper ID: \[Sch20\]
- Bibliographic record: Tibor Schneider, …, and L. Benini. *Q-EEGNet: an Energy-Efficient 8-bit Quantized Parallel EEGNet Implementation for Edge Motor-Imagery Brain-Machine Interfaces*. 2020 IEEE International Conference on Smart Computing, 2020, pp. 284-289.
- Task: 4-class MI EEG decoding on edge hardware.
- Model type: EEGNet.
- Optimization technique: INT8 fixed-point quantization for weights and activations, hardware-aware parallel implementation, custom ISA use.
- Hardware platform: Mr. Wolf parallel ultra-low-power PULP SoC.
- Runtime and deployment toolchain: Custom parallel implementation using RISC-V ISA extensions and 8-core compute cluster.
- Baseline FP32 accuracy: Absolute baseline NR in abstract.
- Optimized accuracy: Negligible 0.4 pp loss after INT8 quantization.
- Latency: 5.82 ms per inference.
- Memory and model size: Up to 85% memory-footprint reduction.
- Power and energy: 0.627 mJ per inference. Reported 21.0 GMAC s per W.
- Transferability to deployable MI-EEG decoding: Very high for INT8 deployment on low-power parallel MCUs \[Sch20\].
- Evidence label: Primary evidence.

### \[Wan20\]

- Paper ID: \[Wan20\]
- Bibliographic record: Xiaying Wang, …, and L. Benini. *An Accurate EEGNet-based Motor-Imagery Brain–Computer Interface for Low-Power Edge Computing*. 2020 IEEE International Symposium on Medical Measurements and Applications, 2020, pp. 1-6.
- Task: 2-class, 3-class, and 4-class MI EEG classification.
- Model type: EEGNet-derived CNN.
- Optimization technique: Temporal downsampling, channel selection, shorter classification window, model scaling.
- Hardware platform: Cortex-M4F MCU and Cortex-M7 MCU.
- Runtime and deployment toolchain: Embedded deployment on commercial Arm Cortex MCUs. Exact runtime framework NR.
- Baseline FP32 accuracy: Standard EEGNet reached 82.43%, 75.07%, and 65.07% on 2-class, 3-class, and 4-class tasks.
- Optimized accuracy: 0.31 pp loss with 7.6× memory reduction, or 2.51 pp loss with 15× reduction.
- Latency: 101 ms on Cortex-M4F for the smallest model, 44 ms on Cortex-M7 for the medium model.
- Memory and model size: 7.6× to 15× memory-footprint reduction.
- Power and energy: 4.28 mJ per inference on Cortex-M4F and 18.1 mJ per inference on Cortex-M7 for the reported operating points.
- Transferability to deployable MI-EEG decoding: Very high. This paper is a direct thesis anchor for memory-accuracy trade-offs on MCU-class hardware \[Wan20\].
- Evidence label: Primary evidence.

### \[Ene23\]

- Paper ID: \[Ene23\]
- Bibliographic record: Daniel Enériz, …, and D. Antolín. *Low-power EEGNet-based Brain-Computer Interface implemented on an Arduino Nano 33 Sense*. 2023 38th Conference on Design of Circuits and Integrated Systems, 2023, pp. 1-5.
- Task: MI EEG decoding from Physionet models mapped to an Arduino-class device.
- Model type: EEGNet-based model.
- Optimization technique: INT8 post-training quantization.
- Hardware platform: Arduino Nano 33 Sense with Arm Cortex-M4F.
- Runtime and deployment toolchain: On-device implementation on Arduino firmware. Exact software toolchain NR.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: Mean downgrade of 2.64 ± 0.77 pp after PTQ.
- Latency: 137 ms per inference.
- Memory and model size: RAM usage and operation count characterized. Absolute footprint NR in abstract.
- Power and energy: 2.55 mJ per inference.
- Transferability to deployable MI-EEG decoding: High. Less efficient than PULP work, but very relevant because Arduino-class deployment is close to realistic low-cost prototyping \[Ene23\].
- Evidence label: Primary evidence.

### \[Bia24\]

- Paper ID: \[Bia24\]
- Bibliographic record: Sizhen Bian, …, and Michele Magno. *On-device Learning of EEGNet-based Network For Wearable Motor Imagery Brain-Computer Interface*. Proceedings of the 2024 ACM International Symposium on Wearable Computers, 2024.
- Task: Wearable MI EEG recognition with user adaptation.
- Model type: EEGNet-based network with on-device learning.
- Optimization technique: Lightweight model design, optimized input stream, online adaptation.
- Hardware platform: GAP9 low-power parallel RISC-V processor.
- Runtime and deployment toolchain: On-device inference and update engine on GAP9. Exact software stack NR.
- Baseline FP32 accuracy: Absolute baseline NR in abstract.
- Optimized accuracy: Up to 7.31 pp gain over baseline after on-device adaptation.
- Latency: 14.9 ms per inference. Training update 20 μs per update.
- Memory and model size: 15.6 kB memory footprint.
- Power and energy: 0.76 mJ per inference and 0.83 μJ per update.
- Transferability to deployable MI-EEG decoding: Very high for theses that need to address inter-subject or inter-session drift under edge constraints \[Bia24\].
- Evidence label: Primary evidence.

### \[Pac24\]

- Paper ID: \[Pac24\]
- Bibliographic record: Federico Pacini, …, and L. Fanucci. *Design and Evaluation of CPU-, GPU-, and FPGA-Based Deployment of a CNN for Motor Imagery Classification in Brain-Computer Interfaces*. Electronics, 2024.
- Task: MI EEG CNN deployment comparison across hardware classes.
- Model type: CNN for MI classification.
- Optimization technique: Cross-platform deployment and design comparison rather than one single compression method.
- Hardware platform: CPU, embedded GPU, FPGA.
- Runtime and deployment toolchain: Cross-platform deployment. Exact toolchain NR in abstract.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: NR in abstract.
- Latency: FPGA has 39% higher inference time than GPU, while both GPU and FPGA outperform CPU. Absolute latency NR in abstract.
- Memory and model size: FPGA reduces memory footprint for inference by up to 98%.
- Power and energy: FPGA reduces power consumption by up to 89% vs CPU and 71% vs GPU. FPGA has best power-consumption and inference-time product.
- Transferability to deployable MI-EEG decoding: Medium to high. Useful for platform framing, but the FPGA and GPU operating points are less directly transferable to lightweight battery wearable designs \[Pac24\].
- Evidence label: Primary evidence.

### \[Bek24\]

- Paper ID: \[Bek24\]
- Bibliographic record: Okba Bekhelifi, N. Berrached. *On Optimizing Deep Neural Networks Inference on CPUs for Brain-Computer Interfaces using Inference Engines*. 2024 IEEE International Symposium on Circuits and Systems, 2024, pp. 1-5.
- Task: EEG-based BCI decoding under CPU inference constraints.
- Model type: Medium and small neural networks.
- Optimization technique: Runtime-engine optimization with ONNX Runtime, OpenVINO, and Apache TVM.
- Hardware platform: CPU.
- Runtime and deployment toolchain: PyTorch baseline versus ONNX Runtime, OpenVINO, and TVM.
- Baseline FP32 accuracy: Same trained models. Accuracy change NR, suggesting runtime focus rather than accuracy change.
- Optimized accuracy: Same predictive task, speedup-focused. Exact accuracy NR.
- Latency: ONNX Runtime gives 5 to 6× average speedup for medium and small models.
- Memory and model size: 38,527 parameters for medium network and 3,945 for small network.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium. Strong for software deployment chapters on CPU-bound BCIs, weaker for MCU-class edge devices \[Bek24\].
- Evidence label: Primary evidence.

### \[Fen22b\]

- Paper ID: \[Fen22b\]
- Bibliographic record: Lichen Feng, …, and Zhangming Zhu. *An Efficient Model-Compressed EEGNet Accelerator for Generalized Brain-Computer Interfaces With Near Sensor Intelligence*. IEEE Transactions on Biomedical Circuits and Systems, 2022, pp. 1239-1249.
- Task: Generalized BCI acceleration across three datasets, including BCIC-IV-2a.
- Model type: EEGNet.
- Optimization technique: Embedded channel selection, normalization merging, product quantization, hardware co-design.
- Hardware platform: FPGA prototype and 65 nm CMOS low-power synthesis.
- Runtime and deployment toolchain: Custom accelerator design.
- Baseline FP32 accuracy: Absolute baseline NR in abstract.
- Optimized accuracy: Negligible loss of 0.80 pp.
- Latency: 24.4 ms per inference in synthesized design.
- Memory and model size: Quantized weights and intermediates reduce memory size. Full footprint NR in abstract.
- Power and energy: 0.267 mJ per inference.
- Transferability to deployable MI-EEG decoding: Medium. Strong hardware evidence, but closer to accelerator co-design than a software-deployed thesis on commodity embedded systems \[Fen22b\].
- Evidence label: Primary evidence.

### \[Mwa23\]

- Paper ID: \[Mwa23\]
- Bibliographic record: Tat’y Mwata-Velu, …, and Adán Antonio Alonso-Ramírez. *Motor Imagery Multi-Tasks Classification for BCIs Using the NVIDIA Jetson TX2 Board and the EEGNet Network*. Sensors, 2023.
- Task: Multi-task MI classification.
- Model type: EEGNet with channel-selection strategies.
- Optimization technique: Discriminant channel selection and cyclic learning schedule.
- Hardware platform: NVIDIA Jetson TX2.
- Runtime and deployment toolchain: Embedded implementation on Jetson TX2.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: 83.7% per subject and 81.3% per task.
- Latency: 48.7 ms average latency.
- Memory and model size: NR.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium. Real hardware and online relevance are useful, but Jetson-class assumptions are materially heavier than MCU or small wearable targets \[Mwa23\].
- Evidence label: Primary evidence with lower transferability.

### Direct MI optimization papers with weak or partial deployment reporting

### \[Asa25\]

- Paper ID: \[Asa25\]
- Bibliographic record: Nana Ofosu Asante, …, and Michele Magno. *TinyEEGConformer: An Attention-Based EEG Decoding Model for Embedded Systems*. 2025 IEEE Sensors Applications Symposium, 2025, pp. 1-6.
- Task: 4-class MI EEG decoding on BCIC IV-2a.
- Model type: Lightweight attention and conformer hybrid.
- Optimization technique: Architecture redesign for embedded constraints.
- Hardware platform: Arm Cortex-M processors.
- Runtime and deployment toolchain: Evaluated for Arm Cortex-M deployment. Exact framework NR.
- Baseline FP32 accuracy: Baseline EEG Conformer is 78.66%, inferred from reported 0.97 pp gap.
- Optimized accuracy: 79.63%.
- Latency: NR in abstract.
- Memory and model size: 37,135 parameters, about 145 kB, 21× fewer parameters than the baseline EEG Conformer.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: High for architecture selection, but weaker than the papers with explicit latency and energy numbers \[Asa25\].
- Evidence label: Primary support.

### \[Tra23\]

- Paper ID: \[Tra23\]
- Bibliographic record: Antonios Tragoudaras, Charalampos Antoniadis, Yehia Massoud. *TinyML for EEG Decoding on Microcontrollers*. 2023 IEEE International Symposium on Circuits and Systems, 2023, pp. 1-5.
- Task: MI EEG decoding on BCIC IV-2a under MCU memory constraints.
- Model type: CNNs found by neural architecture search.
- Optimization technique: NAS with accuracy, size, latency, and peak memory in the objective.
- Hardware platform: MCU target with less than 256 KB SRAM.
- Runtime and deployment toolchain: TinyML deployment-oriented evaluation. Exact MCU and runtime stack NR in abstract.
- Baseline FP32 accuracy: Best-accuracy literature baseline used, exact value NR in abstract.
- Optimized accuracy: Similar accuracy to the baseline.
- Latency: Up to 1.7× average latency speedup.
- Memory and model size: About 20× lower inference memory footprint.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: High. This is useful when the thesis needs a design-space-search argument rather than only a hand-tuned architecture story \[Tra23\].
- Evidence label: Primary support.

### \[Ing20\]

- Paper ID: \[Ing20\]
- Bibliographic record: T. Ingolfsson, …, and L. Benini. *EEG-TCNet: An Accurate Temporal Convolutional Network for Embedded Motor-Imagery Brain–Machine Interfaces*. 2020 IEEE International Conference on Systems, Man, and Cybernetics, 2020, pp. 2958-2965.
- Task: 4-class MI EEG decoding.
- Model type: Temporal convolutional network.
- Optimization technique: Architecture design for low parameter count and low inference complexity.
- Hardware platform: Embedded target motivation, but no explicit device benchmark in abstract.
- Runtime and deployment toolchain: NR.
- Baseline FP32 accuracy: NR.
- Optimized accuracy: 77.35% on BCIC IV-2a and 83.84% with subject-specific hyperparameter tuning.
- Latency: NR.
- Memory and model size: Reported as low-memory and low-complexity, but absolute numbers NR in abstract.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: High for model-choice justification. Low to medium for quantitative hardware benchmarking \[Ing20\].
- Evidence label: Primary support.

### \[Vis21\]

- Paper ID: \[Vis21\]
- Bibliographic record: Vishnupriya., …, and Cuntai Guan. *Performance Evaluation of Compressed Deep CNN for Motor Imagery Classification using EEG*. 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society, 2021, pp. 795-799.
- Task: Subject-independent MI EEG classification.
- Model type: Pre-trained CNN.
- Optimization technique: Magnitude-based weight pruning.
- Hardware platform: No physical hardware deployment reported.
- Runtime and deployment toolchain: NR.
- Baseline FP32 accuracy: 84.46%, inferred from reported 84.44% after 0.02 pp loss.
- Optimized accuracy: 84.44% at up to 90% sparsity.
- Latency: NR.
- Memory and model size: 4.77× compression ratio at 90% sparsity.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium. Good direct MI evidence for unstructured pruning, but sparse software and hardware speedups are not demonstrated \[Vis21\].
- Evidence label: Primary support.

### \[Zha22\]

- Paper ID: \[Zha22\]
- Bibliographic record: Jiayang Zhang, Kang Li. *A Pruned Deep Learning Approach for Classification of Motor Imagery Electroencephalography Signals*. 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society, 2022, pp. 4072-4075.
- Task: MI EEG classification for rehabilitation-oriented BCI.
- Model type: CNN.
- Optimization technique: Contribution-based neuron pruning using fast recursive algorithm.
- Hardware platform: No hardware deployment reported.
- Runtime and deployment toolchain: NR.
- Baseline FP32 accuracy: NR.
- Optimized accuracy: Performance reported as maintained, but exact accuracy NR in abstract.
- Latency: NR.
- Memory and model size: Up to 50% model-size reduction.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium. Useful for arguing structured reduction in compute, but not enough to claim real embedded acceleration on its own \[Zha22\].
- Evidence label: Primary support.

### \[Hua24\]

- Paper ID: \[Hua24\]
- Bibliographic record: Xin-Yao Huang, Sung-Yu Chen, Chun-Shu Wei. *Enhancing Low-Density EEG-Based Brain-Computer Interfacing With Similarity-Keeping Knowledge Distillation*. IEEE Transactions on Emerging Topics in Computational Intelligence, 2024, pp. 1156-1166.
- Task: Low-density MI EEG decoding.
- Model type: Teacher-student EEG decoder framework across multiple architectures.
- Optimization technique: Similarity-keeping knowledge distillation from high-density teacher to low-density student.
- Hardware platform: No physical deployment benchmark reported.
- Runtime and deployment toolchain: NR.
- Baseline FP32 accuracy: Absolute baseline NR in abstract.
- Optimized accuracy: Distilled student consistently improves over non-distilled low-density students across architectures.
- Latency: NR.
- Memory and model size: Low-density student setting reduces channel count, but absolute memory NR.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium to high. Very relevant when the thesis needs a channel-count reduction strategy, but it is not direct hardware evidence \[Hua24\].
- Evidence label: Primary support.

## 2. Secondary transferable evidence

### Fast view

| Paper | Task | Optimization focus | Hardware evidence | Transferability |
|:---|:---|:---|:---|:---|
| \[Tru18\] | Seizure detection | Integer CNN | Integerized model, memory efficiency | Medium |
| \[R22\] | Seizure detection | Integer-Net on FPGA | 5.65× latency acceleration | Medium |
| \[Liu20b\] | Seizure detection and prediction | Compression plus quantization | Microcontroller deployment with measured time, memory, power | Medium |
| \[Zan21\] | iEEG seizure onset detection | TCN on low-power MCU | 1.46 ms and 51.2 μJ on 8 cores | Medium to high |
| \[Bus24\] | Wearable seizure detection | Compact transformer for MCUs | 13.7 ms and 0.31 mJ on GAP9 | Medium |
| \[Ing23\] | Seizure detection | Lightweight network plus embedded evaluation | 0.051 mJ per inference on GAP9 | Medium |
| \[Kav23\] | Sleep staging | INT8 quantization | 1.6 s on Cortex-M4 | Low to medium |
| \[Bha25\] | Mental stress detection | QAT plus pruning | 84.77 ms on phone and watch class target | Low to medium |
| \[Xin24\] | Artifact removal | TFLite smartphone acceleration | 5 ms for 4 s window on smartphone | Low to medium |

### \[Tru18\]

- Paper ID: \[Tru18\]
- Bibliographic record: N. D. Truong, …, and O. Kavehei. *Integer Convolutional Neural Network for Seizure Detection*. IEEE Journal on Emerging and Selected Topics in Circuits and Systems, 2018, pp. 849-857.
- Task: Seizure detection on intracranial and scalp EEG.
- Model type: CNN.
- Optimization technique: Integer-Net with low-bit integer arithmetic.
- Hardware platform: Hardware-friendly formulation targeted to wearable and implantable use. Physical deployment not reported in abstract.
- Runtime and deployment toolchain: Integer convolution design. Toolchain NR.
- Baseline FP32 accuracy: 32-bit real-valued CNN reference.
- Optimized accuracy: 4-bit Integer-Net with only about 2 pp accuracy drop.
- Latency: Exact latency NR in abstract.
- Memory and model size: More than 7× memory-efficiency improvement.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium. Strong evidence that low-bit EEG CNNs can hold accuracy, but seizure detection is not MI decoding \[Tru18\].
- Evidence label: Secondary support.

### \[R22\]

- Paper ID: \[R22\]
- Bibliographic record: S. R., M. Rao. *Hardware characterization of Integer-Net based seizure detection models on FPGA*. 2022 IEEE 15th International Symposium on Embedded Multicore Many-core Systems-on-Chip, 2022, pp. 224-231.
- Task: EEG seizure detection.
- Model type: Integer-Net CNN and hybrid integerized variants.
- Optimization technique: Integerized arithmetic with FPGA acceleration.
- Hardware platform: Zynq-7000 SoC FPGA.
- Runtime and deployment toolchain: FPGA hardware implementation.
- Baseline FP32 accuracy: Full-precision model reference, exact accuracy NR in abstract.
- Optimized accuracy: Close to original model, exact value NR in abstract.
- Latency: 5.65× latency acceleration.
- Memory and model size: 5.99× on-chip memory-usage reduction.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Medium. Useful as proof that integerized EEG CNNs can map well to hardware, but task and platform differ from wearable MI decoding \[R22\].
- Evidence label: Secondary support.

### \[Liu20b\]

- Paper ID: \[Liu20b\]
- Bibliographic record: Xilin Liu, A. Richardson. *Edge deep learning for neural implants: a case study of seizure detection and prediction*. Journal of Neural Engineering, 2020.
- Task: Seizure detection and prediction.
- Model type: DNN, CNN, and LSTM.
- Optimization technique: Iterative model compression and coefficient quantization.
- Hardware platform: Off-the-shelf microcontroller.
- Runtime and deployment toolchain: TensorFlow training and real-time deployment on a microcontroller.
- Baseline FP32 accuracy: Accuracy degradation less than 0.5 pp after compression and quantization.
- Optimized accuracy: Event-detection sensitivity 87.36% for DNN, 96.70% for CNN, 97.61% for LSTM, with corresponding false-positive rates reported.
- Latency: Execution time quantified, but exact numbers NR in abstract.
- Memory and model size: Memory size quantified, but exact values NR in abstract.
- Power and energy: Power consumption quantified, but exact values NR in abstract.
- Transferability to deployable MI-EEG decoding: Medium. Strongest lesson is that MCU deployment of compressed EEG deep models is feasible and measurable end to end \[Liu20b\].
- Evidence label: Secondary support.

### \[Zan21\]

- Paper ID: \[Zan21\]
- Bibliographic record: Marcello Zanghieri, …, and L. Benini. *Low-Latency Detection of Epileptic Seizures from iEEG with Temporal Convolutional Networks on a Low-Power Parallel MCU*. 2021 IEEE Sensors Applications Symposium, 2021, pp. 1-6.
- Task: Real-time seizure onset detection from iEEG.
- Model type: Temporal convolutional network.
- Optimization technique: Deployability-oriented TCN design and low-power parallel execution.
- Hardware platform: Commercial low-power parallel MCU.
- Runtime and deployment toolchain: 1-core and 8-core MCU execution.
- Baseline FP32 accuracy: Same sensitivity and specificity as state of the art HD computing. Exact sample accuracy NR.
- Optimized accuracy: No performance drop versus state of the art while improving delay.
- Latency: 5.68 ms on 1 core and 1.46 ms on 8 cores.
- Memory and model size: NR in abstract.
- Power and energy: 124.5 μJ on 1 core and 51.2 μJ on 8 cores.
- Transferability to deployable MI-EEG decoding: Medium to high. The task differs, but the low-power TCN deployment lesson is directly useful for online EEG decoding \[Zan21\].
- Evidence label: Secondary support.

### \[Bus24\]

- Paper ID: \[Bus24\]
- Bibliographic record: Paola Busia, …, and Luca Benini. *Reducing False Alarms in Wearable Seizure Detection With EEGformer: A Compact Transformer Model for MCUs*. IEEE Transactions on Biomedical Circuits and Systems, 2024, pp. 608-621.
- Task: Wearable seizure detection.
- Model type: Compact transformer named EEGformer.
- Optimization technique: Hardware-oriented design exploration for MCUs.
- Hardware platform: Apollo4 MCU, GAP8 MCU, GAP9 MCU.
- Runtime and deployment toolchain: MCU deployment across three commercial platforms.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: Competitive detection probability with reduced false alarms. 73% detection probability and 0.15 FP per h on CHB-MIT.
- Latency: 13.7 ms per inference on GAP9.
- Memory and model size: NR in abstract.
- Power and energy: 0.31 mJ per inference on GAP9.
- Transferability to deployable MI-EEG decoding: Medium. This is one of the strongest non-MI examples showing that compact transformer-style EEG models can fit low-power MCUs \[Bus24\].
- Evidence label: Secondary support.

### \[Ing23\]

- Paper ID: \[Ing23\]
- Bibliographic record: T. Ingolfsson, …, and Luca Benini. *EpiDeNet: An Energy-Efficient Approach to Seizure Detection for Embedded Systems*. 2023 IEEE Biomedical Circuits and Systems Conference, 2023, pp. 1-5.
- Task: Seizure detection with four EEG channels.
- Model type: Lightweight seizure detection network.
- Optimization technique: Compact architecture plus weighted loss for imbalanced data.
- Hardware platform: Arm Cortex-M4F, Arm Cortex-M7, GAP8, GAP9.
- Runtime and deployment toolchain: Embedded evaluation across Arm and PULP platforms.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: Successful detection of 91.16% and 92.00% seizure events on CHB-MIT and PEDESITE.
- Latency: High-performance throughput reported as 726.46 MMAC s. Absolute latency NR in abstract.
- Memory and model size: NR.
- Power and energy: 0.051 mJ per inference on GAP9 and 40 GMAC s per W.
- Transferability to deployable MI-EEG decoding: Medium. Excellent for embedded efficiency benchmarking, but class imbalance and event-detection framing differ sharply from MI \[Ing23\].
- Evidence label: Secondary support.

### \[Kav23\]

- Paper ID: \[Kav23\]
- Bibliographic record: Ali Kavoosi, …, and Timothy Denison. *MorpheusNet: Resource efficient sleep stage classifier for embedded on-line systems*. IEEE International Conference on Systems, Man, and Cybernetics, 2023, pp. 2315-2320.
- Task: Sleep-stage classification.
- Model type: Compact sleep-stage classifier.
- Optimization technique: Compact architecture and INT8 quantization.
- Hardware platform: Arm Cortex-M4.
- Runtime and deployment toolchain: Firmware implementation on Cortex-M4.
- Baseline FP32 accuracy: NR in abstract.
- Optimized accuracy: Comparable to state of the art with only 0.95 pp average drop after 8-bit quantization.
- Latency: 1.6 s.
- Memory and model size: Up to 280× smaller than state of the art.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Low to medium. Good evidence that EEG deep models can be made tiny, but time scale and online constraints differ from fast MI control \[Kav23\].
- Evidence label: Secondary support.

### \[Bha25\]

- Paper ID: \[Bha25\]
- Bibliographic record: Jyotiska Bharadwaj, Divyasikha Sethia. *Towards Portable Mental Stress Detection Systems: A TinyML Approach for EEG Analysis*. 2025 International Conference on Intelligent Computing and Knowledge Extraction, 2025, pp. 1-6.
- Task: EEG-based stress detection.
- Model type: Lightweight feed-forward neural network.
- Optimization technique: Quantization-aware training and pruning.
- Hardware platform: Portable targets described as smartphones and smartwatches.
- Runtime and deployment toolchain: TinyML-oriented deployment. Exact software stack NR.
- Baseline FP32 accuracy: NR.
- Optimized accuracy: 99.74% on EEGMAT.
- Latency: 84.77 ms.
- Memory and model size: 91.3% model-size reduction.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Low to medium. Relevant mainly because it is one of the few EEG deployment papers in the library to explicitly combine QAT and pruning \[Bha25\].
- Evidence label: Secondary support.

### \[Xin24\]

- Paper ID: \[Xin24\]
- Bibliographic record: L. Xing, Alexander J. Casson. *Deep Autoencoder for Real-Time Single-Channel EEG Cleaning and Its Smartphone Implementation Using TensorFlow Lite With Hardware Software Acceleration*. IEEE Transactions on Biomedical Engineering, 2024, pp. 3111-3122.
- Task: Real-time single-channel EEG artifact removal.
- Model type: Deep autoencoder.
- Optimization technique: Smartphone deployment through TensorFlow Lite delegates and hardware acceleration.
- Hardware platform: Smartphone AI accelerator environment.
- Runtime and deployment toolchain: TensorFlow Lite with delegate-based acceleration.
- Baseline FP32 accuracy: Artifact-removal correlation metrics reported instead of classification accuracy.
- Optimized accuracy: Correlation coefficients 0.96, 0.85, 0.70, and 0.79 across clean reconstruction and artifact categories.
- Latency: Processes a 4 s EEG window within 5 ms.
- Memory and model size: NR.
- Power and energy: NR.
- Transferability to deployable MI-EEG decoding: Low to medium. Useful mainly for the deployment-toolchain story and for a full-stack pipeline argument where preprocessing may also run on device \[Xin24\].
- Evidence label: Secondary support.

## 3. Optimization methods summary

| Method | Direct MI evidence | Secondary transferable evidence | Audit bottom line | Thesis use |
|:---|:---|:---|:---|:---|
| PTQ and INT8 | Strong in \[Sch20\], \[Wan22\], \[Ene23\] | Reinforced by \[Tru18\], \[Kav23\] | Best-supported method in the library for direct MI deployment. Accuracy loss is usually small when models are already compact. | Use as the default compression baseline. |
| QAT | Weak direct MI evidence in current library | Most explicit EEG deployment signal is \[Bha25\]. Additional emotion-recognition QAT exists but is less deployment-complete. | Clear gap. QAT is thesis-relevant, but the library has much less direct MI hardware evidence than for PTQ. | Frame as a promising but under-benchmarked alternative to PTQ. |
| Structured channel reduction | Strong in \[Wan20\], \[Wan22\], \[Hua24\], \[Mwa23\] | Also present in \[Fen22b\] | Very useful because it reduces both signal acquisition burden and model cost. Often more transferable than weight pruning alone. | Use heavily in Chapter 3 design rationale. |
| Unstructured pruning | Direct MI evidence in \[Vis21\] | Limited transfer value elsewhere | Compression gains are real, but runtime wins on MCUs are rarely shown. Sparse software stacks matter. | Use cautiously. Do not equate sparsity with speedup. |
| Neuron and layer pruning | Direct MI evidence in \[Zha22\] | Some indirect support from secondary papers | Can reduce model size and compute, but embedded deployment evidence is incomplete. | Good supporting method, not yet a main thesis pillar. |
| Mixed precision | Direct deep-MI evidence is thin in this library | Stronger support exists in non-deep EEG and general biomedical precision work | Important conceptually, but current direct evidence is weaker than plain INT8 PTQ. | Mention as future work or a secondary experiment. |
| Knowledge distillation | Direct MI evidence in \[Hua24\] and earlier canonical \[Sak17\] | Some 2025 MI KD papers exist, but deployment metrics are sparse | KD is better supported as an accuracy-recovery method under low-density or lightweight settings than as a proven hardware optimization path. | Use to justify student-model design, not to claim embedded efficiency alone. |
| Runtime and toolchain optimization | Strong in \[Bek24\] and \[Xin24\] | Also relevant to secondary wearable deployments | Software stack choice can change latency by multiples even without changing the model. | Reserve a subsection in Chapter 4 for runtime choice. |

### Method-level takeaways

- PTQ plus compact architecture is the most defensible core path for a thesis on deployable MI EEG decoding \[Sch20, Wan20, Wan22, Ene23\].
- Channel selection is more than a preprocessing trick. In this literature it acts as a hardware-relevant co-design variable because it lowers sensor burden, input tensor size, memory traffic, and compute \[Wan20, Wan22, Hua24\].
- Pruning evidence is much stronger for model compression than for end-to-end edge speedups. This matters because many master’s theses overstate the practical value of high sparsity \[Vis21, Zha22\].
- KD is useful when the thesis wants to preserve performance under low-density montages or student-model constraints, but the current library does not show KD as a mature embedded deployment recipe with latency and energy numbers \[Hua24, Sak17\].
- QAT is under-covered relative to PTQ. The thesis should not claim that QAT is the dominant proven method in embedded MI EEG unless new direct evidence is added.

## 4. Platform summary

| Platform class | Representative papers | Reported operating points | Strength for this thesis | Main caveat |
|:---|:---|:---|:---|:---|
| Arm Cortex-M4 and M7 MCUs | \[Wan20\], \[Ene23\], \[Kav23\] | 44 to 137 ms per inference, 2.55 to 18.1 mJ where reported | Closest to lightweight wearable and TinyML deployment | Often tight memory and weaker acceleration than PULP-class chips |
| PULP and GAP8 or GAP9 parallel MCUs | \[Sch20\], \[Wan22\], \[Bia24\], \[Ing23\], \[Bus24\] | 2.95 to 14.9 ms and 30 μJ to 0.76 mJ in direct MI, 0.051 to 0.31 mJ in seizure work | Best direct evidence base for low-power high-efficiency EEG inference | Still a specialized hardware family, not the default for all labs |
| Embedded CPU runtimes | \[Bek24\] | 5 to 6× speedup from runtime engine choice | Useful if thesis prototype runs on SBC or laptop-class CPU first | Latency without energy is an incomplete deployment story |
| FPGA and ASIC style accelerators | \[Fen22b\], \[Pac24\], \[R22\] | 24.4 ms and 0.267 mJ in one accelerator study, major power and memory reductions in platform comparisons | Good upper bound on hardware efficiency and co-design direction | Less directly transferable to software-only embedded deployment |
| Jetson and embedded GPU | \[Pac24\], \[Mwa23\] | 48.7 ms in Jetson TX2 study | Helpful for comparison against heavier edge devices | Power envelope and memory assumptions are not wearable-like |
| Smartphone accelerators | \[Xin24\] | 5 ms for a 4 s preprocessing window | Useful for full-stack mobile BCI pipelines | Artifact-removal and MI classification are different workloads |

### Platform-level takeaways

- The PULP and GAP line is the strongest evidence base in this project for showing explicit accuracy-latency-energy trade-offs in EEG edge inference \[Sch20, Wan22, Bia24\].
- Cortex-M deployments are slower but often more thesis-relevant if the target is minimal hardware complexity or lower system cost \[Wan20, Ene23\].
- CPU runtime work matters because software-stack choice can move latency enough to change whether a model feels online or not \[Bek24\].
- FPGA and ASIC papers are valuable comparison points, but they should not be used as direct performance baselines for a software-only embedded prototype \[Fen22b, Pac24, R22\].

## 5. Unresolved gaps for this thesis

- Direct MI EEG evidence for QAT is thin. The current library supports PTQ strongly, but not a strong claim that QAT has already been validated on low-power embedded MI hardware.
- Direct MI papers with true end-to-end pruning deployment are also thin. Compression ratios are reported, but sparse inference latency and energy are usually not \[Vis21, Zha22\].
- Cross-session and online robustness remain weakly benchmarked. Much of the literature is still offline and public-dataset centric. The strongest counterweight is the on-device adaptation thread \[Bia24, Mei24, Nza25\].
- Many papers report only model inference. They often do not include EEG buffering, filtering, artifact handling, communication, or control-loop overhead. This weakens claims about real-time closed-loop BCI readiness \[Pac24, Bek24, Xin24\].
- Accuracy numbers are not directly comparable across datasets, validation schemes, and class formulations. Physionet, BCIC IV-2a, HaLT, CHB-MIT, and private wearable datasets create very different operating points.
- Energy reporting is not standardized. Some papers report mJ per inference, some GMAC s per W, some only power, and some only estimated operation counts. A thesis should normalize cautiously.
- Low-density and wearable electrode setups are still underrepresented in direct MI deployment papers. KD work helps on channel scarcity, but hardware-backed low-density MI deployment evidence is still modest \[Hua24\].

## Ranked top-10 reading list

| Rank | Paper | Why it should be read early |
|:---|:---|:---|
| 1 | \[Wan22\] | Best overall direct match to embedded MI decoding with explicit accuracy, latency, energy, and channel-reduction trade-offs. |
| 2 | \[Sch20\] | Strongest clean INT8 deployment paper for EEGNet on low-power parallel hardware. |
| 3 | \[Wan20\] | Canonical MCU-oriented MI paper for accuracy versus memory trade-off framing. |
| 4 | \[Bia24\] | Direct answer to the adaptation problem under edge constraints. Useful if the thesis mentions inter-session drift. |
| 5 | \[Ene23\] | Concrete Arduino-class PTQ deployment. Good for realistic prototyping arguments. |
| 6 | \[Ing20\] | Canonical embedded-friendly MI backbone paper. Essential for model selection discussion. |
| 7 | \[Tra23\] | Best paper for showing that MCU-aware search can outperform accuracy-only architecture selection. |
| 8 | \[Hua24\] | Best direct MI KD paper in the library for low-density and student-model arguments. |
| 9 | \[Pac24\] | Useful platform-comparison paper for explaining why deployment target matters. |
| 10 | \[Zan21\] | Best secondary comparator for low-latency EEG TCN deployment on a parallel MCU. |

## Five papers most useful for direct use in Chapters 3 and 4

1.  \[Wan22\]
    - Best direct benchmark for an embedded MI model with quantization, channel reduction, and strong deployment numbers.
2.  \[Sch20\]
    - Best citation for INT8 quantization with explicit energy and latency benefit on low-power parallel hardware.
3.  \[Wan20\]
    - Best citation for the memory-accuracy trade-off and for justifying temporal downsampling and channel reduction.
4.  \[Bia24\]
    - Best citation if the thesis treats online adaptation, personalization, or continual learning as part of deployable BCI design.
5.  \[Ene23\]
    - Best citation for low-cost MCU deployment and for a PTQ story on commodity embedded hardware.

## Recommended citation strategy for a master’s thesis

- Use a narrow direct-evidence backbone for the main related-work argument:
  - \[Wan20\], \[Sch20\], \[Wan22\], \[Ene23\], \[Bia24\], \[Ing20\], \[Tra23\], \[Pac24\], \[Bek24\].
- Use a separate paragraph or table for direct MI optimization support that lacks full device metrics:
  - \[Vis21\], \[Zha22\], \[Hua24\], and, if historical context is needed, \[Sak17\].
- Place non-MI EEG papers in a clearly labeled transfer section only:
  - \[Tru18\], \[Liu20b\], \[Zan21\], \[Bus24\], \[Ing23\], \[Kav23\], \[Bha25\], \[Xin24\].
- In Chapter 3, cite papers by methodological role rather than by date:
  - PTQ and INT8 deployment: \[Sch20\], \[Wan22\], \[Ene23\]
  - Channel selection and compact input design: \[Wan20\], \[Wan22\], \[Hua24\]
  - Architecture choice under embedded constraints: \[Ing20\], \[Tra23\], \[Asa25\]
  - Runtime-engine choice and deployment stack: \[Bek24\], \[Xin24\]
- In Chapter 4, compare only against studies with similar task and hardware assumptions:
  - MCU against MCU and PULP against PULP first.
  - Keep FPGA and Jetson numbers as outer comparison points, not as direct baselines \[Fen22b, Pac24, Mwa23\].
- Use claim strength that matches evidence strength:
  - “shown in direct MI deployment studies” for \[Wan20\], \[Sch20\], \[Wan22\], \[Ene23\], \[Bia24\]
  - “supported by direct MI optimization studies without full hardware benchmarking” for \[Vis21\], \[Zha22\], \[Hua24\]
  - “suggested by transferable non-MI EEG deployment evidence” for \[Tru18\], \[Zan21\], \[Bus24\], \[Ing23\], \[Kav23\], \[Bha25\]

## Explicit warnings about overclaiming

- Do not present seizure, sleep, stress, or artifact-removal results as if they were direct MI BCI evidence. They are only partial transfers.
- Do not equate model compression with on-device speedup. Sparse models often need sparse-aware kernels or hardware before latency actually drops \[Vis21, Zha22\].
- Do not compare accuracy across papers as if they share a common benchmark. Different datasets, window sizes, validation protocols, class counts, and subject splits can overwhelm the effect of the optimization method.
- Do not claim that QAT is well established for embedded MI EEG from this library alone. PTQ is much better supported than QAT here.
- Do not use FPGA, ASIC, or Jetson results as if they were direct evidence for low-power wearable feasibility. Their memory systems, clocks, and power envelopes are materially different \[Fen22b, Pac24, Mwa23\].
- Do not describe a model as real-time unless the paper reports end-to-end latency under the same buffering and preprocessing assumptions that the thesis will use.
- Do not treat low-density KD results as a free compression win. They improve deployability mainly by preserving accuracy under fewer channels, not by automatically proving lower system energy \[Hua24\].
- Do not infer battery life from per-inference energy without stating duty cycle, window stride, standby cost, sensing cost, and wireless overhead.

---

## References

\[Wan22\] X. Wang, M. Hersche, M. Magno, and L. Benini, “MI-BMInet: An Efficient Convolutional Neural Network for Motor Imagery Brain–Machine Interfaces With EEG Channel Selection,” *IEEE Sensors Journal*, vol. 24, pp. 8835–8847, Mar. 2022, doi: [10.1109/JSEN.2024.3353146](https://doi.org/10.1109/JSEN.2024.3353146).

\[Sch20\] T. Schneider, X. Wang, M. Hersche, L. Cavigelli, and L. Benini, “Q-EEGNet: an Energy-Efficient 8-bit Quantized Parallel EEGNet Implementation for Edge Motor-Imagery Brain-Machine Interfaces,” *2020 IEEE International Conference on Smart Computing (SMARTCOMP)*, pp. 284–289, Apr. 2020, doi: [10.1109/SMARTCOMP50058.2020.00065](https://doi.org/10.1109/SMARTCOMP50058.2020.00065).

\[Wan20\] X. Wang, M. Hersche, B. Tömekçe, B. Kaya, M. Magno, and L. Benini, “An Accurate EEGNet-based Motor-Imagery Brain–Computer Interface for Low-Power Edge Computing,” *2020 IEEE International Symposium on Medical Measurements and Applications (MeMeA)*, pp. 1–6, Mar. 2020, doi: [10.1109/MeMeA49120.2020.9137134](https://doi.org/10.1109/MeMeA49120.2020.9137134).

\[Ene23\] D. Enériz, N. Medrano, B. Calvo, and D. Antolín, “Low-power EEGNet-based Brain-Computer Interface implemented on an Arduino Nano 33 Sense,” *2023 38th Conference on Design of Circuits and Integrated Systems (DCIS)*, pp. 1–5, Nov. 2023, doi: [10.1109/DCIS58620.2023.10335978](https://doi.org/10.1109/DCIS58620.2023.10335978).

\[Bia24\] S. Bian *et al.*, “On-device Learning of EEGNet-based Network For Wearable Motor Imagery Brain-Computer Interface,” *Proceedings of the 2024 ACM International Symposium on Wearable Computers*, Aug. 2024, doi: [10.1145/3675095.3676607](https://doi.org/10.1145/3675095.3676607).

\[Asa25\] N. O. Asante, L. Mei, X. Wang, and M. Magno, “TinyEEGConformer: An Attention-Based EEG Decoding Model for Embedded Systems,” *2025 IEEE Sensors Applications Symposium (SAS)*, pp. 1–6, Jul. 2025, doi: [10.1109/SAS65169.2025.11105112](https://doi.org/10.1109/SAS65169.2025.11105112).

\[Tra23\] A. Tragoudaras, C. Antoniadis, and Y. Massoud, “TinyML for EEG Decoding on Microcontrollers,” *2023 IEEE International Symposium on Circuits and Systems (ISCAS)*, pp. 1–5, May 2023, doi: [10.1109/ISCAS46773.2023.10181950](https://doi.org/10.1109/ISCAS46773.2023.10181950).

\[Pac24\] F. Pacini, T. Pacini, G. Lai, A. M. Zocco, and L. Fanucci, “Design and Evaluation of CPU-, GPU-, and FPGA-Based Deployment of a CNN for Motor Imagery Classification in Brain-Computer Interfaces,” *Electronics*, Apr. 2024, doi: [10.3390/electronics13091646](https://doi.org/10.3390/electronics13091646).

\[Bek24\] O. Bekhelifi and N. Berrached, “On Optimizing Deep Neural Networks Inference on CPUs for Brain-Computer Interfaces using Inference Engines,” *2024 IEEE International Symposium on Circuits and Systems (ISCAS)*, pp. 1–5, May 2024, doi: [10.1109/ISCAS58744.2024.10558617](https://doi.org/10.1109/ISCAS58744.2024.10558617).

\[Fen22b\] L. Feng, H. Shan, Y. Zhang, and Z. Zhu, “An Efficient Model-Compressed EEGNet Accelerator for Generalized Brain-Computer Interfaces With Near Sensor Intelligence,” *IEEE Transactions on Biomedical Circuits and Systems*, vol. 16, pp. 1239–1249, Oct. 2022, doi: [10.1109/TBCAS.2022.3215962](https://doi.org/10.1109/TBCAS.2022.3215962).

\[Mwa23\] T. Mwata-Velu, E. Niyonsaba-Sebigunda, J. Aviña-Cervantes, J. Ruiz-Pinales, N. Velu-A-Gulenga, and A. A. Alonso-Ramírez, “Motor Imagery Multi-Tasks Classification for BCIs Using the NVIDIA Jetson TX2 Board and the EEGNet Network,” *Sensors (Basel, Switzerland)*, vol. 23, Apr. 2023, doi: [10.3390/s23084164](https://doi.org/10.3390/s23084164).

\[Ing20\] T. Ingolfsson, M. Hersche, X. Wang, N. Kobayashi, L. Cavigelli, and L. Benini, “EEG-TCNet: An Accurate Temporal Convolutional Network for Embedded Motor-Imagery Brain–Machine Interfaces,” *2020 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*, pp. 2958–2965, May 2020, doi: [10.1109/SMC42975.2020.9283028](https://doi.org/10.1109/SMC42975.2020.9283028).

\[Vis21\] Vishnupriya., N. Robinson, R. Reddy, and C. Guan, “Performance Evaluation of Compressed Deep CNN for Motor Imagery Classification using EEG,” *2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*, pp. 795–799, Nov. 2021, doi: [10.1109/EMBC46164.2021.9631018](https://doi.org/10.1109/EMBC46164.2021.9631018).

\[Zha22\] J. Zhang and K. Li, “A Pruned Deep Learning Approach for Classification of Motor Imagery Electroencephalography Signals,” *2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*, pp. 4072–4075, Jul. 2022, doi: [10.1109/EMBC48229.2022.9871078](https://doi.org/10.1109/EMBC48229.2022.9871078).

\[Hua24\] X.-Y. Huang, S.-Y. Chen, and C.-S. Wei, “Enhancing Low-Density EEG-Based Brain-Computer Interfacing With Similarity-Keeping Knowledge Distillation,” *IEEE Transactions on Emerging Topics in Computational Intelligence*, vol. 8, pp. 1156–1166, Apr. 2024, doi: [10.1109/TETCI.2023.3335943](https://doi.org/10.1109/TETCI.2023.3335943).

\[Tru18\] N. D. Truong *et al.*, “Integer Convolutional Neural Network for Seizure Detection,” *IEEE Journal on Emerging and Selected Topics in Circuits and Systems*, vol. 8, pp. 849–857, Jun. 2018, doi: [10.1109/JETCAS.2018.2842761](https://doi.org/10.1109/JETCAS.2018.2842761).

\[R22\] S. R. and M. Rao, “Hardware characterization of Integer-Net based seizure detection models on FPGA,” *2022 IEEE 15th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)*, pp. 224–231, Dec. 2022, doi: [10.1109/MCSoC57363.2022.00043](https://doi.org/10.1109/MCSoC57363.2022.00043).

\[Liu20b\] X. Liu and A. Richardson, “Edge deep learning for neural implants: a case study of seizure detection and prediction,” *Journal of Neural Engineering*, vol. 18, Dec. 2020, doi: [10.1088/1741-2552/abf473](https://doi.org/10.1088/1741-2552/abf473).

\[Zan21\] M. Zanghieri, A. Burrello, S. Benatti, K. A. Schindler, and L. Benini, “Low-Latency Detection of Epileptic Seizures from iEEG with Temporal Convolutional Networks on a Low-Power Parallel MCU,” Aug. 23, 2021. doi: [10.1109/SAS51076.2021.9530181](https://doi.org/10.1109/SAS51076.2021.9530181).

\[Bus24\] P. Busia *et al.*, “Reducing False Alarms in Wearable Seizure Detection With EEGformer: A Compact Transformer Model for MCUs,” *IEEE Transactions on Biomedical Circuits and Systems*, vol. 18, pp. 608–621, Jan. 2024, doi: [10.1109/TBCAS.2024.3357509](https://doi.org/10.1109/TBCAS.2024.3357509).

\[Ing23\] T. Ingolfsson *et al.*, “EpiDeNet: An Energy-Efficient Approach to Seizure Detection for Embedded Systems,” *2023 IEEE Biomedical Circuits and Systems Conference (BioCAS)*, pp. 1–5, Aug. 2023, doi: [10.1109/BioCAS58349.2023.10388554](https://doi.org/10.1109/BioCAS58349.2023.10388554).

\[Kav23\] A. Kavoosi *et al.*, “MorpheusNet: Resource efficient sleep stage classifier for embedded on-line systems,” *Conference proceedings. IEEE International Conference on Systems, Man, and Cybernetics*, vol. 2023, pp. 2315–2320, Oct. 2023, doi: [10.1109/SMC53992.2023.10394274](https://doi.org/10.1109/SMC53992.2023.10394274).

\[Bha25\] J. Bharadwaj and D. Sethia, “Towards Portable Mental Stress Detection Systems: A TinyML Approach for EEG Analysis,” in *2025 International Conference on Intelligent Computing and Knowledge Extraction (ICICKE)*, Jun. 2025, pp. 1–6. doi: [10.1109/ICICKE65317.2025.11136441](https://doi.org/10.1109/ICICKE65317.2025.11136441).

\[Xin24\] L. Xing and A. J. Casson, “Deep Autoencoder for Real-Time Single-Channel EEG Cleaning and Its Smartphone Implementation Using TensorFlow Lite With Hardware/Software Acceleration,” *IEEE Transactions on Biomedical Engineering*, vol. 71, pp. 3111–3122, Jun. 2024, doi: [10.1109/TBME.2024.3408331](https://doi.org/10.1109/TBME.2024.3408331).

\[Sak17\] S. Sakhavi and C. Guan, “Convolutional neural network-based transfer learning and knowledge distillation using multi-subject data in motor imagery BCI,” *2017 8th International IEEE/EMBS Conference on Neural Engineering (NER)*, pp. 588–591, May 2017, doi: [10.1109/NER.2017.8008420](https://doi.org/10.1109/NER.2017.8008420).

\[Mei24\] L. Mei *et al.*, “An Ultra-Low Power Wearable BMI System With Continual Learning Capabilities,” *IEEE Transactions on Biomedical Circuits and Systems*, vol. 19, pp. 511–522, Sep. 2024, doi: [10.1109/TBCAS.2024.3457522](https://doi.org/10.1109/TBCAS.2024.3457522).

\[Nza25\] P. S. Nzakuna *et al.*, “Real-world evaluation of deep learning decoders for motor imagery EEG-based BCIs,” *Frontiers in Systems Neuroscience*, vol. 19, Dec. 2025, doi: [10.3389/fnsys.2025.1718390](https://doi.org/10.3389/fnsys.2025.1718390).
