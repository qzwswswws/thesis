# 图义说明：被试3第9次实验 Alpha/Beta 功率变化可视化

- 绘图脚本：`/home/woqiu/下载/git/MI_Algorithm_Workbench/visualization/plot_c5_participant3_feature_explanation.py`
- 原始数据目录：`/home/woqiu/文档/nearalQTpro/runtime/records/subject_010/session_009/run_20260419_142145`
- 派生特征表：`/home/woqiu/下载/git/MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Participant3_LateStage_Feature_Separation_20260423.csv`
- 图片输出：`/home/woqiu/下载/git/thesis/01_Thesis_LaTeX/figures/C5-6_participant3_feature_explanation.png`

## 图义

该图使用被试 3 第 9 次实验原始运行目录中的 `Prepare`、`Imagery` 与 `Rest` 分段，对左右手任务在 `通道0` 与 `通道1` 上的 Alpha/Beta 频带功率变化进行比较。图分为两个子图：

- 左图：想象阶段相对准备阶段的频带功率变化
- 右图：想象后阶段相对准备阶段的频带功率变化

其中每个柱值均按 `10*log10(phase_bandpower / prepare_bandpower)` 计算。负值表示该阶段相对准备阶段出现功率下降，正值表示局部回升。横轴按“左手 Alpha、左手 Beta、右手 Alpha、右手 Beta”排列，用于观察左右手任务与两个频带在两个通道上的变化方向与一致性。

## 支撑的正文口径

- 右手任务在两个通道上的 Alpha/Beta 下降更一致，想象阶段 ERD 特征更清楚。
- 左手任务整体也以下降为主，但通道间一致性较弱，部分快频带仅表现为小幅回升。
- 想象后阶段未形成稳定的高于准备阶段的反弹，因此当前证据更支持 ERD，而不是稳定 ERS。
