from __future__ import annotations

from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from scipy.signal import welch


THESIS_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = THESIS_ROOT / "00_AI_Management" / "input"
FIG_DIR = THESIS_ROOT / "01_Thesis_LaTeX" / "figures"
OUT_PATH = FIG_DIR / "C3-6_Alpha_Validation_20260408.png"

STAGE_CSV = INPUT_DIR / "welch_stage_alpha_summary_all_sessions.csv"
SESSION_CSV = INPUT_DIR / "welch_session_alpha_summary_all_sessions.csv"

FONT_DIR = THESIS_ROOT / "01_Thesis_LaTeX" / "tools" / "fonts"
SIMSUN_PATH = FONT_DIR / "simsun.ttf"

SESSION_ORDER = ["20260408_024551", "20260408_025030"]
SESSION_TITLES = {
    "20260408_024551": "顶枕区实验一",
    "20260408_025030": "顶枕区实验二",
}


def register_fonts() -> tuple[str, str]:
    simsun_name = "SimSun"
    if SIMSUN_PATH.exists() and SIMSUN_PATH.stat().st_size > 0:
        fm.fontManager.addfont(str(SIMSUN_PATH))
        simsun_name = fm.FontProperties(fname=str(SIMSUN_PATH)).get_name()

    times_name = "Times New Roman"
    plt.rcParams["font.family"] = [simsun_name, "SimSun", times_name, "serif"]
    plt.rcParams["mathtext.fontset"] = "stix"
    plt.rcParams["axes.unicode_minus"] = False
    return simsun_name, times_name


def zh_font(size: float, *, bold: bool = True, family: str = "SimSun") -> fm.FontProperties:
    prop = fm.FontProperties(family=[family, "SimSun", "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop


def en_font(size: float, *, bold: bool = False) -> fm.FontProperties:
    prop = fm.FontProperties(family=["Times New Roman", "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop


def phase_label(phase: str, cycle_index: int) -> str:
    if phase == "Eyes Open":
        return f"睁眼{cycle_index}"
    return f"闭眼{cycle_index}"


def band_relative_power(
    samples_uv: np.ndarray,
    fs: int,
    nperseg: int,
    alpha_band: tuple[float, float],
    reference_band: tuple[float, float],
) -> float:
    freqs, pxx = welch(
        samples_uv,
        fs=fs,
        window="hann",
        nperseg=nperseg,
        noverlap=0,
        detrend="constant",
        scaling="density",
    )
    alpha_mask = (freqs >= alpha_band[0]) & (freqs <= alpha_band[1])
    ref_mask = (freqs >= reference_band[0]) & (freqs <= reference_band[1])
    alpha_power = np.trapz(pxx[alpha_mask], freqs[alpha_mask])
    ref_power = np.trapz(pxx[ref_mask], freqs[ref_mask])
    if ref_power <= 0.0:
        return float("nan")
    return 100.0 * alpha_power / ref_power


def compute_fine_trend(session_id: str, session_row: pd.Series) -> tuple[list[float], list[float]]:
    raw_path = INPUT_DIR / f"{session_id}_alpha_raw_eeg.csv"
    raw_df = pd.read_csv(raw_path).sort_values(["stage_index", "sample_index"]).reset_index(drop=True)

    fs = int(session_row["sample_rate_hz"])
    settle_sec = float(session_row["settle_sec"])
    nperseg = int(round(float(session_row["welch_window_sec"]) * fs))
    hop = int(round(nperseg * (1.0 - float(session_row["welch_overlap_frac"]))))
    hop = max(hop, 1)
    alpha_band = (
        float(session_row["alpha_band_low_hz"]),
        float(session_row["alpha_band_high_hz"]),
    )
    reference_band = (
        float(session_row["reference_band_low_hz"]),
        float(session_row["reference_band_high_hz"]),
    )

    x_values: list[float] = []
    y_values: list[float] = []

    for stage_index, stage_df in raw_df.groupby("stage_index", sort=True):
        stage_df = stage_df.sort_values("sample_index").reset_index(drop=True)
        stage_start = float(stage_df["experiment_elapsed_sec"].min())
        valid_df = stage_df.loc[
            stage_df["experiment_elapsed_sec"] >= stage_start + settle_sec
        ].reset_index(drop=True)
        if len(valid_df) < nperseg:
            continue

        stage_values: list[float] = []
        for start in range(0, len(valid_df) - nperseg + 1, hop):
            end = start + nperseg
            ch0 = band_relative_power(
                valid_df.loc[start:end - 1, "ch0_uv"].to_numpy(),
                fs=fs,
                nperseg=nperseg,
                alpha_band=alpha_band,
                reference_band=reference_band,
            )
            ch1 = band_relative_power(
                valid_df.loc[start:end - 1, "ch1_uv"].to_numpy(),
                fs=fs,
                nperseg=nperseg,
                alpha_band=alpha_band,
                reference_band=reference_band,
            )
            stage_values.append(float(np.nanmean([ch0, ch1])))

        if not stage_values:
            continue

        slot_margin = 0.12
        if len(stage_values) == 1:
            stage_x = [float(stage_index)]
        else:
            stage_x = np.linspace(
                float(stage_index) - (0.5 - slot_margin),
                float(stage_index) + (0.5 - slot_margin),
                len(stage_values),
            ).tolist()

        x_values.extend(stage_x)
        y_values.extend(stage_values)

    return x_values, y_values


def main() -> None:
    simsun_name, _ = register_fonts()
    stage_df = pd.read_csv(STAGE_CSV)
    session_df = pd.read_csv(SESSION_CSV).set_index("session_id")

    fig, axes = plt.subplots(2, 1, figsize=(10.8, 7.6), sharex=True, dpi=200)

    open_bg = "#f5f1e6"
    closed_bg = "#dbe7f4"
    mean_open = "#2b7bba"
    mean_closed = "#d95f02"
    trend_color = "#9e9e9e"

    for ax, session_id in zip(axes, SESSION_ORDER):
        session_stage = (
            stage_df.loc[stage_df["session_id"] == session_id]
            .sort_values("stage_index")
            .reset_index(drop=True)
        )
        session_row = session_df.loc[session_id]

        stage_x = list(range(1, len(session_stage) + 1))
        stage_y = session_stage["alpha_combined"].tolist()
        fine_x, fine_y = compute_fine_trend(session_id, session_row)

        open_mean = float(session_row["eyes_open_mean_combined"])
        closed_mean = float(session_row["eyes_closed_mean_combined"])

        for idx, row in session_stage.iterrows():
            xpos = idx + 1
            bg_color = open_bg if row["phase"] == "Eyes Open" else closed_bg
            ax.axvspan(xpos - 0.5, xpos + 0.5, color=bg_color, zorder=0)
            ax.text(
                xpos,
                52.0,
                phase_label(row["phase"], int(row["cycle_index"])),
                ha="center",
                va="top",
                fontproperties=zh_font(11.5, family=simsun_name),
                color="#3b4a5a",
            )

        ax.axhline(
            open_mean,
            color=mean_open,
            linestyle="--",
            linewidth=1.8,
            zorder=1,
            dashes=(6, 3),
        )
        ax.axhline(
            closed_mean,
            color=mean_closed,
            linestyle="--",
            linewidth=1.8,
            zorder=1,
            dashes=(6, 3),
        )

        ax.plot(
            fine_x,
            fine_y,
            color=trend_color,
            linewidth=3.4,
            alpha=0.42,
            marker="o",
            markersize=3.0,
            zorder=2,
        )
        ax.plot(
            stage_x,
            stage_y,
            color="#222222",
            linewidth=2.2,
            marker="o",
            markersize=5.2,
            zorder=3,
        )

        ax.set_xlim(0.5, 6.5)
        ax.set_ylim(0, 55)
        ax.set_yticks([0, 10, 20, 30, 40, 50])
        ax.grid(axis="y", color="#d7d7d7", linewidth=0.8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_linewidth(1.0)
        ax.spines["bottom"].set_linewidth(1.0)
        ax.tick_params(axis="y", labelsize=10, width=0.9, length=4.5)
        ax.set_ylabel("Alpha 相对功率（%）", fontproperties=zh_font(12.5, family=simsun_name))
        ax.set_title(
            SESSION_TITLES[session_id],
            loc="left",
            pad=8,
            fontproperties=zh_font(15, family=simsun_name),
        )
        for label in ax.get_yticklabels():
            label.set_fontproperties(en_font(10.5))

    xticklabels = [
        phase_label(row["phase"], int(row["cycle_index"]))
        for _, row in stage_df.loc[stage_df["session_id"] == SESSION_ORDER[0]]
        .sort_values("stage_index")
        .iterrows()
    ]
    axes[-1].set_xticks(range(1, len(xticklabels) + 1))
    axes[-1].set_xticklabels(xticklabels, fontproperties=zh_font(11, family=simsun_name))
    axes[-1].set_xlabel("实验阶段", fontproperties=zh_font(13, family=simsun_name))
    axes[0].tick_params(axis="x", labelbottom=False)

    legend_handles = [
        Line2D([0], [0], color="#222222", marker="o", linewidth=2.2, markersize=5.2, label="阶段综合值"),
        Line2D([0], [0], color=trend_color, linewidth=3.4, alpha=0.42, label="Welch细趋势"),
        Line2D([0], [0], color=mean_open, linestyle="--", linewidth=1.8, label="睁眼平均水平"),
        Line2D([0], [0], color=mean_closed, linestyle="--", linewidth=1.8, label="闭眼平均水平"),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.01),
        ncol=4,
        frameon=False,
        prop=zh_font(11.2, family=simsun_name),
        handlelength=2.8,
        columnspacing=1.2,
    )

    fig.tight_layout(rect=(0, 0, 1, 0.97))
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
