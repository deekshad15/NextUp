SYLLABUS_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "type": {
                        "type": "string",
                        "enum": ["exam", "homework", "quiz", "project"]
                    },
                    "event_kind": {
                        "type": "string",
                        "enum": ["submission", "presentation", "exam", "quiz"]
                    },
                    "due_date": {"type": ["string", "null"]},
                    "due_time": {"type": ["string", "null"]},
                    "timezone": {"type": ["string", "null"]},
                    "grade_weight_percent": {
                        "type": ["number", "null"]
                    },
                    "candidate_dates": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "source_pages": {
                        "type": "array",
                        "items": {"type": "integer"}
                    },
                    "notes": {"type": "string"}
                },
                "required": [
                    "title", "type", "event_kind", "due_date",
                    "due_time", "timezone", "grade_weight_percent",
                    "candidate_dates", "source_pages", "notes"
                ],
                "additionalProperties": False
            }
        }
    },
    "required": ["items"],
    "additionalProperties": False
}