# LaTeX 编译与排障协议 (LaTeX Compilation Protocol)

## 1. 目的

本协议用于约束 AI 在本项目中执行论文编译、日志排查和相关修复时的行为，重点避免以下几类常见问题：

- 把“非阻塞警告”误判为“编译失败”
- 在错误的目录下编译，或使用错误的工具链
- 因误判参考文献或模板机制而擅自改动 `.cls`、`.bst`、`thesis.tex`
- 由于图文件缺失、局部公式结构损坏、PDF 被占用等局部问题，演变成整套模板级返工

## 2. 本项目唯一推荐编译入口

### 2.1 标准做法

在项目中，默认从以下目录执行：

- 工作目录：`01_Thesis_LaTeX`

标准命令：

```bat
cmd /c makepdf.bat
```

### 2.2 当前真实编译链

`makepdf.bat` 当前执行的是：

1. 清理中间文件
2. `xelatex thesis`
3. `bibtex thesis`
4. `xelatex thesis`
5. `xelatex thesis`

因此：

- **默认参考文献工具是 `bibtex`，不是 `biber`**
- **默认入口是 `thesis.tex`，不是单独编译某个 `chap*.tex`**

## 3. 绝对不要做的事

### 3.1 不要擅自切换工具链

即使 `thesis.tex` 文件头部出现了类似 `%!BIB program = biber` 的注释，也**不要**因此自行改成 `biber` 流程。  
当前模板的实际运行链条是 `bibtex`，擅自切换会引发不必要的参考文献问题。

### 3.2 不要为了修编译去改模板底层

除非用户明确要求，否则不要主动修改：

- `nudtpaper.cls`
- `bstutf8.bst`
- `mynudt.sty`
- `thesis.tex`

编译问题优先从以下层面排查：

1. 新增正文是否有括号、环境、公式结构损坏
2. 新增图文件是否真实存在
3. 图路径是否正确
4. `\label` / `\ref` / `\cite` 是否写坏
5. 新增 TikZ/PDF 图是否已经单独编译生成

### 3.3 不要把清理失败误判为编译失败

Windows 下如果 `thesis.pdf` 被预览器占用，`makepdf.bat` 开头或结尾的 `del` 语句经常报：

- `The process cannot access the file because it is being used by another process.`

这通常只表示“部分旧中间文件没删掉”，**不等于 LaTeX 编译失败**。  
判断是否真正编译成功，应优先看日志里是否出现：

- `Output written on thesis.pdf (...)`

## 4. 如何判断是否真的失败

### 4.1 这些通常是“真正失败”

若日志中出现以下内容，应视为阻塞性错误：

- `LaTeX Error:`
- `Undefined control sequence`
- `Emergency stop`
- `Runaway argument`
- `File ... not found`
- `! Missing } inserted`
- `! Extra }, or forgotten \endgroup`
- `No file thesis.bbl`
- `I couldn't open file name ...`

### 4.2 这些通常不是阻塞性错误

以下内容在当前项目里通常可视为“警告而非失败”：

- `Underfull \hbox`
- `Overfull \hbox`
- `Underfull \vbox`
- `LaTeX Font Warning`
- `Missing character: There is no ... in font ...`
- `The process cannot access the file because it is being used by another process.`

这些问题可以记录，但不要因此把整次编译判成失败。

## 5. 图文件相关红线

### 5.1 图存在性先于正文分析

如果某次编译在新改章节后失败，首先检查：

1. `\includegraphics{...}` 对应文件是否真的存在
2. 文件扩展名是否和正文一致
3. 文件是否放在 `01_Thesis_LaTeX/figures/` 或被 `\graphicspath` 覆盖到的路径中

### 5.2 TikZ / 单独 `.tex` 图的处理方式

如果正文引用的是：

- 单独生成的 PDF 图
- 由外部 `.tex` 生成的图

则必须先确认对应 PDF 已生成，例如：

- `C4-10_EdgeMIFormer_Arch.pdf`
- `C4-11_KD_Framework.pdf`

不要直接假设 `.tex` 图源会被主文档自动编译。

### 5.3 不要把无关旧图重新引回正文

当前项目中已有一组与本论文无关的旧 `C5-*` 图素材，已归档至：

- `99_Archive/Unused_Thesis_Figures/2026-03-29_Original_Chap05`

编译排障时不要把这些旧图重新搬回 `01_Thesis_LaTeX/figures/`，除非用户明确要求恢复对应研究线。

## 6. 参考文献相关注意事项

### 6.1 责任边界

项目协作默认约定中：

- `refs.bib` 的系统性维护由 Antigravity 负责
- 但排障时仍应优先判断是“缺条目”还是“编译链错了”

### 6.2 正确处理顺序

如果参考文献显示异常，应按以下顺序排查：

1. 是否使用了标准编译命令 `cmd /c makepdf.bat`
2. 是否新加了 `\cite{...}` 但 `refs.bib` 中无对应条目
3. 是否只是第一次编译尚未完成 `bibtex` 循环

不要为了引用显示异常，直接切换为 `biber` 或重构参考文献模板。

## 7. 协作场景下的编译守则

### 7.1 先看同步板，再动共享文件

如果编译问题涉及：

- `chap*.tex`
- `refs.bib`
- 章节图文件

应先查看：

- `00_AI_Management/_AI_SYNC_BOARD.md`

确认是否已有他人正在编辑相关文件。

### 7.2 先局部修复，再整篇编译

如果问题明显来自最近一次局部修改，建议优先：

1. 定位新改动附近的括号、环境、公式
2. 确认新图是否存在
3. 再执行整篇编译

不要在原因未明时连续改动多个章节，避免把单点错误扩大成多点错误。

## 8. 最实用的经验结论

### 8.1 当前项目里，编译最常见的真正故障源

按经验排序，通常是：

1. 新增公式或环境结构损坏
2. 新增图文件路径错误或文件未生成
3. 新增 `\cite` 缺条目
4. PDF 被占用导致误判
5. 把警告当失败

### 8.2 当前项目里，最应该避免的误操作

按危险程度排序，通常是：

1. 改 `thesis.tex`
2. 改 `.cls` / `.bst`
3. 自行切换到 `biber`
4. 把无关旧图重新塞回正文图目录
5. 在没有锁的情况下边改共享章节边编译

## 9. 给 Antigravity 的一句话版

如果只是想记住最关键的规则，可以浓缩成这一句：

> 一律在 `01_Thesis_LaTeX` 目录下用 `cmd /c makepdf.bat` 编译；先查最近改动和图文件，再看日志中的真正致命错误；不要改模板、不要切 `biber`、不要把 PDF 占用和 Underfull 警告误判成编译失败。
