# 参考文献管理与格式规范 (Reference Management Protocol)

## 🎯 目的 (Purpose)
本规范指导 AI 如何管理与归档用户的文献资料，以及如何提取并生成符合国防科技大学 (`nudtpaper`) 和 `99_Archive/Format_Templates` 底层排版标准的参考文献格式。


## 📝 1. BibTeX 参考文献格式规范 (BibTeX Formatting Standards)
在试图为 `01_Thesis_LaTeX\ref\refs.bib` 插入新的引用条目时，必须严格遵守以下基于 NUDT 模板的底层格式规范：
1. **文献类别精准**：确保正确使用 `@article` (期刊), `@inproceedings` (会议), `@book` (专著), 等条目结构。
2. **核心字段绝对完整**：
   - 期刊文章 (`@article`) 必须包含：`title`, `author`, `journal`, `volume`, `number` (如适用), `pages`, `year`。
   - 会议论文 (`@inproceedings`) 必须包含：`title`, `author`, `booktitle`, `pages`, `year`, 建议加入 `organization`。
3. **安全命名防崩盘法**：
   - 引用键值 (Citation Key) 建议采用 `[第一作者姓氏拼音/英文][年份首词]` 或长缩写。例如：`vaswani2017attention` 或 `songEEG2022`。**必须保证在整个 Bib 库中全局唯一**。
   - 严禁发生**“正文已写了 `\cite{xxx}` 但在 `refs.bib` 里伪造或遗忘”**的情形。每一次在正文追加全新引用的同时，必须连带补齐 `refs.bib` 的详尽条目。
