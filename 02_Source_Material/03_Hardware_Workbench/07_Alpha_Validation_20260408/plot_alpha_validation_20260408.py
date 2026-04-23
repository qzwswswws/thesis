from pathlib import Path
import json
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-codex")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
FIGURE_PATH = (
    BASE_DIR.parents[2]
    / "01_Thesis_LaTeX"
    / "figures"
    / "C3-6_Alpha_Validation_20260408.png"
)

SESSIONS = [
    ("20260408_024551", "顶枕区实验一"),
    ("20260408_025030", "顶枕区实验二"),
]


def load_session(session_id):
    summary = pd.read_csv(BASE_DIR / f"{session_id}_alpha_summary.csv")
    trend = pd.read_csv(BASE_DIR / f"{session_id}_alpha_trend.csv")
    raw_path = BASE_DIR / f"{session_id}_alpha_raw_eeg.csv"
    manifest = json.loads((BASE_DIR / f"{session_id}_alpha_session.json").read_text())

    # The raw file is not plotted directly because the online Alpha trend already
    # contains the real-time FFT results generated from the continuously buffered
    # raw EEG. Keeping this check makes the figure reproducibility explicit.
    if not raw_path.exists():
        raise FileNotFoundError(raw_path)

    return summary, trend, manifest


def phase_label(phase):
    return "闭眼" if phase == "Eyes Closed" else "睁眼"


def draw_stage_background(ax, summary):
    for _, row in summary.iterrows():
        color = "#DDEAF7" if row["phase"] == "Eyes Closed" else "#F7F3E6"
        ax.axvspan(row["start_sec"], row["end_sec"], color=color, alpha=0.70, lw=0)
        mid = (row["start_sec"] + row["end_sec"]) / 2.0
        ax.text(
            mid,
            52.0,
            f"{phase_label(row['phase'])}{int(row['cycle_index'])}",
            ha="center",
            va="center",
            fontsize=9,
            color="#3A4658",
        )


def draw_stage_means(ax, summary):
    for _, row in summary.iterrows():
        color = "#1F77B4" if row["phase"] == "Eyes Open" else "#D55E00"
        ax.hlines(
            row["mean_alpha_combined"],
            row["start_sec"],
            row["end_sec"],
            colors=color,
            linestyles="--",
            linewidth=1.6,
            alpha=0.9,
        )


def main():
    font_path = "/usr/share/fonts/truetype/arphic/uming.ttc"
    if Path(font_path).exists():
        font_prop = fm.FontProperties(fname=font_path)
        plt.rcParams["font.family"] = font_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

    fig, axes = plt.subplots(
        len(SESSIONS),
        1,
        figsize=(7.2, 4.9),
        sharex=True,
        constrained_layout=True,
    )

    if len(SESSIONS) == 1:
        axes = [axes]

    for ax, (session_id, title) in zip(axes, SESSIONS):
        summary, trend, manifest = load_session(session_id)
        open_mean = manifest["alpha_eyes_open_mean"]
        closed_mean = manifest["alpha_eyes_closed_mean"]
        ratio = manifest["alpha_closed_open_ratio"]

        draw_stage_background(ax, summary)
        ax.plot(
            trend["elapsed_sec"],
            trend["alpha_combined"],
            color="#222222",
            linewidth=1.8,
            marker="o",
            markersize=2.6,
            label="综合 Alpha 相对功率",
        )
        draw_stage_means(ax, summary)

        ax.axhline(open_mean, color="#1F77B4", linewidth=1.1, linestyle=":", alpha=0.9)
        ax.axhline(closed_mean, color="#D55E00", linewidth=1.1, linestyle=":", alpha=0.9)
        ax.set_ylim(0, 56)
        ax.set_ylabel("Alpha 相对功率 (%)", fontsize=10)
        ax.set_title(
            f"{title}: 闭眼/睁眼={ratio:.2f}, 睁眼={open_mean:.2f}%, 闭眼={closed_mean:.2f}%",
            fontsize=11,
            loc="left",
        )
        ax.grid(axis="y", color="#D8DCE2", linewidth=0.7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    axes[-1].set_xlabel("实验时间 (s)", fontsize=10)

    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_PATH, dpi=300, bbox_inches="tight")
    print(FIGURE_PATH)


if __name__ == "__main__":
    main()
