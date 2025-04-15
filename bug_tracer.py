from dotenv import load_dotenv
from utils.git_helper import get_recent_commits, format_commit_diffs
from utils.ai_helper import generate_bug_fix_summary
from colorama import Fore, Style, init

load_dotenv()

# Initialize colorama
init(autoreset=True)


def apply_color_tags(text):
    """
    This function will parse the color tags and replace them with corresponding colorama color codes.
    """
    color_map = {
        "[CYAN]": Fore.CYAN,
        "[GREEN]": Fore.GREEN,
        "[YELLOW]": Fore.YELLOW,
        "[RED]": Fore.RED,
        "[WHITE]": Fore.WHITE,
        "[BOLD]": Style.BRIGHT,
        "[RESET]": Style.RESET_ALL,
    }

    for tag, color in color_map.items():
        text = text.replace(tag, color)

    return text


def main():
    repo_path = input("Enter path to git repo: ")
    bug_description = input("Describe the bug: ")

    # Fetch the recent commits from the Git repository
    commits = get_recent_commits(repo_path)

    # Format the commits
    commits_text = format_commit_diffs(commits)

    # Ask the AI to analyze the commits and bug description
    result = generate_bug_fix_summary(bug_description, commits_text)

    # Apply color tags to the AI result
    formatted_result = apply_color_tags(result)

    # Print formatted output

    print(
        Fore.YELLOW
        + "\n============== AI BUG TRACER =============="
        + Style.RESET_ALL
        + "\n"
    )
    print(formatted_result)
    print(
        Fore.YELLOW + "\n==========================================\n" + Style.RESET_ALL
    )


if __name__ == "__main__":
    main()
