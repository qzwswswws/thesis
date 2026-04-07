# 第 3 章写作状态与数据索引

对应章节：
- `01_Thesis_LaTeX/data/chap03.tex`

整理时间：
- `2026-04-01`

文档目的：
- 统一记录第 3 章当前可直接写入正文的实验结论；
- 为后续人工写作或 AI 辅助写作提供可直接引用的数据入口；
- 明确哪些结果可作为主结果，哪些结果只宜作为补充或过程记录；
- 明确当前仍需保守表述的部分。

---

## 一、当前总体判断

截至 `2026-04-01`，第 3 章除“功耗与续航测试”外，整体已进入收束与成稿阶段。

当前状态可概括为：

1. 实验 1“脑电采集有效性验证”已有可引用结果；
2. 实验 3 已从“绝对端到端延迟”调整为“标签链路响应与时序稳定性验证”，已有可引用结果；
3. 实验 2“无线传输稳定性测试”尚缺结构化长时统计，不宜写成“已完成完整定量验证”；
4. 实验 4“功耗与续航测试”仍是当前唯一明显未完成项。

因此，若后续开始集中撰写第 3 章正文，推荐采用如下总体口径：

- 第 3 章主体可先完成；
- 无线稳定性部分采用“当前运行观察 + 后续可补长时统计”的保守表述；
- 功耗部分单独作为最后收尾任务。

---

## 二、各实验完成度

| 实验 | 当前状态 | 是否可写入正文 | 建议写法 |
|---|---|---|---|
| 实验 1：脑电采集有效性验证 | 基本完成 | 可以 | 以前额叶主结果为主，头顶部结果作补充现象 |
| 实验 2：无线传输稳定性测试 | 部分完成 | 可写，但需保守 | 写“当前链路运行稳定，完整长时定量测试留作后续补充” |
| 实验 3：标签链路响应与时序稳定性 | 完成 | 可以 | 不再硬写“绝对端到端时延”，改写为“标签链路响应性能” |
| 实验 4：功耗与续航测试 | 未完成 | 暂不建议 | 待补测后再写入正式结论 |

---

## 三、实验 1 可直接使用的数据索引

### 3.1 推荐主结果

推荐将下列结果作为“前额叶 Alpha 实验”的主结果：

- 文件：
  `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_summary.csv`
- 配套会话文件：
  `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_session.json`
- 配套原始 EEG：
  `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_raw_eeg.csv`
- 配套趋势文件：
  `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_trend.csv`
- 对应 marker：
  `C:\Users\qzwsw\Documents\nearalQT_marker_logs\20260331_160818_markers.csv`
  其中本次实验对应 `marker_id 9-16`

主结果摘要：

| 指标 | 数值 |
|---|---:|
| 导联定位 | 前额叶 |
| 阶段时长 | `15 s` |
| 睁眼均值 `combined` | `22.2563%` |
| 闭眼均值 `combined` | `25.7564%` |
| 闭眼/睁眼比值 | `1.1573` |
| cycle 1 ratio | `1.129` |
| cycle 2 ratio | `1.143` |
| cycle 3 ratio | `1.211` |

推荐解释：

- 该组结果在 3 个 cycle 中均表现为 `closed > open`；
- 对前额叶布置而言，这属于“有一致性增强、强度中等”的可引用结果；
- 由于配有 `raw_eeg.csv + session.json + marker`，该组最适合作为正文主结果与后续离线分析基础。

### 3.2 推荐补充结果

若需要同时展示不同导联位置下的现象，可将下列结果作为“头顶部补充现象”：

- 文件：
  `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_160053_alpha_summary.csv`
- 配套趋势文件：
  `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_160053_alpha_trend.csv`
- 对应 marker：
  `C:\Users\qzwsw\Documents\nearalQT_marker_logs\20260331_154154_markers.csv`
  其中本次实验对应 `marker_id 1-8`

补充结果摘要：

| 指标 | 数值 |
|---|---:|
| 导联定位 | 头顶部，可标记为“大脑顶部的实验现象” |
| 阶段时长 | `10 s` |
| 睁眼均值 `combined` | `23.5528%` |
| 闭眼均值 `combined` | `26.9075%` |
| 闭眼/睁眼比值 | `1.1424` |
| cycle 1 ratio | `1.131` |
| cycle 2 ratio | `1.270` |
| cycle 3 ratio | `1.034` |

推荐解释：

- 该组可作为“不同导联位置下也观察到相似趋势”的补充支撑；
- 写作时应与前额叶结果分开叙述，不宜混写为同一类导联实验。

### 3.3 不建议作为主结果引用的实验

以下实验建议仅作过程记录或对照，不作为正文主结果：

| 文件 | 原因 |
|---|---|
| `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_160443_alpha_summary.csv` | `combined ratio = 1.021`，增强较弱，属边缘结果 |
| `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161008_alpha_summary.csv` | `combined ratio = 0.985`，方向不稳定，不宜作为正向验证结果 |

### 3.4 实验 1 推荐写法

推荐在第 3 章正文中采用如下口径：

- 主结论写“前额叶静息态 Alpha reactivity 已被观察到”；
- 主数据引用 `161122`；
- 若需要展示不同位置的补充现象，再额外引用 `160053`；
- 不建议写成“系统稳定采集到典型枕区 Alpha 阻断现象”，因为本研究采用的是前额叶方法；
- 不建议给出“硬件有效时比值应达到某固定阈值”的绝对表述。

---

## 四、实验 3 可直接使用的数据索引

实验 3 建议统一改称为：

- “标签链路响应与时序稳定性实验”

推荐主文件：

- 结果草稿：
  `C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\Chap03_Experiment03_Label_Response_Results_20260331.md`
- 原始 marker 结果：
  `C:\Users\qzwsw\Documents\nearalQT_marker_logs\20260331_130234_markers.csv`

主结果摘要：

| 指标 | 数值 |
|---|---:|
| 总标签数 | `78` |
| 成功确认数 | `78` |
| 成功率 | `100%` |
| 漏标数 | `0` |
| 平均 `round_trip_ms` | `127.01 ms` |
| 中位数 `round_trip_ms` | `106.5 ms` |
| P95 `round_trip_ms` | `248 ms` |
| 最大 `round_trip_ms` | `429 ms` |

自动打标结果：

| 设定周期 | 设备侧平均间隔 | 设备侧间隔标准差 | 上位机平均发送间隔 |
|---|---:|---:|---:|
| `200 ms` | `239.05 ms` | `15.18 ms` | `243.11 ms` |
| `500 ms` | `540.11 ms` | `23.17 ms` | `544.89 ms` |
| `1000 ms` | `1034.11 ms` | `31.49 ms` | `1044.21 ms` |

推荐解释：

- 当前链路已具备较好的标签可靠性与节奏跟随性；
- 可支持鼠标点击、按钮事件、一般交互事件等脑电标签写入；
- 该结果不应写成“按钮点击到设备打标的绝对单程时延”；
- 更适合写成“标签链路响应性能”与“时序稳定性”。

---

## 五、实验 2 当前可写与不可写的边界

当前对无线传输稳定性的判断是：

- 从日常运行与标签实验观察来看，链路整体工作稳定，未见明显持续性丢帧问题；
- 但尚缺 `10 min / 30 min / 60 min` 三档结构化长时统计；
- 因此不能写成“已完成完整无线稳定性定量验证”。

推荐写法：

- 可写“当前系统在 `500 Hz` 双通道连续采样与 BLE 持续连接条件下表现稳定，短时运行未见明显丢帧与异常中断”；
- 可写“完整长时稳定性定量统计可作为后续补充实验”；
- 不建议写“已完成 10/30/60 min 三档稳定性验证”。

如果后续时间紧张，实验 2 可在第 3 章中保留为：

- 工程观察结论；
- 非核心主实验；
- 或第 5 章扩展验证的前置说明。

---

## 六、当前仍待完成的唯一明显缺口

当前第 3 章最明确的未完成项是：

- 实验 4：功耗与续航测试

建议至少补以下三类工况：

1. 空闲待机
2. 双通道采样但未连接 BLE
3. 双通道采样且 BLE 持续连接发送

若能补测一轮平均电流与理论续航，第 3 章的验证闭环会完整很多。

---

## 七、建议的写作优先顺序

建议按以下顺序收束第 3 章：

1. 先写实验 1 正文，优先使用 `161122`，并根据需要补入 `160053`
2. 再写实验 3 正文，统一使用“标签链路响应与时序稳定性”口径
3. 对实验 2 使用保守表述，只写当前观察到的稳定运行现象
4. 最后单独补实验 4 功耗与续航

---

## 八、可直接交给 AI 的使用说明

后续若需要 AI 继续辅助写作或分析，建议优先提供以下文件：

### 8.1 实验 1 主结果最小文件集

- `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_summary.csv`
- `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_session.json`
- `C:\Users\qzwsw\Documents\nearalQT_alpha_logs\20260331_161122_alpha_raw_eeg.csv`
- `C:\Users\qzwsw\Documents\nearalQT_marker_logs\20260331_160818_markers.csv`

### 8.2 实验 3 主结果最小文件集

- `C:\Users\qzwsw\Documents\nearalQT_marker_logs\20260331_130234_markers.csv`
- `C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\Chap03_Experiment03_Label_Response_Results_20260331.md`

### 8.3 第 3 章状态说明文件

- `C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\Chap03_Experiment01_Alpha_Validation_Protocol_20260331.md`
- `C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\Chap03_Experiment03_Label_Response_Results_20260331.md`
- `C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\Chap03_Writing_Status_And_Data_Index_20260401.md`

AI 后续若基于本文件写正文，应默认遵循以下规则：

- 实验 1 以前额叶主结果 `161122` 为主；
- `160053` 仅作为头顶部补充现象；
- `160443` 和 `161008` 不作为主结果；
- 实验 3 统一使用“标签链路响应与时序稳定性”口径；
- 实验 2 仅作保守表述；
- 功耗尚未完成，不应擅自补写定量结论。

---

## 九、一句话总结

第 3 章目前已经具备进入正文成稿阶段的条件：实验 1 与实验 3 均已有可直接引用的数据基础，实验 2 可作保守性补充说明，当前真正需要补完的核心缺口只剩功耗与续航测试。
