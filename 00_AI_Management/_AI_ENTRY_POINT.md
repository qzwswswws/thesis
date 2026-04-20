---
description: 核心入口指令，每次任务执行前供用户引入，以确保 AI 准确识别任务类型并调用匹配的规范。
---

# 🤖 任务判定与规范导航 (AI Entry Point)

**【全局优先读指令】** 
当你作为一个新的 AI 会话实例接收到本文件时，你**必须**首先根据用户下达的具体任务类型，寻找下方列表中对应的规范字典。在执行任何文件查找、代码修改或正文撰写前，**先去调取并阅读对应的 `.md` 规范文件**。

## 📍 1. 任务路由分配表 (Task Triage)

### ✍️ [A. 章节起草与文风润色任务]
当要求你起草大段正文（特别是第 1、2 章）或评估你写出的长文质量时：
- **必须读取**: `00_AI_Management\Output_Drafts\论文最终结构冻结稿_20260414.md` (已吸收 2026-04-15 新主线与创新点口径，冻结全文中心线、章节职责、创新点表述方式与第 4/5/6 章标题口径)
- **建议同时读取**: `00_AI_Management\Output_Drafts\主线与创新点微调稿_20260415.md` (记录本轮主线与创新点调整依据，便于避免回退到旧说法)
- **必须读取**: `00_AI_Management\Prompt_Library\Chapter_Writing_Style_Guide.md` (界定该章是“讲故事”还是“列教科书等式”)
- **必须读取**: `00_AI_Management\Prompt_Library\Writing_Quality_Standards.md` (控制学术严谨词汇、PEER 论证结构与数学公式的排版硬标)

### 📥 [B. 吸收素材与提取文献任务]
当要求你阅读用户放入 `03_Literature` 或 `Input_Buffer` 的新 PDF、HTML 或检索报告时：
- **必须读取**: `00_AI_Management\Prompt_Library\Interaction_Protocol.md` (指导你如何无损解析特定格式、避免公式乱码，以及如何规范提取高能语料信息)

### 🛠️ [C. 核心代码增删与版本干预任务]
当要求你对真正的 `01_Thesis_LaTeX\data` 或硬件脚本执行批量增删、合并重写操作时：
- **必须读取**: `00_AI_Management\Workflow_Protocol.md` (指导你必须局部增量操作，禁止盲目大面积覆盖)

### 📝 [D. 提示词演进与文献归档任务]
当用户要求“记录这一点 / 新增prompt”以修改系统规则，或要求整理清空当前文献缓存时：
- **必须读取**: `00_AI_Management\Prompt_Library\Prompt_Modification_Protocol.md` (指导如何以增量完善为主更新 Prompt)
- **必须读取**: `00_AI_Management\Prompt_Library\Reference_Management_Protocol.md` (指导文献转移归档逻辑)
- **特别注意**: `99_Archive` 虽然是归档冷区（为节省全局 Token 不默认读取），但当你在 `03_Literature` 中找不到指定的原始数据或文献原文时，**必须主动前往 `99_Archive/Raw_Web_Captures` 或 `99_Archive/Raw_PDFs` 进行按需精准检索**。归档区对 AI 绝非禁区。

### 📚 [E. 完善参考文献索引任务]
当要求你对 `01_Thesis_LaTeX\ref\refs.bib` 进行补充、查重、修正格式以及规范 Citation Key 时：
- **必须读取**: `00_AI_Management\Prompt_Library\Reference_Management_Protocol.md` (指导具体的 BibTeX 严苛排版规范)

### 🧱 [F. 论文编译与日志排障任务]
当要求你执行 `makepdf.bat`、排查 `thesis.log`、判断 LaTeX 编译是否真正失败，或修复图文件/编译链导致的问题时：
- **必须读取**: `00_AI_Management\Prompt_Library\LaTeX_Compilation_Protocol.md` (明确当前项目唯一推荐编译入口、`bibtex` 链条、致命错误与非阻塞警告的判别规则)
- **建议同时读取**: `00_AI_Management\Workflow_Protocol.md` (避免在共享章节与模板文件上误操作)

### 🧪 [G. MI 实验资产整合与第 4/5/6 章联动写作任务]
当要求你处理 `100_remotefiles/MIEXP` 中的离线、伪在线、真实在线实验资产，或据此撰写/修订第 4、5、6 章时：
- **必须读取**: `00_AI_Management\Prompt_Library\Experiment_Asset_Location_Protocol.md` (规定实验资产定位顺序、证据分层与在线/伪在线口径)
- **必须读取**: `00_AI_Management\Output_Drafts\论文最终结构冻结稿_20260414.md` (已吸收 2026-04-15 新主线与创新点口径，冻结第 5 章标题强度、全文中心线和创新点边界)
- **建议同时读取**: `00_AI_Management\Output_Drafts\MIEXP_Quick_Locator_20260414.md` (快速定位高价值实验资产与运行目录)

### ✏️ [H. 语句级修改与逐句批注落实任务]
当要求你逐句修改正文、落实批注、压低 AI 腔或统一摘要/第 1/5/6 章的句子强弱时：
- **必须读取**: `00_AI_Management\_AI_SENTENCE_EDIT_ENTRY_POINT.md` (句级修改专用入口，规定本线程只做句子/段落级微调)
- **必须读取**: `00_AI_Management\Output_Drafts\句级修改对照记录_20260415.md` (登记“原句 -> 修改后”对照、写回状态和批量编译状态)
- **特别注意**: 该类任务默认**不应每次修改后立即编译**；应先累计到对照记录，攒够一批后再统一编译

## 🧠 1.5 长期记忆锚点 (Persistent Memory Anchors)
如果用户明确以“引用本文件”的方式要求你继续协作，那么除了任务对应协议外，还应把下列文件视作当前项目的默认长期记忆锚点：

### 稳定锚点（优先信任）
- `00_AI_Management\Output_Drafts\论文最终结构冻结稿_20260414.md`
  - 用途：冻结章节标题、章节职责、全文中心线、创新点表述方式。
- `00_AI_Management\Output_Drafts\主线与创新点微调稿_20260415.md`
  - 用途：保存“辅助交互与便携式使用场景 -> 少导联采集、有限算力与在线交互约束 -> 任务/模型/系统再收束”的最新调整依据，避免后续写作回退到旧主线。
- `00_AI_Management\_AI_SENTENCE_EDIT_ENTRY_POINT.md`
  - 用途：当任务转入逐句改写、批注落实、摘要压句或段落口气统一时，作为专用入口与流程规范。
- `00_AI_Management\Prompt_Library\Chapter_Writing_Style_Guide.md`
  - 用途：控制各章节讲述方式，避免第 1 章与第 2 章同质化。
- `00_AI_Management\Prompt_Library\Writing_Quality_Standards.md`
  - 用途：控制学术表述边界，尤其是创新点、结果强度和保守措辞。
- `00_AI_Management\Prompt_Library\Experiment_Asset_Location_Protocol.md`
  - 用途：规定实验资产如何定位、哪些能写成主结果、哪些只能写成 pilot 或探索。

### 动态索引（先看索引，再下钻）
- `00_AI_Management\Output_Drafts\句级修改对照记录_20260415.md`
  - 用途：回答“哪些句子已经改过、是否已写回正文、是否需要统一编译”。
- `100_remotefiles/MIEXP/00_AI_Management/Output_Drafts/Thesis_Status_MI_Experiment_Online_Integration_Analysis_20260414.md`
  - 用途：回答“当前实验证据能支撑什么结论”。
- `100_remotefiles/MIEXP/00_AI_Management/Output_Drafts/MI_Experiment_Asset_Index_20260414.md`
  - 用途：回答“实验资产放在哪里”。
- `100_remotefiles/MIEXP/00_AI_Management/Output_Drafts/MI_Experiment_Registry_20260414.md`
  - 用途：回答“每个实验做了什么、效果如何、该不该写进论文”。
- `00_AI_Management\Output_Drafts\MIEXP_Quick_Locator_20260414.md`
  - 用途：在需要快速定位 MIEXP 材料时先用一页卡片缩短搜索路径。

**执行习惯**：
1. 先读稳定锚点，确保主线不漂。
2. 再读动态索引，确认当前实验版本与证据边界。
3. 最后才下钻到具体运行目录、图片、日志或原始结果文件。

## ⏱️ 2. 全局状态强制打卡 (Progress Hook)
无论你执行上述哪一条路由任务，在任务开启前和任务取得实质性成果后：
- **关联动作**: 你**必须**调阅并根据实际情况修改 `00_AI_Management\Session_Logs\Progress.md`。确保进度看板上的状态框（如 `[x]`, `[ ]`）永远是最新的。

## ⏱️ 2.5 句级修改的编译节奏

当任务命中 `H. 语句级修改与逐句批注落实任务` 时，默认遵循以下编译节奏：

1. 先登记到 `句级修改对照记录_20260415.md`；
2. 再将确认后的修改写回正文；
3. 不要每改一句就编译；
4. 仅在以下情况触发统一编译：
   - 用户明确要求；
   - 已累计涉及多个正文文件；
   - 改动了引用、图表、公式、标题或交叉引用；
   - 一轮修改已经达到可交付状态。

若本轮未编译，应在回复中明确说明“本轮为句级修改批次，暂未编译，待累计后统一校验”。

## ⚠️ 3. 兜底守则与排版铁律 (Master Rules)
如果任务不明确，请遵守以下底线要求（摘自过去的 Master Prompt）：
1. 文字交互与正文全部使用**中文**。
2. 遇到模糊需求，**绝不准盲猜，必须先列出 2-3 个可选方案供用户确认**。
3. LaTeX 图表引用必须使用 `\ref{fig:label}`，禁止硬编码央式。
4. 严禁捏造文献 `\cite`，如果缺乏支撑，必须停笔呼叫用户。
5. 创新点、贡献与章节主张必须优先服从 `论文最终结构冻结稿` 与 `主线与创新点微调稿` 的口径；除非有明确证据，不得自行升格为“首次提出”“实现完整在线验证”“稳定优于 baseline”。

## 📖 4. Prompt 术语库 (Prompt Terminology Database)
当用户在日常指令中使用以下特定词汇时，AI 必须严格执行其背后的宏指令逻辑：
- **“根据相关文献”**：意味着仅**参考、提炼文献的文字或宏观结论**进行概括陈述（常用于第 1 章的纯文本综述现状）。
- **“结合相关文献”**：意味着不仅参考文字结论，还必须**结合文献中的数学公式、推导界限、量化指标和实际网络架构结果**进行硬核技术拆解（常用于第 2 章技术原理或后文）。
- **“删除文件”**：无论何种语境下，绝不支持真正的物理抹除。任何要求删除特定文件或旧草稿的操作，**实质上是指将目标文件移动（Move）至 `99_Archive` 文件夹中归档**，任何情况下不可直接且永久删除文件。
- **“记录这一点” / “记一下” / “新增prompt”**：意味着当前我们在语境中敲定了能避免重蹈覆辙的好规矩。此时你必须**立即去修改对应的 `.md` 提示词库功能文本**。该修改动作**尽量以增加完善为主**，把新规则无缝插入并持久化，切勿盲目大面积推翻既有老规矩。
- **“参考文献规范” / “模板红线”**：必须严格按照模板组织参考文献，正文引用**必须保证 `[]` 内使用数字**（如 `[1]`）。**严禁**为追求格式极致而大面积替换或覆写底层的 `.cls`、`.bst` 文件及基础编译系统配置，以防引发 TeX Live 2015 环境下不可修复的大规模排版崩溃。
- **“逐句修改” / “落批注” / “压句子”**：默认视为 `H. 语句级修改与逐句批注落实任务`。应优先进入 `00_AI_Management\_AI_SENTENCE_EDIT_ENTRY_POINT.md`，并先写入 `句级修改对照记录_20260415.md`，而不是直接把整章改乱后立刻编译。

