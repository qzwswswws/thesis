# 图义说明：被试3后段原始实验特征差异可视化

- 绘图脚本：`/home/woqiu/下载/git/MI_Algorithm_Workbench/visualization/plot_c5_participant3_feature_explanation.py`
- 原始数据目录：
  - `/home/woqiu/文档/nearalQTpro/runtime/records/subject_010/session_005/run_20260419_135425`
  - `/home/woqiu/文档/nearalQTpro/runtime/records/subject_010/session_006/run_20260419_140135`
  - `/home/woqiu/文档/nearalQTpro/runtime/records/subject_010/session_007/run_20260419_140839`
  - `/home/woqiu/文档/nearalQTpro/runtime/records/subject_010/session_009/run_20260419_142145`
- 派生特征表：`/home/woqiu/下载/git/MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Participant3_LateStage_Feature_Separation_20260423.csv`
- 图片输出：`/home/woqiu/下载/git/thesis/01_Thesis_LaTeX/figures/C5-6_participant3_feature_explanation.png`

## 图义

该图使用被试 3 原始后段第 5、6、7、9 次实验的运动想象窗，对左右手任务在 `通道0`、`通道1` 和 `差分通道` 上的四类特征进行标准化差异比较。四个子图分别对应：

- 左上：均值幅值差异
- 右上：波动强度差异
- 左下：Alpha 能量差异
- 右下：Beta 能量差异

纵轴为左右手两类试次在该特征上的标准化差异强度，采用绝对 Cohen's d 表示。数值越大，说明该特征对左右手任务的区分越明显。

## 支撑的正文口径

- 后段较高准确率实验中的区分信息不主要来自简单的整体均值幅值偏移。
- 波动强度差异和 Alpha 频段差异在后段更具解释价值，尤其体现在 `通道1` 与 `差分通道`。
- Beta 频段差异存在，但跨实验稳定性弱于 Alpha 频段。
