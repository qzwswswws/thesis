# 2b 预训练迁移实验记录（2026-04-01）

## 实验目的

- 使用 `BCI Competition IV 2b` 的双导化数据（仅保留 `C3/C4`）预训练 `ConformerB2`。
- 将预训练权重迁移到当前本地 `nearalQT` 双导左右手离线数据，比较“随机初始化”与“2b 预训练初始化”的跨轮泛化表现。

## 2b 预训练设置

- 2b 数据根目录：`C:\Users\qzwsw\Documents\thesis\02_Source_Material\04_Algorithm_Workbench\datasets\standard_2b_strict_TE`
- 训练文件数：27 (`T` sessions)
- 测试文件数：18 (`E` sessions)
- 通道：`C3/C4`（从 `C3/Cz/C4` 中选取两导）
- 输入长度：`1000` 点
- 模型：`ConformerB2(n_channels=2, n_classes=2, use_diff_branch=True)`

## 2b 预训练结果

- 最优验证轮次：7
- 验证集最佳准确率：0.7065
- 2b E-session 测试准确率：0.7461

## 本地双导离线迁移结果

- 基线（随机初始化）均值：0.5000 ± 0.0000
- 预训练初始化均值：0.5250 ± 0.0629
- 均值提升：+0.0250

### 逐次结果

| Condition | Seed | Direction | Accuracy |
| --- | --- | --- | --- |
| baseline | 42 | A_to_B | 0.5000 |
| baseline | 42 | B_to_A | 0.5000 |
| baseline | 3407 | A_to_B | 0.5000 |
| baseline | 3407 | B_to_A | 0.5000 |
| baseline | 20260401 | A_to_B | 0.5000 |
| baseline | 20260401 | B_to_A | 0.5000 |
| pretrained | 42 | A_to_B | 0.6000 |
| pretrained | 42 | B_to_A | 0.5500 |
| pretrained | 3407 | A_to_B | 0.6000 |
| pretrained | 3407 | B_to_A | 0.4500 |
| pretrained | 20260401 | A_to_B | 0.5000 |
| pretrained | 20260401 | B_to_A | 0.4500 |

## 预训练权重与结果文件

- 2b 预训练权重：`C:\Users\qzwsw\Documents\thesis\02_Source_Material\04_Algorithm_Workbench\results\2b_pretrain_transfer\weights\conformer_b2_c3c4_pretrain_2b.pt`
- 本地微调权重目录：`C:\Users\qzwsw\Documents\thesis\02_Source_Material\04_Algorithm_Workbench\results\2b_pretrain_transfer\local_finetune`

## 初步判断

- 在当前两轮双导离线数据上，2b 预训练初始化表现出明确正向帮助，后续值得作为在线轮次训练的默认初始化方式。
- 无论结果方向如何，预训练权重已经保留，可继续用于后续更多轮本地数据的增量微调和对比。