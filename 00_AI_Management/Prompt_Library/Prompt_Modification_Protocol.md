# 提示词库动态维护规范 (Prompt Modification Protocol)

## 🎯 目的 (Purpose)
该协议指示 AI 如何响应用户的“记录这一点 / 新增prompt”等术语指令，并在不破坏现有稳定架构的前提下，对 `Prompt_Library` 中的各个规范文件进行扩充和优化。

## 🛠️ 1. 增量更新原则 (Incremental Update Rule)
- 本项目的所有 Prompt 规范（如 `Interaction_Protocol.md`, `Master_Prompt.md`, 等）都经过了历史的沉淀与精调，蕴含着之前踩过坑换来的红线血泪史。
- 当接收到修改或新增指令时，AI **必须以在末尾新增、在相关类目下扩充补充**（Append / Improve）为主。
- 严禁对文件中已有的（特别是未被要求修改的）旧大纲、旧指令进行大面积的盲目删除、重写或覆盖。如果你觉得某条旧规则有冲突，必须通过提示用户，等候批准后再进行破坏性编辑。

## 🎯 2. 操作执行步骤 (Execution Steps)
1. **寻找锚点**：基于用户的指示情境，判断应该修改哪个最对应的文件（如有关写作逻辑的去找 Style Guide，有关解压阅读的去找 Interaction Protocol）。
2. **精准切入**：通过局部文本替换（Replace Content），在文件末尾或对应的知识分类下，新增具有 Markdown 层级的清晰条款。
3. **同步反馈**：修改完成后，向用户确认最新的规则条款已固化，以确保下一次甚至长久未来的会话时能直接生效。
