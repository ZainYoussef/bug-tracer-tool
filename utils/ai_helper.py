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
    # Prompt for the AI model to analyze the bug description and commit diffs,
    # and return a structured bug report using predefined color tags for CLI formatting.
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"""You are a code analysis AI. Given the following inputs:

Bug Description:
{bug_desc}

Commits:
{commits_text}

Analyze the above and output a structured bug report with the following format. Include color tags where appropriate.

Use the following color tags:
- [CYAN] for headers (sections)
- [GREEN] for fix-related information (steps, suggestions)
- [YELLOW] for important details or context
- [WHITE] for general text

Do not use any markdown or HTML notations. Only color tags should be used.
Avoid introductory sentences. Get straight to the point.
Use precise and concise language for each section.
Do not add any extra explanations or summaries.
Ensure each section is clearly defined and includes the appropriate information. If a section is not applicable, leave it out entirely (do not include empty or placeholder sections).

Follow the structure exactly as outlined below:

---

[CYAN] Bug Location:  
[WHITE]File name, function name, and line number if possible  

[CYAN] Bug Description:  
[WHITE]A concise description of the bug that occurred

[GREEN] Root Cause:  
[BOLD]The reasoning behind why the bug exists based on commits

[CYAN] Introduced In Commit:  
[WHITE]Commit hash, message, and timestamp  

[CYAN] How It Happened:  
[WHITE]Explanation of the logic or assumptions that caused the bug 

[CYAN] Fix Steps:  
[GREEN]1. Detailed steps to fix the bug 
[GREEN]2. Include any verification steps 

[CYAN] ✅ Suggested Patch:  
[GREEN]Here is the suggested code fix with highlighted changes 
[WHITE]Ensure the code follows good practices with formatting and proper comments  

Original code:
for i in range(len(items)):  # Off-by-one error in loop condition 
    total += items[i]

Suggested fix:
for i in range(len(items) - 1):  # Adjusted loop condition to exclude the last item 
    total += items[i]
[CYAN]---
"""
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        try:
            response_data = response.json()
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
