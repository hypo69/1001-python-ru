# Как автоматически обновлять свой форк на GitHub через PowerShell с уведомлениями Windows

Если вы сделали форк репозитория на GitHub и хотите получать все обновления из оригинального репозитория ("родительского"), удобно настроить автоматическое обновление через PowerShell.  
В этой шпаргалке создадим скрипт, который:

- Переключится на ветку `main`, если вы на другой ветке.
- Скачает изменения из `upstream`.
- Выполнит `rebase` на `upstream/main`.
- Поможет решить конфликты через удобное меню.
- Отправит обновления в ваш форк на GitHub.
- Покажет всплывающее уведомление о результате!

---

## 1. Минимальная подготовка

Перед тем как начать:

- Убедитесь, что в вашем локальном репозитории настроен `upstream`:

    ```bash
    git remote add upstream https://github.com/оригинальный-проект/репозиторий.git
    ```

- Убедитесь, что основная ветка называется `main`.  
  Если у вас `master`, замените все упоминания `main` на `master` в скрипте.

---

## 2. Базовый скрипт для обновления форка

Создайте функцию PowerShell, которая:

- Переключится на `main`, если нужно.
- Получит изменения.
- Сделает `rebase` на `upstream/main`.
- Автоматически пушит изменения в ваш форк.

```powershell
function Update-Fork {
    Write-Host "🔄 Начинаем обновление форка..." -ForegroundColor Cyan

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if ($currentBranch -ne "main") {
        Write-Host "⚠️  Ты на ветке '$currentBranch'. Переключаюсь на 'main'..." -ForegroundColor Yellow
        git checkout main
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Не удалось переключиться на 'main'. Остановлено." -ForegroundColor Red
            return
        }
    }

    Write-Host "📥 Забираем изменения из upstream..." -ForegroundColor Cyan
    git fetch upstream

    Write-Host "🛠️  Делаем rebase с upstream/main..." -ForegroundColor Cyan
    git rebase upstream/main

    if ($LASTEXITCODE -ne 0) {
        Write-Host "❗ При ребейсе возникли конфликты. Разреши их и выполни: git rebase --continue" -ForegroundColor Red
        return
    }

    Write-Host "🚀 Пушим изменения в свой форк (с --force)..." -ForegroundColor Cyan
    git push origin main --force

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Форк успешно обновлён!" -ForegroundColor Green
    } else {
        Write-Host "❌ Не удалось запушить. Проверь ошибки." -ForegroundColor Red
    }
}
```

---

## 3. Умная обработка конфликтов

Теперь добавим автоматическую обработку конфликтов.  
Если при `rebase` появляются конфликты:

- Скрипт проверит статус.
- Если конфликт можно пропустить — пропустит.
- Если надо решать вручную — попросит вас это сделать.

```powershell
if ($LASTEXITCODE -ne 0) {
    Write-Host "❗ При ребейсе возникли конфликты. Пытаюсь исправить..." -ForegroundColor Red

    while ($true) {
        $status = git status

        if ($status -match "You are currently rebasing") {
            if ($status -match "fix conflicts and then commit the result") {
                Write-Host "⚔️ Обнаружены нерешённые конфликты. Реши их вручную!" -ForegroundColor Yellow
                Write-Host "Когда исправишь — напиши: git add . и git rebase --continue" -ForegroundColor Yellow
                return
            }
            elseif ($status -match "no changes - did you forget to use 'git add'?") {
                Write-Host "📦 Нет изменений для коммита. Пропускаем конфликт." -ForegroundColor Yellow
                git rebase --skip
            }
            else {
                Write-Host "✅ Пытаюсь продолжить ребейc..." -ForegroundColor Green
                git rebase --continue
            }
        }
        else {
            Write-Host "🎉 Rebase успешно завершён!" -ForegroundColor Green
            break
        }
    }
}
```

---

## 4. Улучшаем: добавляем интерактивное меню при конфликтах

Если вы хотите полный контроль, добавьте меню выбора при конфликте:

```powershell
if ($LASTEXITCODE -ne 0) {
    Write-Host "❗ Конфликты при rebase! Запускаю меню действий..." -ForegroundColor Red

    while ($true) {
        Write-Host "`n⚡ Что хочешь сделать?"
        Write-Host "1. Разрешить конфликты вручную и продолжить ребейc"
        Write-Host "2. Пропустить конфликт (git rebase --skip)"
        Write-Host "3. Остановить ребейc (git rebase --abort)"
        Write-Host "4. Выйти из скрипта без изменений"

        $choice = Read-Host "Выбери (1/2/3/4)"

        switch ($choice) {
            "1" {
                Write-Host "🔧 После разрешения конфликтов сделай 'git add .' и нажми Enter, чтобы продолжить..." -ForegroundColor Yellow
                Read-Host "Нажми Enter когда будешь готов"
                git rebase --continue
            }
            "2" {
                Write-Host "⏩ Пропускаем конфликт..." -ForegroundColor Yellow
                git rebase --skip
            }
            "3" {
                Write-Host "🛑 Отменяем ребейc..." -ForegroundColor Red
                git rebase --abort
                return
            }
            "4" {
                Write-Host "🚪 Выход без изменений." -ForegroundColor Yellow
                return
            }
            default {
                Write-Host "❌ Неверный выбор. Попробуй ещё раз." -ForegroundColor Red
            }
        }

        $status = git status
        if ($status -notmatch "You are currently rebasing") {
            Write-Host "🎉 Rebase успешно завершён!" -ForegroundColor Green
            break
        }
    }
}
```

---

## 5. Красота: добавляем уведомления Windows

Чтобы ещё удобнее отслеживать статус, настроим всплывающие уведомления Windows.

### Шаг 1: Установить модуль уведомлений

Открой PowerShell и выполни:

```powershell
Install-Module -Name BurntToast -Force -Scope CurrentUser
```

(Разрешите установку, если потребуется.)

### Шаг 2: Импортировать модуль и добавить уведомления

Добавьте в начало скрипта:

```powershell
Import-Module BurntToast
```

Добавьте уведомления в конец функции:

```powershell
# После успешного пуша:
New-BurntToastNotification -Text "✅ Форк обновлён!", "Можешь продолжать работу!"

# При ошибке:
New-BurntToastNotification -Text "❌ Ошибка при пуше!", "Проверь конфликты вручную."
```

---

## Финальная версия скрипта Update-Fork
```powershell
function Update-Fork {
    Write-Host "🔄 Начинаем обновление форка..." -ForegroundColor Cyan

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if ($currentBranch -ne "main") {
        Write-Host "⚠️  Ты на ветке '$currentBranch'. Переключаюсь на 'main'..." -ForegroundColor Yellow
        git checkout main
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Не удалось переключиться на 'main'. Остановлено." -ForegroundColor Red
            return
        }
    }

    Write-Host "📥 Забираем изменения из upstream..." -ForegroundColor Cyan
    git fetch upstream

    Write-Host "🛠️  Делаем rebase с upstream/main..." -ForegroundColor Cyan
    git rebase upstream/main

    if ($LASTEXITCODE -ne 0) {
        Write-Host "❗ При ребейсе возникли конфликты. Разреши их и выполни: git rebase --continue" -ForegroundColor Red
        return
    }

    Write-Host "🚀 Пушим изменения в свой форк (с --force)..." -ForegroundColor Cyan
    git push origin main --force

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Форк успешно обновлён!" -ForegroundColor Green
        New-BurntToastNotification -Text "✅ Форк обновлён!", "Можешь продолжать работу!"
    } else {
        Write-Host "❌ Не удалось запушить. Проверь ошибки." -ForegroundColor Red
        New-BurntToastNotification -Text "❌ Ошибка при пуше!", "Проверь конфликты вручную."
    }
}
```

Запускать его можно просто командой:

```powershell
Update-Fork
```

---


Приятной работы! 🚀
