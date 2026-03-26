# Codex 最小协作工作流

本文件用于在 Codex 中快速恢复本论文项目的协作方式。目标是：

- 保持主线程连续
- 降低新线程启动成本
- 尽量把信息沉淀到文件而不是聊天记录中

## 1. 线程使用原则

- **主线程**：长期保留，用于论文正文推进、结构决策、统稿与总协调。
- **临时线程**：仅用于单一专题任务，例如文献解析、BibTeX 检查、LaTeX 编译排错。
- **任务完成后回到主线程**：临时线程的结果必须写回工作区文件，并更新 `Session_Logs/Progress.md`。

## 2. 新线程固定开场

在 Codex 新开线程时，优先直接发送下面这句话：

```text
先阅读 00_AI_Management/_AI_ENTRY_POINT.md，并同步查看 00_AI_Management/Session_Logs/Progress.md，然后按其中规范执行。
```

如任务较明确，直接接在后面：

```text
先阅读 00_AI_Management/_AI_ENTRY_POINT.md，并同步查看 00_AI_Management/Session_Logs/Progress.md，然后按其中规范执行。
任务：……
范围：……
要求：……
```

## 3. 推荐任务模板

```text
先按 _AI_ENTRY_POINT 规则执行。
任务：补写/修改/检查……
范围：只改……
依据：结合……
要求：不要编造没有依据的内容；完成后更新 Progress.md。
```

## 4. 文件优先原则

- 长文材料、PDF、PPT、DOCX 以“让我提炼并落盘”为主，不依赖聊天记录长期保存信息。
- 章节内容以 `01_Thesis_LaTeX/data/chap*.tex` 为准。
- 项目规则以 `00_AI_Management/_AI_ENTRY_POINT.md` 和 `Prompt_Library/*.md` 为准。
- 当前状态以 `00_AI_Management/Session_Logs/Progress.md` 为准。

## 5. 适合开临时线程的任务

- 处理 `03_Literature` 中的新文献资料或 `Input_Buffer` 中的素材
- 批量检查 `refs.bib` 与 `\cite{}`
- 排查 LaTeX 编译错误、图表编号、引用格式问题

## 6. 不建议拆线程的任务

- 章节连续写作
- 全文结构调整
- 摘要、结论、创新点提炼
- 多章节联动修改

以上任务优先保留在主线程中，以免上下文割裂。
