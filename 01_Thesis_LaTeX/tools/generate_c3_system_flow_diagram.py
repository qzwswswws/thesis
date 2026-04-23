#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patches as patches
import matplotlib.path as mpath
from matplotlib import font_manager as fm
import matplotlib.patheffects as path_effects


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
DEFAULT_BASENAME = "C3-7_System_Flow_Diagram"


def pick_font_path() -> str:
    candidates = [
        "SimSun",
        "Noto Serif CJK SC",
        "Source Han Serif SC",
        "STSong",
        "Microsoft YaHei",
        "Source Han Sans SC",
        "Source Han Serif SC",
        "SimHei",
        "Microsoft YaHei",
    ]
    for name in candidates:
        try:
            result = subprocess.run(
                ["fc-match", "-f", "%{file}\n", name],
                check=True,
                capture_output=True,
                text=True,
            )
            path = result.stdout.strip()
        except Exception:
            path = ""
        if path and Path(path).exists():
            return path
    return ""


def styled_font(path, size, weight="normal"):
    # Matplotlib's family fallback handles English (Times New Roman) and Chinese (Songti) seamlessly
    prop = fm.FontProperties(family=["Times New Roman", "Tinos", "Nimbus Roman", "SimSun", "Noto Serif CJK SC", "serif"])
    prop.set_size(size)
    prop.set_weight(weight)
    return prop


def draw_round_box(
    ax,
    xy,
    width,
    height,
    edge,
    fill,
    label,
    font_props,
    fontsize=13,
    weight="normal",
    linestyle="-",
    font_color="black",
    zorder=2
):
    x, y = xy
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        linewidth=1.3,
        edgecolor=edge,
        facecolor=fill,
        linestyle=linestyle,
        zorder=zorder
    )
    if linestyle == "-":
        patch.set_path_effects([
            path_effects.SimplePatchShadow(offset=(2.0, -2.0), shadow_rgbFace="#000000", alpha=0.08),
            path_effects.Normal()
        ])
    ax.add_patch(patch)
    if label:
        ax.text(
            x + width / 2,
            y + height / 2,
            label,
            ha="center",
            va="center",
            color=font_color,
            fontproperties=styled_font(font_props.get_file(), fontsize, weight),
            zorder=max(4, zorder + 1)
        )
    return patch


def draw_rounded_polygon(ax, points, edge, fill, radius=0.14, zorder=1):
    vertices = []
    codes = []
    n = len(points)
    for i in range(n):
        p_prev = points[(i - 1) % n]
        p_curr = points[i]
        p_next = points[(i + 1) % n]
        
        dx1, dy1 = p_prev[0] - p_curr[0], p_prev[1] - p_curr[1]
        len1 = (dx1**2 + dy1**2)**0.5
        v1 = (dx1/len1, dy1/len1)
        
        dx2, dy2 = p_next[0] - p_curr[0], p_next[1] - p_curr[1]
        len2 = (dx2**2 + dy2**2)**0.5
        v2 = (dx2/len2, dy2/len2)
        
        start_pt = (p_curr[0] + v1[0]*radius, p_curr[1] + v1[1]*radius)
        end_pt = (p_curr[0] + v2[0]*radius, p_curr[1] + v2[1]*radius)
        
        if i == 0:
            vertices.append(start_pt)
            codes.append(mpath.Path.MOVETO)
        else:
            vertices.append(start_pt)
            codes.append(mpath.Path.LINETO)
            
        vertices.append(p_curr)
        codes.append(mpath.Path.CURVE3)
        vertices.append(end_pt)
        codes.append(mpath.Path.CURVE3)
        
    vertices.append(vertices[0])
    codes.append(mpath.Path.LINETO)
    
    path = mpath.Path(vertices, codes)
    patch = patches.PathPatch(
        path,
        linewidth=1.3,
        edgecolor=edge,
        facecolor=fill,
        zorder=zorder
    )
    patch.set_path_effects([
        path_effects.SimplePatchShadow(offset=(2.0, -2.0), shadow_rgbFace="#000000", alpha=0.08),
        path_effects.Normal()
    ])
    ax.add_patch(patch)
    return patch


def draw_arrow(
    ax,
    start,
    end,
    color,
    font_props,
    text=None,
    text_xy=None,
    lw=2.0,
    ls="-",
    rad=0.0,
):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="->",
        mutation_scale=12,
        linewidth=lw,
        linestyle=ls,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
        zorder=5
    )
    ax.add_patch(arrow)
    if text:
        tx, ty = text_xy if text_xy is not None else ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        ax.text(
            tx,
            ty,
            text,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.9),
            color=color,
            fontproperties=styled_font(None, 10.5),
            zorder=6
        )


def generate_figure(out_base: Path) -> None:
    # Legacy argument used in styled_font calls
    font_path = None
    
    # Register explicitly downloaded or fallback fonts to guarantee dual-font rendering
    try:
        fm.fontManager.addfont("tools/fonts/simsun.ttf")
    except Exception:
        pass
    try:
        fm.fontManager.addfont("/usr/share/fonts/truetype/croscore/Tinos-Regular.ttf")
    except Exception:
        pass
    
    # Configure global renderer to strictly use Serif (Times + Songti fallback)
    plt.rcParams["font.family"] = ["Times New Roman", "Tinos", "Nimbus Roman", "SimSun", "Noto Serif CJK SC", "serif"]
    plt.rcParams["axes.unicode_minus"] = False
    
    # Empty font property structure for retro-compatibility in the script
    font_props = fm.FontProperties()

    fig, ax = plt.subplots(figsize=(16.0, 8.8), dpi=180)
    ax.set_xlim(0, 16.4)
    ax.set_ylim(0, 8.8)
    ax.axis("off")

    # ----- 1. Region Panels (Backgrounds) -----
    # 硬件采集端 (精确对齐黄框顶端的 8.2 高度: 0.4+7.8=8.2)
    draw_round_box(ax, (0.4, 0.4), 3.4, 7.8, "#A3B5DF", "#F2F5FB", "", font_props, fontsize=1, zorder=1)
    ax.text(2.1, 8.45, "便携性脑电解码硬件系统", ha="center", va="center", color="#3B5998", fontproperties=styled_font(font_path, 12.0, "normal"), zorder=5)
    
    # 上位机程序端 (使用自定义连贯圆角多边形绘制真正的 L-Shape，消除一切毛刺、线头与直角)
    pc_bg_color = "#FBFAF7"
    l_points = [
        (4.2, 0.4),      # P1: Bottom Left
        (15.9, 0.4),     # P2: Bottom Right
        (15.9, 4.85),    # P3: Middle Right (Below Edge cell)
        (11.55, 4.85),   # P4: Inner corner (Pulled back heavily to widen gap to Edge box!)
        (11.55, 8.2),    # P5: Top Inner corner
        (4.2, 8.2)       # P6: Top Left
    ]
    draw_rounded_polygon(ax, l_points, edge="#DEC0A4", fill=pc_bg_color, radius=0.14, zorder=1)
    
    ax.text(7.875, 8.45, "上位机状态观测与基础交互闭环", ha="center", va="center", color="#9E6124", fontproperties=styled_font(font_path, 12.0, "normal"), zorder=5)

    # 边缘推理侧 面板 (X坐标起始右推，制造大宽距)
    draw_round_box(ax, (12.1, 5.1), 3.7, 3.1, "#CCCCCC", "#F9F9F9", "", font_props, fontsize=1, zorder=3)
    ax.text(13.95, 8.45, "边缘推理部署侧", ha="center", va="center", color="#666666", fontproperties=styled_font(font_path, 12.0, "normal"), zorder=5)

    # 上位机内部功能链背景区 (Dashed Box Pipeline) 完全包含着所有绿色框
    draw_round_box(ax, (4.4, 0.7), 11.3, 4.05, "#B1612A", "#FFFFFF", "", font_props, fontsize=1, linestyle="--", zorder=3)
    ax.text(10.05, 4.75, "上位机程序关键功能链", ha="center", va="center", color="#83461D", bbox=dict(boxstyle="square,pad=0.1", facecolor="#FFFFFF", edgecolor="none"), fontproperties=styled_font(font_path, 12.0, "normal"), zorder=10)


    # ----- 2. Functional Box Coordinates (Tighter vertical gaps, wider columns) -----
    box_blue_edge = "#455E7B"
    box_org_edge = "#B1612A"
    box_gray_edge = "#586776"
    green_bg = "#F4FFF1"
    green_edge = "#5E8F5C"

    # Row 1 (Hardware/Bottom Pipeline) -> Green Boxes explicitly Y=1.0 to close gap!
    draw_round_box(ax, (0.7, 1.0), 2.8, 1.3, box_blue_edge, "white", "KS1092\n脑电采集前端模块", font_props, 12.0, "normal", zorder=5)
    # Master Aligner spanning C1 and C2
    draw_round_box(ax, (4.6, 1.0), 6.8, 1.3, green_edge, green_bg, "事件标签与样本计数", font_props, 12.0, "normal", zorder=5)
    # Logging C3 
    draw_round_box(ax, (12.3, 1.0), 3.2, 1.3, green_edge, green_bg, "结构化日志记录", font_props, 12.0, "normal", zorder=5)

    # Row 2 (Hardware/Middle Pipeline) -> Y=3.3 (Greatly closes gap with Row 1 to 1.0)
    draw_round_box(ax, (0.7, 3.3), 2.8, 1.3, box_blue_edge, "white", "nRF52832\n主控与缓存", font_props, 12.0, "normal", zorder=5)
    # Paradigm C1, Filter C2, Output C3
    draw_round_box(ax, (4.6, 3.3), 3.2, 1.3, green_edge, green_bg, "实验范式控制", font_props, 12.0, "normal", zorder=5)
    draw_round_box(ax, (8.15, 3.3), 3.2, 1.3, green_edge, green_bg, "数据滤波与频带估计", font_props, 12.0, "normal", zorder=5)
    draw_round_box(ax, (12.3, 3.3), 3.2, 1.3, green_edge, green_bg, "数据接口输出", font_props, 12.0, "normal", zorder=5)
    
    # Row 3 (Hardware/Top Hosts) -> Y=6.2
    draw_round_box(ax, (0.7, 6.2), 2.8, 1.4, box_blue_edge, "white", "BLE 链路\n无线传输模块", font_props, 12.0, "normal", zorder=5)
    draw_round_box(ax, (4.6, 6.2), 3.2, 1.4, box_org_edge, "white", "Qt6 上位机程序", font_props, 12.0, "normal", zorder=5)
    draw_round_box(ax, (8.15, 6.2), 3.2, 1.4, box_org_edge, "white", "配套界面展现\n(状态可视与参数配置)", font_props, 12.0, "normal", zorder=5)
    draw_round_box(ax, (12.3, 6.2), 3.2, 1.4, box_gray_edge, "white", "RK3568/RKNN\n边缘推理节点", font_props, 12.0, "normal", zorder=5)


    # ----- 3. Connecting Arrows -----
    blue = "#2B4DA5"
    orange = "#D87920"
    green = "#3C8946"

    # ----- 3. Connecting Arrows -----
    blue = "#2B4DA5"
    orange = "#D87920"
    green = "#3C8946"

    # Hardware Column Internal
    # Gap 1 (Close gap)
    draw_arrow(ax, (2.3, 2.45), (2.3, 3.15), blue, font_props, "模拟信号", (2.8, 2.8), lw=2.2)
    draw_arrow(ax, (1.9, 3.15), (1.9, 2.45), orange, font_props, "前端增益", (1.2, 2.8), lw=1.8, ls="--")
    # Gap 2 (Wider)
    draw_arrow(ax, (2.3, 4.75), (2.3, 6.05), blue, font_props, "ADC 数据", (2.85, 5.4), lw=2.2)
    draw_arrow(ax, (1.9, 6.05), (1.9, 4.75), orange, font_props, "状态解析", (1.25, 5.4), lw=1.8, ls="--")
    
    # BLE <-> Qt Host
    draw_arrow(ax, (3.5, 6.9), (4.45, 6.9), blue, font_props, "无线回传", (4.0, 7.15), lw=2.2)
    draw_arrow(ax, (4.45, 6.5), (3.5, 6.5), orange, font_props, "参数配置", (4.0, 6.25), lw=1.8, ls="--")

    # Qt Internal Down (Straight vertical mappings as boxes share identical X centers!)
    draw_arrow(ax, (6.2, 6.1), (6.2, 4.7), orange, font_props, "触发实验控制", (5.1, 5.4), lw=1.8, ls="--")
    draw_arrow(ax, (9.75, 6.1), (9.75, 4.7), blue, font_props, "数据帧缓冲", (10.7, 5.4), lw=2.2)
    
    # Pipeline Internal Down (To Master Aligner)
    draw_arrow(ax, (6.2, 3.2), (6.2, 2.4), green, font_props, "交互事件发生", (5.2, 2.8), lw=2.2)
    draw_arrow(ax, (9.75, 3.2), (9.75, 2.4), blue, font_props, "微伏波形", (10.4, 2.8), lw=2.2)
    
    # Pipeline Internal (From Master Aligner)
    draw_arrow(ax, (11.5, 1.65), (12.2, 1.65), blue, font_props, "序列日志", (11.85, 1.4), lw=2.2)
    draw_arrow(ax, (11.4, 2.0), (12.3, 3.35), blue, font_props, "边缘推理输入窗口", (11.2, 2.5), lw=2.2)

    # Edge <-> PC
    draw_arrow(ax, (13.9, 4.7), (13.9, 6.05), blue, font_props, "处理路径输出", (14.65, 5.4), lw=2.2)
    draw_arrow(ax, (12.3, 6.9), (11.55, 6.9), blue, font_props, "任务结果回调", (11.9, 7.15), lw=2.2)

    # UI Interaction
    draw_arrow(ax, (8.15, 6.9), (7.8, 6.9), orange, font_props, "实验干预", (7.95, 7.15), lw=1.8, ls="--")

    out_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_base.with_suffix(".pdf"), bbox_inches="tight", pad_inches=0.0)
    fig.savefig(out_base.with_suffix(".png"), bbox_inches="tight", pad_inches=0.0, dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate the C3 System Flow Diagram")
    parser.add_argument("--out", type=str, default=DEFAULT_BASENAME, help="Output file base name")
    args = parser.parse_args()

    out_path = FIG_DIR / args.out
    generate_figure(out_path)
    print(f"[+] System flow diagram successfully generated at {out_path}.(pdf|png)")
