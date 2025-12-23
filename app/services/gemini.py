import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def ask_gemini(prompt: str) -> str:
    url = f"{BASE_URL}?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    res = requests.post(url, json=data, headers=headers)
    res.raise_for_status()

    body = res.json()
    return body["candidates"][0]["content"]["parts"][0]["text"]
