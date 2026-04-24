from pathlib import Path
import json
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-codex")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")

import matplotlib.font_manager as fm
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
THESIS_ROOT = BASE_DIR.parents[2]
FIGURE_PATH = THESIS_ROOT / "01_Thesis_LaTeX" / "figures" / "C3-6_Alpha_Validation_20260408.png"
SIMSUN_PATH = THESIS_ROOT / "01_Thesis_LaTeX" / "tools" / "fonts" / "simsun.ttf"
TIMES_PATH = THESIS_ROOT / "01_Thesis_LaTeX" / "tools" / "fonts" / "Times.TTF"

SESSIONS = [
    ("20260408_024551", "顶枕区实验一"),
    ("20260408_025030", "顶枕区实验二"),
]

SIMSUN_NAME = "SimSun"
if SIMSUN_PATH.exists():
    fm.fontManager.addfont(str(SIMSUN_PATH))
    SIMSUN_NAME = fm.FontProperties(fname=str(SIMSUN_PATH)).get_name()

TIMES_NAME = "Times New Roman"
if TIMES_PATH.exists():
    fm.fontManager.addfont(str(TIMES_PATH))
    TIMES_NAME = fm.FontProperties(fname=str(TIMES_PATH)).get_name()

plt.rcParams["font.family"] = [SIMSUN_NAME, "SimSun", TIMES_NAME, "serif"]
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["axes.unicode_minus"] = False


def zh_font(size: float, bold: bool = True) -> fm.FontProperties:
    prop = fm.FontProperties(family=[SIMSUN_NAME, "SimSun", TIMES_NAME, "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop


def en_font(size: float, bold: bool = False) -> fm.FontProperties:
    prop = fm.FontProperties(family=[TIMES_NAME, "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop


def thicken_text(text_obj, linewidth: float = 0.35):
    text_obj.set_path_effects(
        [path_effects.withStroke(linewidth=linewidth, foreground=text_obj.get_color())]
    )
    return text_obj


def load_session(session_id):
    summary = pd.read_csv(BASE_DIR / f"{session_id}_alpha_summary.csv")
    trend = pd.read_csv(BASE_DIR / f"{session_id}_alpha_trend.csv")
    raw_path = BASE_DIR / f"{session_id}_alpha_raw_eeg.csv"
    manifest = json.loads((BASE_DIR / f"{session_id}_alpha_session.json").read_text())

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
        label = ax.text(
            mid,
            50.8,
            f"{phase_label(row['phase'])}{int(row['cycle_index'])}",
            ha="center",
            va="center",
            color="#3A4658",
            fontproperties=zh_font(9, bold=True),
        )
        thicken_text(label, linewidth=0.22)


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
    fig, axes = plt.subplots(
        len(SESSIONS),
        1,
        figsize=(7.8, 5.4),
        sharex=True,
        constrained_layout=True,
    )

    if len(SESSIONS) == 1:
        axes = [axes]

    for ax, (session_id, title) in zip(axes, SESSIONS):
        summary, trend, manifest = load_session(session_id)
        open_mean = manifest["alpha_eyes_open_mean"]
        closed_mean = manifest["alpha_eyes_closed_mean"]

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
        ax.set_ylabel("Alpha 相对功率 (%)", fontproperties=zh_font(10, bold=True))
        title_text = ax.set_title(title, loc="left", fontproperties=zh_font(11, bold=True), pad=6)
        thicken_text(title_text, linewidth=0.35)
        ax.grid(axis="y", color="#D8DCE2", linewidth=0.7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        for label in ax.get_yticklabels():
            label.set_fontproperties(en_font(9))

    axes[-1].set_xlabel("实验时间 (s)", fontproperties=zh_font(10, bold=True))
    for label in axes[-1].get_xticklabels():
        label.set_fontproperties(en_font(9))

    legend_handles = [
        Line2D([0], [0], color="#222222", lw=1.8, marker="o", markersize=4.0, label="综合 Alpha 相对功率"),
        Line2D([0], [0], color="#1F77B4", lw=1.2, linestyle="--", label="睁眼阶段均值"),
        Line2D([0], [0], color="#D55E00", lw=1.2, linestyle="--", label="闭眼阶段均值"),
    ]
    legend = fig.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.70, 1.02),
        ncol=3,
        frameon=False,
        borderaxespad=0.0,
        handlelength=2.6,
        columnspacing=1.2,
    )
    for text in legend.get_texts():
        text.set_fontproperties(zh_font(9, bold=True))
        thicken_text(text, linewidth=0.2)

    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_PATH, dpi=320, bbox_inches="tight")
    plt.close(fig)
    print(FIGURE_PATH)


if __name__ == "__main__":
    main()
