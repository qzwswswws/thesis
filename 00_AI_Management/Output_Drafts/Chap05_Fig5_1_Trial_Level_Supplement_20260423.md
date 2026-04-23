# 图 5.1 试次级补充验证（2026-04-23）

## 1. 定位

该附图/附表用于作为图 5.1 的试次级补充证据，回答“跨方法共享困难结构是否还能细化到单个目标端试次”这一问题。

它不替代正文中的批次级主证据，而是作为更细粒度验证：

- 批次级主图用于说明伪在线时间顺序重放中存在共享的在线批次结构。
- 正文中的试次级补充图仅保留被试 9，用于直观展示单试次层面的共同判错形态。
- 其余代表性被试（被试 1、被试 5）的统计结果转为表格进入正文，用于补足跨被试一致性证据。

## 2. 数据口径

- 数据来源：
  - `MI_Algorithm_Workbench/online_simulation/sub1_loso_no_update_trial_agreement_seed42/`
  - `MI_Algorithm_Workbench/online_simulation/sub5_loso_no_update_trial_agreement_seed42/`
  - `MI_Algorithm_Workbench/online_simulation/sub9_loso_no_update_trial_agreement_seed42_v2/`
- 目标被试：被试 1、被试 5、被试 9
- 代表性方法：EdgeMIFormer、RawPatch Transformer、CSP+LDA、MDM、EEGNet
- 条件口径：均为 no-update 条件，与图 5.1 的代表性方法口径保持一致
- 分析单位：单个目标端试次
- 每名被试总试次数：320

说明：当前五种代表性方法的同口径逐试次明细现已完整覆盖被试 1、5、9，因此该补充验证可以写成“代表性被试组上的细粒度证据”；但由于尚未扩展到全部目标被试，仍不宜扩大表述为“全被试试次级主结论”。

## 3. 图和表的资产路径

- 单被试正文图脚本：`MI_Algorithm_Workbench/visualization/plot_stage1_trial_level_representative_methods_sub9.py`
- 单被试正文图文件：`MI_Algorithm_Workbench/visualization/stage1_trial_level_representative_methods_sub9_seed42.png`
- LaTeX 图目录副本：`thesis/01_Thesis_LaTeX/figures/C5-S1_trial_level_representative_methods_sub9_seed42.png`
- 方法汇总表：`MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Trial_Level_Representative_Methods_S1_S5_S9_MethodSummary_seed42.csv`
- 共享试次汇总表：`MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Trial_Level_Representative_Methods_S1_S5_S9_SharingSummary_seed42.csv`
- 原始说明报告：`MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Trial_Level_Representative_Methods_S1_S5_S9_seed42.md`
- 三被试合图资产保留为分析备份：
  - `MI_Algorithm_Workbench/visualization/plot_stage1_trial_level_representative_methods_s1_s5_s9.py`
  - `MI_Algorithm_Workbench/visualization/stage1_trial_level_representative_methods_s1_s5_s9_seed42.png`
  - `thesis/01_Thesis_LaTeX/figures/C5-S1_trial_level_representative_methods_s1_s5_s9_seed42.png`

## 4. 建议图注

被试 9 的试次级补充验证。

图注保持简洁即可，详细解释放在正文或本 md。

## 5. 建议正文说明

可配套写为：

> 为进一步确认跨方法共享困难结构是否还能细化到单个目标端试次，本文在被试 1、被试 5 和被试 9 上补充整理了五种代表性 no-update 方法的逐试次结果。考虑到三名被试逐试次热图并列展示时信息密度过高，正文中仅保留被试 9 的逐试次补充图，用于说明单试次层面的共同判错形态；其余两名代表性被试的统计结果转入正文表格。图中上半部分给出五种方法在 320 个目标端试次上的判对/判错矩阵，其中绿色表示该方法在对应试次上判对，红色表示判错；下半部分统计每个试次的判错方法数，虚线对应“至少 3 种方法同时判错”的共同困难阈值。

> 从统计量上看，被试 9 的五种方法平均两两试次级正确性相关系数为 0.4553；在 320 个试次中，至少 3 种方法同时判错的试次数为 53，至少 4 种方法同时判错的试次数为 32。采用循环移位置换检验后，平均两两试次级相关以及“至少 3 种/4 种方法同时判错”的计数均显著高于随机对齐分布（经验 $p<10^{-4}$）。其余两名代表性被试的统计结果分别为：被试 1 的平均两两试次级相关为 0.5673，至少 3 种方法同时判错 98 次，至少 4 种方法同时判错 72 次，三项统计量经验 $p$ 值均小于 $10^{-4}$；被试 5 的平均两两试次级相关为 0.2888，至少 3 种方法同时判错 95 次，至少 4 种方法同时判错 55 次，其中平均两两相关和“至少 4 种方法同时判错”计数经验 $p$ 值均小于 $10^{-4}$，“至少 3 种方法同时判错”计数经验 $p$ 值为 0.0025。该结果说明，在代表性被试组上，跨方法共享困难结构不仅存在于批次平均层面，也能够进一步细化到单个试次层面。

## 6. 读图说明

- 上半部分：
  - 纵轴是五种代表性方法。
  - 横轴是目标端试次编号。
  - 绿色表示该方法在该试次上判对，红色表示判错。
  - 若某一竖向位置同时出现多条红块，表示该试次对多种方法都较难。
- 下半部分：
  - 纵轴表示该试次上有多少种方法判错，范围为 0--5。
  - 红色柱表示该试次达到“至少 3 种方法同时判错”的共同困难阈值。
  - 灰色柱表示该试次虽然有错误，但尚未达到共同困难阈值。
  - 虚线是共同困难阈值，用于直观看出共享困难试次的密度和聚集位置。

## 7. 关键表格口径

### 7.1 共享试次结构汇总

| 被试 | 平均两两试次级正确性相关 | 至少 3 种方法同时判错 | 至少 4 种方法同时判错 | 5 种方法全部判错 | 5 种方法全部判对 | `p(>=3同判错)` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 被试 1 | 0.5673 | 98 / 320 | 72 / 320 | 44 | 154 | `< 10^{-4}` |
| 被试 5 | 0.2888 | 95 / 320 | 55 / 320 | 25 | 89 | `0.0025` |
| 被试 9 | 0.4553 | 53 / 320 | 32 / 320 | 15 | 191 | `< 10^{-4}` |

## 8. 证据边界

- 这是代表性被试组上的试次级补充验证，不是全被试的试次级主结论。
- 它能够支持“共享困难现象在单试次层面也有体现”这一表述。
- 它不应被写成“所有被试均已稳定证明存在统一的试次级共享难点结构”。
- 因此在正文中更稳妥的写法是：
  - “在被试 1、被试 5 和被试 9 这组三名代表性被试上，试次级补充分析进一步支持了跨方法共享困难结构的存在。”
  - “正文图仅展示被试 9 的直观形态，其余代表性被试通过统计表补足。”
  - “该结果与批次级主图形成一致证据，但试次级资产目前仍以代表性被试组验证为主。”
