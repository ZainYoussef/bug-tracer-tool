# Bug Trace and Analysis using AI

A command-line tool built with python that traces and analyzes recent Git commits along with a bug description to identify the root cause and suggest a fix using Google Gemini AI model.

---

## 🚀 Features:
- **Bug Location**: Identifies the specific file, function, and line where the bug occurs.
- **Bug Description**: Confirms the description of the bug or problem.
- **Root Cause**: Provides the underlying reason for the bug, based on code changes.
- **Introduced In Commit**: Displays the commit hash, message, and timestamp where the bug was introduced (if identifiable).
- **How It Happened**: Explains the logic or assumptions that led to the bug.
- **Fix Steps**: Suggests a step-by-step guide for fixing the bug.
- **Suggested Changes**: Recommends code modifications to resolve the issue.


**Note**: This tool analyzes the code to point out the problem but does not apply fixes in real-time. It analyzes the bug and offer suggestions on how to resolve it.


## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ZainYoussef/bug-tracer-tool
cd bug-tracer-tool
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory and add your Google Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Running the Program

Run the main script:

```bash
python bug_tracer.py
```

You will be prompted to:

- Enter the path to the Git repository (local Git repository)
- Describe the bug you're facing

The AI model will analyze the bug and generate a structured report with suggested fixes.

---

## 📦 Dependencies

- `colorama`
- `GitPython`
- `Requests`

⚠️ Limitations:
This tool may not perform well on large commits that contain a lot of changes or files. The current AI model has input length limitations, which means it can’t process very long commit histories or large diffs effectively.

To improve accuracy and handle larger data:

Use a more advanced AI model that supports longer context windows (e.g., Gemini 1.5 Pro or GPT-4 Turbo with extended context).

Break down large commits into smaller chunks and analyze them individually.

Or, adjust the git_helper logic to reduce the depth of recent commits fetched, minimizing the amount of data passed to the AI.


