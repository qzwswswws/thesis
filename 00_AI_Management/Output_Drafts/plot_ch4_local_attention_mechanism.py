from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.font_manager as fm
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


ROOT = Path(__file__).resolve().parents[2]
THESIS_ROOT = ROOT / "01_Thesis_LaTeX"
FIGURE_PATH = THESIS_ROOT / "figures" / "C4-10_local_window_attention_mechanism.png"

SIMSUN_PATH = THESIS_ROOT / "tools" / "fonts" / "simsun.ttf"
TIMES_PATH = THESIS_ROOT / "tools" / "fonts" / "Times.TTF"
if not TIMES_PATH.exists() or TIMES_PATH.stat().st_size == 0:
    TIMES_PATH = Path(r"C:\WINDOWS\Fonts\times.ttf")
if not SIMSUN_PATH.exists() or SIMSUN_PATH.stat().st_size == 0:
    SIMSUN_PATH = Path(r"C:\WINDOWS\Fonts\simsun.ttc")

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


def zh_font(size, bold=True):
    prop = fm.FontProperties(family=[SIMSUN_NAME, "SimSun", TIMES_NAME, "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop


def en_font(size, bold=False):
    prop = fm.FontProperties(family=[TIMES_NAME, "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop


def thicken_text(text_obj, linewidth=0.35):
    text_obj.set_path_effects(
        [path_effects.withStroke(linewidth=linewidth, foreground=text_obj.get_color())]
    )
    return text_obj


def add_panel(ax, x, y, w, h, title, color):
    panel = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.008,rounding_size=0.015",
        linewidth=1.2,
        edgecolor="#C9CED6",
        facecolor="#FBFCFE",
    )
    ax.add_patch(panel)
    title_box = FancyBboxPatch(
        (x + 0.04 * w, y + h - 0.12 * h),
        0.92 * w,
        0.11 * h,
        boxstyle="round,pad=0.008,rounding_size=0.012",
        linewidth=0,
        facecolor=color,
    )
    ax.add_patch(title_box)
    title_text = ax.text(
        x + 0.5 * w,
        y + h - 0.065 * h,
        title,
        ha="center",
        va="center",
        color="white",
        fontproperties=zh_font(20),
    )
    thicken_text(title_text, linewidth=0.42)
    return panel


def draw_token(ax, cx, cy, w, h, label, highlight=False):
    face = "#EEF3FA" if not highlight else "#C9D9F2"
    edge = "#7B8AA2" if not highlight else "#335C9B"
    token = FancyBboxPatch(
        (cx - w / 2, cy - h / 2),
        w,
        h,
        boxstyle="round,pad=0.002,rounding_size=0.004",
        linewidth=1.0,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(token)
    text = ax.text(
        cx,
        cy,
        label,
        ha="center",
        va="center",
        color="#24364C",
        fontproperties=en_font(12),
    )
    return token, text


def add_arc(ax, start, end, rad, color, lw=1.6, alpha=1.0, arrowstyle="->"):
    patch = FancyArrowPatch(
        start,
        end,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle=arrowstyle,
        mutation_scale=9,
        linewidth=lw,
        color=color,
        alpha=alpha,
        shrinkA=5,
        shrinkB=5,
    )
    ax.add_patch(patch)


def add_down_arrow(ax, x, y1, y2, color="#9098A5"):
    patch = FancyArrowPatch(
        (x, y1),
        (x, y2),
        arrowstyle="simple",
        mutation_scale=26,
        linewidth=0,
        color=color,
        alpha=0.9,
    )
    ax.add_patch(patch)


def main():
    fig = plt.figure(figsize=(16, 7.4), dpi=220)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    blue = "#2F5D9A"
    teal = "#1D8A87"
    orange = "#D9731A"
    light_blue = "#DCE7F6"
    light_teal = "#D9F0ED"
    light_orange = "#FAE4CF"
    gray = "#5F6C7B"

    panels = [
        (0.03, 0.20, 0.29, 0.70, "时空特征嵌入", blue),
        (0.355, 0.20, 0.29, 0.70, "单层局部窗口自注意力", teal),
        (0.68, 0.20, 0.29, 0.70, "多层堆叠后的感受野扩展", orange),
    ]
    for args in panels:
        add_panel(ax, *args)

    # Panel 1: embedding to token sequence
    x, y, w, h, *_ = panels[0]
    feature_box = FancyBboxPatch(
        (x + 0.06 * w, y + 0.45 * h),
        0.20 * w,
        0.18 * h,
        boxstyle="round,pad=0.01,rounding_size=0.01",
        linewidth=1.2,
        edgecolor=blue,
        facecolor=light_blue,
    )
    ax.add_patch(feature_box)
    feature_label = ax.text(
        x + 0.16 * w,
        y + 0.54 * h,
        "脑电特征图",
        ha="center",
        va="center",
        color="#1F3552",
        fontproperties=zh_font(15),
    )
    thicken_text(feature_label)
    for gx in range(3):
        for gy in range(3):
            rect = Rectangle(
                (x + 0.085 * w + gx * 0.043 * w, y + 0.475 * h + gy * 0.045 * h),
                0.026 * w,
                0.026 * h,
                linewidth=0.6,
                edgecolor="#8FA9D6",
                facecolor="#F7FAFE",
            )
            ax.add_patch(rect)

    embed_arrow = FancyArrowPatch(
        (x + 0.29 * w, y + 0.54 * h),
        (x + 0.42 * w, y + 0.54 * h),
        arrowstyle="simple",
        mutation_scale=24,
        linewidth=0,
        color="#A2AAB6",
    )
    ax.add_patch(embed_arrow)
    embed_text = ax.text(
        x + 0.355 * w,
        y + 0.59 * h,
        "时空嵌入",
        ha="center",
        va="center",
        color=gray,
        fontproperties=zh_font(13),
    )
    thicken_text(embed_text, linewidth=0.3)

    token_y = y + 0.54 * h
    token_w = 0.048 * w
    token_h = 0.066 * h
    token_xs = [x + 0.47 * w + i * 0.065 * w for i in range(6)]
    token_labels = [r"$Z_1$", r"$Z_2$", r"$Z_3$", r"$\cdots$", r"$Z_{N-1}$", r"$Z_N$"]
    for cx, label in zip(token_xs, token_labels):
        draw_token(ax, cx, token_y, token_w, token_h, label)
    seq_text = ax.text(
        x + 0.63 * w,
        y + 0.39 * h,
        "时间 token 序列",
        ha="center",
        va="center",
        color=blue,
        fontproperties=zh_font(15),
    )
    thicken_text(seq_text)
    down_box = FancyBboxPatch(
        (x + 0.14 * w, y + 0.10 * h),
        0.72 * w,
        0.12 * h,
        boxstyle="round,pad=0.012,rounding_size=0.012",
        linewidth=1.0,
        edgecolor="#8FA9D6",
        facecolor="#F3F7FD",
        linestyle="--",
    )
    ax.add_patch(down_box)
    low_text = ax.text(
        x + 0.50 * w,
        y + 0.16 * h,
        "连续脑电片段被映射为有序时间表示",
        ha="center",
        va="center",
        color="#314B72",
        fontproperties=zh_font(14),
    )
    thicken_text(low_text)

    # Panel 2: single-layer local attention
    x, y, w, h, *_ = panels[1]
    token_y = y + 0.53 * h
    token_w = 0.048 * w
    token_h = 0.066 * h
    token_xs = [x + 0.12 * w + i * 0.105 * w for i in range(7)]
    token_labels = [r"$Z_{i-3}$", r"$Z_{i-2}$", r"$Z_{i-1}$", r"$Z_i$", r"$Z_{i+1}$", r"$Z_{i+2}$", r"$Z_{i+3}$"]
    for idx, (cx, label) in enumerate(zip(token_xs, token_labels)):
        draw_token(ax, cx, token_y, token_w, token_h, label, highlight=(idx == 3))

    mask_rect = FancyBboxPatch(
        (token_xs[1] - 0.045 * w, token_y - 0.09 * h),
        (token_xs[5] - token_xs[1]) + 0.09 * w,
        0.20 * h,
        boxstyle="round,pad=0.01,rounding_size=0.01",
        linewidth=1.4,
        edgecolor=teal,
        facecolor=light_teal,
        linestyle="--",
        alpha=0.30,
    )
    ax.add_patch(mask_rect)
    mask_text = ax.text(
        x + 0.50 * w,
        y + 0.67 * h,
        "固定局部窗口掩码",
        ha="center",
        va="center",
        color=teal,
        fontproperties=zh_font(14),
    )
    thicken_text(mask_text)
    left_label = ax.text(
        x + 0.11 * w,
        y + 0.40 * h,
        "仅与邻近片段交互",
        ha="left",
        va="center",
        color="#2D6764",
        fontproperties=zh_font(14),
    )
    thicken_text(left_label)

    center = (token_xs[3], token_y + 0.01 * h)
    for idx, cx in enumerate(token_xs[1:6], start=1):
        rad = -0.26 + 0.13 * (idx - 1)
        add_arc(ax, center, (cx, token_y + 0.01 * h), rad, teal, lw=1.6)

    bottom_box = FancyBboxPatch(
        (x + 0.09 * w, y + 0.10 * h),
        0.82 * w,
        0.14 * h,
        boxstyle="round,pad=0.012,rounding_size=0.012",
        linewidth=1.0,
        edgecolor="#6CB4AE",
        facecolor="#EFF9F6",
        linestyle="--",
    )
    ax.add_patch(bottom_box)
    bottom_text = ax.text(
        x + 0.50 * w,
        y + 0.17 * h,
        "注意力计算被限制在长度为 $k$ 的局部时间范围内",
        ha="center",
        va="center",
        color="#265C59",
        fontproperties=zh_font(14),
    )
    thicken_text(bottom_text)

    # Panel 3: stacked layers expanding receptive field
    x, y, w, h, *_ = panels[2]
    row_ys = [y + 0.64 * h, y + 0.47 * h, y + 0.30 * h]
    row_labels = ["第一层", "第二层", "第三层"]
    spans = [(4, 6), (3, 7), (2, 8)]
    token_xs = [x + 0.14 * w + i * 0.08 * w for i in range(9)]
    token_w = 0.042 * w
    token_h = 0.058 * h

    for row_idx, (row_y, row_label, span) in enumerate(zip(row_ys, row_labels, spans)):
        label = ax.text(
            x + 0.07 * w,
            row_y,
            row_label,
            ha="center",
            va="center",
            color="#8A4E16",
            fontproperties=zh_font(14),
        )
        thicken_text(label)
        start_idx, end_idx = span
        region = FancyBboxPatch(
            (token_xs[start_idx - 1] - 0.05 * w, row_y - 0.07 * h),
            (token_xs[end_idx - 1] - token_xs[start_idx - 1]) + 0.10 * w,
            0.14 * h,
            boxstyle="round,pad=0.01,rounding_size=0.01",
            linewidth=1.3,
            edgecolor=orange,
            facecolor=light_orange,
            linestyle="--",
            alpha=0.35,
        )
        ax.add_patch(region)
        for idx, cx in enumerate(token_xs, start=1):
            draw_token(ax, cx, row_y, token_w, token_h, rf"$Z_{idx}$", highlight=(idx == 5))
        offsets = list(range(start_idx, end_idx + 1))
        local_targets = [token_xs[idx - 1] for idx in offsets]
        for j, cx in enumerate(local_targets):
            rad = -0.22 + 0.10 * j
            add_arc(ax, (token_xs[4], row_y + 0.008 * h), (cx, row_y + 0.008 * h), rad, orange, lw=1.5)
        if row_idx < 2:
            add_down_arrow(ax, x + 0.50 * w, row_y - 0.07 * h, row_ys[row_idx + 1] + 0.07 * h, color="#B0A395")

    bottom_box = FancyBboxPatch(
        (x + 0.10 * w, y + 0.08 * h),
        0.80 * w,
        0.10 * h,
        boxstyle="round,pad=0.012,rounding_size=0.012",
        linewidth=1.0,
        edgecolor="#E29C61",
        facecolor="#FEF2E7",
        linestyle="--",
    )
    ax.add_patch(bottom_box)
    bottom_text = ax.text(
        x + 0.50 * w,
        y + 0.13 * h,
        "局部信息在层间传递后形成更长时间上下文",
        ha="center",
        va="center",
        color="#8A4E16",
        fontproperties=zh_font(14),
    )
    thicken_text(bottom_text)

    # Complexity strip
    strip = FancyBboxPatch(
        (0.03, 0.05),
        0.94,
        0.10,
        boxstyle="round,pad=0.008,rounding_size=0.012",
        linewidth=1.2,
        edgecolor="#CDD3DB",
        facecolor="#FBFBFC",
    )
    ax.add_patch(strip)
    header = FancyBboxPatch(
        (0.04, 0.065),
        0.12,
        0.07,
        boxstyle="round,pad=0.008,rounding_size=0.010",
        linewidth=0.8,
        edgecolor="#B7BEC8",
        facecolor="#EEF0F4",
    )
    ax.add_patch(header)
    head_text = ax.text(
        0.10,
        0.10,
        "复杂度对比",
        ha="center",
        va="center",
        color="#485468",
        fontproperties=zh_font(15),
    )
    thicken_text(head_text)
    ax.plot([0.50, 0.50], [0.06, 0.14], linestyle="--", color="#D5DAE2", linewidth=1.0)
    left_text = ax.text(
        0.33,
        0.112,
        "全局自注意力",
        ha="center",
        va="center",
        color=blue,
        fontproperties=zh_font(15),
    )
    thicken_text(left_text)
    ax.text(
        0.33,
        0.082,
        r"$\mathcal{O}(N^2)$",
        ha="center",
        va="center",
        color="#24364C",
        fontproperties=en_font(15),
    )
    right_text = ax.text(
        0.67,
        0.112,
        "局部窗口自注意力",
        ha="center",
        va="center",
        color=teal,
        fontproperties=zh_font(15),
    )
    thicken_text(right_text)
    ax.text(
        0.67,
        0.082,
        r"$\mathcal{O}(N \cdot k),\ k \ll N$",
        ha="center",
        va="center",
        color="#214846",
        fontproperties=en_font(15),
    )

    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_PATH, dpi=300, facecolor="white", bbox_inches="tight", pad_inches=0.05)


if __name__ == "__main__":
    main()
