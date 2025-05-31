import os
import requests
import json


def load_prompt_template():
    """Load the bug analysis prompt template from file."""
    try:
        with open("prompts/analysis_prompt.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(
            "Bug analysis prompt template not found. Please ensure 'prompts/bug_analysis_prompt.txt' exists."
        )
    except Exception as e:
        raise Exception(f"Error loading prompt template: {str(e)}")


def generate_bug_fix_summary(bug_desc, commits_text):
    """Send the bug description and recent commits to the AI model."""
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"

    headers = {
        "Content-Type": "application/json",
    }

    # Load the prompt template and format with the actual data
    try:
        prompt_template = load_prompt_template()
        formatted_prompt = prompt_template.format(
            bug_desc=bug_desc, commits_text=commits_text
        )
    except Exception as e:
        return f"Error loading prompt template: {str(e)}"

    data = {"contents": [{"parts": [{"text": formatted_prompt}]}]}

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
