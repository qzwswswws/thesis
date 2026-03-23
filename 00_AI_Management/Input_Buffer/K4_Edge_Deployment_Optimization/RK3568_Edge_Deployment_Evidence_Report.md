# Knowledge Cluster 4B: Edge Deployment Platforms & RK3568 Evidence Report
*(Extracted from Undermind.ai Research Project)*

## Executive Summary
Compact CNNs and small Transformer-like temporal models can run in real-time on ultra-low-power edge hardware. While direct EEG BCI evidence specifically for the Rockchip RK3568 is limited, strong transferable evidence exists from similar ARM-based NPUs and high-performance MCUs.

## 1. Edge Hardware & Temporal Model Deployment Benchmarks

| Source | Hardware Platform | Toolchain/Runtime | Model/Task | Measured Results | Transferability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Wan20** | Cortex-M4F / M7 | CMSIS-NN | Compact CNN (EEG MI) | Latency: 137ms (M4F), 26ms (M7). Energy: 2.55 mJ (M4F). | **Very High** (Direct EEG evidence). |
| **Bia24** | GAP9 (RISC-V) | PULP-SDK | EEGNet + Adaptation | 15.6 kB RAM. Latency: 14.9 ms. Power: 0.76 mJ. Adaptation update in 20μs. | **Very High** (Solves subject-shift). |
| **Asa25** | Arm Cortex-M | - | TinyEEGConformer | 37,135 params (145 kB). 79.63% Acc on BCIC IV-2a. | **High** (Transformer-based bukti). |
| **Ism23** | Rockchip RK3568 | RKNN | Deep Visual Models | RKNN-Toolkit2 optimization. Latency in 10-30 ms range (NPU). | **Medium** (Proof of NPU speed). |
| **Jun24** | RK3588 (SBC) | RKNN | Time-series Anomaly | >95% Acc at >100Hz real-time frequency. | **Medium** (RKNN stability for temporal). |

## 2. Key Insights for Thesis Chapters 3 and 4
- **RK3568 Positioning**: Should be framed as a "High-Performance Edge Node." Its surplus compute allows for less-aggressive pruning, enabling the use of original Transformer backbones or multi-modal fusion.
- **Challenge**: The primary hurdle is the custom operator support in RKNN-Toolkit2 for specific attention mechanisms (may require operator lowering/conversion).
- **Deployment Strategy**: Prioritize INT8 quantization and structured channel reduction (as per Wan20/Wan22) to minimize memory bus traffic, which is often the bottleneck on SBCs compared to MCUs.
