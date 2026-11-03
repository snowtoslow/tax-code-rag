"""Parse a PDF (local path or URL) with Docling and export Markdown + JSON."""

import argparse
import json
from pathlib import Path

from docling.document_converter import DocumentConverter


def parse_pdf(source: str):
    converter = DocumentConverter()
    result = converter.convert(source)
    return result.document


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse a PDF with Docling")
    parser.add_argument("source", help="Path or URL of the PDF")
    parser.add_argument("-o", "--out-dir", type=Path, default=Path("output"))
    args = parser.parse_args()

    doc = parse_pdf(args.source)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(args.source).stem or "document"

    md_path = args.out_dir / f"{stem}.md"
    json_path = args.out_dir / f"{stem}.json"

    md_path.write_text(doc.export_to_markdown(), encoding="utf-8")
    json_path.write_text(
        json.dumps(doc.export_to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Markdown: {md_path}")
    print(f"JSON:     {json_path}")


if __name__ == "__main__":
    main()