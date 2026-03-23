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

## 🔢 2. 文内引用与模板红线规范 (Citation Style & Template Constraints)
1. **强制数字引用格式**：正文中的参考文献引用必须在编译后显示为方括号数字，即 `[1]`。
2. **底层引擎使用约束 (natbib 优于 biblatex)**：在 TeX Live 2015 及老旧环境下，**禁止使用 `biblatex/biber`** 解析 GB/T 7714-2015 格式（极易导致编译失败或缓存损坏）。必须依赖 `nudtpaper.cls` 中内置的安全回调：在 `thesis.tex` 中移除了 `biber` 参数后，模板会自动降级使用 `natbib` 宏包和自带的 `bstutf8.bst` 格式文件。编译流程统一要求为 `bibtex`。以后任何报错排查，**严禁修改 `.cls` 文件中的这套核心框架**。
编译流程统一要求为 `bibtex`。以后任何报错排查，**严禁修改 `.cls` 文件中的这套核心框架**。
虽然目前模板代码可能存在各种兼容性策略，但**最终导出效果**必须是顺序编码。
3. **严禁修改底层文件**：**绝对禁止**大面积重写覆盖 `nudtpaper.cls`、`.bst` 宏包，或者在 `thesis.tex` 的 preamble 中做破坏性替换。由于存在 TeX Live 2015 兼容问题，这些操作极易引发格式血崩。只能通过安全参数如调整 `\cite` 或 `biblatex` 选项（`style=numeric`）来实现。

## 🔍 3. 常见报错排查工作流 (Troubleshooting Workflow)
如果有文献在生成的 PDF 中显示为 `[?]`（未定义引用），必须按照以下**最小干预原则**依次排查，严禁一来就改动模板环境：
1. **核对正文与 BibTeX 的键值（Key）是否绝对一致**：例如正文中写的是 `\cite{wan2023channel}`，但 `refs.bib` 里的 entry 却叫 `@article{wan2023novel, ...}`，这必然导致 `[?]`。AI 应全局搜索 `.tex` 文件，批量将旧版或手工录入的硬编码键值替换为 `.bib` 文件中真实有效的最新键值。
2. **确认条目真的存在于 `.bib` 中**：如果正文提到了 `\cite{liu2021swin}`，需要去 `01_Thesis_LaTeX/ref/refs.bib` 检索该条目是否真的被追加了进去。如缺失，必须先手动补充正确的 BibTeX 格式条目。
3. **确认编译脚本的完整链路**：文献交叉引用的完全解析需要多遍编译链路支撑（`xelatex -> bibtex -> xelatex -> xelatex`），AI 执行了 `\cite` 替换和 `.bib` 更新后，**必须**直接运行工作区内的 `makepdf.bat` 获取最终版结果。

## 🧪 4. 技术叙事与文献对齐规范 (Technical Narrative & Literature Alignment)
在撰写理论背景（如 $O(N^2)$ 复杂度瓶颈）并引用文献时，必须确保“叙事深度”与“文献实际贡献”高度对齐，严禁夸大或张冠李戴：
1. **复杂度瓶颈的准确描述**：当提到 Transformer 的二次方复杂度时，应明确区分“理论计算量爆发”与“端侧显存/算力溢出”。引文必须支撑该论点。
   - **Wan23/Hua23b**：核心贡献在于通过 Swin/滑动窗口将复杂度降为线性 $O(N)$。
   - **Bus24 (EEGformer)**：核心贡献在于低功耗 MCU 上的真实落地，重点是“端到端延迟”和“能耗”。
   - **Keu24 (EEGCCT)**：重点在于通过卷积嵌入减少特征维度（减少 $N$），以及跨被试的泛化能力。
2. **算法优化 vs. 硬件优化**：
   - 算法优化（如注意力机制改进）解决的是**扩展性问题**，决定了模型能否处理长序列脑电。
   - 硬件级/部署级优化（如量化 Quantization、剪枝 Pruning）解决的是**落地精度与速度的折中**。
   - 在描述端侧部署时，应体现“算法架构优化为先（解决可行性），量化部署为后（解决效率性）”的逻辑，这符合当前主流顶会（如 IEEE TNSRE, Frontiers）的论文叙事逻辑。
3. **核查机制**：在生成新的讨论段落后，AI 应自检：引用的这几篇论文是否真的在讨论我所说的这个点？如果论文主攻量化而 AI 用它来证明 $O(N^2)$ 的降低，应立即修正。
