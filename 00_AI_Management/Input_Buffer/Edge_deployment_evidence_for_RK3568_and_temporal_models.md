---
type: Evidence Report
status: Active
purpose: Summarizes edge deployment literature (RK3568, NPU, MCU) for Chapters 3 and 4.
---

# Edge deployment evidence for RK3568 and temporal models

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Overall judgment](#overall-judgment)
- [Closest evidence for RK3568 and comparable embedded Linux platforms](#closest-evidence-for-rk3568-and-comparable-embedded-linux-platforms)
- [Direct motor-imagery EEG deployment evidence](#direct-motor-imagery-eeg-deployment-evidence)
- [Adjacent biomedical transformer evidence](#adjacent-biomedical-transformer-evidence)
- [Generic temporal model and toolchain evidence](#generic-temporal-model-and-toolchain-evidence)
- [Transferability to motor-imagery EEG decoding](#transferability-to-motor-imagery-eeg-decoding)
- [What this literature can support in a thesis chapter](#what-this-literature-can-support-in-a-thesis-chapter)
- [Platform choice implications](#platform-choice-implications)
- [Gaps that should be named explicitly](#gaps-that-should-be-named-explicitly)
- [Thesis-safe conclusion](#thesis-safe-conclusion)
- [References](#references)

A clear pattern emerges from the literature. Strong direct evidence exists that compact CNNs and small transformer-like temporal models can run in real time on very low-power edge hardware, but the strongest measured evidence comes from Cortex-M MCUs, PULP class parallel MCUs, and embedded FPGAs rather than from Rockchip RK3568 class NPUs. Direct RK3568 evidence is thin and mostly comes from non-EEG workloads \[Ism23, You24\]. That makes the broad feasibility claim defensible, but any thesis claim that specifically centers RK3568 and RKNN for motor-imagery EEG must be framed as an informed extrapolation rather than a directly settled result.

## Overall judgment

The evidence base supports four claims.

- Compact motor-imagery EEG models are already deployable on devices much smaller than RK3568 class SBCs. Measured runtimes range from 2.95 ms to 137 ms per inference, with energy from 30 $`\mu`$J to 4.28 mJ, depending on model size and hardware \[Wan20, Sch20, Wan22b, Ene23, Bia24\].
- Tiny transformer and other temporal models are also deployable at the edge when they are heavily quantized, scheduled for streaming, and matched to the hardware memory hierarchy \[Bur21b, Jun24, Bus24, Bus24b, Bur22, Mir24, Lin24\].
- Direct RK3568 evidence is real but narrow. It shows that RKNN based NPU offload can materially accelerate temporal inference and that RK3568 can run quantized or half-precision networks at a few hundred milliseconds per sample on a moderate board power budget \[Ism23, You24\].
- The weakest point in the literature is the exact combination this thesis cares about most: motor-imagery EEG plus transformer-like decoding plus RK3568 or RKNN. That combination was not directly established in the retrieved corpus.

## Closest evidence for RK3568 and comparable embedded Linux platforms

| Source | Hardware | Runtime and toolchain | Model and input | Numeric deployment evidence and thesis use |
|:---|:---|:---|:---|:---|
| \[You24\] | Rockchip RK3568 SoC with NPU | PyTorch model converted to RKNN | CRNN plus BiGRU for Morse audio decoding using sliding windows | Decoding a one-minute audio signal fell from 12.63 s on CPU to 1.67 s on NPU, roughly a 7 to 8 times speedup. This is the closest direct evidence that RKNN on RK3568 can accelerate a temporal model, but the input is audio rather than EEG, and recurrent audio decoding is easier to map than attention-heavy EEG transformers. Transferability risk is medium. |
| \[Ism23\] | Rockchip RK3568 and RK3588, compared with Jetson Nano | Rockchip deployment of YOLOv4 in half precision and asymmetric quantization | CNN object detection on image frames | The abstract reports RK3568 average inference times of 481 ms at 5.5 W for one model form and 1385 ms for the quantized form, with RK3588 faster at 149 ms and 361 ms. The abstract wording is internally inconsistent about which precision matches which latency, so the numbers are usable only as board-level scale estimates. This is useful for board power and general NPU capability, but transferability to EEG temporal decoding is high risk because the workload is image detection rather than 1D sequence modeling. |
| \[Ido24\] | Raspberry Pi 4 | Python based profiling of standard BCI training and inference pipeline | Ten standard MI classifiers including ANN and Riemannian models | For the neural network models on RPi4, the paper reports 1.74 s training time, 0.405 s inference time, 1154.9 MiB peak memory, and 405.2 MiB incremental memory use, with about 84.3% accuracy and 84.7% precision. This is direct MI evidence on an embedded Linux SBC, but it is not an NPU study and does not show an aggressively optimized edge stack. Transferability risk is low for pipeline realism and medium for optimized deployment claims. |
| \[Pac24\] | Desktop CPU, Jetson Nano 2GB, Xilinx Ultrascale+ ZU7EV FPGA | CPU baseline, TF Lite on Jetson Nano, FPG-AI tool flow on FPGA | EEGNet style CNN for MI classification on a 29 participant EEG dataset | The FPGA path reports 12.97 ms inference time, 1.47 W power, 6.37 MB memory footprint, and 77% test accuracy. The CPU baseline reports 121.57 ms, 13.22 W, and 476 MB. The paper states that the FPGA cuts power by up to 89% relative to CPU and up to 71% relative to GPU, with about 98% lower memory, while the Jetson Nano remains the fastest. This is not RK3568, but it is a strong comparable embedded platform study for platform choice arguments. Transferability risk is low to medium. |

## Direct motor-imagery EEG deployment evidence

| Source | Hardware | Runtime and toolchain | Model and input | Numeric deployment evidence and thesis use |
|:---|:---|:---|:---|:---|
| \[Wan20\] | ARM Cortex-M4F and Cortex-M7 MCUs | Embedded deployment of scaled EEGNet variants | EEGNet for Physionet EEG Motor Movement and Imagery tasks with temporal downsampling, channel selection, and shorter windows | Standard EEGNet reached 82.43%, 75.07%, and 65.07% on 2, 3, and 4 class tasks. Scaled variants reduced memory by 7.6 times with only 0.31% accuracy loss, or by 15 times with 2.51% loss. The smallest deployed model ran in 101 ms at 4.28 mJ on Cortex-M4F, and a medium model ran in 44 ms at 18.1 mJ on Cortex-M7. This is one of the best direct feasibility anchors for an MI EEG thesis chapter. Transferability risk is low. |
| \[Sch20\] | Mr. Wolf PULP SoC with 8 core compute cluster | 8-bit fixed-point, hardware-aware parallel implementation | Quantized EEGNet for 4 class MI EEG | The paper reports only 0.4% accuracy loss from 8-bit quantization, 64 times speedup over a single-core layer-wise baseline, up to 85% memory reduction, 5.82 ms latency, and 0.627 mJ per inference. Energy efficiency reached 21.0 GMAC per W, reported as 256 times better than an ARM Cortex-M7 implementation. This is very strong evidence that carefully quantized CNN EEG decoders can be deeply power efficient on parallel low-power processors. Transferability risk is low. |
| \[Wan22b\] | Leading-edge parallel ultralow-power PULP MCUs | 8-bit quantization plus automatic channel selection | MI-BMInet CNN for MI EEG, with channel reduction | The final two-class solution reaches 82.51% accuracy while using 6.4 times fewer EEG channels, and consumes as little as 30 $`\mu`$J per inference with 2.95 ms latency. This is arguably the strongest direct evidence that MI EEG decoding can be both accurate and extremely cheap on edge hardware when the model is designed for deployment from the start. Transferability risk is low. |
| \[Ene23\] | Arduino Nano 33 Sense with ARM Cortex-M4F | 8-bit integer post-training quantization | EEGNet based MI EEG model on Physionet Motor Movement and Imagery data | Quantization caused a mean accuracy downgrade of 2.64 $`\pm`$ 0.77%. The deployed model ran at 137 ms and 2.55 mJ per inference, described as about 40% lower energy than another EEGNet implementation on the same MCU \[Ene23\]. This is direct, thesis-friendly evidence for low-cost wearable deployment. Transferability risk is low. |
| \[Bia24\] | GAP9 low-power parallel RISC-V processor | On-device learning engine for EEGNet | Wearable MI EEG recognition on Physionet with online adaptation | The paper reports up to 7.31% accuracy gain over the baseline under subject shift, with 15.6 kB memory footprint. Inference takes 14.9 ms and 0.76 mJ, while a single online update takes 20 $`\mu`$s and 0.83 $`\mu`$J. This is unusually valuable because it addresses subject variability, a real weakness of static MI decoders in practice. Transferability risk is low. |
| \[Asa25\] | Arm Cortex-M processors | Embedded evaluation of an attention-based EEG decoder | TinyEEGConformer on BCI Competition IV 2a | TinyEEGConformer achieves 79.63% average accuracy, 0.97% above the baseline EEG Conformer, with 21 times fewer parameters, equal to 37,135 parameters or 145 kB. This is the closest direct paper on attention-based EEG decoding for embedded systems in the retrieved set. However, the available metadata does not report measured latency, energy, or power, so it is best used as architectural evidence rather than as a numeric deployment anchor. Transferability risk is low for task match, but medium for deployment evidence quality. |

## Adjacent biomedical transformer evidence

| Source | Hardware | Runtime and toolchain | Model and input | Numeric deployment evidence and thesis use |
|:---|:---|:---|:---|:---|
| \[Bus22\] | Ambiq Apollo4 MCU | Real-time MCU deployment | EEGformer transformer on raw 4 channel temporal EEG for seizure detection | The model detects 73% of seizure events with 15.2 s average onset latency and 0.8 false positives per hour. On Apollo4 at 96 MHz, inference takes 405 ms and 1.79 mJ. This is the closest raw EEG transformer deployment before the later optimized version. Transferability risk is low to medium because the signal family is EEG, but the task is seizure detection with longer temporal context than MI classification. |
| \[Bus24\] | Apollo4, GAP8, and GAP9 | Hardware-oriented compact transformer deployment | EEGformer for wearable seizure detection on low-channel-count raw EEG | The most efficient implementation on GAP9 reaches 13.7 ms and 0.31 mJ per inference. On CHB-MIT it reports 73% seizure detection probability with 0.15 false positives per hour, and on a second dataset it detects 88% of annotated events with 0.45 false positives per hour. This is one of the strongest adjacent pieces of evidence for transformer-like EEG deployment on edge hardware. Transferability risk is low to medium. |
| \[Bus24b\] | GAP9 | 8-bit integer inference | Tiny transformer for ECG arrhythmia classification | The model uses only 6k parameters, reaches 98.97% accuracy on MIT-BIH, and runs in 4.28 ms with 0.09 mJ per inference. This strongly supports the claim that very small transformer models can be efficient on biosignals, but ECG is cleaner and lower-dimensional than scalp EEG. Transferability risk is medium. |
| \[Bur22\] | GreenWaves GAP8 | PULP deployment of attention-based tiny models | Bioformers for sEMG gesture recognition | The best Bioformer approaches state of the art while reducing parameters and operations by 4.9 times. On GAP8 it runs in 2.72 ms, 0.14 mJ, and occupies 94.2 kB. This is valuable for wearable biosignal edge inference, but sEMG has higher signal-to-noise ratio and more local muscle specificity than MI EEG. Transferability risk is medium. |
| \[Xie23\] | GAP8 | Static and dynamic inference with tiny transformers | Bioformers for sEMG gesture recognition on Ninapro DB6 | The most accurate Bioformer improves accuracy by 3.1% over TEMPONet and uses 7.8 to 44.5 times less energy per inference on GAP8. A three-level dynamic inference scheme cuts energy by another 1.03 to 1.35 times at iso-accuracy. This is useful for arguing that conditional execution can matter as much as architecture choice. Transferability risk is medium. |

## Generic temporal model and toolchain evidence

| Source | Hardware | Runtime and toolchain | Model and input | Numeric deployment evidence and thesis use |
|:---|:---|:---|:---|:---|
| \[Bur21b\] | STM32H7, STM32L4, GAP8 | TinyTransformer kernels for ARM and RISC-V MCUs | Encoder transformer with radar gesture use case | The optimized attention kernels achieve 3.4 times, 1.8 times, and 2.1 times lower latency and energy than prior kernels on STM32H7, STM32L4, and GAP8. A 263 kB transformer fits on GAP8 and runs in 9.24 ms at 0.47 mJ while improving accuracy by 3.5% over a previous convolutional model. This is strong proof that attention blocks can be made MCU-viable when the runtime is attention-aware. Transferability risk is medium. |
| \[Jun24\] | STM32H7, STM32L4, GAP9 | End-to-end deployment framework with fused-weight attention and depth-first tiling | Tiny transformer deployment across several applications, including radar gesture recognition | The framework achieves average latency reductions of 4.79 times against CMSIS-NN on ARM and 2.0 times against PULP-NN on RISC-V. Memory peak falls by up to 6.19 times, fused-weight attention cuts runtime by 1.53 times, and transformer block execution on GAP9 reaches 0.14 ms and 4.92 $`\mu`$J in a radar gesture case. This is a key thesis source for the claim that operator scheduling and memory layout are first-order determinants of feasibility. Transferability risk is medium. |
| \[Mir24\] | GAP9 | Stream-oriented automatic transformation for TCNs | Conv-TasNet style temporal convolution with about 1.2 s receptive field | The stream-oriented conversion reduces MACs by up to 901 times and execution cycles by up to 94.5 times relative to non-streaming models. Hardware tests on GAP9 show that models with about 1.2 s receptive field fit within 128 kB plus 1.5 MB memory and reduce computational intensity by up to 33 times and cycles by up to 313 times. This is a strong non-transformer counterpoint showing that TCNs can be easier to operationalize than attention when long windows are needed. Transferability risk is medium to low for streaming MI EEG pipelines. |
| \[Lin24\] | Xilinx Spartan-7 XC7S15 embedded FPGA | Integer-only quantization with quantization-aware training | Transformer for AIoT time-series forecasting | Compared with a related 8-bit quantized transformer study, the 4-bit design increases test loss by only 0.63% while running up to 132.33 times faster and using 48.19 times less energy. This is powerful evidence that quantized transformers can become edge-feasible on small FPGAs, though the task is forecasting rather than biosignal decoding. Transferability risk is medium to high. |
| \[Rei23b\] | Coral Edge TPU, Coral Dev Board, Intel NCS2, Jetson Nano | Edge TPU oriented transformer deployment methodology using OpenVINO and TensorRT baselines | BERT family and other transformers | The paper demonstrates successful deployment of BERT-Base and BERT-Large on Edge TPU after partitioning problematic layers, and reports extensive latency, power, and energy comparisons across devices, with the Edge TPU retaining the lowest power and energy profile in the study. Exact numeric values are not recoverable from the available metadata here, so this source is best used to support the claim that commercial edge accelerators can run transformers only after model surgery and operator-aware compilation. Transferability risk is medium to high for MI EEG because the models are NLP transformers rather than biosignal decoders. |

## Transferability to motor-imagery EEG decoding

| Evidence family | Transferability risk | Why it transfers or fails to transfer |
|:---|:---|:---|
| Direct MI EEG CNN deployments \[Wan20, Sch20, Wan22b, Ene23, Bia24\] | Low | Same signal family, same task family, similar windowed inference pattern, and direct edge measurements. Best sources for core feasibility claims. |
| Embedded attention-based MI EEG model \[Asa25\] | Low for model form, medium for deployment proof | Direct task match, but the reported metadata does not yet provide the latency and energy detail needed for a hard deployment argument. |
| Raw EEG transformer seizure detection \[Bus22, Bus24\] | Low to medium | Same broad signal family and similar need for low-power continuous monitoring. Risk comes from longer windows, different labels, and different event sparsity. |
| sEMG transformer deployments \[Bur22, Xie23\] | Medium | Wearable biosignal pipeline and gesture-classification setting are relevant, but sEMG is higher SNR and more localized than scalp MI EEG. |
| ECG tiny transformer \[Bus24b\] | Medium | Strong proof of compact transformer efficiency on biosignals, but ECG is more regular and easier to model than EEG. |
| Generic MCU transformer toolchains \[Bur21b, Jun24\] | Medium | Very useful for attention kernel feasibility, quantization, and memory scheduling, but they do not prove EEG-specific accuracy. |
| Streaming TCN evidence \[Mir24\] | Medium to low | Not attention-based, but highly relevant if the thesis compares transformers with lighter temporal alternatives for long windows. |
| RK3568 CRNN audio deployment \[You24\] | Medium | Strong platform match and temporal workload match, but weaker modality match. Useful for RKNN capability claims, not for EEG-specific latency estimates. |
| RK3568 computer vision deployment \[Ism23\] | High | Same board family, but image detection stresses different operators, tensor shapes, and memory traffic than MI EEG or transformer blocks. Useful mainly for board-level power and rough NPU scale. |

## What this literature can support in a thesis chapter

The literature can support a strong statement that on-device MI EEG decoding is already feasible on hardware that is materially more constrained than RK3568 class SBCs \[Wan20, Sch20, Wan22b, Ene23, Bia24\]. That makes raw feasibility the least controversial part of the argument.

It can also support a more specific statement that transformer-like temporal models are deployable on edge hardware when three conditions are met: the model is small, quantization is aggressive, and the runtime is tailored to attention or streaming sequence computation \[Bur21b, Jun24, Bus24, Bus24b, Bur22, Mir24, Lin24\]. In other words, the literature does not suggest that transformers are impossible at the edge. It suggests that naive deployment is usually the wrong baseline.

For RK3568 and RKNN specifically, the literature supports a narrower claim. RK3568 class hardware is plausible for the thesis deployment target because RKNN acceleration has already yielded a large speedup on a temporal model and because RK3568 can sustain moderate-power on-device inference \[You24, Ism23\]. But the literature does not yet provide a direct paper showing a motor-imagery EEG transformer, or even a compact temporal EEG model, running on RK3568 with measured latency, memory, and energy. That gap should be made explicit in the chapter.

## Platform choice implications

Three platform narratives are best supported by the evidence.

- RK3568 class SBC with RKNN
  - Best when the thesis needs embedded Linux, richer I O, and a path to NPU offload in a practical SBC form factor.
  - Weakest point is literature depth. The available evidence is too sparse to make a strong claim about transformer operator support, memory headroom for attention maps, or MI EEG specific latency on RKNN \[Ism23, You24\].
- PULP class parallel MCU such as GAP8 and GAP9
  - Best when the thesis wants the strongest literature-backed energy efficiency story for compact temporal models.
  - This family has the cleanest numeric evidence for tiny transformers, TCNs, and MI EEG CNNs, often at sub-15 ms and sub-1 mJ per inference \[Sch20, Wan22b, Bia24, Bus24, Bus24b, Bur22, Jun24, Mir24\].
- Embedded FPGA
  - Best when the thesis wants deterministic latency, memory compression, and hardware-software co-design as the main argument.
  - The literature is strong for both MI EEG CNN deployment and quantized time-series transformers, though development cost and tool complexity are higher \[Pac24, Lin24\].

## Gaps that should be named explicitly

- No retrieved paper directly establishes transformer-based motor-imagery EEG decoding on RK3568 or RKNN.
- Very few RK3568 papers report full latency, memory, throughput, and energy together.
- Many platform papers report board power or relative gains rather than fine-grained per-layer energy, which limits close cross-paper comparison.
- Direct MI EEG transformer deployment evidence is still emerging. In this corpus, \[Asa25\] is the closest architectural match, but its public metadata is still thinner than the best CNN deployment papers.

## Thesis-safe conclusion

A thesis chapter can credibly argue that edge deployment of temporal deep models for motor-imagery EEG is feasible, and that the feasibility claim is strongest for compact CNNs and increasingly credible for tiny transformers and other temporal models. The evidence is strongest on parallel low-power MCUs and embedded FPGAs \[Sch20, Wan22b, Bia24, Bus24, Bur22, Jun24, Lin24\]. RK3568 remains a plausible and practically attractive target, but the literature supports it mainly by analogy and partial platform matches rather than by direct end-to-end MI EEG transformer demonstrations \[Ism23, You24\]. The most defensible platform-choice argument is therefore comparative: RK3568 is attractive for system integration and NPU-enabled SBC deployment, while GAP9 class MCUs and small FPGAs currently enjoy the stronger published evidence base for measured efficiency on compact temporal models.

---

## References

\[Ism23\] R. Ismagilov, “Performance Evaluation of the Rockchip Systems-on-Chip Through YOLOv4 Object Detection Model,” in *2023 IEEE Ural-Siberian Conference on Biomedical Engineering, Radioelectronics and Information Technology (USBEREIT)*, May 2023, pp. 241–243. doi: [10.1109/USBEREIT58508.2023.10158842](https://doi.org/10.1109/USBEREIT58508.2023.10158842).

\[You24\] X. You and W. Weng, “Real-Time Morse Code Decoding: Exploring Domestic SoC Applications,” in *2024 IEEE 4th International Conference on Software Engineering and Artificial Intelligence (SEAI)*, Jun. 2024, pp. 296–300. doi: [10.1109/SEAI62072.2024.10674174](https://doi.org/10.1109/SEAI62072.2024.10674174).

\[Wan20\] X. Wang, M. Hersche, B. Tömekçe, B. Kaya, M. Magno, and L. Benini, “An Accurate EEGNet-based Motor-Imagery Brain–Computer Interface for Low-Power Edge Computing,” *2020 IEEE International Symposium on Medical Measurements and Applications (MeMeA)*, pp. 1–6, Mar. 2020, doi: [10.1109/MeMeA49120.2020.9137134](https://doi.org/10.1109/MeMeA49120.2020.9137134).

\[Sch20\] T. Schneider, X. Wang, M. Hersche, L. Cavigelli, and L. Benini, “Q-EEGNet: an Energy-Efficient 8-bit Quantized Parallel EEGNet Implementation for Edge Motor-Imagery Brain-Machine Interfaces,” *2020 IEEE International Conference on Smart Computing (SMARTCOMP)*, pp. 284–289, Apr. 2020, doi: [10.1109/SMARTCOMP50058.2020.00065](https://doi.org/10.1109/SMARTCOMP50058.2020.00065).

\[Wan22b\] X. Wang, M. Hersche, M. Magno, and L. Benini, “MI-BMInet: An Efficient Convolutional Neural Network for Motor Imagery Brain–Machine Interfaces With EEG Channel Selection,” *IEEE Sensors Journal*, vol. 24, pp. 8835–8847, Mar. 2022, doi: [10.1109/JSEN.2024.3353146](https://doi.org/10.1109/JSEN.2024.3353146).

\[Ene23\] D. Enériz, N. Medrano, B. Calvo, and D. Antolín, “Low-power EEGNet-based Brain-Computer Interface implemented on an Arduino Nano 33 Sense,” *2023 38th Conference on Design of Circuits and Integrated Systems (DCIS)*, pp. 1–5, Nov. 2023, doi: [10.1109/DCIS58620.2023.10335978](https://doi.org/10.1109/DCIS58620.2023.10335978).

\[Bia24\] S. Bian *et al.*, “On-device Learning of EEGNet-based Network For Wearable Motor Imagery Brain-Computer Interface,” *Proceedings of the 2024 ACM International Symposium on Wearable Computers*, Aug. 2024, doi: [10.1145/3675095.3676607](https://doi.org/10.1145/3675095.3676607).

\[Bur21b\] A. Burrello, M. Scherer, M. Zanghieri, F. Conti, and L. Benini, “A Microcontroller is All You Need: Enabling Transformer Execution on Low-Power IoT Endnodes,” *2021 IEEE International Conference on Omni-Layer Intelligent Systems (COINS)*, pp. 1–6, Aug. 2021, doi: [10.1109/COINS51742.2021.9524173](https://doi.org/10.1109/COINS51742.2021.9524173).

\[Jun24\] V. J. Jung, A. Burrello, M. Scherer, F. Conti, and L. Benini, “Optimizing the Deployment of Tiny Transformers on Low-Power MCUs,” *IEEE Transactions on Computers*, vol. 74, pp. 526–541, Apr. 2024, doi: [10.1109/TC.2024.3500360](https://doi.org/10.1109/TC.2024.3500360).

\[Bus24\] P. Busia *et al.*, “Reducing False Alarms in Wearable Seizure Detection With EEGformer: A Compact Transformer Model for MCUs,” *IEEE Transactions on Biomedical Circuits and Systems*, vol. 18, pp. 608–621, Jan. 2024, doi: [10.1109/TBCAS.2024.3357509](https://doi.org/10.1109/TBCAS.2024.3357509).

\[Bus24b\] P. Busia, M. A. Scrugli, V. J. Jung, L. Benini, and P. Meloni, “A Tiny Transformer for Low-Power Arrhythmia Classification on Microcontrollers,” *IEEE Transactions on Biomedical Circuits and Systems*, vol. 19, pp. 142–152, Feb. 2024, doi: [10.1109/TBCAS.2024.3401858](https://doi.org/10.1109/TBCAS.2024.3401858).

\[Bur22\] A. Burrello *et al.*, “Bioformers: Embedding Transformers for Ultra-Low Power sEMG-based Gesture Recognition,” *2022 Design, Automation & Test in Europe Conference & Exhibition (DATE)*, pp. 1443–1448, Mar. 2022, doi: [10.48550/arXiv.2203.12932](https://doi.org/10.48550/arXiv.2203.12932).

\[Mir24\] S. A. Mirsalari *et al.*, “StreamEase: Enabling Real-Time Inference of Temporal Convolution Networks on Low-Power MCUs with Stream-Oriented Automatic Transformation,” in *2024 31st IEEE International Conference on Electronics, Circuits and Systems (ICECS)*, Nov. 2024, pp. 1–4. doi: [10.1109/ICECS61496.2024.10848742](https://doi.org/10.1109/ICECS61496.2024.10848742).

\[Lin24\] T. Ling, C. Qian, and G. Schiele, “Integer-only Quantized Transformers for Embedded FPGA-based Time-series Forecasting in AIoT,” *2024 IEEE Annual Congress on Artificial Intelligence of Things (AIoT)*, pp. 38–44, Jul. 2024, doi: [10.1109/AIoT63253.2024.00017](https://doi.org/10.1109/AIoT63253.2024.00017).

\[Ido24\] O. P. Idowu, E. Kinney-Lang, A. Gulamhusein, B. Irvine, A. Kirton, and H. Abou-Zeid, “Profiling a Raspberry Pi-Based Motor Imagery Classification to Facilitate At-Home BCI for Children with Disabilities,” *2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)*, pp. 1–7, Jul. 2024, doi: [10.1109/EMBC53108.2024.10781873](https://doi.org/10.1109/EMBC53108.2024.10781873).

\[Pac24\] F. Pacini, T. Pacini, G. Lai, A. M. Zocco, and L. Fanucci, “Design and Evaluation of CPU-, GPU-, and FPGA-Based Deployment of a CNN for Motor Imagery Classification in Brain-Computer Interfaces,” *Electronics*, Apr. 2024, doi: [10.3390/electronics13091646](https://doi.org/10.3390/electronics13091646).

\[Asa25\] N. O. Asante, L. Mei, X. Wang, and M. Magno, “TinyEEGConformer: An Attention-Based EEG Decoding Model for Embedded Systems,” *2025 IEEE Sensors Applications Symposium (SAS)*, pp. 1–6, Jul. 2025, doi: [10.1109/SAS65169.2025.11105112](https://doi.org/10.1109/SAS65169.2025.11105112).

\[Bus22\] P. Busia *et al.*, “EEGformer: Transformer-Based Epilepsy Detection on Raw EEG Traces for Low-Channel-Count Wearable Continuous Monitoring Devices,” *2022 IEEE Biomedical Circuits and Systems Conference (BioCAS)*, pp. 640–644, Oct. 2022, doi: [10.1109/BioCAS54905.2022.9948637](https://doi.org/10.1109/BioCAS54905.2022.9948637).

\[Xie23\] C. Xie *et al.*, “Reducing the Energy Consumption of sEMG-Based Gesture Recognition at the Edge Using Transformers and Dynamic Inference,” *Sensors (Basel, Switzerland)*, vol. 23, Feb. 2023, doi: [10.3390/s23042065](https://doi.org/10.3390/s23042065).

\[Rei23b\] B. Reidy, M. Mohammadi, M. E. Elbtity, and R. Zand, “Efficient Deployment of Transformer Models on Edge TPU Accelerators: A Real System Evaluation,” 2023.
