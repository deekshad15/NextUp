# NextUp

NextUp is a student productivity project that turns course syllabi into structured assignments and deadlines. The goal is to help students organize their coursework and eventually add confirmed deadlines to Google Calendar.

## Project Status

NextUp is currently an early Python prototype. It can extract text from a PDF, send that text to Purdue GenAI Studio, and validate the structure of the AI response.

There is no user interface or Google Calendar integration yet.

## Current Features

- Connects to Purdue GenAI Studio using a private API key.
- Extracts PDF text with PyMuPDF.
- Uses `gpt-oss:120b` to identify assignments, quizzes, exams, and presentations.
- Requests structured JSON using a defined schema.
- Validates required fields and data types with `jsonschema`.
- Supports unresolved deadlines and lists possible dates for review.

## How It Works

1. A syllabus PDF is stored locally.
2. PyMuPDF extracts its text.
3. Purdue GenAI Studio identifies coursework and deadline information.
4. A validator checks the response against the schema.
5. The extracted information is manually reviewed for accuracy.

Schema validation checks the output format. It does not guarantee that dates are correct or that every assignment was found.

## Technologies

- Python
- Purdue GenAI Studio
- PyMuPDF
- Requests
- python-dotenv
- jsonschema

## Project Files

| File | Purpose |
| --- | --- |
| `test_genai.py` | Tests API access and a simple AI response |
| `extract_pdf.py` | Extracts text from the test syllabus |
| `parse_syllabus.py` | Sends extracted text to the AI |
| `syllabus_schema.py` | Defines the expected response structure |
| `validate_output.py` | Validates the saved AI response |
| `evaluation_notes.md` | Records findings and known issues |
| `requirements.txt` | Lists Python dependencies |

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/deekshad15/NextUp.git
cd NextUp
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API access

Get an API key from your Purdue GenAI Studio account.

Create a `.env` file in the project root:

```text
GENAI_API_KEY=your_actual_api_key
```

The `.env` file is excluded from Git. Never commit an API key.

### 5. Test the connection

```bash
python test_genai.py
```

### 6. Add a syllabus and run the prototype

Create a `syllabi` folder in the project root and place your PDF inside it.

The scripts currently use the filename `ENTR200 Syllabus.pdf`. To use a different filename, update the paths in `extract_pdf.py`, `parse_syllabus.py`, and `validate_output.py`.

Run these commands in order:

```bash
python extract_pdf.py
python parse_syllabus.py
python validate_output.py
```

Extracted text and AI responses are saved in `syllabi/`.

## Initial Findings

Testing has started with one ENTR 200 syllabus.

- Text extraction initially mixed class dates with assignment deadlines.
- Extracting text blocks improved the reading order for the inspected section.
- The AI identified a genuine conflict between two Project 1 deadlines.
- The latest inspected response kept alternative presentation dates in one item.
- All 17 items in that response passed schema validation.

Full accuracy and completeness have not yet been evaluated. Findings are recorded in `evaluation_notes.md`.

## Known Limitations

- Scripts currently use fixed filenames for one syllabus.
- Scanned PDFs and OCR are not supported yet.
- Other layouts and departments have not been tested.
- Dates, timezones, and grade weights still require manual review.
- Conflicting or ambiguous dates require student confirmation.
- Model responses can vary between runs.

## Next Steps

- Collect 15–20 syllabi across departments and course levels.
- Hand-label 3–5 syllabi to create an evaluation dataset.
- Compare PDF extraction libraries and add support for scans.
- Compare Purdue GenAI Studio with a second provider.
- Measure extraction accuracy, response time, and cost.
- Integrate validation into the parsing workflow.
- Add Google Calendar authorization and event creation.
- Build a review interface before exporting deadlines.

## Data Handling

API keys, syllabus PDFs, extracted text, and AI responses are excluded from Git.

PDF text extraction runs locally. Running `parse_syllabus.py` sends the extracted syllabus text to Purdue GenAI Studio.
