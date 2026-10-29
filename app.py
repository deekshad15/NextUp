from pathlib import Path
from tempfile import TemporaryDirectory

from flask import Flask, render_template, request

from extract_pdf import extract_pdf
from parse_syllabus import parse_syllabus

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("syllabus")

    if not file or not file.filename:
        return "Please choose a PDF.", 400

    if not file.filename.lower().endswith(".pdf"):
        return "Please upload a PDF file.", 400

    try:
        with TemporaryDirectory() as folder:
            path = Path(folder) / "syllabus.pdf"
            file.save(path)
            text = extract_pdf(path)
    except Exception:
        app.logger.exception("PDF extraction failed")
        return "This PDF could not be read. Try another file.", 400

    try:
        items = parse_syllabus(text)
    except Exception:
        app.logger.exception("AI extraction failed")
        return (
            "Assignment extraction failed. Return to the homepage "
            "and try again. See the terminal for error details.",
            502
        )

    items.sort(
        key=lambda item: (
            item["due_date"] is None,
            item["due_date"] or "",
            item["due_time"] or "",
            item["title"]
        )
    )

    review_count = sum(
        1 for item in items
        if not item["due_date"]
        or not item["due_time"]
        or not item["timezone"]
        or item["candidate_dates"]
    )

    return render_template(
        "review.html",
        items=items,
        filename=file.filename,
        review_count=review_count
    )


@app.errorhandler(413)
def too_large(error):
    return "Please choose a PDF smaller than 10 MB.", 413


if __name__ == "__main__":
    app.run(port=5001, debug=True)