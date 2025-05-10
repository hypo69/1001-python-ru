# PowerShell: автоматизация обновления форка GitHub

## Часть 2. Финальная функция `Update-Fork`

### Готовая функция `Update-Fork`

```powershell
function Update-Fork {
    param(
        [Parameter(Mandatory)]
        [string]$RepoPath,
        [string]$TelegramToken,
        [string]$TelegramChatId
    )

    Set-Location -Path $RepoPath

    $logPath = "$RepoPath\update-log.txt"
    "[$(Get-Date)] Начало обновления $RepoPath" | Out-File -FilePath $logPath -Append

    try {
        git remote -v | Out-Null
    } catch {
        Write-Error "Не git-репозиторий: $RepoPath"
        "[$(Get-Date)] ❌ Не git-репозиторий" | Out-File -FilePath $logPath -Append
        return
    }

    if (-not (git remote | Select-String -Pattern 'upstream')) {
        Write-Error "Удалённый 'upstream' не найден"
        "[$(Get-Date)] ❌ 'upstream' не найден" | Out-File -FilePath $logPath -Append
        return
    }

    try {
        git checkout main
        git fetch upstream
        git rebase upstream/main
        git push origin main --force

        "[$(Get-Date)] ✅ Fork успешно обновлён" | Out-File -FilePath $logPath -Append

        if (Get-Command New-BurntToastNotification -ErrorAction SilentlyContinue) {
            New-BurntToastNotification -Text "Fork обновлён", "Репозиторий: $RepoPath"
        } else {
            Write-Host "✅ Fork обновлён: $RepoPath"
        }

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "✅ Fork обновлён: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    } catch {
        Write-Error "Ошибка при обновлении форка: $_"
        "[$(Get-Date)] ❌ Ошибка: $_" | Out-File -FilePath $logPath -Append

        if (Get-Command New-BurntToastNotification -ErrorAction SilentlyContinue) {
            New-BurntToastNotification -Text "Ошибка обновления форка", $_.Exception.Message
        }

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "❌ Ошибка при обновлении форка: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    }
}
```

---

### Способы использования

#### 1. Обновить один репозиторий:

```powershell
Update-Fork -RepoPath "C:\Projects\my-fork" -TelegramToken "<TOKEN>" -TelegramChatId "<CHAT_ID>"
```

#### 2. Обновить несколько форков из списка:

```powershell
$forks = @(
    "C:\Projects\repo1",
    "C:\Projects\repo2"
)

foreach ($fork in $forks) {
    Update-Fork -RepoPath $fork -TelegramToken "<TOKEN>" -TelegramChatId "<CHAT_ID>"
}
```

---

### Частые ошибки и их причины

| Ошибка                        | Причина                                                |
| ----------------------------- | ------------------------------------------------------ |
| `fatal: not a git repository` | Путь не указывает на git-репозиторий                   |
| `error: could not apply`      | Конфликты при rebase — требует ручного разрешения      |
| `upstream not found`          | Не настроен remote `upstream`                          |
| `! [rejected]` при push       | Rebase не был выполнен, ветка расходится с origin/main |

---

### Автоматизация через ярлык

Создайте ярлык `.ps1`:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Scripts\update-forks.ps1"
```

Содержимое `update-forks.ps1`:

```powershell
$token = "<TOKEN>"
$chatId = "<CHAT_ID>"
$forks = Get-Content "C:\Scripts\repos.txt"
foreach ($repo in $forks) {
    Update-Fork -RepoPath $repo -TelegramToken $token -TelegramChatId $chatId
}
```

Файл `repos.txt`:

```
C:\Projects\repo1
C:\Projects\repo2
```

---

## Часть 3. Экспорт логов и Telegram

(см. выше — встроены в `Update-Fork`)

Функция отправки сообщений:

```powershell
function Send-TelegramMessage {
    param(
        [string]$Message,
        [string]$Token,
        [string]$ChatId
    )

    $uri = "https://api.telegram.org/bot$Token/sendMessage"
    $body = @{ chat_id = $ChatId; text = $Message }
    Invoke-RestMethod -Uri $uri -Method Post -Body $body
}
```

---

## Часть 4. GUI-интерфейс на Windows Forms

```powershell
Add-Type -AssemblyName System.Windows.Forms

$form = New-Object Windows.Forms.Form
$form.Text = "Update Forks"
$form.Size = New-Object Drawing.Size(400,200)

$button = New-Object Windows.Forms.Button
$button.Text = "Обновить форки"
$button.Dock = "Top"
$button.Add_Click({
    $repos = Get-Content "C:\Scripts\repos.txt"
    $token = "<TOKEN>"
    $chatId = "<CHAT_ID>"
    foreach ($repo in $repos) {
        Update-Fork -RepoPath $repo -TelegramToken $token -TelegramChatId $chatId
    }
})

$form.Controls.Add($button)
$form.ShowDialog()
```

---

В следующей части можно оформить приложение в `.exe`, добавить выбор токенов через GUI, интеграцию с Windows Task Scheduler или автозагрузку.

import shutil
import os
import subprocess

# Подготовим структуру проекта
project_dir = "/mnt/data/UpdateForkApp"
script_path = os.path.join(project_dir, "UpdateForkApp.ps1")
form_code_path = os.path.join(project_dir, "UpdateForkForm.ps1")
installer_script_path = os.path.join(project_dir, "installer.iss")

# Создание папки проекта
os.makedirs(project_dir, exist_ok=True)

# Содержимое основного PowerShell-скрипта
script_content = """
param (
    [string]$Token = "<TOKEN>",
    [string]$ChatId = "<CHAT_ID>"
)

function Send-TelegramMessage {
    param(
        [string]$Message,
        [string]$Token,
        [string]$ChatId
    )

    $uri = "https://api.telegram.org/bot$Token/sendMessage"
    $body = @{ chat_id = $ChatId; text = $Message }
    Invoke-RestMethod -Uri $uri -Method Post -Body $body
}

function Update-Fork {
    param(
        [Parameter(Mandatory)]
        [string]$RepoPath,
        [string]$TelegramToken,
        [string]$TelegramChatId
    )

    Set-Location -Path $RepoPath
    $logPath = "$RepoPath\\update-log.txt"
    "[$(Get-Date)] Начало обновления $RepoPath" | Out-File -FilePath $logPath -Append

    try {
        git remote -v | Out-Null
    } catch {
        "[$(Get-Date)] ❌ Не git-репозиторий" | Out-File -FilePath $logPath -Append
        return
    }

    if (-not (git remote | Select-String -Pattern 'upstream')) {
        "[$(Get-Date)] ❌ 'upstream' не найден" | Out-File -FilePath $logPath -Append
        return
    }

    try {
        git checkout main
        git fetch upstream
        git rebase upstream/main
        git push origin main --force

        "[$(Get-Date)] ✅ Fork успешно обновлён" | Out-File -FilePath $logPath -Append

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "✅ Fork обновлён: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    } catch {
        "[$(Get-Date)] ❌ Ошибка: $_" | Out-File -FilePath $logPath -Append

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "❌ Ошибка при обновлении форка: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    }
}

# Чтение списка репозиториев из файла
$repos = Get-Content "$PSScriptRoot\\repos.txt"
foreach ($repo in $repos) {
    Update-Fork -RepoPath $repo -TelegramToken $Token -TelegramChatId $ChatId
}
"""

# Сохраняем PowerShell-скрипт
with open(script_path, "w", encoding="utf-8") as f:
    f.write(script_content)

# Сохраняем пример GUI-обёртки отдельно (если нужно отдельно запускать форму)
form_code = """
Add-Type -AssemblyName System.Windows.Forms

$form = New-Object Windows.Forms.Form
$form.Text = "Update Forks"
$form.Size = New-Object Drawing.Size(400,200)

$button = New-Object Windows.Forms.Button
$button.Text = "Обновить форки"
$button.Dock = "Top"
$button.Add_Click({
    & "$PSScriptRoot\\UpdateForkApp.ps1" -Token "<TOKEN>" -ChatId "<CHAT_ID>"
})

$form.Controls.Add($button)
$form.ShowDialog()
"""
with open(form_code_path, "w", encoding="utf-8") as f:
    f.write(form_code)

# Подготовка скрипта для Inno Setup
installer_script = f"""
[Setup]
AppName=UpdateForkApp
AppVersion=1.0
DefaultDirName={{pf}}\\UpdateForkApp
DefaultGroupName=UpdateForkApp
OutputDir={project_dir}
OutputBaseFilename=UpdateForkAppInstaller

[Files]
Source: "{script_path}"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{form_code_path}"; DestDir: "{{app}}"; Flags: ignoreversion

[Icons]
Name: "{{group}}\\Update Fork GUI"; Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -File \\"{{app}}\\\\UpdateForkForm.ps1\\""; WorkingDir: "{{app}}"
"""
with open(installer_script_path, "w", encoding="utf-8") as f:
    f.write(installer_script)

project_dir
