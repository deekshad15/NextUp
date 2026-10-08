from pathlib import Path
import pymupdf


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


folder = Path(__file__).parent / "syllabi"
text = extract_pdf(folder / "ENTR200 Syllabus.pdf")

output = folder / "ENTR200_extracted.txt"
output.write_text(text, encoding="utf-8")

print(f"Saved extracted text to: {output.name}")