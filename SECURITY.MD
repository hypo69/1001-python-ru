<table>
<tr>
<TD>
<A HREF = 'https://github.com/hypo69/hypotez/blob/master/README.MD'>[Root ↑]</A>
</TD>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/src/README.MD'>Code</a>
</td>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/docs/gemini/out/README.MD'>Documentation</a> 
</td>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/README.RU.MD'>Русский</a>
</td>
</tr>
</table>

Storing Application Settings
===============================

### 1. Storing Passwords and Credentials in KeePass

To securely store credentials such as passwords and API keys, use KeePass. Follow these steps:

1. **Create a KeePass Database**:
   - Open KeePass and create a new database by selecting **File > New Database**.
   - Set a strong master password to protect the database.
   - **Location**: Save the KeePass database file (`credentials.kdbx`) in the `secrets` folder of your project:
     ```
     root
     ├── data
     ├── secrets
     │   └── credentials.kdbx  # <-- KeePass database file
     |   └── passowrd.txt
     |   └── <googke api josn kes>.json
     ├── src
     └── ...

    - Never share the `credentials.kdbx` file with others. ❗
    - Ensure the file is stored in a secure location accessible only to you. (The `secrets` folder in the project root is excluded from `git`).
    - Regularly update your API keys and database passwords.     ```

2. **Create Groups and Entries**:
   - Your database should contain multiple groups to organize credentials. For example:
     - **suppliers**
       - **aliexpress**
         - Entry for API containing:
           - `api_key`: Your Aliexpress API key.
           - `secret`: Your Aliexpress secret key.
           - `tracking_id`: Tracking ID.
           - `email`: Your email address.
           - `password`: Your Aliexpress password.
       - **openai**
         - Entry for OpenAI API containing:
           - `api_key`: Your OpenAI API key.
       - **discord**
         - Entry for Discord API containing:
           - `application_id`: Discord application ID.
           - `public_key`: Public key.
           - `bot_token`: Bot token.
       - **prestashop** and other services with corresponding entries.

3. **Add Custom Properties**:
   - When creating entries, add custom properties for storing additional data. For instance, in the Aliexpress entry, add fields for:
     - `tracking_id`
     - `username`
     - `email`

### 2. Configuration of the `settings.json` File

The `settings.json` file stores the main settings for your project. Here's how to configure it:

1. **Create the `settings.json` File**:
   - Create a file named `settings.json` in the `/src` directory of your project.

2. **Example Content of the `settings.json` File**:
   ```json
   {
     "google_drive": "H:\\My Drive\\hypo69",  // Path to the Google Drive folder used for storing data.
     "mode": "debug",                          // Mode of the application: 'debug' for development or 'production' for live mode.
     "git_user": "hypo69",                    // Username for accessing the Git repository.
     "git": "hypo"                             // Name of the Git repository.
   }
   ```

3. **Description of the Fields**:
   - **google_drive**: The path to the directory on your Google Drive where project data will be stored. Ensure this path is correct for your system.
   - **mode**: Specify the mode of your application. Use `debug` for testing and `production` for deployment.
   - **git_user**: Your username on GitHub or another platform where your repository is hosted.
   - **git**: The name of your repository that is used for tracking code changes.

### 3. Protecting Sensitive Information

- **Sensitive Data**: The file containing your API keys and passwords is stored in the `secrets` folder, which is **not included in the Git repository** to prevent unauthorized access. All passwords and API keys should be loaded from KeePass at the start of the program, as described in the code.
- **Backup**: Regularly back up your KeePass database and `settings.json` file to prevent data loss.

## Reporting a Vulnerability

If you find a security vulnerability in our project, please report it by following these steps:

1. **Email**: Send an email to [security@example.com] with a description of the vulnerability.
2. **Information to Include**:
   - A detailed description of the issue
   - Steps to reproduce the vulnerability
   - Affected version(s)
   - Any other relevant information
   
3. **Response Time**: You can expect to receive an acknowledgment within 48 hours. We aim to provide updates on the status of the reported vulnerability every week until it's resolved.

4. **Outcome**: If the vulnerability is confirmed, we will work on a fix and notify you when it’s available. If we determine the report is not a vulnerability, we will inform you of our decision.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

Thank you for helping us keep our project secure!

---

Let me know if you need further adjustments!