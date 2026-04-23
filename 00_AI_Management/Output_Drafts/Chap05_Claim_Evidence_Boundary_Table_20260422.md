# 第 5 章主张-证据-边界表（2026-04-22）

## 1. 用途

本文档用于将第 5 章的正文判断固定为“主张 - 证据 - 边界”三联结构。其作用不是重复资产索引，而是回答以下问题：

1. 每一节到底要下什么判断。
2. 这个判断由哪些文件和哪些数字支撑。
3. 这个判断允许写到什么强度，不能越过哪条边界。

使用规则：

- 没有进入本表的判断，先不写进正文。
- 正文中的每一个强结论，都必须能回溯到本表中的一行。
- 若后续补充新实验，先增补本表，再修改正文。

---

## 2. 章级总主张

### 2.1 本章总主张

`本文已经在低通道运动想象脑电解码系统中建立了从伪在线冷启动评估到真实在线训练-反馈联动机制的初步证据链。`

### 2.2 章级总证据

- 伪在线：`BCI2B_3Subject_NoEA_Online_Baseline_Sweep_Analysis.md`
- 伪在线：`Stage1_Total_Comparison_seed42.md`
- 伪在线：`Stage1_Round_Dependency_Indicators_seed42.md/csv`
- 伪在线：`Unified_Core_Seed_Stability_seed42_43_44_s1_5_9.md`
- 真实在线：`Online_Experiment_Program_Version_Evolution_And_Asset_Organization_20260419.md`
- 真实在线：`NearalQTpro_Online_Active_Inference_Summary_20260419.md`
- 真实在线：`NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260419.csv`
- 真实在线补充：`NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260422.csv`

### 2.3 章级总边界

- 不能写成“真实在线系统已经稳定达到应用级性能”。
- 不能写成“完整端侧闭环部署已经完成”。
- 不能写成“所有在线方法优劣已经被最终确定”。

---

## 3. `5.1 公开数据集伪在线冷启动实验`

### 3.1 `5.1.1 实验设置与评价框架`

| 项目 | 内容 |
| --- | --- |
| 主张 | 伪在线实验采用严格 LOSO 与时间顺序 replay，用于模拟低通道冷启动，而不是普通离线随机切分。 |
| 直接证据 | `BCI2B_3Subject_NoEA_Online_Baseline_Sweep_Analysis.md`；`pretrain_loso_2b_generic.py`；`simulate_stage1_2b_matrix.py` |
| 关键数字 | `S1/S5/S9`；每轮 `10 trials`；最多 `69 轮`；`pretrained_full` 三被试平均 `mean raw acc = 0.7633`，高于 `scratch = 0.7425`；`early10 = 0.6800`，高于 `0.5667` |
| 正文允许写法 | `结果表明公开数据集预训练能够为双导冷启动提供有限但可重复的早段帮助。` |
| 正文禁止写法 | `预训练已经充分解决低通道冷启动问题。` |
| 必须补的解释 | 为什么第 5 章用 `AULC10/AULC20/Instability` 而不只用平均准确率。 |
| 必须写的边界 | 伪在线不是完整真实在线，只是为真实在线方法选择提供中间层证据。 |

### 3.2 `5.1.2 在线批次依赖现象与预训练数据质量调制`

| 项目 | 内容 |
| --- | --- |
| 主张 | 在线批次依赖是解释伪在线结果时必须显式控制的强混杂因素；在此基础上，质量降权确实改善了若干关键在线指标，其收益主要集中在前段和稳定性指标；这一现象也提示真实在线实验应尽早建立批次级表现反馈与数据质量监测机制。 |
| 直接证据 | `Stage1_Round_Dependency_Indicators_seed42.md/csv`；`MI_Round_Dependency_and_Source_Filtering_Experiment_Map.md`；`Unified_Core_Seed_Stability_seed42_43_44_s1_5_9.md`；`Random_Repeats_Regularization_Controls_seed42_43_44_s1_5_9.md` |
| 关键数字 | `S1/S5/S9` 上逐轮相关 `0.7404 / 0.7017 / 0.8122`；`round effect eta^2 = 0.7740 / 0.7145 / 0.8344`；`strategy effect eta^2 = 0.0036 / 0.0355 / 0.0013`；`random_weighted` 在 `9` 组配对中 `8 胜 1 负`，平均 `+1.01 pct`；`classic_weighted` 平均 `-1.53 pct` |
| 正文允许写法 | `结果表明在线批次依赖的解释力显著高于策略主效应。` |
| 正文禁止写法 | `删掉坏 trial 之后性能必然提升。` |
| 必须补的解释 | 为什么单次 `random_weighted` 的正结果不能直接解释为规律。 |
| 必须写的边界 | 质量降权的收益主要集中在前段准确率、累计面积和中前段稳定性，不宜扩大成“所有指标都稳定占优”；批次级表现反馈与数据质量监测属于后续真实在线实验设计启示，不等于当前已经完成在线质量控制闭环。 |

### 3.3 `5.1.3 在线更新策略与模型结构对照`

| 项目 | 内容 |
| --- | --- |
| 主张 | `upper-refit` 是当前更值得保留的在线更新方式，`weighted_source` 在该分支上体现出有效的预训练数据优化帮助。 |
| 直接证据 | `Stage1_Total_Comparison_seed42.md`；`Stage1_Complete_Strategy_Comparison_with_EEGNet_seed42.md`；`Stage1_Source_Bridge_Full70_Controls_seed42_43_44_s1_5_9.md` |
| 关键数字 | `upper_refit_no_ea`：`mean raw acc = 0.7174`，`AULC20 = 0.6561`；`no_update = 0.6952 / 0.6184`；`online EA = 0.6952 / 0.6202`；`EEGNet no-update = 0.7242 / 0.6605`；`weighted_source` 相对 `unweighted_source`：`mean raw acc +0.0054`，`AULC20 +0.0137`，`instability -0.0095` |
| 正文允许写法 | `upper-refit 比单独 online EA 更值得保留。` |
| 正文禁止写法 | `Conformer 已经全面优于经典结构。` |
| 必须补的解释 | 为什么要同时保留 EEGNet 背景基线。 |
| 必须写的边界 | `weighted_source` 的收益主要集中在若干过程指标，不宜写成全面提升。 |

---

## 4. `5.2 真实在线实验与训练-反馈联动机制`

### 4.1 `5.2.1 在线实验平台与训练交互方法`

| 项目 | 内容 |
| --- | --- |
| 主张 | 真实在线实验已经实现了轮次级及时训练、模型反馈与再训练的联动机制，并形成可回溯记录。 |
| 直接证据 | `Online_Experiment_Program_Version_Evolution_And_Asset_Organization_20260419.md`；`nearalQTpro/Main.qml`；`nearalQTpro/eegdataprocessor.cpp/.h`；`nearalQTpro/mi_pipeline/README.md`；`online_mi_round_bridge.py` |
| 关键证据对象 | `subject/session/run` 组织；`train-round`；`infer-trial`；`mi_session.json`；`mi_summary.csv`；`mi_raw_eeg.csv`；`mi_predictions.csv` |
| 正文允许写法 | `真实在线平台已经形成训练-反馈联动机制。` |
| 正文禁止写法 | `完整系统闭环部署已经在端侧节点上完成。` |
| 必须补的解释 | 说明首轮不产生 active prediction 与冷启动逻辑的关系。 |
| 必须写的边界 | 当前运行载体主要是 Linux PC 原型环境；`RK3568 / RKNN` 仅在 `5.3` 作为后续迁移目标讨论。 |

### 4.2 `5.2.2 在线实验结果与误差分析`

| 项目 | 内容 |
| --- | --- |
| 主张 | 真实在线记录已经能够支撑“部分参与者、部分完整会话进入或接近可用区间”的判断，但整体稳定性尚未建立。 |
| 直接证据 | `NearalQTpro_Online_Active_Inference_Summary_20260419.md`；`NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260419.csv`；`NearalQTpro_Online_ThreeParticipant_Selected_Run_Metrics_20260422.csv`；`NearalQTpro_Subject009_Session007_Review_And_Plots_20260419.md` |
| 关键数字 | 第一位真实参与者：一次短时运行 `6/8 = 0.75`；第二位真实参与者：一次修正后的完整会话 `13/20 = 0.65`；第三位真实参与者：完整会话 `15/20 = 0.75`、`17/20 = 0.85`，后续补充完整会话 `15/20 = 0.75`、`16/20 = 0.80`；总体主记录中第二位 `0.4768`，第三位 `0.6067` |
| 正文允许写法 | `在当前实验条件下，部分真实参与者的完整在线会话已达到或接近 70% 的可用区间。` |
| 正文禁止写法 | `真实在线系统已经稳定达到离线 70% 以上准确率。` |
| 必须补的解释 | 必须区分“总体汇总”“完整会话”“短时局部运行”三种口径。 |
| 必须写的边界 | 样本量有限、协议异质性明显、置信度校准仍未收敛。 |

---

## 5. `5.3 本章小结与证据边界`

| 项目 | 内容 |
| --- | --- |
| 主张 | 本章已经完成低通道运动想象脑电解码方法从伪在线方法筛选到真实在线训练-反馈机制的初步收口。 |
| 直接证据 | `5.1` 与 `5.2` 全部 A 级证据；`Thesis_Status_MI_Experiment_Online_Integration_Analysis_20260414.md` |
| 必须回收的判断 | `upper-refit` 值得保留；round dependency 是强混杂因素；真实在线联动机制已经实现；真实在线结果支撑初步可用性，但不是稳定性能结论。 |
| 必须回收的边界 | `RK3568 / RKNN` 的系统级闭环迁移仍待完成；移动场景与长期稳定性仍待补充；真实在线样本仍需扩充。 |
| 正文允许写法 | `本文已经完成从离线低通道主线走向在线实验验证的初步收口。` |
| 正文禁止写法 | `本文已经完成最终端侧闭环脑机接口系统验证。` |

---

## 6. 可直接复用的判断模板

### 6.1 伪在线方法判断

- `结果表明，在严格时间顺序重放条件下，upper-refit 比单独 online EA 更值得保留。`
- `结果表明，round / trial batch 难度对伪在线曲线的解释力显著高于策略主效应。`
- `因此，质量降权可以写成一种有效的预训练数据优化策略，但其收益主要体现在冷启动前段和中前段稳定性。`

### 6.2 真实在线机制判断

- `结果表明，当前真实在线平台已经实现了轮次级及时训练、模型反馈与再训练的联动机制。`
- `由此说明，本文方法已经从离线算法可行性进入真实在线实验流程。`

### 6.3 真实在线可用性判断

- `在当前实验条件下，部分真实参与者的完整在线会话已经达到或接近可用区间。`
- `这说明该方法不仅具有离线算法可行性，而且已经表现出进入真实在线使用场景的初步可用性。`
- `不过，这一判断仍受样本量、会话一致性和置信度校准问题限制。`

---

## 7. 当前最容易越界的写法

以下写法当前一律禁用：

1. `真实在线结果已经稳定达到应用级水平。`
2. `端侧完整闭环部署已经完成。`
3. `source weighting 已被证明稳定有效。`
4. `伪在线结果足以替代真实在线验证。`
5. `某一次高分运行即可代表整体真实在线性能。`
