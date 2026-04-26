# -*- coding: utf-8 -*-
from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
FIGURE_PATH = ROOT / "01_Thesis_LaTeX" / "figures" / "C3-0_Board_Block_Diagram.png"
FONT_DIR = ROOT / "01_Thesis_LaTeX" / "tools" / "fonts"

SIMSUN = FONT_DIR / "simsun.ttf"
TIMES = FONT_DIR / "times.ttf"
TIMES_BOLD = FONT_DIR / "Timesbd.TTF"

W, H = 2500, 1320
WHITE = (255, 255, 255)
LIGHT = (248, 248, 248)
MID = (238, 238, 238)
BLACK = (20, 20, 20)
GRAY = (96, 96, 96)


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


ZH_24 = load_font(SIMSUN, 24)
ZH_26 = load_font(SIMSUN, 26)
ZH_28 = load_font(SIMSUN, 28)
ZH_32 = load_font(SIMSUN, 32)
ZH_34 = load_font(SIMSUN, 34)
ZH_36 = load_font(SIMSUN, 36)
ZH_40 = load_font(SIMSUN, 40)
ZH_44 = load_font(SIMSUN, 44)
EN_28 = load_font(TIMES, 28)
EN_30 = load_font(TIMES, 30)
EN_34 = load_font(TIMES, 34)
EN_42_B = load_font(TIMES_BOLD, 42)
EN_48_B = load_font(TIMES_BOLD, 48)


def draw_bold_multiline(draw, xy, text, font, fill=BLACK, align="left", spacing=8, passes=2):
    x, y = xy
    for dx, dy in [(0, 0), (1, 0)][:passes]:
        draw.multiline_text(
            (x + dx, y + dy),
            text,
            font=font,
            fill=fill,
            align=align,
            spacing=spacing,
        )


def multiline_size(draw, text, font, spacing=8):
    box = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing, align="center")
    return box[2] - box[0], box[3] - box[1]


def centered_block(draw, box, lines, fonts, fills=None, spacing=14, line_gap=10):
    if fills is None:
        fills = [BLACK] * len(lines)
    widths = []
    heights = []
    for text, fnt in zip(lines, fonts):
        w, h = multiline_size(draw, text, fnt, spacing=spacing)
        widths.append(w)
        heights.append(h)
    total_h = sum(heights) + line_gap * (len(lines) - 1)
    x1, y1, x2, y2 = box
    y = y1 + (y2 - y1 - total_h) / 2
    for text, fnt, fill, w, h in zip(lines, fonts, fills, widths, heights):
        x = x1 + (x2 - x1 - w) / 2
        if fnt in {ZH_24, ZH_26, ZH_28, ZH_32, ZH_34, ZH_36, ZH_40, ZH_44}:
            draw_bold_multiline(draw, (x, y), text, fnt, fill=fill, align="center", spacing=spacing)
        else:
            draw.multiline_text((x, y), text, font=fnt, fill=fill, align="center", spacing=spacing)
        y += h + line_gap


def rect(draw, box, fill=WHITE, outline=BLACK, width=4):
    draw.rectangle(box, fill=fill, outline=outline, width=width)


def label_box(draw, xy, text, font, padding=(16, 8), fill=WHITE, outline=BLACK):
    w, h = multiline_size(draw, text, font, spacing=6)
    x, y = xy
    x2 = x + w + padding[0] * 2
    y2 = y + h + padding[1] * 2
    draw.rectangle((x, y, x2, y2), fill=fill, outline=outline, width=2)
    tx = x + padding[0]
    ty = y + padding[1]
    if font in {ZH_24, ZH_26, ZH_28, ZH_32, ZH_34, ZH_36, ZH_40, ZH_44}:
        draw_bold_multiline(draw, (tx, ty), text, font, fill=BLACK, align="center", spacing=6)
    else:
        draw.multiline_text((tx, ty), text, font=font, fill=BLACK, align="center", spacing=6)
    return (x, y, x2, y2)


def plain_label(draw, center_xy, text, font, padding=(10, 6), fill=BLACK, bg=WHITE):
    w, h = multiline_size(draw, text, font, spacing=6)
    cx, cy = center_xy
    x = cx - w / 2 - padding[0]
    y = cy - h / 2 - padding[1]
    draw.rectangle((x, y, x + w + padding[0] * 2, y + h + padding[1] * 2), fill=bg)
    tx = x + padding[0]
    ty = y + padding[1]
    if font in {ZH_24, ZH_26, ZH_28, ZH_32, ZH_34, ZH_36, ZH_40, ZH_44}:
        draw_bold_multiline(draw, (tx, ty), text, font, fill=fill, align="center", spacing=6)
    else:
        draw.multiline_text((tx, ty), text, font=font, fill=fill, align="center", spacing=6)


def line(draw, start, end, width=5, fill=BLACK, dashed=False):
    x1, y1 = start
    x2, y2 = end
    if not dashed:
        draw.line((x1, y1, x2, y2), fill=fill, width=width)
        return
    total = math.hypot(x2 - x1, y2 - y1)
    if total == 0:
        return
    dash_len = 28
    gap = 18
    dx = (x2 - x1) / total
    dy = (y2 - y1) / total
    dist = 0
    while dist < total:
        seg = min(dash_len, total - dist)
        sx = x1 + dx * dist
        sy = y1 + dy * dist
        ex = x1 + dx * (dist + seg)
        ey = y1 + dy * (dist + seg)
        draw.line((sx, sy, ex, ey), fill=fill, width=width)
        dist += dash_len + gap


def arrow(draw, start, end, width=5, fill=BLACK, dashed=False, head=18):
    line(draw, start, end, width=width, fill=fill, dashed=dashed)
    x1, y1 = start
    x2, y2 = end
    ang = math.atan2(y2 - y1, x2 - x1)
    left = ang + math.radians(154)
    right = ang - math.radians(154)
    p2 = (x2 + head * math.cos(left), y2 + head * math.sin(left))
    p3 = (x2 + head * math.cos(right), y2 + head * math.sin(right))
    draw.polygon((end, p2, p3), fill=fill)


def main():
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    board = (180, 110, 2310, 1180)
    electrode = (300, 315, 530, 790)
    ks = (700, 285, 1140, 790)
    nrf = (1330, 285, 1770, 790)
    antenna = (1880, 255, 2190, 405)
    debug = (1880, 545, 2190, 695)
    power = (700, 885, 1140, 1060)
    i2c = (1330, 885, 1770, 1060)

    rect(draw, board, fill=WHITE, outline=BLACK, width=4)
    rect(draw, electrode, fill=WHITE, outline=BLACK, width=4)
    rect(draw, ks, fill=WHITE, outline=BLACK, width=4)
    rect(draw, nrf, fill=WHITE, outline=BLACK, width=4)
    rect(draw, antenna, fill=WHITE, outline=BLACK, width=4)
    rect(draw, debug, fill=WHITE, outline=BLACK, width=4)
    rect(draw, power, fill=MID, outline=BLACK, width=4)
    rect(draw, i2c, fill=WHITE, outline=BLACK, width=4)

    centered_block(draw, electrode, ["双导", "电极", "接口"], [ZH_44, ZH_44, ZH_44], line_gap=14)
    centered_block(
        draw,
        ks,
        ["KS1092", "脑电采集前端", "双通道模拟调理", "偏置驱动与导联状态检测"],
        [EN_48_B, ZH_40, ZH_28, ZH_28],
        fills=[BLACK, BLACK, GRAY, GRAY],
        line_gap=16,
    )
    centered_block(
        draw,
        nrf,
        ["nRF52832", "主控与 BLE SoC", "SAADC 采样", "缓存与协议封装", "BLE 回传"],
        [EN_48_B, ZH_40, ZH_28, ZH_28, ZH_28],
        fills=[BLACK, BLACK, GRAY, GRAY, GRAY],
        line_gap=14,
    )
    centered_block(draw, antenna, ["BLE 天线"], [ZH_36], line_gap=10)
    centered_block(draw, debug, ["调试接口", "SWD / UART"], [ZH_34, EN_42_B], line_gap=10)
    centered_block(
        draw,
        i2c,
        ["预留 I²C 生理扩展接口", "心率/血氧等辅助模块"],
        [ZH_32, ZH_28],
        fills=[BLACK, GRAY],
        line_gap=8,
    )
    centered_block(
        draw,
        power,
        ["Type-C / 充电管理", "电池接口"],
        [ZH_32, ZH_28],
        fills=[BLACK, GRAY],
        line_gap=10,
    )

    arrow(draw, (530, 590), (700, 590), width=5)
    plain_label(draw, (615, 525), "差分输入", ZH_24)

    arrow(draw, (1140, 500), (1330, 500), width=5)
    plain_label(draw, (1235, 435), "VO1 / VO2", EN_30)

    arrow(draw, (1330, 650), (1140, 650), width=5, dashed=True)
    plain_label(draw, (1235, 715), "SPI / GPIO", EN_30)

    arrow(draw, (1770, 430), (1880, 330), width=5)
    arrow(draw, (1770, 620), (1880, 620), width=5)

    line(draw, (920, 885), (920, 835), width=5)
    line(draw, (920, 835), (1450, 835), width=5)
    arrow(draw, (920, 835), (920, 790), width=5)
    arrow(draw, (1450, 835), (1450, 790), width=5)

    arrow(draw, (1560, 790), (1560, 885), width=5)
    plain_label(draw, (1560, 838), "I²C / INT", EN_30)

    img.save(FIGURE_PATH, quality=95)
    print(FIGURE_PATH)


if __name__ == "__main__":
    main()
