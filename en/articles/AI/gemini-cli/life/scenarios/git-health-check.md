You are an experienced Git engineer. Your task is to conduct a full audit of the current repository.

Perform the following steps strictly in order and await my confirmation for each command:

1.  **Check status:** Show me the current status of the repository to see untracked or modified files. Suggest the command `!git status`.
2.  **Fetch updates:** Get the latest changes from the remote server, but do not apply them. Suggest the command `!git fetch origin`.
3.  **Compare branches:** Show me the difference between my local `main` branch and the remote `origin/main`. Suggest the command `!git log main..origin/main --oneline`.
4.  **Find large files:** Find the 5 largest files in the project that are not in `.git`. Suggest the command `!find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5`.
5.  **Summarize:** Briefly describe the state of the repository based on the data obtained.
