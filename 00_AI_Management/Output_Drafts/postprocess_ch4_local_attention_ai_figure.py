from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
THESIS_ROOT = ROOT / "01_Thesis_LaTeX"
BASE_IMAGE = Path(
    r"C:\Users\qzwsw\.codex\generated_images\019dc787-801f-7541-8198-3910335866bb\ig_0cd39758b6af259a0169ed8639991c8191a70415275395917b.png"
)
OUTPUT_IMAGE = THESIS_ROOT / "figures" / "C4-10_local_window_attention_mechanism.png"

SIMSUN_PATH = THESIS_ROOT / "tools" / "fonts" / "simsun.ttf"
if not SIMSUN_PATH.exists() or SIMSUN_PATH.stat().st_size == 0:
    SIMSUN_PATH = Path(r"C:\WINDOWS\Fonts\simsun.ttc")

TIMES_PATH = Path(r"C:\WINDOWS\Fonts\times.ttf")


def zh(size):
    return ImageFont.truetype(str(SIMSUN_PATH), size=size)


def en(size):
    return ImageFont.truetype(str(TIMES_PATH), size=size)


def center_text(draw, box, text, font, fill, stroke_width=1, stroke_fill=None, spacing=4):
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    draw.multiline_text(
        (cx, cy),
        text,
        font=font,
        fill=fill,
        anchor="mm",
        align="center",
        spacing=spacing,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill or fill,
    )


def fill_box(draw, box, fill="#FFFFFF", radius=12, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def main():
    img = Image.open(BASE_IMAGE).convert("RGBA")
    draw = ImageDraw.Draw(img)

    blue = "#234F8E"
    teal = "#17807D"
    orange = "#E06E1B"
    dark = "#334155"
    white = "#FFFFFF"
    pale = "#FBFCFE"

    # Top title bars
    center_text(draw, (98, 38, 491, 91), "时空特征嵌入", zh(34), blue, stroke_width=1)
    center_text(draw, (645, 38, 1074, 91), "单层局部窗口自注意力", zh(31), teal, stroke_width=1)
    center_text(draw, (1274, 38, 1719, 91), "多层堆叠后的感受野扩展", zh(30), orange, stroke_width=1)

    # Panel 1 labels
    fill_box(draw, (42, 145, 270, 188), fill=white, radius=10)
    center_text(draw, (42, 145, 270, 188), "脑电特征图", zh(23), blue, stroke_width=1)

    fill_box(draw, (18, 434, 252, 499), fill=white, radius=10)
    center_text(draw, (18, 434, 252, 499), "时间片段序列", zh(23), blue, stroke_width=1)

    fill_box(draw, (194, 570, 314, 610), fill=white, radius=8)
    center_text(draw, (194, 570, 314, 610), "时间", zh(21), blue, stroke_width=1)

    # Panel 2 main header removal and replacements
    fill_box(draw, (620, 110, 1038, 164), fill=white, radius=12)
    fill_box(draw, (676, 194, 962, 235), fill=white, radius=8)
    center_text(draw, (676, 194, 962, 235), "局部窗口（宽度为 2k+1）", zh(22), teal, stroke_width=1)

    fill_box(draw, (620, 478, 1118, 540), fill=white, radius=10)
    draw.rounded_rectangle((640, 489, 706, 518), radius=6, fill="#E9F5F2")
    draw.line((638, 526, 700, 526), fill="#98A4B5", width=3)
    center_text(draw, (715, 483, 1112, 507), "局部注意掩码（仅窗口内计算）", zh(17), dark, stroke_width=1)
    center_text(draw, (715, 507, 1112, 535), "窗口外掩码（不参与计算）", zh(17), dark, stroke_width=1)

    fill_box(draw, (579, 555, 1039, 626), fill=white, radius=10)
    center_text(
        draw,
        (579, 555, 1039, 626),
        "中心片段 Zi 仅与固定局部窗口内的邻近片段交互",
        zh(21),
        teal,
        stroke_width=1,
    )

    # Panel 3 remove English header and relabel layers
    fill_box(draw, (1200, 112, 1675, 182), fill=white, radius=12)

    layer_boxes = [
        ((1105, 198, 1302, 296), "第一层"),
        ((1105, 348, 1302, 448), "第二层"),
        ((1105, 502, 1302, 602), "第三层"),
    ]
    cover_boxes = [(1105, 198, 1302, 296), (1105, 348, 1302, 448), (1105, 502, 1302, 602)]
    for box in cover_boxes:
        fill_box(draw, box, fill=white, radius=10)
    for box, label in layer_boxes:
        center_text(draw, box, label, zh(24), "#C35D13", stroke_width=1)

    for box, text in [
        ((1406, 268, 1616, 320), "覆盖约 ±k"),
        ((1406, 422, 1622, 474), "覆盖约 ±2k"),
        ((1406, 576, 1622, 628), "覆盖约 ±3k"),
    ]:
        fill_box(draw, box, fill=white, radius=10)
        center_text(draw, box, text, zh(20), "#C35D13", stroke_width=1)

    # Bottom strip relabeling
    fill_box(draw, (36, 730, 314, 838), fill=white, radius=16)
    center_text(draw, (36, 730, 314, 838), "复杂度对比", zh(28), dark, stroke_width=1)

    draw.rounded_rectangle((451, 707, 720, 744), radius=10, fill=blue)
    center_text(draw, (451, 707, 720, 744), "全局自注意力", zh(21), white, stroke_width=1)
    draw.rounded_rectangle((966, 707, 1237, 744), radius=10, fill=teal)
    center_text(draw, (966, 707, 1237, 744), "局部窗口自注意力", zh(20), white, stroke_width=1)

    fill_box(draw, (804, 739, 909, 802), fill=white, radius=10)
    center_text(draw, (804, 739, 909, 802), "对比", zh(26), dark, stroke_width=1)

    fill_box(draw, (464, 806, 699, 846), fill=pale, radius=8)
    center_text(draw, (464, 806, 699, 846), "平方复杂度", zh(18), dark, stroke_width=1)
    fill_box(draw, (979, 806, 1235, 846), fill=pale, radius=8)
    center_text(draw, (979, 806, 1235, 846), "线性复杂度", zh(18), dark, stroke_width=1)

    fill_box(draw, (1377, 735, 1665, 833), fill="#F7F8FB", radius=18)
    draw.text((1519, 766), "k << N", font=en(34), fill="#39465A", anchor="mm")
    center_text(draw, (1388, 782, 1655, 834), "窗口大小 k 远小于序列长度 N", zh(18), dark, stroke_width=1)

    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUTPUT_IMAGE)


if __name__ == "__main__":
    main()
