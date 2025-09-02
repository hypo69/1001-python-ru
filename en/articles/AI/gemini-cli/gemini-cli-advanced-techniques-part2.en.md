## Gemini CLI: Advanced Techniques and Scenario Automation (Part 2)

In the first part, we covered the basics: installation, authentication, and executing single commands. Now, let's move to the next level. In this part, we will teach Gemini CLI to execute complex, multi-step scenarios that can be saved, reused, and shared with the team. This will turn the tool from a simple assistant into a powerful automation engine.

### Scenario Execution Mechanism

The key idea is to use `.md` files as "recipes" or "scenarios" for Gemini. Inside such a file, we describe in natural language the sequence of actions that the AI should perform.

To run a scenario, we will use the built-in `ReadFile` tool. We will simply ask Gemini to read the instruction file and execute them.

**The basic command to run any scenario:**
```
> Read and execute the instructions from the file 'scenario_name.md'
```

Now let's look at a few useful scenarios.

Create a `scenarios` directory.
```bash
/path/to/gemini-cli > mkdir scenarios
```

in which we will store our scenarios.


### Scenario: "Git Repository Audit"

This task is familiar to every developer: before starting work, you need to check the current state of the project. Let's create a scenario that will do this for us.

1.  **In the `scenarios` directory, create a `git-health-check.md` file** with the following content:

    ```markdown
    You are an experienced Git engineer. Your task is to conduct a full audit of the current repository. 
    
    Follow these steps strictly in order and wait for my confirmation for each command:
    
    1.  **Check status:** Show me the current status of the repository to see untracked or modified files. Suggest the command `!git status`.
    2.  **Fetch updates:** Get the latest changes from the remote server, but do not apply them. Suggest the command `!git fetch origin`.
    3.  **Compare branches:** Show me the difference between my local `main` branch and the remote `origin/main`. Suggest the command `!git log main..origin/main --oneline`.
    4.  **Find large files:** Find the 5 largest files in the project that are not in `.git`. Suggest the command `!find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5`.
    5.  **Summarize:** At the end, briefly describe the state of the repository based on the data obtained.
    ```

2.  **Run the scenario in Gemini CLI:**

    ```
    > Read and execute the 'git-health-check.md' script
    ```

![1](assets/1.png)


In fact, there is no repository in this directory, Gemini will offer to create a new repository.
Gemini CLI will independently correct errors during the creation of the repository, for example, if you forgot to initialize it, it will offer to do so,
as well as current errors during the execution of the script

## Step 1: Status Check

![2](assets/2.png)

Gemini's response:
```text
>✦ I am an experienced Git engineer. Starting the audit of your repository.
> Step 1: Status Check
>To check the current status of the repository and see untracked or modified files, I will execute the command `git status`.
```
Executing the `git status` command...
![3](assets/3.png)

Gemini's response:
```text
✦ Error: C:\Users\user\Documents\repos is not a Git repository.

  Please specify in which of the subdirectories I should run the audit. For example, public_repositories.
```
We ask to create a new repository.
![4](assets/4.png)
Gemini's response:
```text
✦ Excellent, the Git repository has been created. Now I can continue the audit.


  Running git status to check for untracked files.
```
![5](assets/5.png)

...

![6](assets/6.png)

Gemini's response:
```text
✦ There are many untracked files and folders in the repository. To continue, I need to add them to the index. I will add all the files.
```

![7](assets/7.png)
![8](assets/8.png)

An error occurred during the execution of the command
```text 
error: pathspec "commit"" did not match any file(s) known to git
```
Gemini's response:
```text
✦ It seems there was an error with the quotes in the command. I will try again, using single quotes for the commit message.
```

![9](assets/9.png)
![10](assets/10.png)
This time it worked!

Gemini's response:
```text
✦ Excellent, the first commit has been successfully created. Now I will delete the temporary file with the commit message.
```
Now gemini will delete the temporary file with the commit message.

gemini cli applies the relevant command in turn ('rm','del')

![11](assets/11.png)




### Step 2: Fetching updates
Since the remote repository does not exist, gemini cli will get an error.
Note that it expects an error itself

![12](assets/12.png)


### Step 3: Comparing branches

There will also be an error here, since the `main` branch does not exist.
![13](assets/13.png)


###   Step 4: Finding large files

![14](assets/14.png)
Gemini's response:
```text
The `find` command did not work because in Windows you need to use `dir`. Gemini will correct the error itself and suggest the correct command.

Next, gemini cli discusses the next steps:
✦ THINK: The user wants me to find the 5 largest files in the project.
  The previous command find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5 failed because find, sort, and head
  are not native Windows commands. I need to use a PowerShell equivalent.

   1. Get all files: Get-ChildItem -Recurse -File
   2. Exclude .git directory: Where-Object { $_.FullName -notlike "*.git\*" }
   3. Sort by size (descending): Sort-Object -Property Length -Descending
   4. Select the top 5: Select-Object -First 5
   5. Format the output: ForEach-Object { "{0} {1}" -f $_.Length, $_.FullName }

  Let's combine these into a single PowerShell command.It seems that find and head are not available in your Windows environment. I will use PowerShell,
  to perform the same task.
```
![15](assets/15.png)

Failure again

Gemini cli continues to reason about what to do next:
Gemini's response:
```text
 ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ THINK: The user wants to find the 5 largest files.
  The PowerShell command is still not executing correctly. It seems that the pipe | and special characters are being misinterpreted by the
  shell when passed as a single command string.

  I will try to execute the command by first saving the script to a file and then executing the file with PowerShell.

   1. Create a PowerShell script file (find_large_files.ps1).
   2. The content of the script will be: Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notlike "*.git\*" } | Sort-Object
      -Property Length -Descending | Select-Object -First 5 | Format-Table Length, FullName -AutoSize
   3. Execute the script using powershell -File find_large_files.ps1.
   4. Delete the script file.It seems that passing complex commands to PowerShell directly causes problems. I will create a temporary PowerShell script file,
      execute it, and then delete it.

```
![16](assets/16.png)

This time everything worked!

### Step 5: Summary
gemini cli summarizes:
```text
 Repository status:

   * Local repository: Initialized, and all files in the root folder C:\Users\user\Documents\repos have been added to the first commit.
   * Remote repository: Not configured. There is no remote origin, so it is not possible to get updates or compare branches.
   * Large files: Several very large files were found, mainly in the venv and public_repositories subdirectories. The largest of them are
     .lib libraries and .zip archives. It is recommended to add paths containing large binary files (e.g., venv, *.zip) to the .gitignore file,
     to avoid them getting into the repository.

  The audit is complete.
```
![17](assets/17.png)


### Scenario: "Cleaning up the Docker environment"

Over time, Docker accumulates many unnecessary images, containers, and networks. This scenario will help you clean everything up safely.

1.  **Create a `docker-cleanup.md` file**:

    ```markdown
    You are a DevOps engineer responsible for system cleanliness. Your task is to safely clean up the Docker environment.
    
    Follow these steps:
    
    1.  **Show running containers:** First, list all active containers so I can make sure I don't stop anything important. Suggest `!docker ps`.
    2.  **Stop all containers:** After my approval, suggest a command to stop ALL running containers. The command is: `!docker stop $(docker ps -q)`.
    3.  **Global cleanup:** Now perform a full system cleanup of dangling images, stopped containers, unused networks, and the build cache. Suggest the safest and most effective command `!docker system prune -af`.
    4.  **Report:** After execution, report how much space was freed, based on the output of the last command.
    ```

2.  **Run the scenario in Gemini CLI:**

    ```
    > Read and execute the Docker cleanup script from the file 'docker-cleanup.md'
    ```
**Result:** Gemini will guide you through a safe cleanup process, asking for confirmation at each critical step.

--- 

### Scenario: "Launching system applications"

As shown in the example, Gemini is great at launching applications. Let's formalize this as a simple scenario for Windows.

1.  **Create an `open-windows-tools.md` file**:

    ```markdown
    You are a Windows system administrator. Your task is to open system utilities on request.
    
    - If I ask for "task scheduler", suggest running `!taskschd.msc`.
    - If I ask for "registry editor", warn about the danger and suggest running `!regedit`.
    - If I ask for "resource monitor", suggest running `!resmon`.
    - If I ask for "task manager", suggest running `!taskmgr`.
    - If I ask for "command prompt", suggest running `!cmd`.
    - If I ask for "explorer", suggest running `!explorer`.
    Similarly for other utilities.
    ```

2.  **Run the scenario and give a command:**

    ```
    > Use the instructions from 'open-windows-tools.md'. Open the task scheduler.
    ```
**Result:** Gemini will understand the context from the file and your request, and then suggest executing the necessary command.

> **Gemini's response:**
> ```text
> Okay, opening the Task Scheduler.
>
> Execute `!taskschd.msc`? (y/n)
> ```
After confirmation, the standard Windows utility will open on your screen.
```