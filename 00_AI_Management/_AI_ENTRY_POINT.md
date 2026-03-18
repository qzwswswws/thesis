---
description: 核心入口指令，每次任务执行前供用户引入，以确保 AI 准确识别任务类型并调用匹配的规范。
---

# 🤖 任务判定与规范导航 (AI Entry Point)

**【全局优先读指令】** 
当你作为一个新的 AI 会话实例接收到本文件时，你**必须**首先根据用户下达的具体任务类型，寻找下方列表中对应的规范字典。在执行任何文件查找、代码修改或正文撰写前，**先去调取并阅读对应的 `.md` 规范文件**。

## 📍 1. 任务路由分配表 (Task Triage)

### ✍️ [A. 章节起草与文风润色任务]
当要求你起草大段正文（特别是第 1、2 章）或评估你写出的长文质量时：
- **必须读取**: `00_AI_Management\Prompt_Library\Chapter_Writing_Style_Guide.md` (界定该章是“讲故事”还是“列教科书等式”)
- **必须读取**: `00_AI_Management\Prompt_Library\Writing_Quality_Standards.md` (控制学术严谨词汇、PEER 论证结构与数学公式的排版硬标)

### 📥 [B. 吸收素材与提取文献任务]
当要求你阅读用户刚放入 `Input_Buffer` 的新 PDF、HTML 或 Undermind 检索报告时：
- **必须读取**: `00_AI_Management\Prompt_Library\Interaction_Protocol.md` (指导你如何无损解析特定格式、避免公式乱码，以及如何规范提取高能语料信息)

### 🛠️ [C. 核心代码增删与版本干预任务]
当要求你对真正的 `01_Thesis_LaTeX\data` 或硬件脚本执行批量增删、合并重写操作时：
- **必须读取**: `00_AI_Management\Workflow_Protocol.md` (指导你必须局部增量操作，禁止盲目大面积覆盖)

### 📝 [D. 提示词演进与文献归档任务]
当用户要求“记录这一点 / 新增prompt”以修改系统规则，或要求整理清空当前文献缓存时：
- **必须读取**: `00_AI_Management\Prompt_Library\Prompt_Modification_Protocol.md` (指导如何以增量完善为主更新 Prompt)
- **必须读取**: `00_AI_Management\Prompt_Library\Reference_Management_Protocol.md` (指导文献转移归档逻辑)

### 📚 [E. 完善参考文献索引任务]
当要求你对 `01_Thesis_LaTeX\ref\refs.bib` 进行补充、查重、修正格式以及规范 Citation Key 时：
- **必须读取**: `00_AI_Management\Prompt_Library\Reference_Management_Protocol.md` (指导具体的 BibTeX 严苛排版规范)

## ⏱️ 2. 全局状态强制打卡 (Progress Hook)
无论你执行上述哪一条路由任务，在任务开启前和任务取得实质性成果后：
- **关联动作**: 你**必须**调阅并根据实际情况修改 `00_AI_Management\Session_Logs\Progress.md`。确保进度看板上的状态框（如 `[x]`, `[ ]`）永远是最新的。

## ⚠️ 3. 兜底守则与排版铁律 (Master Rules)
如果任务不明确，请遵守以下底线要求（摘自过去的 Master Prompt）：
1. 文字交互与正文全部使用**中文**。
2. 遇到模糊需求，**绝不准盲猜，必须先列出 2-3 个可选方案供用户确认**。
3. LaTeX 图表引用必须使用 `\ref{fig:label}`，禁止硬编码央式。
4. 严禁捏造文献 `\cite`，如果缺乏支撑，必须停笔呼叫用户。

## 📖 4. Prompt 术语库 (Prompt Terminology Database)
当用户在日常指令中使用以下特定词汇时，AI 必须严格执行其背后的宏指令逻辑：
- **“根据相关文献”**：意味着仅**参考、提炼文献的文字或宏观结论**进行概括陈述（常用于第 1 章的纯文本综述现状）。
- **“结合相关文献”**：意味着不仅参考文字结论，还必须**结合文献中的数学公式、推导界限、量化指标和实际网络架构结果**进行硬核技术拆解（常用于第 2 章技术原理或后文）。
- **“删除文件”**：无论何种语境下，绝不支持真正的物理抹除。任何要求删除特定文件或旧草稿的操作，**实质上是指将目标文件移动（Move）至 `99_Archive` 文件夹中归档**，任何情况下不可直接且永久删除文件。
- **“记录这一点” / “记一下” / “新增prompt”**：意味着当前我们在语境中敲定了能避免重蹈覆辙的好规矩。此时你必须**立即去修改对应的 `.md` 提示词库功能文本**。该修改动作**尽量以增加完善为主**，把新规则无缝插入并持久化，切勿盲目大面积推翻既有老规矩。
