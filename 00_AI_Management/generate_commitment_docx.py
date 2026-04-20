from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


OUTPUT_PATH = Path(r"C:\Users\qzwsw\Documents\thesis\承诺书_ACAIT2025_模板.docx")


def xml_text(text: str) -> str:
    return escape(text, {"'": "&apos;", '"': "&quot;"})


def make_run(text: str, *, bold: bool = False, size: int = 24) -> str:
    props = [f"<w:sz w:val=\"{size}\"/>", f"<w:szCs w:val=\"{size}\"/>"]
    if bold:
        props.append("<w:b/>")
    return (
        "<w:r>"
        f"<w:rPr>{''.join(props)}</w:rPr>"
        f"<w:t xml:space=\"preserve\">{xml_text(text)}</w:t>"
        "</w:r>"
    )


def make_paragraph(
    text: str = "",
    *,
    align: str | None = None,
    bold: bool = False,
    indent_chars: int | None = None,
    spacing_after: int | None = None,
    size: int = 24,
) -> str:
    paragraph_props: list[str] = []
    if align:
        paragraph_props.append(f"<w:jc w:val=\"{align}\"/>")
    if indent_chars is not None:
        paragraph_props.append(f"<w:ind w:firstLineChars=\"{indent_chars}\"/>")
    if spacing_after is not None:
        paragraph_props.append(f"<w:spacing w:after=\"{spacing_after}\"/>")
    ppr = f"<w:pPr>{''.join(paragraph_props)}</w:pPr>" if paragraph_props else ""
    run = make_run(text, bold=bold, size=size)
    return f"<w:p>{ppr}{run}</w:p>"


def build_document_xml(paragraphs: list[str]) -> str:
    body = "".join(paragraphs)
    sect_pr = (
        "<w:sectPr>"
        "<w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1800\" w:bottom=\"1440\" w:left=\"1800\" "
        "w:header=\"851\" w:footer=\"992\" w:gutter=\"0\"/>"
        "<w:cols w:space=\"425\"/>"
        "<w:docGrid w:linePitch=\"312\"/>"
        "</w:sectPr>"
    )
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" "
        "xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" "
        "xmlns:o=\"urn:schemas-microsoft-com:office:office\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
        "xmlns:v=\"urn:schemas-microsoft-com:vml\" "
        "xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" "
        "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "xmlns:w10=\"urn:schemas-microsoft-com:office:word\" "
        "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" "
        "xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" "
        "xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" "
        "xmlns:wne=\"http://schemas.microsoft.com/office/word/2006/wordml\" "
        "xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" "
        "mc:Ignorable=\"w14 wp14\">"
        f"<w:body>{body}{sect_pr}</w:body>"
        "</w:document>"
    )


def build_styles_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="宋体" w:cs="Times New Roman"/>
        <w:lang w:val="en-US" w:eastAsia="zh-CN"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault/>
  </w:docDefaults>
</w:styles>
"""


def build_content_types_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


def build_root_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


def build_document_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""


def build_core_xml() -> str:
    created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:dcmitype="http://purl.org/dc/dcmitype/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>承诺书 ACAIT2025 模板</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{created}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{created}</dcterms:modified>
</cp:coreProperties>
"""


def build_app_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
  xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
"""


paragraphs = [
    make_paragraph("承诺书", align="center", bold=True, spacing_after=300, size=32),
    make_paragraph(
        "本人[姓名]，学号[学号]，智能科学学院[系别]系[专业名称]专业硕士研究生。",
        indent_chars=200,
        spacing_after=120,
    ),
    make_paragraph(
        "本人论文《Efficient Transformer-Based Motor Imagery Classification for Edge-Deployed Brain-Computer Interfaces》已于2025年8月14日收到 2025 Asian Conference on Artificial Intelligence Technology（ACAIT 2025）的正式录用通知，论文编号为 ACAIT2025-270。",
        indent_chars=200,
        spacing_after=120,
    ),
    make_paragraph(
        "本人为该论文第[作者排序]作者，[单位名称]为第[单位排序]完成单位。该论文目前处于会议论文集出版流程中，尚未完成正式出版及图书馆检索收录。",
        indent_chars=200,
        spacing_after=120,
    ),
    make_paragraph(
        "由于录用时间较晚，当前图书馆检索系统尚未收录，特此说明。本人及导师承诺以上信息真实有效，并承诺该文章将在一年内完成正式刊出或网络在线发表。如有伪造或与事实不符之处，本人及导师自愿承担相应责任。",
        indent_chars=200,
        spacing_after=240,
    ),
    make_paragraph("承诺人：", spacing_after=200),
    make_paragraph("导师：", spacing_after=200),
    make_paragraph("日期：      年      月      日", spacing_after=0),
]


document_xml = build_document_xml(paragraphs)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(OUTPUT_PATH, "w", compression=ZIP_DEFLATED) as docx:
    docx.writestr("[Content_Types].xml", build_content_types_xml())
    docx.writestr("_rels/.rels", build_root_rels_xml())
    docx.writestr("docProps/core.xml", build_core_xml())
    docx.writestr("docProps/app.xml", build_app_xml())
    docx.writestr("word/document.xml", document_xml)
    docx.writestr("word/styles.xml", build_styles_xml())
    docx.writestr("word/_rels/document.xml.rels", build_document_rels_xml())

print(OUTPUT_PATH)
