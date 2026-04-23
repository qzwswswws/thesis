import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import matplotlib.patheffects as path_effects
import os

simsun_path = "01_Thesis_LaTeX/tools/fonts/simsun.ttf"
simsun_name = "SimSun"
try:
    if os.path.exists(simsun_path):
        fm.fontManager.addfont(simsun_path)
        simsun_name = fm.FontProperties(fname=simsun_path).get_name()
except: pass

en_font_path = "/usr/share/fonts/truetype/croscore/Tinos-Regular.ttf"
en_name = "Times New Roman"
try:
    if os.path.exists(en_font_path):
        fm.fontManager.addfont(en_font_path)
        en_name = fm.FontProperties(fname=en_font_path).get_name()
except: pass

plt.rcParams["font.family"] = [simsun_name, "SimSun", "Times New Roman", en_name, "serif"]
plt.rcParams['mathtext.fontset'] = 'stix' 
plt.rcParams["axes.unicode_minus"] = False

def get_font(size, bold=False):
    prop = fm.FontProperties(family=[simsun_name, "SimSun", "Times New Roman", en_name, "serif"])
    prop.set_size(size)
    prop.set_weight("bold" if bold else "normal")
    return prop

def draw_container(ax, center, width, height, title):
    x = center[0] - width / 2
    y = center[1] - height / 2
    box = patches.FancyBboxPatch((x, y), width, height,
                                 boxstyle="round,pad=0.1,rounding_size=0.1",
                                 facecolor="#FAFAFA", edgecolor="#555555", 
                                 linewidth=1.2, linestyle='--', zorder=1)
    ax.add_patch(box)
    txt = ax.text(x + 0.25, y + height - 0.12, title, ha='left', va='top',
            color='#111111', fontproperties=get_font(13, bold=True), zorder=2)
    txt.set_path_effects([path_effects.withStroke(linewidth=0.5, foreground='#111111')])

def draw_box(ax, center, width, height, text, fontsize=12.5):
    x = center[0] - width / 2
    y = center[1] - height / 2
    box = patches.FancyBboxPatch((x, y), width, height,
                                 boxstyle="round,pad=0.1,rounding_size=0.1",
                                 facecolor="#FFFFFF", edgecolor="#000000", linewidth=1.1, zorder=3)
    box.set_path_effects([
        path_effects.SimplePatchShadow(offset=(2.0, -2.0), shadow_rgbFace="#000000", alpha=0.08),
        path_effects.Normal()
    ])
    ax.add_patch(box)
    txt = ax.text(center[0], center[1], text, ha='center', va='center',
            color="#000000", fontproperties=get_font(fontsize, bold=True), linespacing=1.5, zorder=4)
    txt.set_path_effects([path_effects.withStroke(linewidth=0.4, foreground='#000000')])

def draw_vertical_arrow(ax, x, start_y, end_y, text=''):
    # start_y and end_y are exact points. arrowprops determines how it's drawn.
    ax.annotate('', xy=(x, end_y), xytext=(x, start_y),
                arrowprops=dict(facecolor='#000000', edgecolor='#000000', width=1.5, headwidth=6, headlength=8, shrink=0),
                zorder=2)
    if text:
        ax.text(x + 0.25, (start_y + end_y) / 2, text, ha='left', va='center', color='#000000', fontproperties=get_font(12), zorder=5)


fig, ax = plt.subplots(figsize=(6.5, 14), dpi=180)

# Layout Algorithm
X_C = 3.25
box_w = 4.8
cont_w = 5.8
box_h = 0.85
pad_top = 0.7  # inner pad from top of container to first box
pad_bot = 0.3  # inner pad from last box to bot of container
pad_gap = 0.8  # vertical gap between boxes in a container
pad_inter = 1.3 # vertical gap between containers
arr_gap = 0.05 # small gap between arrow ends and shapes

y_cursor = 18.0

# 1. Input Node
y_input_top = y_cursor
y_input_bot = y_input_top - box_h
y_input_c = (y_input_top + y_input_bot) / 2
draw_box(ax, (X_C, y_input_c), 4.2, box_h, "预处理脑电信号\n$\mathbf{X} \in \mathbb{R}^{C \\times T}$", fontsize=13)
y_cursor = y_input_bot
y_cursor -= pad_inter

# 2. Stage 1 Layout
s1_top = y_cursor
box1_s1_c = s1_top - pad_top - box_h/2
box2_s1_c = box1_s1_c - box_h/2 - pad_gap - box_h/2
s1_bot = box2_s1_c - box_h/2 - pad_bot
s1_h = s1_top - s1_bot
s1_c = (s1_top + s1_bot) / 2

draw_container(ax, (X_C, s1_c), cont_w, s1_h, "时空解耦特征提取")
draw_box(ax, (X_C, box1_s1_c), box_w, box_h, "时间卷积 (提取局部频带波形)", fontsize=12.5)
draw_vertical_arrow(ax, X_C, box1_s1_c - box_h/2 - arr_gap, box2_s1_c + box_h/2 + arr_gap)
draw_box(ax, (X_C, box2_s1_c), box_w, box_h, "空间卷积 (跨导联空间聚合)", fontsize=12.5)

# Arrow from Input to Stage 1 Top
draw_vertical_arrow(ax, X_C, y_input_bot - arr_gap, s1_top + arr_gap)

y_cursor = s1_bot
y_cursor -= pad_inter

# 3. Stage 2 Layout
s2_top = y_cursor
box1_s2_c = s2_top - pad_top - box_h/2
box2_s2_c = box1_s2_c - box_h/2 - pad_gap - box_h/2
box3_s2_c = box2_s2_c - box_h/2 - pad_gap - box_h/2
s2_bot = box3_s2_c - box_h/2 - pad_bot
s2_h = s2_top - s2_bot
s2_c = (s2_top + s2_bot) / 2

draw_container(ax, (X_C, s2_c), cont_w, s2_h, "局部窗口自注意力编码 ( $\\times$ $6$ 级联 )")
draw_box(ax, (X_C, box1_s2_c), box_w, box_h, "局部窗口自注意力计算 ($O(N \cdot k)$)", fontsize=12.5)
draw_vertical_arrow(ax, X_C, box1_s2_c - box_h/2 - arr_gap, box2_s2_c + box_h/2 + arr_gap)
draw_box(ax, (X_C, box2_s2_c), box_w, box_h, "前馈神经网络 ($\mathbf{FFN}$)", fontsize=12.5)
draw_vertical_arrow(ax, X_C, box2_s2_c - box_h/2 - arr_gap, box3_s2_c + box_h/2 + arr_gap)
draw_box(ax, (X_C, box3_s2_c), box_w, box_h, "残差连接与层归一化", fontsize=12.5)

# Arrow from Stage 1 to Stage 2
draw_vertical_arrow(ax, X_C, s1_bot - arr_gap, s2_top + arr_gap, text="$\mathbf{Z} \in \mathbb{R}^{N \\times D}$ 特征序列")

y_cursor = s2_bot
y_cursor -= pad_inter

# 4. Stage 3 Layout
s3_top = y_cursor
box1_s3_c = s3_top - pad_top - box_h/2
box2_s3_c = box1_s3_c - box_h/2 - pad_gap - box_h/2
s3_bot = box2_s3_c - box_h/2 - pad_bot
s3_h = s3_top - s3_bot
s3_c = (s3_top + s3_bot) / 2

draw_container(ax, (X_C, s3_c), cont_w, s3_h, "分类输出")
draw_box(ax, (X_C, box1_s3_c), box_w, box_h, "全局平均池化 & 多尺度最大池化", fontsize=12.5)
draw_vertical_arrow(ax, X_C, box1_s3_c - box_h/2 - arr_gap, box2_s3_c + box_h/2 + arr_gap)
draw_box(ax, (X_C, box2_s3_c), box_w, box_h, "层归一化 + $\mathbf{ELU}$ & 全连接层", fontsize=12.5)

# Arrow from Stage 2 to Stage 3
draw_vertical_arrow(ax, X_C, s2_bot - arr_gap, s3_top + arr_gap)

y_cursor = s3_bot
y_cursor -= pad_inter

# 5. Output
y_out_top = y_cursor
y_out_bot = y_out_top - box_h
y_out_c = (y_out_top + y_out_bot) / 2
draw_box(ax, (X_C, y_out_c), 4.2, box_h, "分类概率预测", fontsize=13)

# Arrow from Stage 3 to Output
draw_vertical_arrow(ax, X_C, s3_bot - arr_gap, y_out_top + arr_gap)

# Setup AX limits to tightly fit layout
ax.set_xlim(0, 6.5)
ax.set_ylim(y_out_bot - 0.5, 18.5)
ax.axis('off')

fig.savefig("EdgeMIFormer_Arch_Rendered.pdf", bbox_inches="tight", pad_inches=0.1)
fig.savefig("EdgeMIFormer_Arch_Rendered.png", bbox_inches="tight", pad_inches=0.1, dpi=300)
print("Plots generated with programmatic layout and separated arrows.")
