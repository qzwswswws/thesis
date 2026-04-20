from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W_NS)


def w_tag(name: str) -> str:
    return f"{{{W_NS}}}{name}"


BASE_DIR = Path(r"C:\Users\qzwsw\Documents\thesis")
DOCX_PATH = next(BASE_DIR.glob("*ACAIT2025*.docx"))


def get_or_create(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(tag)
    if child is None:
        child = ET.SubElement(parent, tag)
    return child


def set_paragraph_format(paragraph: ET.Element, *, align: str | None, line: str | None) -> None:
    ppr = get_or_create(paragraph, w_tag("pPr"))

    if line is not None:
        spacing = ppr.find(w_tag("spacing"))
        if spacing is None:
            spacing = ET.SubElement(ppr, w_tag("spacing"))
        spacing.set(w_tag("line"), line)
        spacing.set(w_tag("lineRule"), "auto")

    if align is not None:
        jc = ppr.find(w_tag("jc"))
        if jc is None:
            jc = ET.SubElement(ppr, w_tag("jc"))
        jc.set(w_tag("val"), align)


def set_run_format(run: ET.Element, *, size: str) -> None:
    rpr = get_or_create(run, w_tag("rPr"))

    rfonts = rpr.find(w_tag("rFonts"))
    if rfonts is None:
        rfonts = ET.SubElement(rpr, w_tag("rFonts"))
    rfonts.set(w_tag("ascii"), "Times New Roman")
    rfonts.set(w_tag("hAnsi"), "Times New Roman")
    rfonts.set(w_tag("cs"), "Times New Roman")
    rfonts.set(w_tag("eastAsia"), "\u5b8b\u4f53")

    for size_tag in ("sz", "szCs"):
        size_node = rpr.find(w_tag(size_tag))
        if size_node is None:
            size_node = ET.SubElement(rpr, w_tag(size_tag))
        size_node.set(w_tag("val"), size)


def format_document(xml_bytes: bytes) -> bytes:
    root = ET.fromstring(xml_bytes)
    body = root.find(w_tag("body"))
    if body is None:
        raise RuntimeError("Missing Word body node.")

    paragraphs = [node for node in body.findall(w_tag("p"))]
    if len(paragraphs) < 6:
        raise RuntimeError(f"Expected at least 6 paragraphs, found {len(paragraphs)}.")

    body_paragraphs = paragraphs[1:]
    signature_paragraphs = paragraphs[-3:]

    for paragraph in body_paragraphs:
        set_paragraph_format(paragraph, align=None, line="360")
        for run in paragraph.findall(w_tag("r")):
            set_run_format(run, size="28")

    for paragraph in signature_paragraphs:
        set_paragraph_format(paragraph, align="right", line="360")

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main() -> None:
    with ZipFile(DOCX_PATH, "r") as source:
        document_xml = format_document(source.read("word/document.xml"))
        styles_xml = source.read("word/styles.xml")
        file_map = {name: source.read(name) for name in source.namelist()}

    file_map["word/document.xml"] = document_xml
    file_map["word/styles.xml"] = styles_xml

    with NamedTemporaryFile(delete=False, suffix=".docx", dir=str(DOCX_PATH.parent)) as tmp:
        tmp_path = Path(tmp.name)

    with ZipFile(tmp_path, "w", compression=ZIP_DEFLATED) as target:
        for name, data in file_map.items():
            target.writestr(name, data)

    tmp_path.replace(DOCX_PATH)
    print(DOCX_PATH)


if __name__ == "__main__":
    main()
