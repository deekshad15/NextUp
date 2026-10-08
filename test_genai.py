import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise SystemExit("Missing GENAI_API_KEY in your .env file.")

response = requests.get(
    "https://genai.rcac.purdue.edu/api/models",
    headers={"Authorization": f"Bearer {api_key}"},
    timeout=30,
)

print("Status:", response.status_code)

if response.ok:
    for model in response.json().get("data", []):
        print(model["id"])
else:
    print("The request failed. Check the status code above.")

print("\nAsking the AI...")

reply = requests.post(
    "https://genai.rcac.purdue.edu/api/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-oss:120b",
        "messages": [
            {
                "role": "user",
                "content": "Say hello to NextUp in one short sentence."
            }
        ],
        "stream": False
    },
    timeout=120,
)

print("Chat status:", reply.status_code)

if reply.ok:
    data = reply.json()
    if data and data.get("choices"):
        print(data["choices"][0]["message"]["content"])
    else:
        print("No answer returned. Try again in a minute.")
else:
    print("Chat request failed.")