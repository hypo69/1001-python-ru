# Как автоматически обновлять свой форк на GitHub через PowerShell с уведомлениями Windows

Если вы сделали форк репозитория на GitHub и хотите получать все обновления из оригинального репозитория ("родительского"), удобно настроить автоматическое обновление через PowerShell.  
В этом **howto** мы создадим скрипт, который:

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

(Текст продолжается в таком же стиле...)