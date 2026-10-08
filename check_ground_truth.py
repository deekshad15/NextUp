import csv
from pathlib import Path

path = Path(__file__).parent / "syllabi" / "ENTR200_ground_truth.csv"

expected_headers = [
    "Syllabus ID", "Item Title", "Type", "Event Kind",
    "Due Date", "Due Time", "Timezone", "Grade Weight (%)",
    "Candidate Dates", "Source Pages", "Notes"
]

with path.open(encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
    headers = next(reader, [])
    rows = [
        (number, row)
        for number, row in enumerate(reader, start=2)
        if any(cell.strip() for cell in row)
    ]

print("Headers correct:", headers == expected_headers)
print("Number of items:", len(rows))

problems = []

for number, row in rows:
    if len(row) != 11:
        problems.append(
            f"Row {number}: expected 11 columns, found {len(row)}"
        )
    elif not all(row[index].strip() for index in range(4)):
        problems.append(f"Row {number}: missing an identifying field")

if problems:
    for problem in problems:
        print(problem)
else:
    print("All rows have 11 columns and identifying fields.")

for number, row in rows[:3]:
    print(
        f"Row {number}: date={row[4]!r}, "
        f"time={row[5]!r}, timezone={row[6]!r}"
    )