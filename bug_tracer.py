# bug_tracer.py
import os
from dotenv import load_dotenv
from utils.git_helper import get_recent_commits, format_commit_diffs
from utils.ai_helper import generate_bug_fix_summary

load_dotenv()


def main():
    repo_path = input("Enter path to git repo: ")
    bug_description = input("Describe the bug: ")

    # Fetch the recent commits from the Git repository
    commits = get_recent_commits(repo_path)

    # Format the commits
    commits_text = format_commit_diffs(commits)

    # Ask the AI to analyze the commits and bug description
    result = generate_bug_fix_summary(bug_description, commits_text)

    # Print AI's analysis
    print("\n🧠 AI Analysis:\n")
    print(result)


if __name__ == "__main__":
    main()
