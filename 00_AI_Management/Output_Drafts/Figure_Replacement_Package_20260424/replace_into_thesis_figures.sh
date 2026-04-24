#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
TARGET_DIR=$(cd -- "$SCRIPT_DIR/../../../01_Thesis_LaTeX/figures" && pwd)

FILES=(
  "C3-6_Alpha_Validation_20260408.png"
  "C4-12_confusion_matrix_key_conditions.png"
  "C5-3_stage1_source_bridge_full70_controls_all_subjects.png"
  "C5-4_online_threeparticipant_accuracy_confidence.png"
  "C5-6_participant3_feature_explanation.png"
)

for file in "${FILES[@]}"; do
  cp -f "$SCRIPT_DIR/$file" "$TARGET_DIR/$file"
  printf 'Replaced %s\n' "$TARGET_DIR/$file"
done
