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
| `01_Thesis_LaTeX\data\chap01.tex` | 待分配 | `Free` | 暂无当前任务 | 2026-03-23 |
| `01_Thesis_LaTeX\data\chap02.tex` | Codex | `Free` (最后进行理论润色) | 等待基于 Undermind 结果补强 `2.1` | 2026-03-23 |
| `01_Thesis_LaTeX\ref\refs.bib` | Antigravity | `Free` (已修复国标与丢失条目) | 继续作为参考文献责任区 | 2026-03-18 |
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

## 🔄 当前任务接力 (Current Handoffs)
*这里记录正在推进、即将交接或需要对方知晓的主线事项。*

| 工作流 | 当前责任 AI | 当前状态 | 下一步 | 若阻塞则交给谁 |
| :--- | :--- | :--- | :--- | :--- |
| 第 2 章 `2.1` MI 生理基础 | Codex | 基于 Undermind 审计结果整理写作蓝图 | 等待用户继续投喂报告 / 原文后起草正文 | Antigravity 仅在引用链或编译异常时介入 |
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
