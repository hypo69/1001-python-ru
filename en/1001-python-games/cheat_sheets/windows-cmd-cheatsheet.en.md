## **1. File and Directory Management:**

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
        *   `attrib -r myfile.txt`: Remove the "read-only" attribute from `myfile.txt`.
        *   `attrib *.*`: Display attributes of all files in the current directory.

*   **`cd` or `chdir`**: Changes the current directory.
    *   **Syntax:** `cd [path]` or `chdir [path]`
    *   **Options:**
        *   `..`: Go to the parent directory.
        *   `\`: Go to the root of the drive.
    *   **Examples:**
        *   `cd Documents`: Go to the `Documents` folder in the current directory.
        *   `cd C:\Users\User\Downloads`: Go to the `Downloads` folder on drive C.
        *   `cd ..`: Go to the parent directory.
        *   `cd \`: Go to the root of the current drive.

*   **`copy`**: Copies one or more files.
    *   **Syntax:** `copy [source_file] [destination_file]`
    *   **Options:**
        *  `/a` - Copy ASCII file
        *  `/b` - Copy binary file
        *  `/v` - Verify that files were copied correctly
    *   **Examples:**
        *   `copy myfile.txt mycopy.txt`: Copy `myfile.txt` to `mycopy.txt`.
        *   `copy *.txt C:\Backup`: Copy all files with the `.txt` extension to the `C:\Backup` folder.

*   **`del` or `erase`**: Deletes one or more files.
    *   **Syntax:** `del [filename]` or `erase [filename]`
    *   **Options:**
        *   `/p`: Prompt for confirmation before deleting each file.
        *   `/f`: Delete "read-only" files.
        *   `/s`: Delete files from subdirectories.
        *   `/q` - Delete files without prompting.
    *   **Examples:**
        *   `del myfile.txt`: Delete `myfile.txt`.
        *   `del *.tmp`: Delete all files with the `.tmp` extension.
        *   `del /f /s *.log` - Delete all files with the .log extension in the current directory and all subdirectories, without confirmation.

*   **`dir`**: Displays a list of files and directories in the current directory.
    *   **Syntax:** `dir [path] [options]`
    *   **Options:**
        *   `/a`: Display all files (including hidden ones).
        *   `/w`: Display the list in wide format.
        *   `/p`: Display the list page by page.
        *   `/s`: Output files from subdirectories as well.
        *   `/b` - Output only the filename.
    *   **Examples:**
        *   `dir`: Display a list of files and directories in the current directory.
        *   `dir C:\Users\User\Documents /a`: Display all files in the `Documents` directory.
        *   `dir /w`: Display a list of files and directories in the current directory in wide format.
         *   `dir /b /s *.txt`: Show all *.txt files with full path.

*   **`mkdir` or `md`**: Creates a new directory.
    *   **Syntax:** `mkdir [path]` or `md [path]`
    *   **Examples:**
        *   `mkdir NewFolder`: Create a new folder `NewFolder` in the current directory.
        *   `mkdir C:\Backup`: Create a new folder `Backup` on drive `C`.

*   **`move`**: Moves one or more files or directories.
    *   **Syntax:** `move [source_file] [destination_file]`
    *   **Examples:**
        *   `move myfile.txt C:\Documents`: Move `myfile.txt` to the `C:\Documents` folder.
        *  `move dir1 dir2` - Move folder `dir1` to folder `dir2`.

*  **`rd` or `rmdir`**: Deletes a directory.
    *   **Syntax:** `rd [path]` or `rmdir [path]`
    *   **Options:**
         *   `/s`: Delete a directory with all its subdirectories.
        *   `/q` - Delete a directory without prompting.
    *   **Examples:**
        *   `rd myfolder`: Delete an empty folder `myfolder`.
        *  `rd /s /q myfolder` - Delete folder `myfolder` with all its contents without prompting.

*   **`ren` or `rename`**: Renames a file or directory.
    *   **Syntax:** `ren [old_name] [new_name]`
    *   **Examples:**
        *   `ren myfile.txt newfile.txt`: Rename `myfile.txt` to `newfile.txt`.

*   **`type`**: Displays the contents of a text file.
    *   **Syntax:** `type [filename]`
    *   **Example:** `type myfile.txt`: Display the contents of `myfile.txt`.

*   **`xcopy`**: Copies files and directories (including subdirectories).
    *   **Syntax:** `xcopy [source] [destination] [options]`
    *   **Options:**
        *   `/s`: Copy directories and subdirectories (except empty ones).
        *   `/e`: Copy directories and subdirectories (including empty ones).
        *   `/i`: If the destination does not exist, create it.
        *   `/y`: Suppress prompt for confirmation of overwrite.
        *  `/d` - Copy only new files.
    *   **Examples:**
        *   `xcopy C:\Source D:\Destination /s`: Copy directory `C:\Source` to all subdirectories in `D:\Destination`.
        *   `xcopy C:\Source D:\Destination /e /y`: Copy directory `C:\Source` to all subdirectories in `D:\Destination`, including empty ones and without prompting for overwrite.

**2. Working with Drives:**

*   **`diskpart`**: Launches a utility for managing disks (partitions, volumes).
    *   **Syntax:** `diskpart`
    *   **Notes:**
        *   `diskpart` is an interactive utility that has its own set of commands.
        *   Administrator privileges are required to use it.
        *   You can learn more about using `diskpart` with the `help` command within this utility.
*   **`format`**: Formats a drive.
    *   **Syntax:** `format [drive:] [options]`
    *   **Options:**
        *  `/q` - Quick format.
        *  `/fs:file-system` - Select file system type (e.g., NTFS, FAT32).
    *   **Examples:**
        *   `format D: /q`: Quick format of drive D:.
        *   `format E: /fs:NTFS`: Format drive E: to NTFS file system.
    *   **Warning:** Formatting a drive deletes all data on it!
*   **`label`**: Sets or changes a drive label.
    *   **Syntax:** `label [drive:][label]`
    *   **Examples:**
        * `label D: NewLabel` - Set label on drive D to NewLabel.
        * `label D:` - Clear label from drive D.

**3. System Management:**

*   **`cls`**: Clears the command prompt screen.
    *   **Syntax:** `cls`
*   **`date`**: Displays or changes the current date.
    *   **Syntax:** `date [new_date]`
    *   **Examples:**
        *   `date`: Display the current date.
        *   `date 12-25-2024`: Change the date to December 25, 2024.
*   **`exit`**: Exits the command prompt.
    *   **Syntax:** `exit`
*   **`shutdown`**: Shuts down or restarts the computer.
    *   **Syntax:** `shutdown [options]`
    *   **Options:**
        *   `/s`: Shut down the computer.
        *   `/r`: Restart the computer.
        *   `/a`: Abort shutdown or restart.
        *  `/t xxx` - Delay in seconds before shutdown or restart.
    *   **Examples:**
        *   `shutdown /s /t 60`: Shut down the computer in 60 seconds.
        *   `shutdown /r`: Restart the computer.
        *   `shutdown /a`: Abort scheduled shutdown or restart.
*   **`tasklist`**: Displays a list of running processes.
    *   **Syntax:** `tasklist [options]`
    *  `/v` - More information.
    *  `/fo csv` - Output in CSV format.
    *  `/fi "imagename eq notepad.exe"` - Find all notepad processes.
    *   **Examples:**
        *   `tasklist`: Show a list of running processes.
        *   `tasklist /v`: Show a list of running processes with detailed information.

*   **`taskkill`**: Terminates a process.
    *   **Syntax:** `taskkill [options]`
    *   **Options:**
         * `/im imagename` - Terminate process by name.
        *   `/pid pid` - Terminate process by ID.
        *   `/f` - Forcefully terminate process.
     *   **Examples:**
        *   `taskkill /im notepad.exe`: Terminate all processes named `notepad.exe`.
        *   `taskkill /pid 1234`: Terminate process with ID 1234.
        *  `taskkill /im notepad.exe /f` - Forcefully terminate all `notepad.exe` processes.
*   **`time`**: Displays or changes the current time.
    *   **Syntax:** `time [new_time]`
    *   **Examples:**
        *   `time`: Display the current time.
        *   `time 15:30`: Set the time to 15:30.
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
        *   `/renew`: Request a new IP address.
    *   **Examples:**
        *   `ipconfig`: Display basic network configuration.
        *   `ipconfig /all`: Display full information about all network adapters.
        * `ipconfig /release` - Release IP address.
        * `ipconfig /renew` - Request a new IP address.
*   **`ping`**: Sends an echo request to another computer on the network.
    *   **Syntax:** `ping [hostname_or_ip_address] [options]`
     *  `-n xxx` - Number of requests.
     *  `-t` - Ping indefinitely.
    *   **Examples:**
        *   `ping google.com`: Ping the `google.com` server.
        *   `ping 192.168.1.100`: Ping a computer with IP address `192.168.1.100`.
        *  `ping google.com -n 10` - Perform 10 pings.
*   **`tracert`**: Displays the path of packets to another computer on the network.
    *   **Syntax:** `tracert [hostname_or_ip_address]`
    *   **Example:** `tracert google.com`: Display the path of packets to `google.com`.
*   **`netstat`**: Displays network connections.
    *   **Syntax:** `netstat [options]`
    *   **Options:**
         *   `-a`: Shows all connections.
        *   `-b`: Shows applications that created connections.
    *   **Examples:**
        * `netstat` - Show all active connections.
        * `netstat -a -b` - Show all connections and running applications that opened them.

*   **`nslookup`**: Queries DNS information.
    *   **Syntax:** `nslookup [hostname]`
    *   **Example:** `nslookup google.com`: Query DNS information for `google.com`.

**5. Other commands:**

*   **`assoc`**: Displays or changes file associations.
    *   **Syntax:** `assoc [.extension]=[file_type]`
    *   **Examples:**
        *   `assoc .txt`: Display the file type for the `.txt` extension.
        *   `assoc .txt=txtfile`: Set the file type for the `.txt` extension to `txtfile`.
*   **`call`**: Calls one batch file from another.
    *   **Syntax:** `call [batch_file_name]`
    *   **Example:** `call mybatch.bat`: Call the batch file `mybatch.bat`.
*   **`chcp`**: Changes the console code page.
    *   **Syntax:** `chcp [code_page_number]`
    *   **Examples:**
        *   `chcp 1251`: Set the code page for Cyrillic.
        *   `chcp`: Display the current code page.
*   **`choice`**: Allows the user to choose from a list of options.
    *   **Syntax:** `choice [/c [options]] [/n] [/t [seconds]] [/d [option]] [text]`
    *   **Options:**
        *   `/c`: Specifies available options.
        *   `/n`: Hides the list of available options.
        *   `/t`: Sets the timeout (in seconds).
        *   `/d`: Sets the default option.
    *   **Example:** `choice /c yn /t 10 /d n "Do you really want to exit?"
*   **`find`**: Searches for a text string in a file.
    *   **Syntax:** `find "string" [filename]`
    *   **Examples:**
        *  `find "Hello" myfile.txt` - searches for the string "Hello" in the file myfile.txt.

*   **`findstr`**: Searches for text strings in files (more powerful than `find`).
    *   **Syntax:** `findstr [options] "string" [filename]`
    *   **Options:**
         *  `/i` - Case-insensitive search.
        *   `/n` - Output line numbers.
        *   `/s` - Search in all subdirectories.
    *   **Examples:**
        *   `findstr /i "error" myfile.log`: Searches for the string "error" (case-insensitive) in `myfile.log`.
        * `findstr /n "error" *.log` - searches for the string "error" in all .log files, and shows line numbers.

*   **`gpupdate`**: Updates group policies.
    *   **Syntax:** `gpupdate [options]`
    *   **Options:**
         *  `/force` - Force update.
    *   **Example:** `gpupdate /force` - Force update group policies.
*   **`help` or `/?`**: Displays help for a command.
    *   **Syntax:** `help [command_name]` or `[command_name] /?`
    *   **Example:** `help dir` or `dir /?`: Display help for the `dir` command.
*   **`pause`**: Pauses batch file execution and waits for a key press.
    *   **Syntax:** `pause`
*  **`path`**: Displays or changes PATH environment variables.
   *   **Syntax**: `path [path]`
   *   **Examples**: 
         *  `path`: Show the current value of the PATH variable.
        *  `path C:\bin` - Add folder C:\bin to the PATH variable.
*   **`prompt`**: Configures the command prompt string.
    *   **Syntax:** `prompt [text]`
    *   **Examples:**
        *   `prompt $p$g`: Set the prompt string for the current path.
        *   `prompt MyPrompt>`: Set the prompt string to `MyPrompt>`.
*   **`set`**: Displays, sets, or deletes environment variables.
    *   **Syntax:** `set [name=[value]]`
    *   **Examples:**
        *   `set`: Display all environment variables.
        *   `set myvar=myvalue`: Set environment variable `myvar` to `myvalue`.
        *   `set myvar=`: Delete environment variable `myvar`.
*   **`start`**: Launches a program or opens a file.
    *   **Syntax:** `start [program_or_file_name] [options]`
    *   **Examples:**
        *   `start notepad.exe`: Launch Notepad.
        *   `start myfile.txt`: Open `myfile.txt` with the default program.
        *   `start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"` - Open website in Chrome.
*   **`tree`**: Displays the graphical directory structure.
    *   **Syntax:** `tree [drive:][path] [options]`
    *   **Options:**
        * `/f`: Also output filenames.
        * `/a` - Use ASCII characters.
    *   **Examples:**
         *   `tree` - Show the structure of the current directory.
         *   `tree /f` - Show the structure of the current directory with files.

*   **`where`**: Finds the location of a file.
    *   **Syntax:** `where notepad.exe`

**6. Commands for working with batch files:**

*   **`echo`**: Displays text on the screen.
    *   **Syntax:** `echo [text]`
    *  `echo on` - Enable command display when executing a batch file.
    *  `echo off` - Disable command display when executing a batch file.
    *   **Examples:**
        *   `echo Hello, world!`: Display "Hello, world!".
        *   `echo off` - Disable command output.
        *  `echo on` - Enable command output.
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
*   **`if`**: Executes conditional logic.
    *   **Syntax:** `if [not] condition (command1) else (command2)`
    *   **Examples:**
         * `if exist file.txt echo file exists` - Check for file existence.
         * `if %var%== "text" echo variable has value` - Check for variable value.
*  **`for`**: Executes a loop action.
  * **Syntax:** `for %%variable in (set) do [command]`
  * **Example:**
        ```batch
        for %%a in (*.txt) do (
         echo %%a
         type %%a
         echo -------------
        )
       ```
       * Display the name of each `.txt` file and its content.

**Warning:**
*   Be careful when using commands that can modify the system, especially when used with administrator privileges.
*   Before executing the `format` command, make sure you have selected the correct drive.
