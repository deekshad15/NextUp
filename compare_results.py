import csv
import json
import re
from pathlib import Path

folder = Path(__file__).parent / "syllabi"

with (folder / "ENTR200_ground_truth.csv").open(
    encoding="utf-8-sig", newline=""
) as file:
    expected = list(csv.DictReader(file))

actual = json.loads(
    (folder / "ENTR200_ai_response.txt").read_text(encoding="utf-8")
)["items"]


def item_key(title, event_kind):
    title = title.lower()

    if "questionnaire" in title:
        return "questionnaire"

    project = re.search(r"project\s*#?\s*(\d+)", title)
    if project:
        return f"project-{project.group(1)}-{event_kind.lower()}"

    module = re.search(r"module\s*(\d+)", title)
    quiz = re.search(r"quiz\s*(\d+)", title)

    if "quiz" in title:
        if module:
            return f"quiz-module-{module.group(1)}"
        if quiz:
            return f"quiz-module-{quiz.group(1)}"

    return None


for row in expected:
    key = item_key(row["Item Title"], row["Event Kind"])

    matches = [
        item for item in actual
        if key is not None
        and item_key(item["title"], item["event_kind"]) == key
    ]

    if len(matches) != 1:
        print(f"{key}: cannot compare, found {len(matches)} matches")
        continue

    item = matches[0]

    fields = {
        "Due Date": "due_date",
        "Due Time": "due_time",
        "Timezone": "timezone"
    }

    for column, field in fields.items():
        expected_value = row[column].strip() or None
        actual_value = item.get(field)

        if isinstance(actual_value, str):
            actual_value = actual_value.strip() or None

        if expected_value != actual_value:
            print(
                f"{key} | {column}: "
                f"expected {expected_value!r}, "
                f"got {actual_value!r}"
            )

print("\nAI item titles:")
for item in actual:
    print(f"{item['title']} | {item['event_kind']}")