<!-- Translated to en -->
You are absolutely right. Thank you for the clarification. The use of "guillemets" is standard for Russian typography.

Here is the corrected version of the article with the correct quotation marks:

***

### How to automatically update programs with Ninite and Windows Task Scheduler

Keeping your software up-to-date is key to the security and stability of your system. However, manually checking and installing updates for each application can be time-consuming. In this article, we will look at how to automate this process using the Ninite.com service and the built-in Windows Task Scheduler.

### Part 1: Getting started with Ninite and creating an installer

Ninite — is a service designed to install and update several popular applications simultaneously. It aims to save you time by eliminating the need to manually install each program, scroll through installation wizards, and decline offers to install toolbars or other unwanted software.

**Key features and benefits of Ninite:**

*   **Installation without unnecessary actions:** You don't need to click "next" or decline toolbars and extra junk. Just select the applications you need and run the installer.
*   **Always up-to-date versions:** Ninite uses bots to track updates, so you always get the latest stable versions of applications.
*   **Process automation:** Ninite works in the background, installing applications in standard locations and in your system's language. It skips already updated applications and ignores reboot requests from installers.
*   **Security:** Applications are downloaded directly from official publisher websites, and their digital signatures or hashes are verified before launch to ensure authenticity.
*   **System support:** Ninite works on Windows 11, 10, 8.x, 7, and equivalent server versions.
*   **Free for home use:** The site is free for personal use (no ads or unwanted software). The paid version of Ninite Pro offers extended features for managing software in organizations.

**Application sections (categories) you can choose from:**

Ninite offers a wide range of programs grouped by categories:

*   **Web Browsers:** Chrome, Opera, Firefox, Edge, Brave.
*   **Messaging:** Zoom, Discord, Teams, Pidgin, Thunderbird.
*   **Media:** iTunes, VLC, AIMP, foobar2000, Audacity, K-Lite Codecs, Spotify, HandBrake.
*   **Imaging:** Krita, Blender, Paint.NET, GIMP, IrfanView, Inkscape, Greenshot, ShareX.
*   **Documents:** Foxit Reader, LibreOffice, SumatraPDF, OpenOffice.
*   **Security:** Malwarebytes, Avast, AVG, Avira.
*   **Online Storage:** Dropbox, Google Drive, OneDrive.
*   **Utilities:** TeamViewer, ImgBurn, TeraCopy, Revo, WinDirStat, CCleaner.
*   **Compression:** 7-Zip, PeaZip, WinRAR.
*   **Developer Tools:** Python, Git, FileZilla, Notepad++, WinSCP, PuTTY, Visual Studio Code.
*   **And much more:** including .NET, Java, utilities, and other useful tools.

**How to select and download the installation file:**

1.  **Select applications:** On the main page of ninite.com, you will see a list of categories with applications. Check the boxes next to the programs you want to install or keep up-to-date.
2.  **Download installer:** After selecting applications, click the **"Get Your Ninite"** button. The site will generate and offer you to download a personal executable file. This small file is your universal installer/updater.

### Part 2: Setting up automatic updates

Now that you have a configured Ninite installer, let's figure out where best to place it and how to set up automatic launch.

**Where to place the Ninite file**

For the system to be able to find and run your Ninite file without problems, it is recommended to create a separate folder for it. This will prevent accidental deletion or movement of the file.

**Placement recommendations:**

*   **Avoid system folders:** Do not save the file in the root of drive `C:` or in the `C:\Windows` folder.
*   **Create a special folder:** A good practice would be to create a folder, for example, `C:\NiniteUpdater`. This will simplify file management and future searches.

Move the Ninite file downloaded from the Ninite website (e.g., `Ninite-software-bundle.exe`) to the folder you created earlier (<code>C:\NiniteUpdater</code>).

**Setting up automatic launch via Windows Task Scheduler**

To ensure that programs are checked and updated automatically every Sunday, we will use the built-in Windows tool — **Task Scheduler**.

**1. Opening Task Scheduler:**

*   Press `Win + R`, type `taskschd.msc`, and press Enter.

**2. Creating a new task:**

In the Task Scheduler window, in the right-hand "Actions" pane, select **"Create Basic Task..."**.

*   **Name and description:** Enter a clear name for your task, for example, "Weekly Ninite Update". Click "Next".
*   **Trigger (launch time):** In this step, you need to specify how often the task will run.
    *   Select "Weekly" and click "Next".
    *   Specify the day of the week — "Sunday". You can also choose a convenient launch time for you, for example, when the computer is usually on but not actively used. Click "Next".
*   **Action:** Here we will specify which program to run.
    *   Select "Start a program" and click "Next".
    *   In the "Program or script" field, click the "Browse..." button and find your Ninite file in the folder you created earlier (<code>C:\NiniteUpdater\Ninite-software-bundle.exe</code>).
    *   Click "Next".
*   **Finish:** In the last step, check all the specified parameters. If everything is correct, click "Finish".

Now, Task Scheduler will automatically run your Ninite file every Sunday at the time you specified. When Ninite runs, it will check the versions of your selected programs in the background and, if it finds updates, will download and install them without your intervention. Thus, you get a simple and reliable system for keeping your software up-to-date.
