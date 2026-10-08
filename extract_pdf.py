from pathlib import Path
import pymupdf
import sys


def extract_pdf(path):
    pages = []

    with pymupdf.open(path) as document:
        for number, page in enumerate(document, start=1):
            blocks = page.get_text("blocks", sort=False)
            text = "\n\n".join(
                block[4].strip()
                for block in blocks
                if block[6] == 0 and block[4].strip()
            )
            pages.append(f"--- Page {number} ---\n{text.strip()}")

    return "\n\n".join(pages)


if __name__ == "__main__":
    folder = Path(__file__).parent / "syllabi"

    if len(sys.argv) != 2:
        raise SystemExit(
            'Usage: python extract_pdf.py "TDM101 Syllabus.pdf"'
        )

    pdf_path = folder / sys.argv[1]
    text = extract_pdf(pdf_path)

    output = pdf_path.with_name(
        pdf_path.stem + "_extracted.txt"
    )
    output.write_text(text, encoding="utf-8")

    print(f"Saved extracted text to: {output.name}")