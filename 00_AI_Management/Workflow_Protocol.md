# AI 辅助论文协作协议 (Workflow Protocol)

本协议旨在建立 AI 与用户之间稳定、高效的协作机制，确保论文撰写过程具有可追溯性、逻辑连贯性且格式规范。

## 1. 空间结构说明 (`00_AI_Management`)

*   **`Prompt_Library/`**: 存放经过验证的提示词模板。AI 在执行特定任务前应先读取这里的模板（如 LaTeX 绘图、文献概括）。
*   **`Input_Buffer/`**: 用户将外部 AI（如网页端 ChatGPT/Claude）或搜索到的信息粘贴至此处，AI 负责从中提取核心论点并集成到论文中。
*   **`Output_Drafts/`**: AI 生成的长文档初稿存放地。在正式合并入 `05_Manuscript` 前，应在此由用户进行审阅。
*   **`Session_Logs/`**: 记录每轮对话的进度摘要，防止长对话导致的记忆衰减。

## 2. 协作规则 (Rules of Engagement)

1.  **先调研后撰写**: AI 在撰写任何技术章节前，必须先检索 `01_Proposal_Midterm` (开题) 和 `02_Literature` (文献库) 中的相关背景。
2.  **输入优先**: AI 应主动询问用户是否有外部信息（来自 `Input_Buffer`）需要集成。
3.  **格式一致性**: 所有的 LaTeX 输出必须严格遵守 `nudtpaper.cls` 的定义。
4.  **增量更新**: 修改论文时，尽量采用局部替换（Replace）而非全表重写，以节省 Token 并减少错误。

3.  **科研绘图规范**:
    *   **首选方案**: 使用 LaTeX TikZ 或 PGFPlots 编写矢量绘图代码，确保与论文排版完美融合。
    *   **外部协作**: 若需复杂示意图，AI 负责提供 DALL-E/Midjourney 提示词或 Mermaid 草图，由用户生成图片后放入 `01_Thesis_LaTeX/figures/`。
    *   **自动化**: AI 应自动为所有图形生成对应的 `\caption` 和 `\label`。

4.  **文献调研规范 (Undermind 协作)**:
    *   **严禁幻觉**: AI 禁止直接捏造文献引用或在该领域进行“盲写”。
    *   **触发机制**: 当 AI 发现论证缺乏数据支持或需要最新研究动态时，必须**明确提示用户**：“此处需要使用 Undermind 进行针对性文献调研，关键词建议为：[XXX]”。
    *   **信息录入**: 用户将 Undermind 的搜索结果粘贴至 `00_AI_Management/Input_Buffer/`，AI 再进行深度解析与综述撰写。

5.  **信息获取路径 (Data Acquisition Path)**:

*   **内部**: `01_Proposal`, `03_Methodology_Scripts`, `04_Data`.
*   **外部**: 用户通过 `Input_Buffer` 提供的第三方 AI 见解或网页摘要。
*   **反馈**: AI 生成内容后，用户在 `Output_Drafts` 中标注 “修改建议”，AI 迭代后再合并。

## 4. 质量保证 (Quality Assurance)

*   每章完成后，执行一次 `makepdf.bat` 检查编译错误。
*   通过 `Session_Logs` 维护一个“待办列表”，确保没有跳过的逻辑盲点。
