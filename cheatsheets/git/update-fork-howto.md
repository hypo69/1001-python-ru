# 🔄 Как автоматически обновлять свой форк на GitHub через PowerShell и получать уведомления в Windows

Если вы сделали форк проекта на GitHub и хотите регулярно получать обновления из оригинального репозитория (upstream), этот гайд поможет вам автоматизировать процесс через PowerShell. В результате вы получите удобную команду `Update-Fork`, которая:

* Работает с любой веткой (`main`, `master`, `develop`, и т. д.).
* Делает `fetch` и `rebase` с `upstream`.
* Пушит изменения с `--force` в ваш форк.
* Показывает всплывающие уведомления в Windows.

---

## ✅ Что понадобится

Перед началом убедитесь, что:

1. В вашем локальном репозитории настроен `upstream`:

   ```bash
   git remote add upstream https://github.com/ОригинальныйПроект/репозиторий.git
   ```

2. Установлен модуль [BurntToast](https://www.powershellgallery.com/packages/BurntToast), который используется для отображения уведомлений:

   ```powershell
   Install-Module -Name BurntToast -Force -Scope CurrentUser
   ```

---

## 🛠 Как работает `Update-Fork`

Функция:

* Определяет текущую ветку.
* Выполняет `fetch` из `upstream`.
* Делает `rebase` с `upstream/текущая_ветка`.
* При успехе делает `push --force` в ваш форк.
* Показывает уведомление об успехе или ошибке.

---

## 💡 PowerShell скрипт

```powershell
function Update-Fork {
    param(
        [string]$GitDirectory = (Get-Location)
    )

    Import-Module BurntToast

    Write-Host "🔄 Начинаем обновление форка в директории: $GitDirectory" -ForegroundColor Cyan
    Set-Location -Path $GitDirectory

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if (-not $currentBranch) {
        Write-Host "❌ Не удалось определить текущую ветку. Проверь, что ты в Git-репозитории." -ForegroundColor Red
        return
    }

    Write-Host "📍 Текущая ветка: $currentBranch" -ForegroundColor Yellow

    Write-Host "📥 Забираем изменения из upstream..." -ForegroundColor Cyan
    git fetch upstream

    Write-Host "🛠️  Делаем rebase с upstream/$currentBranch..." -ForegroundColor Cyan
    git rebase "upstream/$currentBranch"

    if ($LASTEXITCODE -ne 0) {
        Write-Host "❗ Конфликты при rebase. Разреши вручную и выполни: git rebase --continue" -ForegroundColor Red
        New-BurntToastNotification -Text "⚠️ Конфликты при rebase!", "Разреши вручную и продолжи."
        return
    }

    Write-Host "🚀 Пушим изменения в origin/$currentBranch (с --force)..." -ForegroundColor Cyan
    git push origin "$currentBranch" --force

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Форк успешно обновлён!" -ForegroundColor Green
        New-BurntToastNotification -Text "✅ Форк обновлён!", "Можешь продолжать работу!"
    } else {
        Write-Host "❌ Не удалось запушить. Проверь ошибки." -ForegroundColor Red
        New-BurntToastNotification -Text "❌ Ошибка при пуше!", "Проверь конфликты вручную."
    }
}
```

---

- Функцию можно запустить из командной строки PowerShell, передав путь к директории с форком или добавить в профиль PowerShell для автоматического использования.
## 💾 Как добавить функцию в профиль PowerShell

1. Откройте профиль:

   ```powershell
   notepad $PROFILE
   ```

   Если файл не существует — PowerShell предложит его создать.

2. Вставьте туда весь скрипт `Update-Fork`.

3. Сохраните и перезапустите PowerShell.

Теперь функция доступна в любой новой сессии.

---

## 🚀 Как использовать

Перейдите в директорию с форком и выполните:

```powershell
Update-Fork
```

Или передайте путь к репозиторию:

```powershell
Update-Fork "C:\Users\Имя\Projects\MyFork"
```

---


