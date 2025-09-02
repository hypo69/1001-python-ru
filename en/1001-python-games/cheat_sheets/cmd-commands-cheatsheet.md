**1. File and directory management:**

*   **`attrib`**: Displays or changes file or directory attributes (hidden, read-only, archive, etc.).
    *   **Syntax:** `attrib [+r|-r] [+a|-a] [+s|-s] [+h|-h] [drive:][path]filename`
    *   **Options:**
        *   `+r`: Set "read-only" attribute
        *   `-r`: Clear "read-only" attribute
        *   `+a`: Set "archive" attribute
        *   `-a`: Clear "archive" attribute
        *   `+s`: Set "system" attribute
        *   `-s`: Clear "system" attribute
        *   `+h`: Set "hidden" attribute
        *   `-h`: Clear "hidden" attribute
    *   **Examples:**
        *   `attrib +h myfile.txt`: Make `myfile.txt` hidden.
        *   `attrib -r myfile.txt`: Clear "read-only" attribute from `myfile.txt`.
        *   `attrib *.*`: Display attributes of all files in the current directory.

*   **`cd` or `chdir`**: Changes the current directory.
    *   **Syntax:** `cd [path]` or `chdir [path]`
    *   **Options:**
        *   `..`: Go to parent directory.
        *   `\`: Go to root of drive.
    *   **Examples:**
        *   `cd Documents`: Go to `Documents` folder in the current directory.
        *   `cd C:\Users\User\Downloads`: Go to `Downloads` folder on drive C.
        *   `cd ..`: Go to parent directory.
        *   `cd \`: Go to root of current drive.

*   **`copy`**: Copies one or more files.
    *   **Syntax:** `copy [source_file] [destination_file]`
    *   **Options:**
        *  `/a` - Copy ASCII file
        *  `/b` - Copy binary file
        *  `/v` - Verify that files were copied correctly
    *   **Examples:**
        *   `copy myfile.txt mycopy.txt`: Copy `myfile.txt` to `mycopy.txt`.
        *   `copy *.txt C:\Backup`: Copy all files with `.txt` extension to `C:\Backup` folder.

*   **`del` or `erase`**: Deletes one or more files.
    *   **Syntax:** `del [filename]` or `erase [filename]`
    *   **Options:**
        *   `/p`: Prompt for confirmation before deleting each file.
        *   `/f`: Force delete read-only files.
        *   `/s`: Delete files from subdirectories.
        *   `/q` - Delete files without prompting.
    *   **Examples:**
        *   `del myfile.txt`: Delete `myfile.txt`.
        *   `del *.tmp`: Delete all files with `.tmp` extension.
        *   `del /f /s *.log` - delete all files with .log extension in the current directory and all subdirectories, without confirmation

*   **`dir`**: Displays a list of files and directories in the current directory.
    *   **Syntax:** `dir [path] [options]`
    *   **Options:**
        *   `/a`: Display all files (including hidden).
        *   `/w`: Display list in wide format.
        *   `/p`: Display list page by page.
        *   `/s`: Display files from subdirectories as well
        *   `/b` - Display only filename
    *   **Examples:**
        *   `dir`: Display list of files and directories in the current directory.
        *   `dir C:\Users\User\Documents /a`: Display all files in `Documents` directory.
        *   `dir /w`: Display list of files and directories in the current directory in wide format.
         *   `dir /b /s *.txt`: Show all *.txt files with full path.

*   **`mkdir` or `md`**: Creates a new directory.
    *   **Syntax:** `mkdir [path]` or `md [path]`
    *   **Examples:**
        *   `mkdir NewFolder`: Create a new folder `NewFolder` in the current directory.
        *   `mkdir C:\Backup`: Create a new folder `Backup` on drive `C`.

*   **`move`**: Moves one or more files or directories.
    *   **Syntax:** `move [source_file] [destination_file]`
    *   **Examples:**
        *   `move myfile.txt C:\Documents`: Move `myfile.txt` to `C:\Documents` folder.
        *  `move dir1 dir2` - Move `dir1` folder to `dir2` folder

*  **`rd` or `rmdir`**: Deletes a directory.
    *   **Syntax:** `rd [path]` or `rmdir [path]`
    *   **Options:**
         *   `/s`: Delete directory with all its subdirectories.
        *   `/q` - Delete directory without prompting.
    *   **Examples:**
        *   `rd myfolder`: Delete empty folder `myfolder`
        *  `rd /s /q myfolder` - delete `myfolder` folder with all its contents without prompting.

*   **`ren` or `rename`**: Renames a file or directory.
    *   **Syntax:** `ren [old_name] [new_name]`
    *   **Examples:**
        *   `ren myfile.txt newfile.txt`: Rename `myfile.txt` to `newfile.txt`.

*   **`type`**: Displays the content of a text file.
    *   **Syntax:** `type [filename]`
    *   **Example:** `type myfile.txt`: Display content of `myfile.txt`.

*   **`xcopy`**: Copies files and directories (including subdirectories).
    *   **Syntax:** `xcopy [source] [destination] [options]`
    *   **Options:**
        *   `/s`: Copy directories and subdirectories (except empty ones).
        *   `/e`: Copy directories and subdirectories (including empty ones).
        *   `/i`: If destination does not exist, create it.
        *   `/y`: Suppress confirmation prompt for overwriting.
        *  `/d` - Copy only new files
    *   **Examples:**
        *   `xcopy C:\Source D:\Destination /s`: Copy `C:\Source` directory to all subdirectories in `D:\Destination` folder.
        *   `xcopy C:\Source D:\Destination /e /y`: Copy `C:\Source` directory to all subdirectories in `D:\Destination` folder, including empty ones and without overwriting prompt.

**2. Disk management:**

*   **`diskpart`**: Launches disk management utility (partitions, volumes).
    *   **Syntax:** `diskpart`
    *   **Notes:**
        *   `diskpart` is an interactive utility that has its own set of commands.
        *   Administrator rights are required to use it.
        *   You can learn more about using `diskpart` with the `help` command within this utility.
*   **`format`**: Formats a disk.
    *   **Syntax:** `format [drive:] [options]`
    *   **Options:**
        *  `/q` - Quick format
        *  `/fs:file-system` - Choose file system type (e.g., NTFS, FAT32)
    *   **Examples:**
        *   `format D: /q`: Quick format of drive D:.
        *   `format E: /fs:NTFS`: Format drive E: to NTFS file system.
    *   **Warning:** Formatting a drive deletes all data on it!
*   **`label`**: Sets or changes a disk label.
    *   **Syntax:** `label [drive:][label]`
    *   **Examples:**
        * `label D: NewLabel` - Set label on drive D as NewLabel
        * `label D:` - Clear label from drive D

**3. System management:**

*   **`cls`**: Clears the command prompt screen.
    *   **Syntax:** `cls`
*   **`date`**: Displays or changes the current date.
    *   **Syntax:** `date [new_date]`
    *   **Examples:**
        *   `date`: Display current date.
        *   `date 12-25-2024`: Change date to December 25, 2024.
*   **`exit`**: Exits the command prompt.
    *   **Syntax:** `exit`
*   **`shutdown`**: Shuts down or restarts the computer.
    *   **Syntax:** `shutdown [options]`
    *   **Options:**
        *   `/s`: Shut down the computer.
        *   `/r`: Restart the computer.
        *   `/a`: Abort shutdown or restart.
        *  `/t xxx` - Delay in seconds before shutdown or restart
    *   **Examples:**
        *   `shutdown /s /t 60`: Shut down the computer in 60 seconds.
        *   `shutdown /r`: Restart the computer.
        *   `shutdown /a`: Abort scheduled shutdown or restart.
*   **`tasklist`**: Displays a list of running processes.
    *   **Syntax:** `tasklist [options]`
    *  `/v` - Additional information
    *  `/fo csv` - Output in CSV format
    *  `/fi "imagename eq notepad.exe"` - Find all notepad processes
    *   **Examples:**
        *   `tasklist`: Show list of running processes.
        *   `tasklist /v`: Show list of running processes with detailed information.

*   **`taskkill`**: Terminates a process.
    *   **Syntax:** `taskkill [options]`
    *   **Options:**
         * `/im imagename` - Terminate process by name
        *   `/pid pid` - Terminate process by ID
        *   `/f` - Force terminate process
     *   **Examples:**
        *   `taskkill /im notepad.exe`: Terminate all processes named `notepad.exe`.
        *   `taskkill /pid 1234`: Terminate process with ID 1234.
        *  `taskkill /im notepad.exe /f` - force terminate all `notepad.exe` processes
*   **`time`**: Displays or changes the current time.
    *   **Syntax:** `time [new_time]`
    *   **Examples:**
        *   `time`: Display current time.
        *   `time 15:30`: Set time to 15:30.
*   **`ver`**: Displays the operating system version.
    *   **Syntax:** `ver`
*   **`systeminfo`**: Displays detailed system information.
    *   **Syntax:** `systeminfo`

*   **`taskmgr`**: Launches Task Manager.
    *  **Syntax:** `taskmgr`

**4. Network:**

*   **`ipconfig`**: Displays network configuration.
    *   **Syntax:** `ipconfig [options]`
    *   **Options:**
        *   `/all`: Display full information about network adapters.
        *   `/release`: Release IP address.
        *   `/renew`: Request new IP address.
    *   **Examples:**
        *   `ipconfig`: Display basic network configuration.
        *   `ipconfig /all`: Display full information about all network adapters.
        * `ipconfig /release` - Release IP address
        * `ipconfig /renew` - Request new IP address
*   **`ping`**: Sends an echo request to another computer on the network.
    *   **Syntax:** `ping [hostname_or_ip_address] [options]`
     *  `-n xxx` - Number of requests
     *  `-t` - Ping indefinitely
    *   **Examples:**
        *   `ping google.com`: Ping `google.com` server.
        *   `ping 192.168.1.100`: Ping computer with IP address `192.168.1.100`.
        *  `ping google.com -n 10` - Perform 10 pings
*   **`tracert`**: Displays the path of packets to another computer on the network.
    *   **Syntax:** `tracert [hostname_or_ip_address]`
    *   **Example:** `tracert google.com`: Display path of packets to `google.com`.
*   **`netstat`**: Displays network connections.
    *   **Syntax:** `netstat [options]`
    *   **Options:**
         *   `-a`: Shows all connections
        *   `-b`: Shows applications that created connections.
    *   **Examples:**
        * `netstat` - Show all active connections
        * `netstat -a -b` - Show all connections and running applications that opened them

*   **`nslookup`**: Queries DNS information.
    *   **Syntax:** `nslookup [hostname]`
    *   **Example:** `nslookup google.com`: Query DNS information for `google.com`.

**5. Other commands:**

*   **`assoc`**: Displays or changes file associations.
    *   **Syntax:** `assoc [.extension]=[file_type]`
    *   **Examples:**
        *   `assoc .txt`: Display file type for `.txt` extension.
        *   `assoc .txt=txtfile`: Set file type for `.txt` extension to `txtfile`.
*   **`call`**: Calls one batch file from another.
    *   **Syntax:** `call [batch_file_name]`
    *   **Example:** `call mybatch.bat`: Call `mybatch.bat` batch file.
*   **`chcp`**: Changes the console code page.
    *   **Syntax:** `chcp [code_page_number]`
    *   **Examples:**
        *   `chcp 1251`: Set code page for Cyrillic.
        *   `chcp`: Display current code page.
*   **`choice`**: Allows the user to choose from a list of options.
    *   **Syntax:** `choice [/c [options]] [/n] [/t [seconds]] [/d [option]] [text]`
    *   **Options:**
        *   `/c`: Specifies available options.
        *   `/n`: Hides the list of available options.
        *   `/t`: Specifies timeout (in seconds).
        *   `/d`: Specifies default option.
    *   **Example:** `choice /c yn /t 10 /d n "Do you really want to exit?"`
*   **`find`**: Searches for a text string in a file.
    *   **Syntax:** `find "string" [filename]`
    *   **Examples:**
        *  `find "Hello" myfile.txt` - searches for "Hello" in myfile.txt

*   **`findstr`**: Searches for text strings in files (more powerful than `find`).
    *   **Syntax:** `findstr [options] "string" [filename]`
    *   **Options:**
         *  `/i` - Case-insensitive search
        *   `/n` - Display line numbers
        *   `/s` - Search in all subdirectories
    *   **Examples:**
        *   `findstr /i "error" myfile.log`: Searches for "error" (case-insensitive) in `myfile.log`.
        * `findstr /n "error" *.log` - searches for "error" in all .log files, and shows line numbers

*   **`gpupdate`**: Updates group policies.
    *   **Syntax:** `gpupdate [options]`
    *   **Options:**
         *  `/force` - Force update
    *   **Example:** `gpupdate /force` - force update group policies
*   **`help` or `/?`**: Displays help for a command.
    *   **Syntax:** `help [command_name]` or `[command_name] /?`
    *   **Example:** `help dir` or `dir /?`: Display help for `dir` command.
*   **`pause`**: Pauses batch file execution and waits for a key press.
    *   **Syntax:** `pause`
*  **`path`**: Displays or changes PATH environment variables
   *   **Syntax**: `path [path]`
   *   **Examples**: 
         *  `path`: Show current PATH variable value
        *  `path C:\bin` - add C:\bin folder to PATH variable
*   **`prompt`**: Customizes the command prompt string.
    *   **Syntax:** `prompt [text]`
    *   **Examples:**
        *   `prompt $p$g`: Set prompt string to current path.
        *   `prompt MyPrompt>`: Set prompt string to `MyPrompt>`.
*   **`set`**: Displays, sets, or deletes environment variables.
    *   **Syntax:** `set [name=[value]]`
    *   **Examples:**
        *   `set`: Display all environment variables.
        *   `set myvar=myvalue`: Set `myvar` environment variable to `myvalue`.
        *   `set myvar=`: Delete `myvar` environment variable.
*   **`start`**: Launches a program or opens a file.
    *   **Syntax:** `start [program_or_file_name] [options]`
    *   **Examples:**
        *   `start notepad.exe`: Launch Notepad.
        *   `start myfile.txt`: Open `myfile.txt` with default program.
        *   `start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"` - Open website in Chrome
*   **`tree`**: Displays graphical directory structure.
    *   **Syntax:** `tree [drive:][path] [options]`
    *   **Options:**
        * `/f`: Also display filenames
        * `/a` - Use ASCII characters
    *   **Examples:**
         *   `tree` - Show current directory structure
         *   `tree /f` - Show current directory structure with files

*   **`where`**: Finds file location.
    *   **Syntax:** `where notepad.exe`

**6. Commands for working with batch files:**

*   **`echo`**: Displays text on screen.
    *   **Syntax:** `echo [text]`
    *  `echo on` - enable command display when executing batch file
    *  `echo off` - disable command display when executing batch file
    *   **Examples:**
        *   `echo Hello, world!`: Display "Hello, world!".
        *   `echo off` - disable command output
        *  `echo on` - enable command output
*   **`rem`**: Adds a comment to a batch file.
    *   **Syntax:** `rem [comment]`
    *   **Example:** `rem This is a comment`
*   **`goto`**: Jumps to a label.
    *   **Syntax:** `goto [label]`
    *   **Example:**
        ```batch
        :start
        echo Hello
        goto end
        echo This will not be displayed
        :end
        echo Goodbye
        ```
*   **`if`**: Performs conditional logic.
    *   **Syntax:** `if [not] condition (command1) else (command2)`
    *   **Examples:** 
         * `if exist file.txt echo file exists` - check for file existence
         * `if %var%== "text" echo variable has value` - check for variable value
*  **`for`**: Performs a loop
  * **Syntax:** `for %%variable in (set) do [command]`
  * **Example:**
        ```batch
        for %%a in (*.txt) do (
         echo %%a
         type %%a
         echo ------------- 
        )
       ```
       * Display each `.txt` file name and its content

**Warning:**
*   Be careful when using commands that can modify the system, especially when used with administrator privileges.
*   Before executing the `format` command, make sure you have selected the correct drive.
