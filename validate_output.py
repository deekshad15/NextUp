import json
from pathlib import Path

from jsonschema import validate, ValidationError
from syllabus_schema import SYLLABUS_SCHEMA

path = (
    Path(__file__).parent
    / "syllabi"
    / "ENTR200_ai_response.txt"
)

try:
    data = json.loads(path.read_text(encoding="utf-8"))
    validate(instance=data, schema=SYLLABUS_SCHEMA)
    print(f"Schema passed! Found {len(data['items'])} items.")
except json.JSONDecodeError as error:
    print("The response is not valid JSON:", error)
except ValidationError as error:
    print("Schema check failed:", error.message)
    print("Location:", list(error.absolute_path))