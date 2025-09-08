### How to Check and Fix Hard Drive Errors in Windows: CHKDSK and PowerShell Cheat Sheet

Over time, logical errors can accumulate on a hard drive or SSD, and damaged sectors may appear, leading to system slowdowns, program crashes, and even data loss. Fortunately, Windows has built-in tools for diagnosing and fixing such problems.

In this cheat sheet, I will show two ways to monitor disk states: the `chkdsk` utility and PowerShell commands.

### Part 1: CHKDSK Utility

**CHKDSK** (Check Disk) is a standard command-line utility that checks a volume's file system for logical and physical errors.

#### How to Run CHKDSK

To execute commands that make changes to the system, you will need administrator rights.

1.  Press `Win + S` or the "Start" button.
2.  Type `cmd` or "Command Prompt".
3.  In the search results, right-click on "Command Prompt" and select **"Run as administrator"**.

#### Main Parameters (Switches) of CHKDSK

The command has the following syntax: `chkdsk [drive:] [parameters]`

Frequently used parameters:

*   `chkdsk C:`
    Starts checking drive C: in "read-only" mode. The utility will report found errors but will not fix them.

*   **/f**
    Fixes errors on the disk. If there are open files on the disk (which is almost always the case for the system drive), the utility will offer to perform the check on the next system restart.
    *Example:* `chkdsk D: /f`

*   **/r**
    Locates bad sectors and attempts to recover readable information. This switch **includes the functionality of the `/f` switch**, so using them together is not strictly necessary, although not an error. A check with `/r` takes significantly longer.
    *Example:* `chkdsk D: /r`

*   **/x**
    Forces the volume to dismount before checking, if necessary. All open handles to this disk will become invalid. This switch also **includes the functionality of `/f`**.
    *Example:* `chkdsk D: /x`

*   **/b** (for NTFS file system only)
    Performs a re-evaluation of bad clusters on the disk. This switch is the most comprehensive, as it **includes the functionality of `/r`**.
    *Example:* `chkdsk C: /b`

*   **/scan** (for NTFS only)
    Runs an online scan of the volume. This means the disk does not need to be dismounted, and you can continue working on the system during the scan. However, fixing found problems will require the next switch or a restart.
    *Example:* `chkdsk C: /scan`

*   **/spotfix** (for NTFS only)
    Performs a pinpoint, very fast fix of errors on the volume. Requires dismounting the disk, just like the `/f` switch.
    *Example:* `chkdsk D: /spotfix`

#### Examples of Running CHKDSK

*   **Quick check of drive D: without fixing:**
    ```
    chkdsk D:
    ```

*   **Check and fix errors on drive D:**
    ```
    chkdsk D: /f
    ```

*   **Most comprehensive check of system drive C: with bad sector detection and recovery:**
    ```
    chkdsk C: /f /r
    ```
    *or simply:*
    ```
    chkdsk C: /r
    ```

#### What to do if the disk is in use?

When attempting to run a check with fixing (`/f` or `/r`) for the system drive (usually `C:`), you will see a message:

`Cannot run CHKDSK because the specified volume is in use by another process. Would you like to schedule this volume to be checked the next time the system restarts? (Y/N)`

Press `Y`, then `Enter`. The check will be scheduled and will automatically start on the next computer restart.

---

### Part 2: PowerShell Commands

PowerShell is an automation shell that offers modern and flexible commands for system management.

#### How to Run PowerShell

As with the Command Prompt, you will need administrator rights.

1.  Press `Win + S` or the "Start" button.
2.  Type `powershell`.
3.  In the search results, right-click on "Windows PowerShell" and select **"Run as administrator"**.

#### Main Command: `Repair-Volume`

In PowerShell, the `Repair-Volume` cmdlet is used to check and fix disks.

First, it might be useful to view a list of all volumes on the system using the command:
```powershell
Get-Volume
```

#### Main Parameters of `Repair-Volume`

*   `-DriveLetter`
    Specifies the drive letter to check.

*   `-Scan`
    Scans the volume for errors and reports them. This is analogous to `chkdsk` without switches.
    *Example:* `Repair-Volume -DriveLetter D -Scan`

*   `-SpotFix`
    Performs a quick online fix without the need to dismount the volume for a long time. Analogous to `chkdsk /spotfix`.
    *Example:* `Repair-Volume -DriveLetter D -SpotFix`

*   `-OfflineScanAndFix`
    Performs a full disk check and fix offline. This is the most complete analogue of the `chkdsk /f /r` command. The system will prompt for a restart if the volume is in use.
    *Example:* `Repair-Volume -DriveLetter C -OfflineScanAndFix`

#### PowerShell Examples

*   **Scan drive C: for errors (without fixing):**
    ```powershell
    Repair-Volume -DriveLetter C -Scan
    ```
    You will see the result in the `HealthStatus` field (e.g., `Healthy` or `Needs-Repair`).

*   **Perform a quick fix for drive D:**
    ```powershell
    Repair-Volume -DriveLetter D -SpotFix
    ```

*   **Schedule a full check and fix for system drive C: on the next restart:**
    ```powershell
    Repair-Volume -DriveLetter C -OfflineScanAndFix
    ```
    PowerShell, like `chkdsk`, will notify you of the need for a restart and schedule the task.


For most users, the result of `chkdsk C: /r` and `Repair-Volume -DriveLetter C -OfflineScanAndFix` will be the same. The choice depends on your preferences and tasks.

**Important note:** Before performing any serious disk operations, especially if you suspect physical problems, **always back up important data!** Tools can fix errors, but they cannot guarantee 100% data integrity on a damaged medium.