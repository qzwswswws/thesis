# Figure Replacement Package 2026-04-24

本目录收集了本次按绘图规范重新导出的替代图片，供协作者直接覆盖论文图片目录使用。

适用目标目录：

`thesis/01_Thesis_LaTeX/figures/`

包含文件：

- `C3-6_Alpha_Validation_20260408.png`
- `C4-12_confusion_matrix_key_conditions.png`
- `C5-3_stage1_source_bridge_full70_controls_all_subjects.png`
- `C5-4_online_threeparticipant_accuracy_confidence.png`
- `C5-6_participant3_feature_explanation.png`
- `winsize_ai_edit_preview.png`

说明：

- `winsize.pdf` 的正式可复算替代版本本轮仍未提供，因此未纳入自动替换范围。
- `winsize_ai_edit_preview.png` 是基于原始 `winsize.pdf` 的 AI 图像编辑尝试稿，仅供人工比较，不建议直接作为正式论文图替换。
- 文件名已与论文正式引用路径保持一致，直接覆盖即可。
- 如需自动覆盖，可执行同目录下的 `replace_into_thesis_figures.sh`。
- `replace_into_thesis_figures.sh` 不会处理 `winsize_ai_edit_preview.png`，因为该文件不是正式定稿替代图。

来源脚本：

- `C3-6_Alpha_Validation_20260408.png`
  - `02_Source_Material/03_Hardware_Workbench/07_Alpha_Validation_20260408/plot_alpha_validation_20260408.py`
- `C4-12_confusion_matrix_key_conditions.png`
  - `../MI_Algorithm_Workbench/visualization/analyze_confusion_matrices.py`
- `C5-3_stage1_source_bridge_full70_controls_all_subjects.png`
  - `../MI_Algorithm_Workbench/visualization/plot_stage1_source_bridge_full70_controls.py`
- `C5-4_online_threeparticipant_accuracy_confidence.png`
  - `../MI_Algorithm_Workbench/visualization/plot_nearalqtpro_threeparticipant_accuracy_confidence_20260422.py`
- `C5-6_participant3_feature_explanation.png`
  - `../MI_Algorithm_Workbench/visualization/plot_c5_participant3_feature_explanation.py`
