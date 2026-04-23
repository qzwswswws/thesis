# 第 5 章图表规划清单（2026-04-22）

## 1. 用途

本文档用于固定第 5 章正文计划使用的主图和主表，并明确：

1. 哪些图表继续保留。
2. 哪些图表需要改用 `full70` 最终版本数据重绘。
3. 哪些旧图不再作为正文主图，而转为段内文字证据或补充资产。
4. 如果坚持某个原命题，需要额外补什么实验，而不是强行替换图。

---

## 2. 图表选择原则

### 2.1 总原则

- 主图只保留能直接支撑正文主张的资产。
- 不混用不同协议的数据去支撑同一幅图的单一结论。
- `full70` 优先用于已经完成统一复核、且结论正好对应当前正文写法的部分。
- 如果现有 `full70` 资产覆盖不了原图命题，就改图题和图义，不硬套。

### 2.2 当前最重要的约束

当前工作区中，`full70` 统一复核明确覆盖的是：

- `pretrained_upper_refit_no_ea`
- `unweighted_source`
- `weighted_source`
- `random_source`
- `weight_decay_source`
- seeds `42/43/44`
- 目标被试 `S1-S9`

但当前工作区中**没有**同一层级的 `full70` 统一矩阵去同时覆盖：

- `pretrained_no_update`
- `pretrained_online_ea`
- `pretrained_upper_refit_no_ea`

因此，如果图 5.3 还坚持写成“`upper_refit` 比 `EA only` 更具保留价值”的 `full70` 主图，那么需要补跑新的统一复核；现有资产不能直接替代。

---

## 3. 正文主图计划

| 序号 | 计划图题 | 拟放位置 | 主张 | 计划数据/资产 | 处理决定 |
| --- | --- | --- | --- | --- | --- |
| 图 5.1 | 代表性方法族条件下的伪在线轮次依赖现象 | `5.1.2` | 局部轮次难度不是某一个模型族内部的偶然现象，而是在传统方法、卷积网络和注意力模型之间共同存在 | `Stage1_Round_Dependency_Representative_Methods_seed42.md/csv`；`visualization/stage1_round_dependency_representative_methods_seed42.png` | 已重绘并同步到 LaTeX 图目录 |
| 图 5.2 | `full70` 条件下预训练数据桥接条件的稳定性复核 | `5.1.2` 或 `5.1.3` 前半段 | 在识别出强轮次依赖之后，进一步检验预训练数据优化能否改善关键在线指标；结果显示质量降权条件在上层重拟合路线中保留了更稳定的前段正向信号 | `Stage1_Source_Bridge_Full70_Controls_seed42_43_44_all_subjects.md`；`stage1_source_bridge_full70_controls_seed42_43_44_all_subjects.png` | 用最终 `full70 all_subjects` 版本替换现图 |
| 图 5.3 | `full70` 条件下 `weighted_source` 相对 `unweighted_source` 的增益分布 | `5.1.3` | 收益主要集中在 `AULC10/AULC20/instability_6_20`，而不是尾段平台或阈值到达时间 | `stage1_source_bridge_full70_delta_summary_seed42_43_44_all_subjects.csv` | 新绘制一张 delta 视角图 |

---

## 4. 各图的具体写法

### 4.1 图 5.1：已重绘为代表方法族版本

**计划图题：**

`代表性方法族条件下的伪在线轮次依赖现象。图中比较传统空间滤波方法、黎曼几何方法、紧凑卷积网络、纯注意力试验模型和 EdgeMIFormer 在相同时间顺序重放协议下的逐轮准确率。不同方法族在同一目标被试上仍呈现同步起伏，说明局部轮次难度是影响伪在线判断的重要混杂因素。`

**计划资产：**

- 主图：`/home/woqiu/下载/git/MI_Algorithm_Workbench/visualization/stage1_round_dependency_representative_methods_seed42.png`
- LaTeX 图：`/home/woqiu/下载/git/thesis/01_Thesis_LaTeX/figures/C5-2_stage1_round_dependency_seed42.png`
- 指标报告：`/home/woqiu/下载/git/MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Round_Dependency_Representative_Methods_seed42.md`
- 绘图脚本：`/home/woqiu/下载/git/MI_Algorithm_Workbench/visualization/plot_stage1_round_dependency_representative_methods.py`

**决定：**

- 这张图的主张是“存在跨方法族的轮次依赖”，不是“某个方法最终最好”。
- `full70 all-subjects` 资产只覆盖同一主线分支下的 source 条件，不能支撑跨方法族对照；因此图 5.1 改用三名代表目标被试上的补充实验，而不是强行使用 `full70`。
- 正文中避免直接写实验目录中的原始被试变量名，可表述为“三名代表性目标被试”或“目标 A、目标 B、目标 C”。

### 4.2 图 5.2：改用 `full70 all_subjects`

**建议新图题：**

`多随机种子与多目标被试条件下，full70 伪在线协议中的预训练数据桥接条件复核结果。相较于未加权预训练条件，质量降权预训练条件在上层重拟合路线中保持了更稳定的前段正向趋势，而随机加权和权重衰减对照未能同时复制其在前 20 轮累计面积与中前段波动控制上的组合优势。`

**计划资产：**

- 报告：`/home/woqiu/下载/git/MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Source_Bridge_Full70_Controls_seed42_43_44_all_subjects.md`
- 现成图：`/home/woqiu/下载/git/MI_Algorithm_Workbench/visualization/stage1_source_bridge_full70_controls_seed42_43_44_all_subjects.png`
- 汇总 CSV：`/home/woqiu/下载/git/MI_Algorithm_Workbench/online_simulation/stage1_source_weight_bridge_full70/stage1_source_bridge_full70_combined_summary_seed42_43_44_all_subjects.csv`

**决定：**

- 这张图替换当前正文里的 `unified_core_seed_stability` 主图。
- 用 `all_subjects` 版本比 `S1/S5/S9` 更有说服力。
- 这张图的前因后果要写清楚：不是为了继续堆预训练条件，而是在识别出强轮次依赖之后，进一步追问“通过优化预训练数据使用方式，能否改善更贴近在线体验的关键指标”。
- 当前结果允许写成“质量降权条件确实有效，是一种值得保留的预训练数据优化策略，且效果主要集中在若干过程指标”，但不宜写成“在所有指标和所有条件下都稳定占优”。
- 图义也需要同步调整，不再写 `classic_weighted / random_weighted / loss_drop_protected` 那组旧命题，而改写为 `full70 source bridge` 的最终复核。
- 正文中不要直接写内部实验变量名，统一使用“未加权预训练条件”“质量降权预训练条件”“随机加权对照”“权重衰减对照”等解释性名称。

### 4.3 图 5.3：新做 `delta` 视角图

**建议新图题：**

`full70 伪在线协议下 weighted_source 相对 unweighted_source 的指标增益分布。其收益主要集中在 mean raw acc、AULC10、AULC20 和 instability_6_20，而 tailacc_last10 与 TTT@0.8 未表现出同等稳定优势，因此该方法更适合作为改善冷启动前段表现和中前段稳定性的 bridge 方案。`

**计划资产：**

- delta 汇总：`/home/woqiu/下载/git/MI_Algorithm_Workbench/online_simulation/stage1_source_weight_bridge_full70/stage1_source_bridge_full70_delta_summary_seed42_43_44_all_subjects.csv`
- 计划新图文件名：`C5-3_stage1_source_bridge_full70_delta_all_subjects.png`

**建议画法：**

- 以 `weighted_source` 相对 `unweighted_source` 的 delta 为主。
- 同时标出：
  - `mean_raw_acc`
  - `meanacc_at_10`
  - `aulc10`
  - `aulc20`
  - `ttt_0p8`
  - `instability_6_20`
  - `tailacc_last10`
- 最好在同图中补一个 win/tie/loss 小面板，避免只看均值。

**决定：**

- 图 5.3 不再沿用当前 `stage1_total_comparison_seed42.png` 的命题。
- 改成 `full70` 最终复核下“收益集中在哪里”的证据图。
- 这样第 5 章的两张主结果图都能换成最终 `full70` 版本数据。

---

## 5. 正文主表计划

| 序号 | 计划表题 | 拟放位置 | 用途 | 状态 |
| --- | --- | --- | --- | --- |
| 表 5.2 | 真实在线平台中的关键环节与运行产物 | `5.2.1` | 说明 `subject/session/run`、轮后训练、逐 trial 推理与落盘关系 | 已在正文中 |
| 表 5.3 | 真实参与者在线记录的总体概览 | `5.2.2` | 压缩呈现三位真实参与者的总体准确率与代表性现象 | 已在正文中 |

### 5.1 `5.1.1` 的协议说明方式

当前更合适的写法不是单独保留一张“伪在线实验设置与评价指标框架表”，而是在 `5.1.1` 中改写为正文分点说明，按以下顺序交代：

- 数据集与任务设置
- 跨被试预训练口径
- 当前被试评估方式与在线批次组织
- 主要比较对象
- 评价指标框架

这样处理的原因是：这部分更像协议边界说明，而不是需要压缩比较信息的结果表。把它写成正文分点后，可以顺带解释哪些设置真正影响后文判断，避免出现“表里信息很多，但正文并未解释其必要性”的问题。

---

## 6. 不再作为正文主图的现有资产

### 6.1 退为辅助证据

1. `unified_core_seed_stability_seed42_43_44_s1_5_9.png`

- 仍然有价值。
- 适合作为“旧一层 source quality core control”的辅助证据。
- 但若图 5.2 改用 `full70 all_subjects`，它不再占正文主图位。

2. `stage1_total_comparison_seed42.png`

- 仍然是当前“`upper_refit` 比 `EA only` 更值得保留”的直接证据。
- 但它不是 `full70` 统一复核结果。
- 更适合保留在段内文字和表格叙述中，而不是继续作为正文主图。

### 6.2 为什么不继续把 `stage1_total_comparison_seed42.png` 当主图

原因不是它没价值，而是它和当前拟写的第 5 章主线有两个冲突：

1. 它只覆盖 seed42、`S1/S5/S9`。
2. 它的命题是 `upper_refit vs EA only`，而当前已完成的最终 `full70` 复核只覆盖 `upper_refit` 分支内部的 source 条件。

因此，如果继续把它放在主图位，会造成：

- 图 5.2 和图 5.3 的证据等级不一致。
- 读者会误以为“`EA only` 也做了同等层级的 `full70` 统一复核”。

---

## 7. 如果坚持原图 5.3 命题，需要补什么

如果坚持保留原来的图 5.3 命题：

`upper_refit 类策略比 EA only 更具保留价值`

那么需要额外补一轮统一复核，而不是简单重绘现图。至少要统一补齐：

- `pretrained_no_update`
- `pretrained_online_ea`
- `pretrained_upper_refit_no_ea`
- seeds `42/43/44`
- 目标被试 `S1-S9`
- `max_rounds=70`

只有这样，图 5.3 才能在 `full70` 口径下继续讲“`upper_refit` 对 `EA only`”这一命题。

在当前资产条件下，我不建议这样写主图；更稳的方案是把这个判断保留在正文段落里，把两张主结果图都收敛到已经完成的 `full70` 证据上。

---

## 8. 当前推荐的最终组合

### 8.1 推荐主图组合

- 图 5.1：轮次依赖现象图，保留。
- 图 5.2：`full70 all_subjects` 预训练数据桥接条件总览图，替换。
- 图 5.3：`full70 all_subjects` delta 增益分布图，新绘。

### 8.2 推荐主表组合

- 表 5.2：真实在线运行链与落盘产物，保留。
- 表 5.3：真实参与者总体概览，保留。

### 8.3 推荐写法上的联动

- `5.1.2` 主要由图 5.1 + 图 5.2 支撑。
- `5.1.3` 主要由图 5.3 + 段内数值支撑。
- `upper_refit` 比 `EA only` 更值得保留，这一句保留在正文段落中，用已有 `Stage1_Total_Comparison_seed42` 数字支持，但不再占正文主图位。

---

## 9. 下一步执行顺序

1. 将 `full70 all_subjects` 总览图复制为第 5 章新图位。
2. 基于 `delta_summary_seed42_43_44_all_subjects.csv` 新绘图 5.3。
3. 在 `chap05.tex` 中同步调整图题、图号和 `5.1.2/5.1.3` 的段落主张。
4. 将 `unified_core_seed_stability` 和 `stage1_total_comparison_seed42` 退为段内证据，不再占主图位。
