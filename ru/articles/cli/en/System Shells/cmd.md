# cmd

## Category: System Shells

### Purpose: Classic Windows command prompt.

### Introduction
The Windows Command Prompt (`cmd.exe`) is a command-line interpreter for Windows operating systems. It allows users to execute commands to perform various tasks, manage files and directories, configure system settings, and more. It provides a text-based interface for interacting with the operating system.

### Important Commands and Examples

Here are some essential `cmd` commands and their usage:

#### 1. `dir` - Display a list of files and subdirectories

The `dir` command displays a list of files and subdirectories within a specified directory.

```cmd
dir [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N] [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4]
```

**Flags/Parameters**:
*   `/A[[:]attributes]`: Displays files with specified attributes.
    *   `D`: Directories
    *   `R`: Read-only files
    *   `H`: Hidden files
    *   `A`: Files ready for archiving
    *   `S`: System files
    *   `I`: Not content indexed files
    *   `L`: Reparse Points
    *   `O`: Offline files
    *   `-`: Prefix meaning "not" (e.g., `/A:-H` to exclude hidden files).
*   `/B`: Uses bare format (no heading information or summary), listing only the directory name or file name and extension.
*   `/S`: Displays files in the specified directory and all subdirectories.
*   `/P`: Pauses after each screenful of information.
*   `/O[[:]sortorder]`: Sorts the output.
    *   `N`: Alphabetically by name.
    *   `E`: Alphabetically by extension.
    *   `S`: By size, smallest first.
    *   `D`: By date/time, oldest first.
    *   `G`: Group directories first.
    *   `-`: Prefix to reverse the sort order.
*   `/W`: Uses wide list format.
*   `/?`: Displays help for the command.

**Examples**:
*   `dir`: Lists files and directories in the current directory.
*   `dir /S`: Lists all files and subdirectories in the current directory and its subdirectories.
*   `dir *.txt`: Lists all files with a `.txt` extension in the current directory.
*   `dir /A:H`: Lists hidden files.
*   `dir /S /B *.log > logs.txt`: Finds all `.log` files in the current directory and subdirectories, lists them in bare format, and redirects the output to `logs.txt`.

**Success Conditions**:
*   The command executes and displays the requested directory listing.
*   No error messages are displayed.
*   The command typically returns an exit code of `0`.

**Failure Conditions**:
*   "File Not Found": If the specified path or filename pattern does not exist.
*   "Access is denied.": If you do not have the necessary permissions to access the directory.
*   If the output is redirected to a file and the directory for the output file does not exist, it might result in a "File creation error."

#### 2. `copy` - Copy one or more files

The `copy` command duplicates one or more files from one location to another.

```cmd
copy [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B] source [/A | /B] [+ source [/A | /B] [+ ...]] [destination [/A | /B]] [/?]
```

**Flags/Parameters**:
*   `source`: Specifies the file(s) to copy. Wildcards (`*`, `?`) can be used.
*   `destination`: Specifies the directory and/or filename for the new file(s).
*   `/V`: Verifies that new files are written correctly.
*   `/Y`: Suppresses confirmation prompts to overwrite an existing destination file.
*   `/-Y`: Forces prompting to confirm overwriting an existing destination file.
*   `/A`: Indicates an ASCII text file.
*   `/B`: Indicates a binary file.
*   `/Z`: Copies files in restartable mode, useful for large files over a network.
*   `/?`: Displays help for the command.

**Examples**:
*   `copy file.txt C:\backup`: Copies `file.txt` from the current directory to `C:\backup`.
*   `copy *.doc C:\reports /V`: Copies all `.doc` files from the current directory to `C:\reports` and verifies the copy.
*   `copy C:\source\file1.txt + C:\source\file2.txt C:\destination\combined.txt`: Combines `file1.txt` and `file2.txt` into `combined.txt`.
*   `copy D:\readme.htm`: Copies `readme.htm` from the D: drive to the current directory.

**Success Conditions**:
*   The file(s) are copied to the destination without error messages.
*   A message like "1 file(s) copied." is displayed.
*   The `ERRORLEVEL` is `0`.

**Failure Conditions**:
*   "The system cannot find the file specified.": If the source file does not exist.
*   "Access is denied.": If you do not have write permissions to the destination directory or read permissions for the source file.
*   "There is not enough space on the disk.": If the destination drive is full.
*   If `/V` is used and verification fails, an error message will appear.
*   `ERRORLEVEL` will be non-zero (e.g., `1` for general failure).

#### 3. `ping` - Verify IP-level connectivity

The `ping` command sends Internet Control Message Protocol (ICMP) echo request messages to a target host to verify IP-level connectivity.

```cmd
ping [/t] [/a] [/n count] [/l size] [/f] [/i TTL] [/v TOS] [/r count] [/s count] [{/j hostlist | /k hostlist}] [/w timeout] [/R] [/S srcaddr] [/4] [/6] targetname
```

**Flags/Parameters**:
*   `targetname`: Specifies the host name or IP address of the destination.
*   `/t`: Pings the specified host until interrupted (Ctrl+C to stop, Ctrl+Break to display statistics).
*   `/a`: Resolves addresses to hostnames.
*   `/n count`: Specifies the number of echo requests to send (default is 4).
*   `/l size`: Specifies the size of the send buffer in bytes (default is 32).
*   `/w timeout`: Specifies the timeout in milliseconds to wait for each reply (default is 4000ms).
*   `/?`: Displays help for the command.

**Examples**:
*   `ping google.com`: Pings `google.com` four times.
*   `ping 192.168.1.1 -n 10`: Pings the IP address `192.168.1.1` ten times.
*   `ping localhost`: Pings the local machine.
*   `ping -t 8.8.8.8`: Continuously pings Google's DNS server until manually stopped.

**Success Conditions**:
*   "Reply from <IP address>": Indicates a successful response from the target.
*   "TTL=" in the output.
*   A summary showing "Packets: Sent = X, Received = X, Lost = 0 (0% loss)".
*   The command returns an exit code of `0`.

**Failure Conditions**:
*   "Request timed out.": The target did not respond within the specified timeout.
*   "Destination host unreachable.": No route to the destination host could be found.
*   "Ping request could not find host <hostname>. Please check the name and try again.": The hostname could not be resolved to an IP address (DNS issue).
*   "General failure.": Indicates a problem with the local network interface.
*   A summary showing "Packets: Sent = X, Received = Y, Lost = Z (Z% loss)" where Z > 0.
*   The command returns a non-zero exit code (e.g., `1` if the host is unreachable).

#### 4. `mkdir` (or `md`) - Create a directory

The `mkdir` command creates a new directory or subdirectory.

```cmd
mkdir [drive:]path
```

**Flags/Parameters**:
*   `[drive:]path`: Specifies the drive and path of the directory to create.
*   `/?`: Displays help for the command.
*   (Note: The `-p` flag for creating parent directories, common in Unix-like systems, is not a standard `cmd` flag. Command extensions in Windows allow creating intermediate directories in a specified path with a single `mkdir` command, effectively similar to `-p` in some cases).

**Examples**:
*   `mkdir new_folder`: Creates a directory named `new_folder` in the current directory.
*   `mkdir C:\projects\my_project`: Creates `my_project` inside `C:\projects`. If `C:\projects` doesn't exist, `cmd` with command extensions enabled will create it.
*   `md 