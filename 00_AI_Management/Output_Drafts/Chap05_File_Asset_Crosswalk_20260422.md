# 第 5 章写作文件资产对照表

更新时间：`2026-04-22`

## 1. 用途与总判断

本文档用于给论文第 5 章写作建立“文件资产到小节”的对照表。阅读范围以当前本地工作区为准，重点覆盖：

- `MI_Algorithm_Workbench`
- `nearalQTpro`
- `olrecord`
- `forexp`
- `thesis`
- `/home/woqiu/文档/nearalQTpro/runtime`
- `在线实验记录`

当前第 5 章最稳的定位不是“完整在线性能已经验证完毕”，而是：

> 公开数据集伪在线冷启动实验提供主要方法证据；真实双导在线实验提供系统联动、训练交互和小规模实测记录；二者共同支撑“从离线低通道主线走向在线原型验证”的章节，但不宜混写成同一类在线结果。

进一步地，第 5 章整体写作应固定为：

> 以工程系统验证为主，以在线方法验证为辅。也就是说，伪在线部分首先用于初步确定可保留的方法路径，真实在线部分则重点说明这些方法已经进入在线训练与反馈机制，并在真实运行记录中表现出初步可用性。

与第 4 章的边界关系应写清楚：

> 第 4 章已经完成模型侧端侧部署基础的验证，第 5 章不再重复展开部署流程本身，而是将 RK3568 / RKNN 仅作为后续系统级闭环迁移目标放在 `5.3` 讨论。

建议第 5 章标题从当前的“系统集成、在线实现与初步验证”进一步收束为：

- 推荐章名：`低通道运动想象脑电解码系统的在线实验与初步验证`
- 备选章名：`低通道运动想象脑电解码系统的在线化实现与初步验证`

建议小节结构：

| 建议小节 | 原暂拟小节 | 写作定位 |
| --- | --- | --- |
| `5.1 公开数据集伪在线冷启动实验` | `5.1 伪在线实验` | 论文第 5 章的主证据层，使用 BCI IV 2b chronological replay |
| `5.1.1 实验设置与评价框架` | `5.1.1 实验设置和评价框架` | 交代 LOSO、时间顺序 replay、每轮更新、AULC/TTT/instability 等指标 |
| `5.1.2 轮次依赖现象与源数据质量调制` | `5.1.2 轮次依赖现象和数据降权方法` | 先写 round/trial dependency，再写 source weighting 的边界 |
| `5.1.3 在线更新策略与模型结构对照` | `5.1.3 在线网络结构优化` | 写 `upper_refit_no_ea`、source 条件、EEGNet/CSP/MDM/RawPatch 等对照 |
| `5.2 真实双导在线实验与训练交互闭环` | `5.2 在线实验` | 写 Qt 程序、训练桥接、真实被试 session、active inference 结果 |
| `5.2.1 在线实验平台与训练交互方法` | `在线实验设计和训练交互方法` | 代码、程序版本、runtime、run 目录结构、train-round/infer-trial |
| `5.2.2 在线实验结果与误差分析` | `在线实验结果分析` | 三参与者记录、session 修正、置信度、左右错误偏置 |
| `5.3 本章小结与证据边界` | `5.3 本章小节` | 明确哪些结论稳、哪些只是初步验证或后续工作 |

写作约束补充：

- `RK3568 / RKNN` 相关内容主要放在 `5.3` 作为边界与后续工作，不建议在 `5.2` 主线中展开，以免将当前尚未完成的端侧闭环验证与已经完成的真实在线记录混写。
- “用户适应 / 被试策略调整”当前只弱写，不建议作为 `5.2` 的独立主线。

## 2. 章节总入口资产

| 资产 | 类型 | 用途 | 使用建议 |
| --- | --- | --- | --- |
| `thesis/01_Thesis_LaTeX/data/chap05.tex` | 当前正文 | 现有第 5 章文本主入口 | 修改正文前先对照本文件，不要直接把伪在线和真实在线混写 |
| `thesis/00_AI_Management/Output_Drafts/Chap05_Before_Closure_20260415.tex` | 旧正文备份 | 回看 2026-04-15 前的第 5 章状态 | 只作历史参考 |
| `thesis/00_AI_Management/Output_Drafts/Thesis_Chapter_Experiment_Crosswalk_20260420.md` | 总体资产对照 | 已指出第 5 章伪在线强、真实在线中等、2026-04-19 新材料尚未吸收 | 本文件是在它基础上专门细化第 5 章 |
| `thesis/00_AI_Management/Output_Drafts/MIEXP_Quick_Locator_20260414.md` | 快速定位表 | 一页式实验入口 | 查找方向时先看，写作时看本文件 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/MI_Experiment_Asset_Index_20260414.md` | 实验资产总账 | `MI_Algorithm_Workbench`、`nearalQTpro`、`olrecord` 的总入口 | 作为路径索引，不直接替代正文证据 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Thesis_Status_MI_Experiment_Online_Integration_Analysis_20260414.md` | 阶段总判断 | 解释第 5 章为什么应写成“系统集成与初步验证” | 写小结和边界时优先引用其判断 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/MI_Round_Dependency_and_Source_Filtering_Experiment_Map.md` | 伪在线主台账 | 第 5 章伪在线部分最重要的解释层入口 | `5.1.2` 和 `5.1.3` 的核心依据 |

## 3. `5.1.1 实验设置与评价框架`

写作目标：说明伪在线实验不是普通离线随机切分，而是用公开数据集按时间顺序模拟在线冷启动；目标被试与源训练被试互斥；当前轮结果不使用未来标签；主指标应从单一平均准确率扩展到早期面积、达到阈值时间和不稳定性。

| 资产 | 类型 | 对应内容 | 写作优先级 |
| --- | --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/BCI2B_3Subject_NoEA_Online_Baseline_Sweep_Analysis.md` | 分析稿 | BCI IV 2b、C3/C4、S1/S5/S9、每轮 10 trials、最多 69 轮；`scratch / pretrained_full / pretrained_frozen_head` no-EA baseline | 高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/BCI2B_Sub9_LOSO_Online_Adaptation_Walkthrough_Revised.md` | 早期单被试复盘 | Sub9 chronological few-shot simulation 的边界、raw 与平滑曲线差异 | 中；可作为方法演化背景 |
| `MI_Algorithm_Workbench/online_simulation/pretrain_loso_2b_generic.py` | 脚本 | LOSO 预训练入口 | 高；写可复现路径 |
| `MI_Algorithm_Workbench/online_simulation/simulate_fewshot_2b_generic.py` | 脚本 | 早期 few-shot chronological replay | 中；历史入口 |
| `MI_Algorithm_Workbench/online_simulation/simulate_stage1_2b_matrix.py` | 脚本 | stage1 策略矩阵仿真主入口 | 高 |
| `MI_Algorithm_Workbench/online_simulation/run_stage1_source_weight_bridge.py` | 脚本 | source condition 与 stage1 update 的桥接实验 | 高 |
| `MI_Algorithm_Workbench/online_simulation/overnight_runs/no_ea_subject_sweep_20260408_v2/` | 结果目录 | 三代表被试 no-EA baseline sweep，含 `manifest.csv`、`sub*_summary.csv`、`sub*_rounds.csv`、曲线图 | 中；用于交代实验由来 |
| `MI_Algorithm_Workbench/00_AI_Management/Input_Buffer/MI_EEG_cold_start_evaluation_protocol_core_papers/Core_Papers_Key_Summaries.md` | 文献梳理 | 支撑 pseudo-online、AULC10/AULC20、防泄漏、时间顺序 replay | 高；适合写方法合理性 |
| `MI_Algorithm_Workbench/00_AI_Management/Input_Buffer/MI_EEG_parameter_adaptation_core_papers/Core_Papers_Key_Summaries.md` | 文献梳理 | 支撑 upper-block refit、保守个体化、轻量参数适配 | 中高 |

可直接写入的指标口径：

- 主指标：`AULC10`、`AULC20`
- 重要辅指标：`MeanAcc@5/10`、`MeanAcc@20`、`Instability@6:20`
- 降级辅指标：`TTT@0.8`、`TailAcc`
- 结果解释必须说明：每轮测试窗口较小，raw 逐轮曲线天然会有较强离散波动。

## 4. `5.1.2 轮次依赖现象与源数据质量调制`

写作目标：先确立“round/trial batch 难度本身是强混杂因素”，再介绍 source trial 降权/保护/随机对照等方法尝试。结论要克制：源数据质量调制有潜力，但不是“删掉坏 trial 后必然提升性能”。

| 资产 | 类型 | 对应内容 | 写作优先级 |
| --- | --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Round_Dependency_Indicators_seed42.md` | 指标说明 | S1/S5/S9 跨 7 策略逐轮相关、round effect eta2、strategy effect eta2 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Round_Dependency_Indicators_seed42.csv` | 指标表 | 轮次依赖量化数据 | 最高 |
| `MI_Algorithm_Workbench/visualization/stage1_round_dependency_seed42.png` | 图 | 当前正文 `C5-2` 来源 | 最高 |
| `thesis/01_Thesis_LaTeX/figures/C5-2_stage1_round_dependency_seed42.png` | 论文图 | 已进入论文目录的第 5 章图 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/MI_Round_Dependency_and_Source_Filtering_Experiment_Map.md` | 主台账 | round dependency、classic weighting、protected keep1、unified controls、random repeats、full70 bridge 的总说明 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Weighted_LOSO_AllSubjects_Summary_seed42.md` | 旧 pilot 总结 | 9 被试 source soft weighting / hard filtering 早期证据 | 中；必须说明旧协议训练轮数偏少 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/ConformerB2_DownweightFrac_Sweep_seed42.md` | sweep 总结 | 降权比例 `0.1/0.2/0.3` 的早期探索 | 低到中；适合作为补充 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Unified_Source_Quality_Controls_seed42_s1_5_9.md` | 统一协议报告 | seed42、S1/S5/S9、15 epoch、`unweighted/classic/random/pattern/loss_drop` | 高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Unified_Core_Seed_Stability_seed42_43_44_s1_5_9.md` | 多 seed 核心报告 | seed42/43/44 × S1/S5/S9，四核心变体稳定性 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Random_Repeats_Regularization_Controls_seed42_43_44_s1_5_9.md` | random repeat 报告 | 90 次 random repeat + weight decay + label smoothing，排除单次随机好运 | 高 |
| `MI_Algorithm_Workbench/online_simulation/unified_source_quality_core_seed42_43_44_s1_s5_s9/` | 结果目录 | accuracy、delta、transition、HCE 等 CSV | 高 |
| `MI_Algorithm_Workbench/online_simulation/random_repeats_regularization_controls_seed42_43_44_s1_s5_s9/` | 结果目录 | random repeat 分布和逐 trial 明细 | 高 |
| `MI_Algorithm_Workbench/visualization/unified_core_seed_stability_seed42_43_44_s1_5_9.png` | 图 | 当前正文 `C5-3` 来源 | 最高 |
| `thesis/01_Thesis_LaTeX/figures/C5-3_unified_core_seed_stability.png` | 论文图 | 已进入论文目录的第 5 章图 | 最高 |

当前较稳结论：

- `stage1` 中 round/trial batch 依赖强，S1/S5/S9 上 round effect 明显大于 strategy effect。
- hard filtering 风险大，容易误伤本来可判对的 trial。
- classic probe weighting 没有稳定优于 unweighted，也没有稳定优于 random repeat 分布。
- `loss_drop_protected` 比 classic weighting 更安全，但总体仍接近中性。
- 质量降权可以写成一种有效的源端优化策略，但不要写成所有指标上的通用稳定提升方法。

新补强资产：

| 资产 | 状态 | 使用建议 |
| --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Source_Bridge_Full70_Controls_seed42_43_44_all_subjects.md` | 当前 git 中显示为未跟踪文件 | 已扩到 S1-S9、3 seeds、27 pairs，可作为强补充；纳入正文前建议先确认文件已归档或提交 |
| `MI_Algorithm_Workbench/online_simulation/stage1_source_weight_bridge_full70/stage1_source_bridge_full70_combined_summary_seed42_43_44_all_subjects.csv` | 未跟踪结果表 | 显示 `weighted_source + upper_refit_no_ea` 在 27 pairs 上 mean raw、AULC10/AULC20、instability 有小幅优势 |
| `MI_Algorithm_Workbench/visualization/stage1_source_bridge_full70_controls_seed42_43_44_all_subjects.png` | 未跟踪图 | 可作为 `C5-3` 或补充图候选，但正文采用前需统一图号和口径 |

## 5. `5.1.3 在线更新策略与模型结构对照`

写作目标：把“在线网络结构优化”改写为更准确的“在线更新策略与模型结构对照”。这里不宜只写网络结构本身，因为最有证据的变量是 source 条件、upper-block refit、no-update、EA、以及 backbone 对照的交互。

| 资产 | 类型 | 对应内容 | 写作优先级 |
| --- | --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Total_Comparison_seed42.md` | stage1 总表 | seed42、S1/S5/S9，Conformer stage1 策略比较 | 高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Complete_Strategy_Comparison_with_EEGNet_seed42.md` | stage1 + EEGNet | 加入 `eegnet_pretrained_no_update` 背景基线 | 高 |
| `MI_Algorithm_Workbench/visualization/stage1_total_comparison_seed42.png` | 图 | 当前正文 `C5-1` 来源 | 最高 |
| `thesis/01_Thesis_LaTeX/figures/C5-1_stage1_total_comparison_seed42.png` | 论文图 | 已进入论文目录的第 5 章图 | 最高 |
| `MI_Algorithm_Workbench/visualization/stage1_complete_strategy_comparison_with_eegnet_seed42.png` | 图 | 含 EEGNet 的补充图 | 中；如正文篇幅有限可不放 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Source_Bridge_Early20_Controls_seed42_43_44_s1_5_9.md` | early20 报告 | source condition × `upper_refit/no_update` 冷启动早段结果 | 高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Stage1_Source_Bridge_Full70_Controls_seed42_43_44_s1_5_9.md` | full70 报告 | `upper_refit_no_ea` 下 source 条件的 70 轮验证 | 高 |
| `MI_Algorithm_Workbench/visualization/stage1_source_bridge_full70_controls_seed42_43_44_s1_5_9.png` | 图 | full70 三被试图 | 高 |
| `MI_Algorithm_Workbench/online_simulation/eegnet_stage1_seed42/` | 结果目录 | EEGNet no-update stage1 | 中高 |
| `MI_Algorithm_Workbench/online_simulation/csp_lda_stage1_seed42/` | 结果目录 | CSP+LDA stage1 对照 | 中 |
| `MI_Algorithm_Workbench/online_simulation/mdm_stage1_seed42/` | 结果目录 | MDM stage1 对照 | 中 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/EEGNet_vs_Conformer_NoUpdate_Round_Alignment_seed42.md` | 对齐分析 | EEGNet 与 Conformer no-update 逐轮低谷一致性 | 中 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Attention_Backbone_Filter_Compare_S1_S5_S9_seed42.md` | backbone/过滤对比 | EEGNet、ConformerB2、RawPatch Transformer 在 filtered/weighted 下的差异 | 中 |
| `MI_Algorithm_Workbench/visualization/attention_backbone_filter_compare_s1_s5_s9_seed42.png` | 图 | backbone filter compare 图 | 中；适合补充图或附录 |
| `MI_Algorithm_Workbench/online_simulation/simulate_stage1_2b_eegnet_no_update.py` | 脚本 | EEGNet stage1 no-update | 中 |
| `MI_Algorithm_Workbench/online_simulation/simulate_stage1_2b_csp_lda_no_update.py` | 脚本 | CSP+LDA stage1 no-update | 中 |
| `MI_Algorithm_Workbench/online_simulation/simulate_stage1_2b_mdm_no_update.py` | 脚本 | MDM stage1 no-update | 中 |

当前较稳结论：

- `pretrained_upper_refit_no_ea` 比单独 online EA 更有希望，是当前 Conformer stage1 中较稳的在线更新分支。
- EEGNet no-update 作为背景基线并不弱，因此不能把所有提升简单归因于 Conformer backbone。
- `weighted_source + upper_refit_no_ea` 在 full70 中保留了早期 AULC 和 instability 方面的小幅优势，但不应写成全面提升。
- RawPatch/attention backbone 对 source weighting 可能更敏感，但当前还缺足够统一的 random control，不宜作为主结论。

## 6. `5.2.1 在线实验平台与训练交互方法`

写作目标：说明真实在线实验的工程闭环已经打通。这里应写“程序版本、run 组织、每轮训练、逐 trial 推理、模型缓存与元数据”，而不是重复第 3 章硬件电路。

| 资产 | 类型 | 对应内容 | 写作优先级 |
| --- | --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Online_Experiment_Program_Version_Evolution_And_Asset_Organization_20260419.md` | 版本说明 | `forexp/nearalQT` 第一代、`nearalQTpro` 第二代主线、`olrecord` 归档快照 | 最高 |
| `nearalQTpro/README.md` | 程序说明 | Qt 上位机基础能力、采样率、显示、BLE、频谱 | 中 |
| `nearalQTpro/Main.qml` | 前端源码 | MI 控制界面、subject/session/run 上下文、source 条件和 strategy 下拉框 | 高 |
| `nearalQTpro/eegdataprocessor.cpp` | C++ 主逻辑 | run 目录创建、`mi_summary.csv`、`mi_raw_eeg.csv`、`mi_predictions.csv`、`mi_session.json` 写入；`train-round` 与 `infer-trial` 启动 | 最高 |
| `nearalQTpro/eegdataprocessor.h` | 头文件 | 默认 `unweighted_source / pretrained_upper_refit_no_ea` 配置 | 高 |
| `nearalQTpro/mi_pipeline/README.md` | pipeline 说明 | bridge、模型、bootstrap、runtime 目录和环境变量 | 高 |
| `nearalQTpro/mi_pipeline/scripts/online_mi_round_bridge.py` | Python bridge | 支持 `train-round`、`infer-trial`、`unweighted_source`、`weighted_source`、`scratch_source`、`pretrained_no_update`、`pretrained_upper_refit_no_ea` | 最高 |
| `nearalQTpro/mi_pipeline/scripts/scratch_replay_proto_core.py` | online arm | `scratch_replay_proto` 的 replay + prototype 分支 | 中高；用于 2026-04-19 scratch runs |
| `nearalQTpro/mi_pipeline/scripts/conformer_lowchannel_b2_diff.py` | 模型定义 | 在线 bridge 使用的低通道 ConformerB2 | 高 |
| `nearalQTpro/mi_pipeline/bootstrap/weights/` | 预训练权重 | `conformer_b2_c3c4_pretrain_2b.pt`、`conformer_b2_c3c4_pretrain_2b_weighted_source.pt` | 高 |
| `nearalQTpro/mi_pipeline/docs/mi_subject_guide.svg` | 被试说明图 | 在线实验流程说明素材 | 中 |
| `/home/woqiu/文档/nearalQTpro/runtime/records` | live runtime | 当前真实在线 run 原始记录根目录 | 最高；但不在 git 仓内 |
| `/home/woqiu/文档/nearalQTpro/runtime/models` | live runtime | active 模型与 per-arm checkpoint | 高 |
| `/home/woqiu/文档/nearalQTpro/runtime/reports` | live runtime | 最新训练/推理报告 | 高 |
| `olrecord/nearalQTpro_src/` | 归档源码 | `nearalQTpro` 某时点源码快照 | 高；归档证据 |
| `olrecord/nearalQTpro_runtime/` | 归档 runtime | 2026-04-11 左右在线运行记录、模型、报告 | 高；归档证据 |
| `forexp/nearalQT/` | 第一代原型 | 最早在线闭环程序 | 低到中；只作版本演化背景 |
| `forexp/neurameter/` | 固件工程 | 第 3 章和第 5 章基础链路背景 | 中；不要在第 5 章重复展开 |

run 目录中论文应关注的四类文件：

- `mi_session.json`：session/run 元数据、状态、停止原因、配置。
- `mi_summary.csv`：trial 级 cue、阶段时间、marker。
- `mi_raw_eeg.csv`：原始双通道 EEG 与 phase 标注。
- `mi_predictions.csv`：逐 trial 在线推理结果、active 标记、置信度。

## 7. `5.2.2 在线实验结果与误差分析`

写作目标：把真实在线结果写成“初步真实运行证据”，重点是 session 完整性、active prediction 数量、三参与者趋势、错误方向偏置、置信度校准问题。不要把这些小样本结果写成最终应用精度。

| 资产 | 类型 | 对应内容 | 写作优先级 |
| --- | --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_Raw_Session_Record_Table_20260419.md` | 原始 session 索引 | 记录 subject/session/run、配置、完成数、active 结果、备注 | 高；作为原始台账 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_Active_Inference_Summary_20260419.md` | subject 级汇总 | subject 级 active trials、accuracy、balanced accuracy、conf、Brier、NLL、MCC | 高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_Active_Inference_Subject_Table_20260419.csv` | subject 表 | 上述统计的 CSV | 高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_ThreeParticipant_Judgment_Log_20260419.md` | 三参与者整理 | `Participant_1/2/3` 映射与 session 索引 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_ThreeParticipant_Judgment_Log_20260419.csv` | trial 明细 | 三参与者逐判断日志 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_ThreeParticipant_Session_Index_20260419.csv` | session 索引 | 三参与者精选 session 指标 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260419.csv` | 精选 run 指标 | 可直接绘制准确率/置信度/错误方向图 | 最高 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260422.csv` | 补充精选 run 指标 | 含第三位真实参与者后续两次完整补充会话，分别为 15/20 与 16/20 | 最高；用于加固“0.85 不是孤立尖峰”的边界内表述 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/NearalQTpro_Subject009_Session007_Review_And_Plots_20260419.md` | 修正说明 | `subject_009/session_007/run_20260419_130542` 从旧值修正为 `20/13/0.65` | 最高；优先级高于旧 raw 表 |
| `MI_Algorithm_Workbench/visualization/nearalqtpro_threeparticipant_selected_runs_accuracy_confidence_20260419.png` | 图 | 三参与者精选 run 的准确率与置信度趋势 | 高；可作为新增 C5 图候选 |
| `MI_Algorithm_Workbench/visualization/nearalqtpro_threeparticipant_selected_runs_accuracy_confidence_20260422.png` | 图 | 三参与者精选 run 的准确率与置信度趋势，含第三位真实参与者补充运行 | 高；可作为新增 C5 图候选 |
| `MI_Algorithm_Workbench/visualization/nearalqtpro_threeparticipant_selected_runs_error_direction_20260419.png` | 图 | 左右方向错误统计 | 高；可作为新增 C5 图候选 |
| `MI_Algorithm_Workbench/visualization/nearalqtpro_subject009_session007_trial_review_20260419.png` | 图 | subject009 session007 trial 级复核图 | 中高；适合补充图 |
| `/home/woqiu/文档/nearalQTpro/runtime/records/subject_001` | live raw | Participant_1 的部分 run | 高；不在 git 内 |
| `/home/woqiu/文档/nearalQTpro/runtime/records/subject_002` | live raw | Participant_1 的部分 run | 高；不在 git 内 |
| `/home/woqiu/文档/nearalQTpro/runtime/records/subject_006` | live raw | Participant_1 的部分 run | 高；不在 git 内 |
| `/home/woqiu/文档/nearalQTpro/runtime/records/subject_009` | live raw | Participant_2 的 run | 最高；含 session007 修正 |
| `/home/woqiu/文档/nearalQTpro/runtime/records/subject_010` | live raw | Participant_3 的 run | 最高 |

重要口径提醒：

- `NearalQTpro_Online_Raw_Session_Record_Table_20260419.md` 中 `subject_009/session_007` 曾有旧值；正式写作优先采用 `NearalQTpro_Subject009_Session007_Review_And_Plots_20260419.md`、`NearalQTpro_Online_ThreeParticipant_Session_Index_20260419.csv` 和 `NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260419.csv` 中的修正值。
- `Participant_1 = subject_001 + subject_002 + subject_006`，不是单一 subject。
- `Participant_2 = subject_009`，有中断前后/约 1h 后继续的观察。
- `Participant_3 = subject_010`，`session_003` 后动作想象策略改变，后段结果更好。
- 真实在线结果当前应写为“小规模初步验证”，不要和 BCI IV 2b 的伪在线指标做同口径横向比较。
- 上述 `Participant_*`、`subject_*`、`session_*`、`run_*` 仅用于资产定位和原始记录追溯，不建议未经解释直接进入论文正文；正文应改写为“第一位真实参与者”“某次修正后的完整会话”等自然语言表述。

可写入的核心观察：

- 当前真实在线记录已经包含三位真实参与者、多个 session、active inference 结果。
- 第二位真实参与者存在一次修正后的完整会话达到 `0.65`。
- 第三位真实参与者存在完整会话达到 `15/20 = 0.75` 和 `17/20 = 0.85`，后续补充实验又达到 `15/20 = 0.75` 与 `16/20 = 0.80`。
- 第一位真实参与者当前归档完整会话整体仍偏低，但存在一次短时运行达到 `0.75`。
- 因此，真实在线部分可以支撑“部分参与者、部分会话已接近或进入可用区间”的判断，但当前仍应避免写成整体稳定性能结论。
- `subject_001/002/006` 存在明显左右方向误差偏置，部分 run 高置信但错误。
- `subject_009` 有中断/恢复和 session 级波动，适合写系统真实性与状态漂移，而不是写稳定高精度。

## 8. `5.3 本章小结与证据边界`

写作目标：把伪在线和真实在线证据各自收束，明确当前系统已经打通的环节和不能过度声称的地方。

应写入的小结要点：

1. 伪在线层面已经建立较完整证据链：LOSO source pretraining、chronological replay、stage1 更新、round dependency、source condition 和更新策略对照。
2. `upper_refit_no_ea` 是当前比单独 online EA 更值得保留的更新策略。
3. round/trial batch 难度是强混杂因素，解释力可超过方法主效应，因此平均准确率不能单独作为在线策略判断依据。
4. source weighting 在 `weighted_source + upper_refit_no_ea` 下有冷启动前段潜力，但不是通用稳定提升方法。
5. 真实在线层面，`nearalQTpro` 已经形成 subject/session/run 管理、轮次训练、逐 trial 推理和结果落盘闭环。
6. 三参与者在线记录能证明系统可运行、可记录、可分析，但样本量和会话一致性还不足以支撑强性能结论。

不宜写成强结论的内容：

- “真实在线 MI 分类准确率已经稳定达到某个应用级水平。”
- “传统 probe 能可靠识别坏 trial，降权后必然提升深度模型。”
- “随机降权稳定优于 unweighted。”
- “full70 tail accuracy 已经等价于真实在线长期使用效果。”
- “`nearalQTpro` 已完成最终端侧 RK3568/RKNN 全闭环验证。”

## 9. 不在拟定小节内但应记录的相关资产

| 资产 | 关系 | 处理建议 |
| --- | --- | --- |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Data_Fraction_Sensitivity_Summary.md` | 校准数据量敏感性，能支撑第 5 章“校准成本”讨论 | 可放 `5.3` 或讨论段；不是伪在线主线 |
| `MI_Algorithm_Workbench/results_summaries/data_fraction_pilot_raw_latest.csv` | 数据比例原始表 | 可作为补充表 |
| `MI_Algorithm_Workbench/results_summaries/data_fraction_pilot_summary_latest.csv` | 数据比例汇总表 | 可作为补充表 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/Online_MI_EEG_Parameter_Adaptation_Memo_Codex_Reading.md` | 参数适配文献 memo | 支撑 `upper_refit_no_ea` 与保守个体化的讨论 |
| `MI_Algorithm_Workbench/00_AI_Management/Output_Drafts/MI_BCI_Local_Temporal_Variability_Original_Papers_Review.md` | 局部时间变异性文献复核 | 支撑 round dependency 现象的理论背景 |
| `在线实验记录/alpha实验/` | 旧 alpha 图和 marker | 更适合第 3 章；第 5 章可用一句话说明基础链路前提 |
| `olrecord/legacy_online_records/alpha实验/` | alpha 归档 | 同上 |
| `olrecord/nearalQTpro_logs/markers/` | marker 归档 | 支撑事件标签链路；不要替代 MI active inference 结果 |
| `olrecord/paper_support/` | 论文支撑文档归档 | 与 `MI_Algorithm_Workbench/Output_Drafts` 内容部分重复，优先用 live workbench，归档用于追溯 |
| `thesis/02_Source_Material/04_Algorithm_Workbench/` | 论文仓内嵌算法快照 | 不是最新账本；只作历史快照 |

## 10. 资产使用优先级

| 等级 | 可进入正文主线 | 代表资产 |
| --- | --- | --- |
| A | 是 | `Stage1_Round_Dependency_Indicators_seed42.*`、`Stage1_Total_Comparison_seed42.*`、`Stage1_Source_Bridge_Full70_Controls_seed42_43_44_s1_5_9.md`、`Unified_Core_Seed_Stability_seed42_43_44_s1_5_9.md`、`nearalQTpro` bridge 与 runtime 结构 |
| B | 可进入正文或补充说明 | `BCI2B_3Subject_NoEA_Online_Baseline_Sweep_Analysis.md`、`EEGNet_vs_Conformer_NoUpdate_Round_Alignment_seed42.md`、`Attention_Backbone_Filter_Compare_S1_S5_S9_seed42.md`、三参与者在线汇总 |
| C | 只作历史/探索/附录 | 旧 4 epoch `pilot_weighted_loso_*`、`ConformerB2_DownweightFrac_Sweep_seed42.md`、`forexp/nearalQT`、`在线实验记录/alpha实验` |
| D | 暂不建议正文使用 | `_smoke_*`、`_cuda_debug_*`、意外嵌套 `online_simulation/MI_Algorithm_Workbench/`、未确认归档的半成品目录 |

## 11. 写作时的最短取材顺序

如果后续只想快速写第 5 章，建议按这个顺序取材：

1. 先读 `thesis/01_Thesis_LaTeX/data/chap05.tex`，确认现有正文已经写了什么。
2. 写 `5.1.1` 时看 `BCI2B_3Subject_NoEA_Online_Baseline_Sweep_Analysis.md` 与 cold-start protocol 文献摘要。
3. 写 `5.1.2` 时看 `MI_Round_Dependency_and_Source_Filtering_Experiment_Map.md`、`Stage1_Round_Dependency_Indicators_seed42.md`、`Unified_Core_Seed_Stability_seed42_43_44_s1_5_9.md`。
4. 写 `5.1.3` 时看 `Stage1_Complete_Strategy_Comparison_with_EEGNet_seed42.md` 和 `Stage1_Source_Bridge_Full70_Controls_seed42_43_44_s1_5_9.md`。
5. 写 `5.2.1` 时看 `Online_Experiment_Program_Version_Evolution_And_Asset_Organization_20260419.md`、`nearalQTpro/eegdataprocessor.cpp`、`nearalQTpro/mi_pipeline/scripts/online_mi_round_bridge.py`。
6. 写 `5.2.2` 时看三参与者在线汇总、修正后的 session index、selected run metrics 和三张 nearalQTpro 图。
7. 写 `5.3` 时回到本文件第 8 节的边界表述，避免过度结论。
