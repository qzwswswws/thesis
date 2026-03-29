# 🤖 双 AI 协作同步看板 (AI Sync Board)

**目标 (Purpose):** 本文件作为 Antigravity 模型 (Gemini) 与 Codex/Cursor 模型之间的异步通信状态机。
在每次进行大型代码修改或论文章节更新前，必须阅读此文件，结束时更新此文件，以防止 Git 冲突、职责漂移与文件损坏。

## 🧭 协作总原则 (Collaboration Rules)
1. **先读后改**：任何 AI 在修改正文、参考文献、编译链或提示词前，必须先阅读本文件。
2. **锁优先于编辑**：涉及 `chap*.tex`、`refs.bib` 或其它高风险共享文件时，先声明锁，再编辑，再释放锁。
3. **Git 责任单点化**：除非用户明确改派，`Git` 版本管理、提交与历史整理默认由 **Antigravity** 负责；Codex 默认不主动接管。
4. **正文与工程分工明确**：Codex 侧重正文起草、文献吸收、结构收束；Antigravity 侧重 Git、`refs.bib`、编译兜底与辅助脚手架。
5. **冲突先留言，不硬改**：若跨责任区出现依赖或疑似冲突，先通过下方“受限交流机制”留言，不直接覆盖对方工作。

## 📍 当前文件锁状态 (File Locks)
*在编辑特定章节文件前，请在此处声明锁定，编辑完成后释放。*

| 编辑文件路径 (File Path) | 当前责任 AI (Assigned AI) | 锁定状态 (Status) | 当前任务 / 下一步 | 最后更新时间 |
| :--- | :--- | :--- | :--- | :--- |
| `01_Thesis_LaTeX\data\chap01.tex` | Codex | `Free` | 已补写“现有研究存在的不足”，后续可按统稿需要再收束 | 2026-03-26 |
| `01_Thesis_LaTeX\data\chap02.tex` | Codex | `Free` | 第 2 章 `2.3`--`2.6` 已完成初稿并通过编译 | 2026-03-26 |
| `01_Thesis_LaTeX\data\chap04.tex` (及相关实验章) | Codex | `LOCKED` (待 Codex 动笔) | 将 `04_Algorithm_Workbench` 的新出成果转译写入正文 | 今日期 |
| `01_Thesis_LaTeX\ref\refs.bib` | Antigravity | `Free` | 第 2 章新增部署 cite key 已补录，后续恢复参考文献责任区 | 2026-03-26 |
| `01_Thesis_LaTeX\thesis.tex` (主架构) | **严禁修改** | `LOCKED` (需用户确认) | 主入口文件，非必要不触碰 | - |

## 👥 责任分工快照 (Role Split Snapshot)

| 工作类型 | 主责任 AI | 说明 |
| :--- | :--- | :--- |
| 正文主笔、章节扩写、文风收束 | Codex | 包括章节结构、综述写作、实验叙述与论文润色 |
| 文献吸收后的正文转写 | Codex | 将 Undermind / 原文证据整理为论文可用内容 |
| `Git` 版本管理与提交 | Antigravity | 默认唯一责任方，避免双重提交与历史混乱 |
| `refs.bib` 维护与引用链排障 | Antigravity | 参考文献条目、国标样式与丢失条目修复 |
| 编译兜底、模板故障排查 | Antigravity | 处理 `makepdf.bat`、模板异常和高风险构建问题 |
| 图示、Mermaid、脚手架辅助 | Antigravity | 后台支持项，按需调用 |

## 📬 受限交流机制 (Restricted Relay Channel)
*只允许传递阻塞性、跨责任区、可执行的信息，避免把本文件变成长对话聊天记录。*

若**单行留言不足以完成一次协作**，应改用 [\_AI_RELAY_CHAT.md](C:/Users/qzwsw/Documents/thesis/00_AI_Management/_AI_RELAY_CHAT.md) 开启 `Thread` 式对话；对话结束后，再把结论摘要回写到本文件。

### 允许的留言类型
- `HANDOFF`: 任务交接或阶段性产出移交
- `REF_CHECK`: 参考文献 / `cite` / `refs.bib` 依赖请求
- `BUILD_HELP`: 编译、模板、环境异常请求
- `RISK_ALERT`: 发现潜在冲突、覆盖风险或事实不一致
- `LOCK_NOTICE`: 文件即将锁定、已释放、请求协同

### 留言规则
1. 只在**需要对方行动**时留言，普通阅读与分析无需记录。
2. 每条留言必须写清：`相关文件`、`希望对方做什么`、`为什么阻塞当前工作`。
3. 对方收到后，优先更新同一行的 `状态`，而不是另起重复留言。
4. 留言内容应短、具体、可执行；禁止只写“看一下”“帮我处理”这类模糊句。
5. 若问题已自行解决，应将状态改为 `Closed`，避免悬挂。
6. 若同一问题需要来回回应 2 轮以上，请转入 [\_AI_RELAY_CHAT.md](C:/Users/qzwsw/Documents/thesis/00_AI_Management/_AI_RELAY_CHAT.md)，不要在本表中堆积长文本。

| ID | From | To | Type | 相关文件 | 请求 / 上下文 | 状态 | 最后更新时间 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T001 | Codex | Antigravity | `HANDOFF` | `00_AI_Management/Input_Buffer`, `03_Literature`, `99_Archive` | 已在 `_AI_RELAY_CHAT.md` 发起“既有文献材料去留与整理建议”线程，请确认哪些旧缓存仍有活跃价值。 | `Closed` | 2026-03-23 |
| T002 | Codex | Antigravity | `HANDOFF` | `Hardware_aware_EEG_BCI_model_optimization_evidence_report.md` | 解析硬件相关审查报告并浓缩一份 5-8 篇的最优下载清单。 | `Closed` | 2026-03-23 |
| T002 | Codex | Antigravity | `REF_CHECK` | `01_Thesis_LaTeX/data/chap02.tex`, `01_Thesis_LaTeX/ref/refs.bib`, `00_AI_Management/Input_Buffer/MI_EEG_sensorimotor_physiology_evidence_report.md` | `[Pfu06] [Mcf04] [Zap20b] [Xu19] [Rim23b]` 等核心条目已按用户要求补入 `refs.bib` 并完成重编译；若后续需要统一键名或国标细修，可继续接管。 | `Closed` | 2026-03-23 |
| T003 | Codex | Antigravity | `HANDOFF` | `00_AI_Management/Input_Buffer/Hardware_aware_EEG_BCI_model_optimization_evidence_report.md`, `00_AI_Management/_AI_RELAY_CHAT.md` | 已在 `_AI_RELAY_CHAT.md` 发起“硬件优化报告解析与下载清单接力”线程，请接手筛选 5-8 篇最值得下载全文的论文。 | `Closed` | 2026-03-23 |

## 🔄 当前任务接力 (Current Handoffs)
*这里记录正在推进、即将交接或需要对方知晓的主线事项。*

- **文风/排版基座已封死工作项**: 详见 `_AI_ENTRY_POINT.md`。
- **文献库组织变革**: 论文原件现已全部转移至 **Knowledge Clusters (K1-K4)** 并统一归档于 `03_Literature/K*`。
- **活跃报告区**: 精炼后的研报及结构化笔记现统一存于 `00_AI_Management/Input_Buffer`，不再按 `K*_Support` 分文件夹。请直接从中查阅宏观纲要或 Prompt。
| 工作流 | 当前责任 AI | 当前状态 | 下一步 | 若阻塞则交给谁 |
| :--- | :--- | :--- | :--- | :--- |
| 第 2 章相关技术基础 | Codex | 已完成 `2.1`--`2.6` 初稿并通过编译 | 后续按整篇统稿再做文风与图表收束 | Antigravity 仅在引用链或编译异常时介入 |
| 第 4/5 章算法实验结果与退化分析 | Codex | `Prompt已就绪` / 刚激活 | 读取新传入的 CSV/PNG，撰写基线与退化实验节，并负责生成 Banano 画图提示词 | Antigravity 已完成物料筹备并下发指令 |
| 参考文献总表维护 | Antigravity | 常驻责任区 | 保持 `refs.bib` 与正文引用一致 | Codex 提供缺失条目线索 |
| 项目版本与提交历史 | Antigravity | 常驻责任区 | 统一处理 commit / sync / 回滚策略 | 用户明确改派前不切换 |

## 🚦 下一步协作计划 (Next Collaborative Steps)
1. **Antigravity (后台支持)**: 随时待命处理 `makepdf.bat` 报错，制作 Mermaid 硬件流转图，或预处理 Python 实验脚手架代码。
2. **Codex/Cursor (正文主笔)**: 可开始接手 `chap03.tex` 或 `chap04.tex` 的正文扩展。
3. **安全须知**: 若遇到任何未定义的引用 `[?]`，请严格遵照 `00_AI_Management\Prompt_Library\Reference_Management_Protocol.md` 中第 4 节的排查工作流，**切勿覆盖修改 `.cls` 模板或切换为 `biblatex`**。

---
*更新记录 (Log):*
- **[2026-03-23]**: (Antigravity) 初始化看板。确认了第二章的注意力推导公式已被 Codex 完善，且 LaTeX 编译环境通过健康检查。
- **[2026-03-23]**: (Codex) 增补协作总原则、职责分工、受限留言队列与当前任务接力；确认 `Git` 与 `refs.bib` 默认继续由 Antigravity 负责。
- **[2026-03-26]**: (Codex) 按用户要求完成第 2 章后半章写作，新增边缘部署、BLE 与 KS1092 采集前端技术基础，并将更适合绪论的研究不足回写至 `chap01.tex`；同步补录相关部署文献并完成整篇编译。
