# 论文章节与本地实验资产对照分析

更新日期：`2026-04-20`

## 1. 分析范围与总判断

本次分析只基于 `/home/woqiu/下载/git` 下当前可见的本地仓库与文件，不假设 git 外部路径中的额外原始数据一定可作为论文正式证据。

总判断如下：

1. 当前论文主线已经基本成形，`第 3 章`、`第 4 章`、`第 5 章` 都能在本地找到较明确的资产对应。
2. `第 4 章` 中离线 baseline、通道退化、任务收束、多 seed、外部数据集、经典对照、通道组合和混淆矩阵，和本地 `MI_Algorithm_Workbench` 的对应关系最完整。
3. 最大的证据口径风险不在低通道 baseline，而在 `EdgeMIFormer + RK3568/RK NPU 部署` 这一段：论文现在把它写成已完成主结果，但当前本地主工作区并没有同等级、同协议、可复核的完整实验闭环。
4. `第 5 章` 的伪在线部分与本地 `online_simulation` 匹配度较高；真实在线部分则是“有分析稿、有部分归档、有新一轮汇总，但 git 内原始 run 证据分散且不完全同一口径”。
5. 以后如果要继续修论文，定位规则必须固定为：`thesis/01_Thesis_LaTeX` 看正文，`MI_Algorithm_Workbench` 看离线与伪在线主实验，`nearalQTpro` 看当前在线程序源码，`olrecord` 看在线归档与论文支撑，`thesis/02_Source_Material/04_Algorithm_Workbench` 只能当快照而不是最新账本。

### 1.1 远端同步后的影响评估

本文件初稿完成后，`thesis` 仓库又同步到了远端新提交：

- 提交：`0efe004`
- 说明：`docs: sync current thesis revision notes`

该提交只改动了 3 个文档：

- `00_AI_Management/Output_Drafts/Chap01_Reorg_Plan_20260415.md`
- `00_AI_Management/Output_Drafts/主线与创新点微调稿_20260415.md`
- `00_AI_Management/Output_Drafts/论文修改意见v1.md`

判断如下：

1. 它**没有直接改动** `thesis/01_Thesis_LaTeX/data/chap01.tex` 到 `chap06.tex`，也没有改动算法实验目录、图表目录和在线程序目录。
2. 因此，本文件关于“现有正文和现有实验资产之间的对应关系”的主判断**不变**。
3. 这次同步带来的新增信息主要是：
   - 第 1 章正在被进一步重构；
   - 全文主线与创新点口径正在被统一；
   - 已新增一个可继续填写的总修改意见模板。
4. 它对本文件结论的影响是“**补强写作层面判断**”，而不是“推翻实验映射判断”。
5. 换句话说，本文件中关于 `EdgeMIFormer/RK NPU` 证据偏强、`第 5 章` 真实在线证据链不够统一、`MI_Algorithm_Workbench` 才是最新实验账本等判断，**同步后仍然成立**。

---

## 2. 本地 Git 相关目录定位图

| 目录 | 角色 | 权威级别 | 优先用于定位什么 | 备注 |
| --- | --- | --- | --- | --- |
| `thesis/01_Thesis_LaTeX` | 论文正文与插图主入口 | 最高 | 当前论文写了什么、图表是否已进文稿 | 以 `data/chap01.tex` 到 `data/chap06.tex` 为准 |
| `thesis/02_Source_Material/03_Hardware_Workbench` | 第 3 章硬件素材库 | 高 | 原理图、PCB、BOM、协议说明、UI 截图 | 更像材料归档，不是运行日志中心 |
| `thesis/02_Source_Material/04_Algorithm_Workbench` | 论文内嵌算法快照 | 中 | 第 4 章早期快照、复制到论文仓的图表与 csv | 不是最新实验账本 |
| `MI_Algorithm_Workbench` | 算法主工作区 | 最高 | 第 4 章与第 5 章的大部分离线/伪在线证据 | 后续找算法实验应优先看这里 |
| `MI_Algorithm_Workbench/results_summaries` | 离线结果表根目录 | 高 | baseline、退化、多 seed、外部数据集、EEGNet、通道组合、复杂度 | 适合做论文表格追溯 |
| `MI_Algorithm_Workbench/visualization` | 论文图和分析图根目录 | 高 | 第 4 章和第 5 章大部分 png 图来源 | 与 `results_summaries` 配套 |
| `MI_Algorithm_Workbench/online_simulation` | 伪在线/冷启动/源数据加权主实验根目录 | 高 | stage1、round dependency、source weighting、trial diagnostics | 第 5 章伪在线部分主要来自这里 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts` | 管理层总结与中间分析稿 | 高 | 快速读结论、定位实验族谱、找“哪项已完成/未完成” | 解释层入口，不等于原始实验本体 |
| `nearalQTpro` | 当前在线实验程序源码 | 高 | 第 5 章真实在线程序、Qt 前端、bridge 脚本 | 当前主线程序，不是归档 |
| `olrecord` | 在线实验归档库 | 高 | 归档源码、归档 runtime、归档 marker/alpha 日志、论文支撑文档 | 用于追溯已跑过的在线实验 |
| `forexp` | 第一代原型程序与固件工程 | 中 | 第 3 章早期程序与固件来源、协议演化 | 旧原型，不应当成当前主线版本 |
| `在线实验记录` | 物理实验静态标本库 | 中 | alpha 实验图、marker 记录等 | 更像精选归档，不是完整在线系统账本 |
| `Data_Analysis_Tools` | 数据清洗与绘图脚本 | 中 | alpha 图、趋势图、汇总图的脚本支撑 | 支持第 3 章或在线日志清洗 |
| `MI_Paper_Knowledge_Clusters_20260414` | 文献知识簇 | 中 | 第 1/2 章和第 5 章方法背景 | 主要用于综述与论证，不是实验结果 |
| `Charge/MI_Algorithm_Workbench_Snapshot_20260329` | 旧快照镜像 | 低 | 查 2026-03-29 时点的算法工作区状态 | 可当历史参照，不应用作最新证据 |
| `EEG-Conformer`、`EEGDformer`、`ICA` | 更早历史算法目录 | 低 | 回溯旧模型来源 | 当前论文主线不应优先引用这些目录 |

---

## 3. 论文章节与现有实验资产对照表

匹配度口径：

- `强`：正文主张能在 git 内找到脚本、结果表、图或归档材料的完整链条。
- `中`：正文主张有本地分析稿或部分归档支撑，但原始 run 或统一协议证据不完整。
- `弱`：正文主张当前更多依赖候选代码、归档文字或外部前期成果，本地主工作区闭环不足。

| 章节/部分 | 论文当前主张 | 本地对应资产 | 匹配度 | 主要判断 |
| --- | --- | --- | --- | --- |
| `第 1 章` 绪论 | 建立便携式、低通道、端侧 BCI 问题背景 | `thesis/01_Thesis_LaTeX/data/chap01.tex`；`thesis/03_Literature`；`MI_Paper_Knowledge_Clusters_20260414` | 中 | 主要是文献与问题定义，不依赖实验；本地文献资产充足，但不是“实验映射章” |
| `第 2 章` 技术基础 | 运动想象 EEG、生理基础、Transformer、BLE、KS1092、RK3568 约束 | `thesis/01_Thesis_LaTeX/data/chap02.tex`；`thesis/03_Literature`；`thesis/02_Source_Material/03_Hardware_Workbench`；`MI_Algorithm_Workbench/candidates` | 中 | 理论与系统背景较完整；但 `EdgeMIFormer` 技术部分与当前主工作区实验闭环并不完全同步 |
| `第 3 章` 硬件架构/电路/UI/协议 | 已完成双导硬件、主控、BLE、上位机、PCB/原理图设计与实现 | `thesis/02_Source_Material/03_Hardware_Workbench`；`forexp/neurameter`；`forexp/nearalQT`；`nearalQTpro`；`thesis/01_Thesis_LaTeX/figures/C3-*` | 强 | 图纸、截图、协议说明、固件源码、上位机源码在本地都能落到目录 |
| `第 3 章` Alpha 验证 | 闭眼/睁眼比值 `1.1573`、`1.1424` 证明有生理可解释性 | `thesis/00_AI_Management/Output_Drafts/Chap03_Writing_Status_And_Data_Index_20260401.md`；`在线实验记录/alpha实验`；`olrecord/nearalQTpro_logs/alpha` | 中 | 有汇总稿和日志，但正文主要使用整理后的统计，不是从单一规范实验目录直接回溯 |
| `第 3 章` 标签链路验证 | `78` 条标签、`127.01 ms` 平均往返、`248 ms` P95 | `thesis/00_AI_Management/Output_Drafts/Chap03_Experiment03_Label_Response_Results_20260331.md`；`thesis/00_AI_Management/Output_Drafts/Chap03_Writing_Status_And_Data_Index_20260401.md`；`olrecord/nearalQTpro_logs/markers` | 中 | 有统计稿和 marker csv，但仍偏“分析结果先行、原始 run 后找” |
| `第 3 章` 无线稳定性/供电便携化 | 系统可短时稳定运行，但长时/功耗/移动量化不足 | `forexp/neurameter`；`nearalQTpro`；`olrecord`；`thesis/02_Source_Material/03_Hardware_Workbench` | 中 | 正文当前口径比较克制，和本地证据强度基本一致 |
| `第 4 章` 全通道 baseline、退化曲线、双导二分类重定义 | `22->8->3->2` 退化，`C3/C4 2-class` 恢复可用性 | `MI_Algorithm_Workbench/results_summaries/baseline_full_channel.csv`、`degradation_4class.csv`、`degradation_2class.csv`；`visualization/C4-7/C4-8` 对应图 | 强 | 这是当前全仓库里证据最完整、最适合论文主线的一段 |
| `第 4 章` 低通道优化路径与 KD | `lowchannel_v1/b1/b2` 未稳定超越 baseline，KD 有限正收益 | `MI_Algorithm_Workbench/results_summaries/lowchannel_*`、`kd_*`；`visualization/C4-9`；`conformer_kd_student.py` | 强 | 路径、汇总表、图都在；结论与本地总结稿一致 |
| `第 4 章` 多 seed / 外部数据集 / EEGNet / 通道组合 / 混淆矩阵 | 多随机种子、`2b`、`PhysioNet`、`EEGNet`、通道组合、混淆矩阵都支撑主线判断 | `multi_seed_*`、`physionet_*`、`eegnet_*`、`channel_combo_*`、`confusion_*`；对应 `Output_Drafts` 总结文档 | 强 | 这些补充实验与正文对应关系清楚，属于“能写且应写”的部分 |
| `第 4 章` EdgeMIFormer 架构与 RK3568/RK NPU 部署 | 已提出 EdgeMIFormer，完成量化/剪枝/31ms 部署验证 | `MI_Algorithm_Workbench/candidates/EdgeMIcformer.py`；`thesis/01_Thesis_LaTeX/C4-10_EdgeMIFormer_Arch.pdf`；`thesis/99_Archive/Raw_Web_Captures/paper_text.txt`；`MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Experiment_Results_Overall_Summary.md` 第 4.9 节 | 弱 | 当前本地主工作区自己写明“尚未形成同等级、可复核闭环”，但正文已经把它写成已完成主结果，这是本论文最明显的证据口径偏移 |
| `第 5 章` 伪在线策略比较 | `stage1` 下 `upper_refit` 类优于 `EA only`，但增益有限 | `MI_Algorithm_Workbench/online_simulation/stage1_*`；`Stage1_Total_Comparison_seed42.md/csv`；`visualization/stage1_total_comparison_seed42.png` | 强 | 图、表、目录和分析稿均完整，和正文匹配良好 |
| `第 5 章` round dependency 与 source weighting 稳定性边界 | round 效应大于方法效应，source weighting 更适合探索性方向 | `Stage1_Round_Dependency_Indicators_seed42.md/csv`；`Unified_Core_Seed_Stability_seed42_43_44_s1_5_9.md`；`online_simulation/unified_source_*` | 强 | 当前本地证据充分，正文表述也较谨慎 |
| `第 5 章` 真实在线 quick check 与顺序复盘 | `20260401_141355_mi_lr` quick check 有预训练增益；4 轮顺序复盘未稳定优于 baseline | `thesis/00_AI_Management/Output_Drafts/MI_Last_Session_Quickcheck_20260401.md`；`MI_Online_Sessions_Analysis_20260401.md`；`mi_online_sessions_analysis.py` | 中 | 分析稿在 git 内，但对应 `20260401_*` 原始 run 目录没有在 git 内检到，复现性依赖中间分析稿 |
| `第 5 章` 当前真实在线程序与归档 | 双导硬件、Qt 前端、bridge、runtime/marker/训练报告已经打通 | `nearalQTpro`；`olrecord/nearalQTpro_runtime`；`olrecord/nearalQTpro_logs`；`latest_training_report.json`；`latest_inference_report.json` | 中 | 程序与归档确实存在，但 git 内归档主要是 `2026-04-11`，而更新的 `2026-04-19` 多被试记录只见汇总稿、原始路径指向 git 外目录 |
| `第 5 章` 推理节点/系统时延/移动场景 | 模型侧部署已证，整链路时延和移动稳定性仍待补充 | `chap05.tex`；`Model_Complexity_Analysis_Summary.md`；`nearalQTpro`；`forexp`；`olrecord` | 中 | 正文已经承认这些边界，因此问题不是“写错”，而是标题仍略强于证据强度 |
| `第 6 章` 结论与展望 | 总结三条主线，承认在线和部署边界 | `thesis/01_Thesis_LaTeX/data/chap06.tex` | 中 | 结论总体与章节一致，但会继承第 4 章 `EdgeMIFormer/RK NPU` 证据口径问题 |

---

## 4. 当前论文的明确遗漏与叙述偏移

### 4.1 最大偏移：`EdgeMIFormer + RK3568/RK NPU` 被写得比本地主工作区证据更强

当前正文中的写法：

- `chap04.tex` 将 `EdgeMIFormer` 的结构、量化压缩到 `47.9%`、`RK NPU` 上约 `31 ms` 推理，写成了本章已成立结果。
- `abstract.tex` 和 `chap05.tex` 也沿用了这一口径。

但本地主工作区的内部总结明确写了相反判断：

- `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Experiment_Results_Overall_Summary.md`
- `thesis/02_Source_Material/04_Algorithm_Workbench/docs/Experiment_Results_Overall_Summary.md`

这两处都明确写到：

- `EdgeMIFormer` 只有候选脚本；
- 尚未形成与 baseline 同等级、同协议、可复核的完整结果闭环；
- 不能把它写成论文中的已完成结果。

判断：

- 如果当前论文的 `EdgeMIFormer` 与 `31 ms` 部署结果确实来自“前期已完成研究/已发表论文/独立归档成果”，那正文必须把证据来源说清楚，明确它不是 `MI_Algorithm_Workbench` 当前主实验链新跑出来的结果。
- 如果正文希望完全以当前本地主工作区为证据基础，那么这一段现在写得偏强。

### 4.2 第 4 章存在“前期成果”和“当前统一协议结果”混写风险

当前第 4 章内部实际上混了两类证据：

1. 当前 `MI_Algorithm_Workbench` 可直接复核的统一协议实验。
2. 更像前期研究或归档文稿的 `EdgeMIFormer + RK NPU` 部署结果。

风险不在于二者不能同时出现，而在于：

- 表格、图和结论口径现在看起来像一条连续的同源实验链；
- 但本地目录结构显示，这两部分的来源并不完全一致。

建议：

- 在 `第 4 章` 中显式分成“前期研究基础”和“本论文当前统一协议补充验证”两层；
- 或在表题/图注/段首直接交代“下述部署结果承接自前期工作”。

### 4.3 `第 5 章` 真实在线部分目前更依赖中间分析稿，而不是 git 内统一归档的原始 run

正文中真实在线 quick check 用到的关键证据主要来自：

- `MI_Last_Session_Quickcheck_20260401.md`
- `MI_Online_Sessions_Analysis_20260401.md`

问题在于：

- 这些分析稿在 git 内；
- 但对应的 `20260401_*` 原始 run 目录没有在 `/home/woqiu/下载/git` 下直接检到。

这意味着：

- 对论文作者自己来说，这些结论可能是真实可信的；
- 但从“本地 git 目录可追溯性”角度，它们现在更像“二级分析结论”，不是一条直接落到 raw run 目录的证据链。

### 4.4 `2026-04-19` 的三被试在线汇总尚未吸收到正文

本地已有更新材料：

- `NearalQTpro_Online_ThreeParticipant_Judgment_Log_20260419.md`
- `NearalQTpro_Online_Active_Inference_Summary_20260419.md`
- `Online_Experiment_Program_Version_Evolution_And_Asset_Organization_20260419.md`

这些材料说明：

- 真实在线实验程序已经从 `forexp/nearalQT` 进化到 `nearalQTpro`；
- 还有三位真实被试的在线判断汇总分析；
- 但正文 `第 5 章` 仍主要围绕 `2026-04-01` 那一批 quick check 口径展开。

判断：

- 这不算“写错”，但确实是“本地已有新材料尚未纳入”。
- 如果后续要增强 `第 5 章`，这些 `2026-04-19` 材料是现成可吸收的候选补充。

### 4.5 `thesis/02_Source_Material/04_Algorithm_Workbench` 只是快照，不是最新证据库

当前论文仓里已经复制了一份算法快照：

- `thesis/02_Source_Material/04_Algorithm_Workbench`

但它只包含：

- 早期 docs；
- 少量结果 csv；
- 少量 figures；
- 少量 scripts。

它不覆盖后续大量新增内容，例如：

- `multi_seed_*`
- `PhysioNet/2b` 全量补充验证
- `EEGNet` 最小经典对照
- `online_simulation` 里的 stage1 / source weighting / unified controls
- `2026-04-19` 在线实验整理文档

因此：

- 以后只看 `thesis/02_Source_Material/04_Algorithm_Workbench` 会漏掉很多新实验；
- 查实验时必须以 live 的 `MI_Algorithm_Workbench` 为准。

### 4.6 有一项值得补吸收的本地实验：训练数据比例敏感性

本地已经有：

- `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Data_Fraction_Sensitivity_Summary.md`
- `results_summaries/data_fraction_pilot_*`

这项实验能回答：

- 双导二分类在校准数据减少时会掉多少点；
- `75%` 数据是否已逼近 `100%`；
- 第 5 章和讨论部分里“校准成本”能不能更具体。

当前正文还没有明显吸收这条结果。  
它不是必须补，但如果希望把“可落地性”讲得更完整，这是优先级较高的可选补充。

---

## 5. 推荐的修订优先级

### 5.1 高优先级

1. 先处理 `EdgeMIFormer` 证据来源问题。
   - 要么把它明确标成“前期研究基础/归档成果”。
   - 要么把当前正文里过强的“已完成闭环验证”表述降级。

2. 统一 `第 5 章` 真实在线证据口径。
   - 明确正文到底以 `2026-04-01` quick check 为主，还是吸收 `2026-04-19` 三被试汇总。
   - 最好不要同时混用两套不同整理口径但不交代差异。

3. 固定实验定位规则。
   - 以后凡是找算法结果，先查 `MI_Algorithm_Workbench`，不要先查论文内嵌快照。

### 5.2 中优先级

1. 在 `第 5 章` 增补一句当前真实在线程序版本关系：
   - `forexp/nearalQT` 是第一代原型；
   - `nearalQTpro` 是当前主线；
   - `olrecord` 是归档证据库。

2. 视篇幅吸收 `Data_Fraction_Sensitivity_Summary.md`，用于支撑“校准成本不是必须全量”的讨论。

3. 如果要增强在线章节但又不想重跑实验，可把 `2026-04-19` 三被试在线汇总降格放入“补充证据/附录式讨论”。

### 5.3 低优先级

1. 清理 `thesis/02_Source_Material/04_Algorithm_Workbench` 的说明文字，显式标出“这是快照，不是最新工作区”。
2. 为 `online_simulation` 里重要实验族补更明确的 `README.md` 或 `RUN_NOTE.md`，降低后续定位成本。

---

## 6. 一句话版本

如果只保留一句结论，可以这样概括：

> 当前论文中最稳、最完整的证据链是“低通道离线主线 + 伪在线 stage1”；最需要警惕的不是 baseline 本身，而是 `EdgeMIFormer/RK NPU` 结果在正文里的证据强度已经超过了本地主工作区当前可直接复核的程度，而真实在线部分则存在“分析稿多、统一归档原始 run 少、且有新材料尚未吸收”的问题。
