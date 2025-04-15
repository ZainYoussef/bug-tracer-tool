# utils/ai_helper.py
import os
import requests
import json


def generate_bug_fix_summary(bug_desc, commits_text):
    """Send the bug description and recent commits to the AI model."""
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"

    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"answer this problem in one sentence. Bug Report: {bug_desc}\n\nRecent Commits:\n{commits_text}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        try:
            response_data = response.json()
            print("\nFull JSON parsed response:")
            print(json.dumps(response_data, indent=4))

            if response_data and "candidates" in response_data:
                return response_data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return "Error: Unexpected response format from the AI API."
        except json.JSONDecodeError:
            print("Error: Failed to parse response as JSON.")
            return "Error: Response is not valid JSON."

    else:
        print(f"Error: Received status code {response.status_code} from the API.")
        print(f"Raw response content: {response.text}")
        return "Error: Could not analyze the data."
