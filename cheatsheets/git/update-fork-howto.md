
# 🔄 Как обновлять форк GitHub через PowerShell — с нуля до автоматизации

Если вы форкнули репозиторий на GitHub и хотите регулярно получать обновления из оригинального (upstream), в этом гайде вы шаг за шагом создадите PowerShell-функцию `Update-Fork`. В финале она:

* Работает в любой ветке.
* Подтягивает изменения из upstream.
* Делает `rebase`.
* Пушит изменения с `--force`.
* Показывает нотификации в Windows.

---

## ✅ Подготовка

Перед началом:

1. Убедитесь, что в вашем репозитории добавлен `upstream` на **ОРИГИАНЛЬНЫЙ** репозиторий:

   ```bash
   git remote add upstream https://github.com/ОригинальныйПроект/репозиторий.git
   ```

2. Установите модуль уведомлений \[BurntToast], чтобы получать уведомления о процессе. (Полезно при автоматизации):

   ```powershell
   Install-Module -Name BurntToast -Force -Scope CurrentUser
   ```

---

## 🧩 Шаг 1. Создадим функцию, которая переходит в нужную директорию и определяет текущую ветку:

```powershell
function Update-Fork {
    param(
        [string]$GitDirectory = (Get-Location)
    )

    Set-Location -Path $GitDirectory

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if (-not $currentBranch) {
        Write-Host "❌ Не удалось определить текущую ветку. Убедитесь, что вы в Git-репозитории." -ForegroundColor Red
        return
    }

    Write-Host "📍 Текущая ветка: $currentBranch" -ForegroundColor Yellow
}
```

---

## 🔁 Шаг 2: Добавим fetch и rebase

Теперь подтянем изменения и сделаем `rebase`:

```powershell
    Write-Host "📥 Получаем обновления из upstream..." -ForegroundColor Cyan
    git fetch upstream

    Write-Host "🛠️  Выполняем rebase с upstream/$currentBranch..." -ForegroundColor Cyan
    git rebase "upstream/$currentBranch"
```

Добавьте этот блок в середину функции.

---

## ⚠️ Шаг 3: Обработка конфликтов

Если `rebase` не проходит чисто, PowerShell подскажет, что делать:

```powershell
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❗ Конфликты при rebase!" -ForegroundColor Red
        New-BurntToastNotification -Text "⚠️ Rebase конфликт", "Разреши вручную или выбери действие"

        while ($true) {
            Write-Host "`nЧто делаем?"
            Write-Host "1. Продолжить после ручного решения"
            Write-Host "2. Пропустить конфликт"
            Write-Host "3. Прервать rebase"
            Write-Host "4. Выход"

            $choice = Read-Host "Выбор (1-4)"

            switch ($choice) {
                "1" {
                    Read-Host "После git add . нажми Enter для продолжения"
                    git rebase --continue
                }
                "2" { git rebase --skip }
                "3" { git rebase --abort; return }
                "4" { return }
                default { Write-Host "❌ Неверный ввод." -ForegroundColor Red }
            }

            if ((git status) -notmatch "rebase") {
                break
            }
        }
    }
```

---

## 🚀 Шаг 4: Push и уведомление

В конце запушим изменения с `--force` и покажем результат:

```powershell
    Write-Host "🚀 Пушим в origin/$currentBranch (с --force)..." -ForegroundColor Cyan
    git push origin "$currentBranch" --force

    if ($LASTEXITCODE -eq 0) {
        New-BurntToastNotification -Text "✅ Форк обновлён!", "Можно продолжать работу"
    } else {
        New-BurntToastNotification -Text "❌ Ошибка при пуше", "Проверь вручную"
    }
```

---

## 🧩 Финальная версия функции:

```powershell
function Update-Fork {
    param(
        [string]$GitDirectory = (Get-Location)
    )

    Import-Module BurntToast

    Write-Host "🔄 Обновляем форк в: $GitDirectory" -ForegroundColor Cyan
    Set-Location -Path $GitDirectory

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if (-not $currentBranch) {
        Write-Host "❌ Не в Git-репозитории" -ForegroundColor Red
        return
    }

    Write-Host "📍 Текущая ветка: $currentBranch" -ForegroundColor Yellow
    git fetch upstream
    git rebase "upstream/$currentBranch"

    if ($LASTEXITCODE -ne 0) {
        New-BurntToastNotification -Text "⚠️ Конфликт при rebase", "Выберите действие"

        while ($true) {
            Write-Host "`n1. Продолжить после решения"
            Write-Host "2. Пропустить конфликт"
            Write-Host "3. Прервать rebase"
            Write-Host "4. Выйти"

            $choice = Read-Host "Выбор (1-4)"

            switch ($choice) {
                "1" { Read-Host "Сделайте git add . и нажмите Enter"; git rebase --continue }
                "2" { git rebase --skip }
                "3" { git rebase --abort; return }
                "4" { return }
                default { Write-Host "❌ Неверный ввод." }
            }

            if ((git status) -notmatch "rebase") {
                break
            }
        }
    }

    git push origin "$currentBranch" --force

    if ($LASTEXITCODE -eq 0) {
        New-BurntToastNotification -Text "✅ Форк обновлён!", "Готово к работе"
    } else {
        New-BurntToastNotification -Text "❌ Ошибка при пуше", "Разберись вручную"
    }
}
```

---

## 💡 Как запускать функцию

Вы можете использовать `Update-Fork` несколькими способами:

### 1. Вручную в текущей сессии

Скопируйте код и вставьте его в строку PowerShell. (PowerShell принимает многострочную вставку) Запустите:

```powershell
Update-Fork
```

или с указанием пути:

```powershell
Update-Fork "C:\Users\Вы\Repo"
```

---

Вот более подробная инструкция, как открыть и отредактировать PowerShell-профиль с помощью команды `notepad $PROFILE`:

---

### 🛠️ Как добавить функцию `Update-Fork` в профиль PowerShell

Это позволит вам вызывать `Update-Fork` в любой новой PowerShell-сессии, без повторного копирования кода.

---

#### ✅ Шаг 1. Откройте PowerShell

* Нажмите **Win + R**, введите `powershell`, нажмите **Enter**.
* Или откройте PowerShell через меню Пуск.

---

#### 📄 Шаг 2. Выполните команду для открытия профиля:

```powershell
notepad $PROFILE
```

🔍 Что делает эта команда:

* `$PROFILE` — это переменная PowerShell, содержащая путь к вашему пользовательскому конфигурационному скрипту (обычно что-то вроде `C:\Users\<Имя>\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`).
* `notepad` — запускает Блокнот и открывает этот файл.

---

#### 🧾 Что делать, если файл не существует

Если вы увидите сообщение вида:

> **"Файл C:\Users...\profile.ps1 не существует. Хотите создать его?"**

— просто нажмите **"Да"**, и PowerShell создаст пустой файл.

---

#### ✏️ Шаг 3. Вставьте функцию

Скопируйте всю функцию `Update-Fork` (из гайда выше) и вставьте в открывшийся Блокнот.

Например, так:

```powershell
function Update-Fork {
    param(
        [string]$GitDirectory = (Get-Location)
    )
    # ...весь код функции...
}
```

---

#### 💾 Шаг 4. Сохраните и закройте

* Нажмите **Ctrl+S**, затем **Закрыть** Блокнот.

---

#### 🔄 Шаг 5. Перезапустите PowerShell

* Закройте текущее окно PowerShell.
* Откройте новое — теперь функция `Update-Fork` будет доступна сразу после запуска.

Проверьте:

```powershell
Get-Command Update-Fork
```

Если команда найдена, вы всё сделали правильно 🎉

---

Вот как можно добавить функцию `Update-Fork` в профиль PowerShell с помощью **Visual Studio Code**, если вы предпочитаете работать в нём:

---

### 💡 Альтернатива: редактирование профиля через VS Code

Если вы используете [Visual Studio Code (VS Code)](https://code.visualstudio.com/), вы можете редактировать PowerShell-профиль в нём, что удобнее благодаря подсветке синтаксиса, автодополнению и другим функциям.

---

#### ✅ Шаг 1. Убедитесь, что установлен PowerShell-расширение

1. Откройте VS Code.
2. Перейдите на вкладку **Extensions** (`Ctrl+Shift+X`).
3. Найдите и установите расширение **PowerShell** от Microsoft (если ещё не установлено).

---

#### 📝 Шаг 2. Откройте профиль PowerShell

В PowerShell выполните команду:

```powershell
code $PROFILE
```

🔍 Что происходит:

* `$PROFILE` указывает на путь к вашему пользовательскому скрипту PowerShell.
* `code` — команда запуска VS Code с этим файлом.

📌 Если `code` не распознаётся как команда, значит VS Code не добавлен в `PATH`. Чтобы это исправить:

* Откройте VS Code.
* Откройте палитру команд (`Ctrl+Shift+P`) → **"Shell Command: Install 'code' command in PATH"**.

---

#### ✏️ Шаг 3. Вставьте код функции

Скопируйте полный текст функции `Update-Fork` и вставьте в файл профиля.

---

#### 💾 Шаг 4. Сохраните и закройте VS Code

---

#### 🔄 Шаг 5. Перезапустите PowerShell

После этого вы можете использовать `Update-Fork` в любой новой PowerShell-сессии.

Проверьте:

```powershell
Update-Fork
```

Если VS Code спросит, доверять ли рабочему пространству — выберите "Yes", особенно если профиль содержит только ваш код.

---


Вот как можно редактировать профиль PowerShell в **Windows PowerShell** и **PowerShell Core** (если используешь его), добавив функцию `Update-Fork`:

---

### 📂 Редактирование профиля PowerShell в Windows PowerShell

#### ✅ Шаг 1. Откройте профиль PowerShell

1. В Windows PowerShell или PowerShell Core выполните команду:

   ```powershell
   notepad $PROFILE
   ```

   * Эта команда откроет файл профиля в **Notepad**.
   * Если профиль не существует, PowerShell предложит создать его автоматически.

   🔍 Пояснение:

   * `$PROFILE` — это встроенная переменная, которая указывает путь к профилю пользователя в PowerShell. В зависимости от конфигурации PowerShell, это может быть файл для **Windows PowerShell** или **PowerShell Core**.

---

#### ✏️ Шаг 2. Вставьте код функции

1. Вставьте скрипт функции `Update-Fork` в открытый файл профиля.

2. Сохраните файл и закройте Notepad.

---

#### 🔄 Шаг 3. Перезапустите PowerShell

Теперь функция `Update-Fork` будет доступна в любой новой сессии PowerShell.

---

Если у тебя возникнут сложности с поиском профиля, вот где обычно находится файл профиля в зависимости от версии PowerShell:

* Для **Windows PowerShell** (до версии 5.1) профиль обычно расположен в:

  ```text
  C:\Users\<ВашеИмя>\Documents\WindowsPowerShell\profile.ps1
  ```

* Для **PowerShell Core**:

  ```text
  C:\Users\<ВашеИмя>\Documents\PowerShell\profile.ps1
  ```

Если не удаётся найти, воспользуйся командой `$PROFILE` в PowerShell для получения точного пути.

---

Теперь ты сможешь использовать команду `Update-Fork` в любой новой сессии PowerShell, что сделает обновление форка значительно проще и быстрее.


### 3. Как отдельный `.ps1`-файл

1. Сохраните функцию в файл `update-fork.ps1`.
2. Запускайте так:

   ```powershell
   .\update-fork.ps1
   Update-Fork
   ```

---

Готово! Теперь вы можете легко синхронизировать ваш форк с оригиналом одной командой и без лишней рутины.
