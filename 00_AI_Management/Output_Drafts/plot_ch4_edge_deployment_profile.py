from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(r"C:\Users\qzwsw\Documents\thesis")
CSV_PATH = ROOT / "100_remotefiles" / "MIEXP" / "results_summaries" / "model_complexity_profile_latest.csv"
OUT_PATH = ROOT / "01_Thesis_LaTeX" / "figures" / "C4-14_edge_deployment_profile.png"

ORDER = [
    "baseline_full_4class",
    "baseline_central8_4class",
    "baseline_c3czc4_4class",
    "baseline_c3c4_4class",
    "baseline_c3c4_2class",
    "lowch_b1_c3c4_2class",
    "lowch_b2_c3c4_2class",
]

LABELS = {
    "baseline_full_4class": "22ch/4cls",
    "baseline_central8_4class": "8ch/4cls",
    "baseline_c3czc4_4class": "3ch/4cls",
    "baseline_c3c4_4class": "2ch/4cls",
    "baseline_c3c4_2class": "2ch/2cls",
    "lowch_b1_c3c4_2class": "Batch1",
    "lowch_b2_c3c4_2class": "Batch2",
}

COLORS = {
    "baseline_full_4class": "#4C5B7F",
    "baseline_central8_4class": "#69789C",
    "baseline_c3czc4_4class": "#8797B7",
    "baseline_c3c4_4class": "#A5B4D0",
    "baseline_c3c4_2class": "#8FB996",
    "lowch_b1_c3c4_2class": "#E39B4B",
    "lowch_b2_c3c4_2class": "#C96B50",
}


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    row_map = {row["tag"]: row for row in rows}
    return [row_map[tag] for tag in ORDER]


def add_bar_labels(ax: plt.Axes, bars, fmt: str) -> None:
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + max(width * 0.02, 0.01),
            bar.get_y() + bar.get_height() / 2,
            format(width, fmt),
            va="center",
            ha="left",
            fontsize=8,
            color="#333333",
        )


def main() -> None:
    rows = load_rows()
    labels = [LABELS[row["tag"]] for row in rows]
    colors = [COLORS[row["tag"]] for row in rows]
    y = np.arange(len(rows))

    metrics = [
        ("params_m", "Params (M)"),
        ("macs_g", "MACs (G)"),
        ("state_dict_size_mb", "Model Size (MB)"),
        ("cpu_latency_mean_ms", "CPU Latency (ms)"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)
    axes = axes.flatten()

    for ax, (key, title) in zip(axes, metrics):
        values = [float(row[key]) for row in rows]
        bars = ax.barh(y, values, color=colors, edgecolor="white", linewidth=0.8)
        ax.set_title(title, fontsize=11, pad=8)
        ax.set_yticks(y)
        ax.set_yticklabels(labels, fontsize=9)
        ax.invert_yaxis()
        ax.grid(axis="x", linestyle="--", alpha=0.25)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        add_bar_labels(ax, bars, ".3f")

    fig.suptitle("Deployment-Oriented Complexity Profile", fontsize=14, y=1.02)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=220, bbox_inches="tight")


if __name__ == "__main__":
    main()
