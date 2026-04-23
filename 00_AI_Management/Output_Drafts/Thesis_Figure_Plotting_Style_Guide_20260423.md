# 论文绘图通用规范（2026-04-23）

## 1. 适用范围

本文档用于统一论文章节主图、补充图和由 Python 脚本生成的实验图。当前优先适用于第 5 章伪在线实验、在线实验记录图和后续重绘图。

## 2. 字体规范

- 中文：宋体，加粗。
- 英文与数字：Times New Roman。
- 数学符号：优先使用 STIX 数学字体。
- 图内中文标题、图例中文、横轴类别中文均使用宋体加粗。
- 纵轴刻度、柱顶数值、坐标刻度数字使用 Times New Roman，通常不加粗。
- 若系统中没有注册字体，优先从论文工具目录加载：
  - 宋体：`thesis/01_Thesis_LaTeX/tools/fonts/simsun.ttf`
  - Times New Roman：`thesis/01_Thesis_LaTeX/tools/fonts/Times.TTF`

推荐 Python 字体初始化方式：

```python
from pathlib import Path
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

THESIS_ROOT = Path("/home/woqiu/下载/git/thesis")
SIMSUN_PATH = THESIS_ROOT / "01_Thesis_LaTeX" / "tools" / "fonts" / "simsun.ttf"
TIMES_PATH = THESIS_ROOT / "01_Thesis_LaTeX" / "tools" / "fonts" / "Times.TTF"

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
```

注意：部分宋体文件只有常规字重，单独设置 `fontweight="bold"` 可能不会形成明显加粗。正文图中的中文标题和横轴类别标签建议同时使用 `fontweight=bold` 与轻微描边，例如子图标题 `linewidth=0.45`，横轴类别 `linewidth=0.35`。

## 3. 图内文字规范

- 图内文字尽量使用中文。
- 必要英文缩写可以保留，但应以“中文名称 + 英文缩写”的形式出现。
- 指标缩写示例：
  - 前十批次平均准确率（Avg@10）
  - 前二十批次累计面积（AULC20）
  - 第六至二十批次波动（Instab.6-20）
  - 最后十批次平均准确率（Tail@10）
- 图内不写冗长解释，如“越高越好”“越低越好”。方向性说明放在正文或图注中。
- 图内不直接写实验代码中的内部变量名，例如 `weighted_source`、`pretrained_upper_refit_no_ea`、`subject/session/run` 等。需要先转成可解释中文名称。

## 3.1 试次、批次与运行单位

- `trial` 统一译为“试次”，用于指一次提示、一次运动想象任务段或一次逐试次推理样本。
- 伪在线 `stage1` 图中的 `round` 不是单个试次，而是由 10 个目标端试次组成的时间顺序评估单位，正文和图内统一写为“在线批次”或简称“批次”。
- 当指标名涉及 `Avg@10`、`AULC20`、`Instab.6-20`、`Tail@10` 时，`10`、`20` 指在线批次数，不指单个试次数。
- 真实在线系统中的 `run` 统一写为“会话”或“run 级记录”；只有在引用文件层级或命令名称时保留 `run`。
- 避免在同一图或同一段中混用“轮次”“试次”“批次”。真实在线流程中优先写“会话后训练”“逐试次推理”，避免再使用“轮后训练”。

## 4. 实验条件命名

正文图中的条件名应按照方法原理命名，而不是按照代码变量名翻译。

以第 5 章源端桥接图为例：

| 内部变量名 | 图内名称 | 正文名称 |
| --- | --- | --- |
| `unweighted_source` | 未调制 | 未调制源端基线 |
| `weighted_source` | 质量降权 | 源端质量降权条件 |
| `random_source` | 随机降权 | 随机降权对照 |
| `weight_decay_source` | 参数衰减 | 参数衰减对照 |

命名原则：

- 如果方法本质是降低部分样本权重，优先写“降权”，不要泛写“加权”。
- 如果是随机选择同等数量样本降权，写“随机降权”，突出其对照性质。
- 如果是优化器正则化，不写成样本权重方法，写“参数衰减”或“正则化对照”。
- 如果是论文主方法，统一使用论文确定名称，例如 `EdgeMIFormer`。

## 5. 图题与图注分工

- 正文主图通常不设置图内总标题，图题交给 LaTeX 图注。
- 如果是独立展示用图片而必须设置图内总标题，只写图的核心对象，不写实验目录或内部标签。
- 具体协议如“完整 70 个在线批次”“3 个随机种子与 9 名目标被试”“时间顺序重放”等，优先放在图注或正文解释中。
- 图注保持简洁，说明：
  - 图展示什么。
  - 各子图分别是什么。
  - 基线或虚线代表什么。
  - 能支持的结论边界。
- 详细读图说明放在管理 md 中，不堆进图注。

## 6. 视觉与版式规范

- 主图优先输出 PNG，同时保留绘图脚本和 CSV/报告路径。
- 论文正文图建议宽度：
  - 单图：`0.92\textwidth` 至 `0.97\textwidth`
  - 多子图：优先保持 2×2 或 1×3 的规整布局
- 子图标题字号一般 12--14。
- 横轴类别标签字号一般 10--12。
- 纵轴刻度和数值标注字号一般 9--11。
- 颜色应保持可区分，不使用过度鲜艳或大面积单一紫蓝色。
- 若纵轴采用局部放大尺度，正文或图注必须说明“绝对差异较小，图中用于比较相对趋势”。

## 7. 数据与证据边界

- 图必须能直接对应正文主张，不用旧协议图支撑新协议结论。
- 不混用不同协议、不同目标被试范围或不同轮数的结果去支撑同一幅主图。
- 若图中使用公开数据集的代表性被试，优先使用真实编号，例如“被试 1、被试 5、被试 9”；不要再额外映射成“目标 A/B/C”。
- 若图中使用完整复核数据，应在正文说明“覆盖多少随机种子、多少目标被试组合、多少在线批次”。
- 对探索性结果，优先写“小幅正向趋势”“条件性补充”“初步可用性”，避免写成“显著提升”“已定型主方法”。

## 8. 输出与归档要求

每张正文图应至少保留：

- 绘图脚本路径。
- 原始或汇总数据 CSV 路径。
- 图片输出路径。
- 图义说明 md。
- 如替换旧图，应保留旧图或说明旧图退为辅助证据。

推荐命名：

- 脚本：`plot_<chapter>_<figure_topic>.py`
- 图片：`C5-<n>_<short_topic>.png`
- 图义文档：`Chap05_Fig5_<n>_<short_topic>_<date>.md`

## 9. 最终检查清单

- 中文是否为宋体加粗。
- 英文和数字是否为 Times New Roman。
- 图内是否存在未解释的内部变量名。
- 图内是否出现不必要的英文长句。
- 图题是否简洁。
- 正文主图是否去掉了图内正上方总标题。
- 图注是否解释了基线、子图含义和结论边界。
- 局部放大坐标轴是否在正文或图注中说明。
- 图片是否已同步到 LaTeX 图目录。
- LaTeX 正文引用的文件名是否与最新图一致。
