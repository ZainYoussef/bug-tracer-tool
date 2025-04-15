from git import Repo


def get_recent_commits(repo_path, n=5):
    """
    Fetch the recent commits from the Git repository.
    """
    repo = Repo(repo_path)
    commits = list(repo.iter_commits("main", max_count=n))
    return [
        (commit.hexsha, commit.message, commit.diff(create_patch=True))
        for commit in commits
    ]


def format_commit_diffs(commits):
    """
    Format the commit diffs into a readable summary.
    """
    commit_summaries = []
    for sha, msg, diff in commits:
        diffs = "\n".join(
            d.diff.decode("utf-8", errors="ignore") for d in diff if d.diff
        )
        commit_summaries.append(f"Commit: {sha}\nMessage: {msg}\nDiff:\n{diffs}\n---")
    return "\n\n".join(commit_summaries)
