**PowerShell Commands Guide**

**1. Basic Navigation and File/Directory Operations**

*   **`Get-ChildItem` (or `gci`, `ls`, `dir`)**: Gets a list of files and subdirectories in the specified location.
    *   **Syntax**: `Get-ChildItem [path] [parameters]`
    *   **Key parameters:**
        *   `-Path`: Specifies the path to the directory.
        *   `-Include`: Filters by file name (with wildcards `*` and `?`).
        *   `-Exclude`: Excludes files by name.
        *   `-Recurse`: Shows files and folders in all subdirectories.
        *   `-Force`: Show hidden files.
        *   `-File`: Show only files.
        *   `-Directory`: Show only folders.
    *   **Examples:**
        *   `Get-ChildItem`: List of files and folders in the current directory.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: List of files and folders in `C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: List only text files in the current directory.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: Show all directories on drive C.
        *  `Get-ChildItem -Force`: Show all files, including hidden ones.

*   **`Set-Location` (or `sl`, `cd`)**: Changes the current directory.
    *   **Syntax**: `Set-Location [path]`
    *   **Examples:**
        *   `Set-Location C:\Windows`: Go to the `C:\Windows` directory.
        *   `Set-Location ..`: Go to the parent directory.
        * `Set-Location /` - Go to the root of the drive.
*   **`New-Item`**: Creates a new file or directory.
    *   **Syntax**: `New-Item -Path [path] -ItemType [type] -Name [name]`
    *   **Key parameters:**
        *   `-ItemType`: `file` or `directory`.
        *   `-Name`: Name of the new item.
        *   `-Value`: Content of the file.
    *   **Examples:**
        *   `New-Item -ItemType directory -Name NewFolder`: Create a folder `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: Create an empty file `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: Create `myfile.txt` with content.

*  **`Remove-Item` (or `rm`, `del`, `erase`)**: Deletes files and directories.
    *   **Syntax:** `Remove-Item [path] [parameters]`
    *   **Key parameters:**
         *   `-Recurse`:  Delete all subdirectories.
        *   `-Force`: Force deletion (including read-only files and directories).
       *  `-Confirm` - Prompt for confirmation for each deletion.
    *   **Examples:**
        *   `Remove-Item myfile.txt`: Delete `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: Delete folder `C:\Temp` with all nested folders and files.

*   **`Copy-Item`**: Copies files and directories.
    *   **Syntax**: `Copy-Item [source_path] [destination_path] [parameters]`
    *   **Key parameters:**
        *   `-Recurse`: Copy all subdirectories.
        *   `-Force`: Overwrite existing files without prompting.
    *   **Examples:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: Copy `myfile.txt` to `mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: Copy folder `C:\Source` to all subdirectories in `D:\Backup` folder.

*   **`Move-Item`**: Moves files and directories.
    *   **Syntax**: `Move-Item [source_path] [destination_path] [parameters]`
      *  `-Force` - Force move and overwrite.

    *   **Examples:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: Move `myfile.txt` to `D:\Documents` folder.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: Move folder C:\MyFolder to D:\ forcibly, even if a folder with that name already exists there.

*   **`Rename-Item`**: Renames a file or directory.
    *   **Syntax**: `Rename-Item -Path [path] -NewName [new_name]`
    *   **Example:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: Rename `myfile.txt` to `newfile.txt`.

*   **`Get-Content` (or `gc`)**: Displays or gets the content of a file.
    *   **Syntax**: `Get-Content [path]`
    *   **Example:**
        *   `Get-Content myfile.txt`: Show content of `myfile.txt`.
*   **`Set-Content`**: Replaces or creates the content of a file.
    *  **Syntax:** `Set-Content [path] [parameters]`
        *  `-value` - text to write.
   *   **Example:** `Set-Content myfile.txt "New text"` - Replace content of `myfile.txt`.

*   **`Add-Content`**: Appends content to the end of a file.
   * **Syntax:** `Add-Content [path] [parameters]`
       *  `-value` - text to append.

   *   **Example:** `Add-Content myfile_file.txt "More text"` - Append text to the end of `myfile.txt`.

**2. Process Management:**

*   **`Get-Process` (or `gps`)**: Gets a list of running processes.
    *   **Syntax**: `Get-Process [parameters]`
    *   **Key parameters:**
        *   `-Name`: Filter by process name.
        *   `-Id`: Filter by process ID.
        *    `-IncludeUserName`: Display the user who started the process.
    *   **Examples:**
        *   `Get-Process`: List all running processes.
        *   `Get-Process -Name notepad`: List processes with name `notepad`.
        *    `Get-Process -IncludeUserName`: List all running processes with users.

*   **`Stop-Process`**: Terminates a process.
    *   **Syntax**: `Stop-Process [parameters]`
     *  `-Id` - Specify process ID.
    *   `-Name` - Specify process name.
    *  `-Force` - Force terminate process.
    *   **Examples:**
        *   `Stop-Process -Name notepad`: Terminate all `notepad` processes.
         *    `Stop-Process -Id 1234` : Terminate process with ID 1234.
        *    `Stop-Process -Name chrome -Force` : Force terminate all `chrome` processes.

**3. Service Management:**

*   **`Get-Service`**: Gets a list of services.
    *   **Syntax**: `Get-Service [parameters]`
    *   **Key parameters:**
         * `-Name`: Display only services with the specified name.
         * `-DisplayName`: Display only services with the specified display name.
        *   `-Status`: Filter by status (Running, Stopped).
    *   **Examples:**
        *   `Get-Service`: List all services.
        *   `Get-Service -Name Spooler`: Display Spooler service.
       *   `Get-Service -Status Running`: Show running services.
*  **`Start-Service`**: Starts a service.
   *   **Syntax**: `Start-Service [service_name]`
   *   **Example:** `Start-Service Spooler` - Start Spooler service.

*   **`Stop-Service`**: Stops a service.
    *   **Syntax**: `Stop-Service [service_name]`
        *  `-Force` - Force stop service.
    *   **Example:** `Stop-Service Spooler`: Stop Spooler service.
        *   `Stop-Service Spooler -Force` - Force stop Spooler service.

*  **`Restart-Service`**: Restarts a service.
   *   **Syntax:** `Restart-Service [service_name]`
   *   **Example:** `Restart-Service Spooler` - Restart Spooler service.

**4. Networking**

*   **`Test-NetConnection`**: Tests network connection.
    *   **Syntax**: `Test-NetConnection [hostname_or_ip_address] [parameters]`
    *  `-Port` - Port number.
    *   **Examples:**
        *   `Test-NetConnection google.com`: Test connection to `google.com`.
        * `Test-NetConnection google.com -Port 80`: Test connection to google.com on port 80.
*   **`Get-NetIPConfiguration`**: Gets network configuration.
    *   **Syntax**: `Get-NetIPConfiguration`
    *   **Example:**
        *   `Get-Net2IPConfiguration`: Display network configuration.
*   **`Resolve-DnsName`**: Queries DNS information.
    *   **Syntax**: `Resolve-DnsName [hostname]`
    *   **Example:** `Resolve-DnsName google.com`: Query DNS information for `google.com`.

**5. Registry Operations**

*   **`Get-ItemProperty`**: Gets a property value from the registry.
    *   **Syntax**: `Get-ItemProperty -Path [registry_path]`
    *   **Example:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: Sets a property value in the registry.
    *   **Syntax**: `Set-ItemProperty -Path [registry_path] -Name [property_name] -Value [value]`
    *   **Example:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. Other**

*   **`Clear-Host`**: Clears the console screen.
    *   **Syntax:** `Clear-Host`
*   **`Get-Date`**: Gets the current date and time.
    *   **Syntax:** `Get-Date`
*    **`Start-Process`**: Launches a program or opens a file.
    *   **Syntax:** `Start-Process [program_or_file_name] [options]`
   *   **Examples:**
        *   `Start-Process notepad.exe`: Launch Notepad.
        *   `Start-Process myfile.txt`: Open `myfile.txt` with default program.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - Open website in Chrome.

*   **`Get-Help`**: Shows help for a command.
    *   **Syntax**: `Get-Help [command_name]`
    *   **Example:** `Get-Help Get-Process`: Show help for `Get-Process` command.
*   **`Exit`**: Ends the PowerShell session.
    *   **Syntax:** `Exit`
*  **`Get-Variable`**: Shows current variables.
    *  **Syntax**: `Get-Variable`
*   **`Get-Alias`**: Shows command aliases.
    *   **Syntax**: `Get-Alias`
*   **`Set-Alias`**: Creates an alias for a command.
    *  **Syntax**: `Set-Alias [alias_name] [command_name]`
    *  **Example**: `Set-Alias gci Get-ChildItem`

**Notes:**

*   `PowerShell` commands (cmdlets) usually have the form `Verb-Noun` (e.g., `Get-Process`, `Set-Location`).
*   `PowerShell` is case-insensitive, so you can write commands as `Get-ChildItem` or `get-childitem`.
*   `PowerShell` works with objects, so you can use the `|` operator to pipe the output of one command to the input of another (e.g., `Get-Process | Sort-Object -Property CPU`).
*  Many commands support the use of wildcards (*) for working with multiple files (e.g., `Get-ChildItem *.txt`).
*   Some commands require administrator privileges.
