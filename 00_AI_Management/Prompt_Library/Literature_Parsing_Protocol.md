# Literature Parsing Protocol (文献解析与协作规范)

当 AI 助手在 `03_Literature` 或对应暂存区中检测到新放入的文献时，**必须**严格遵循以下自动化处理流程（SOP）：

### Step 1: 格式嗅探与优先处理 (Format Sniffing)
1. **优先扫描** `.tex`, `.tar.gz`, `.zip` 文件。如果存在，立即解压并直接读取核心的 `.tex` 源码，跳过同名的 PDF 文件。
2. **其次扫描** `.html` 文件。使用 Python 的结构化文本提取脚本（如 BeautifulSoup）解析段落和表格。
3. **最后处理** `.pdf` 文件。如果仅存在 PDF，进入 Step 2。

### Step 2: 降级 PDF 智能解析策略 (Fallback PDF Parsing)
1. **轻量预览**：先使用系统命令 `pdftotext -layout <file.pdf>` 生成初步文本字典，快速定位 Abstract, Introduction, Conclusion。
2. **遇错即停**：如果发现提取的文本存在严重的双栏混行或大量的数学公式乱码（例如出现成排的不可读符号），**严禁**直接使用该文本生成长篇综述。
3. **脚本开路**：立即在后台编写并静默运行 Python 脚本（使用 `PyMuPDF` / `fitz` 库提取纯文本块，或使用专用的排版还原库），确保双栏文本的逻辑连贯性。

### Step 3: 信息提纯与输出 (Information Extraction)
- 在执行核心内容的撰写前，AI 必须基于解析出的准确文本，独立输出具有公式推导支撑和量化数据支撑的学术段落，并在注脚中明确标注文献引用（如 `[Wan23]`）。
