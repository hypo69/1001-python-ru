
**Руководство по командам PowerShell**

**1. Основы навигации и работы с файлами и каталогами**

*   **`Get-ChildItem` (или `gci`, `ls`, `dir`)**: Получает список файлов и подкаталогов в указанном местоположении.
    *   **Синтаксис**: `Get-ChildItem [путь] [параметры]`
    *   **Основные параметры:**
        *   `-Path`: Указывает путь к каталогу.
        *   `-Include`: Фильтрует по имени файла (с подстановочными знаками `*` и `?`).
        *   `-Exclude`: Исключает файлы по имени.
        *   `-Recurse`: Показывает файлы и папки во всех подкаталогах.
        *   `-Force`: Показать скрытые файлы
        *   `-File`: Показать только файлы
        *   `-Directory`: Показать только папки
    *   **Примеры:**
        *   `Get-ChildItem`: Список файлов и папок в текущем каталоге.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: Список файлов и папок в `C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: Список только текстовых файлов в текущем каталоге.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: Показать все каталоги на диске C
        *  `Get-ChildItem -Force`: Показать все файлы, включая скрытые

*   **`Set-Location` (или `sl`, `cd`)**: Меняет текущий каталог.
    *   **Синтаксис**: `Set-Location [путь]`
    *   **Примеры:**
        *   `Set-Location C:\Windows`: Перейти в каталог `C:\Windows`.
        *   `Set-Location ..`: Перейти в родительский каталог.
        * `Set-Location /` - Перейти в корень диска
*   **`New-Item`**: Создает новый файл или каталог.
    *   **Синтаксис**: `New-Item -Path [путь] -ItemType [тип] -Name [имя]`
    *   **Основные параметры:**
        *   `-ItemType`: `file` или `directory`.
        *   `-Name`: Имя нового элемента.
        *   `-Value`: Содержимое файла.
    *   **Примеры:**
        *   `New-Item -ItemType directory -Name NewFolder`: Создать папку `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: Создать пустой файл `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: Создать файл `myfile.txt` с содержимым.

*  **`Remove-Item` (или `rm`, `del`, `erase`)**: Удаляет файлы и каталоги.
    *   **Синтаксис:** `Remove-Item [путь] [параметры]`
    *   **Основные параметры:**
         *   `-Recurse`:  Удалить все подкаталоги
        *   `-Force`: Принудительное удаление (в том числе файлов "только для чтения" и каталогов).
       *  `-Confirm` - Запросить подтверждения на каждое удаление
    *   **Примеры:**
        *   `Remove-Item myfile.txt`: Удалить файл `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: Удалить папку `C:\Temp` со всеми вложенными папками и файлами.

*   **`Copy-Item`**: Копирует файлы и каталоги.
    *   **Синтаксис**: `Copy-Item [исходный_путь] [целевой_путь] [параметры]`
    *   **Основные параметры:**
        *   `-Recurse`: Копировать все подкаталоги.
        *   `-Force`: Перезаписать существующие файлы без запроса.
    *   **Примеры:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: Скопировать файл `myfile.txt` в `mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: Скопировать папку `C:\Source` во все подкаталоги в папку `D:\Backup`.

*   **`Move-Item`**: Перемещает файлы и каталоги.
    *   **Синтаксис**: `Move-Item [исходный_путь] [целевой_путь] [параметры]`
      *  `-Force` - Принудительно переместить и перезаписать

    *   **Примеры:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: Переместить файл `myfile.txt` в папку `D:\Documents`.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: Переместить папку C:\MyFolder в D:\ принудительно, даже если там уже существует папка с таким именем

*   **`Rename-Item`**: Переименовывает файл или каталог.
    *   **Синтаксис**: `Rename-Item -Path [путь] -NewName [новое_имя]`
    *   **Пример:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: Переименовать файл `myfile.txt` в `newfile.txt`.

*   **`Get-Content` (или `gc`)**: Отображает или получает содержимое файла.
    *   **Синтаксис**: `Get-Content [путь]`
    *   **Пример:**
        *   `Get-Content myfile.txt`: Показать содержимое файла `myfile.txt`.
*   **`Set-Content`**: Заменяет или создает содержимое файла.
    *  **Синтаксис:** `Set-Content [путь] [параметры]`
        *  `-value` - текст для записи
   *   **Пример:** `Set-Content myfile.txt "Новый текст"` - Заменить текст файла `myfile.txt`

*   **`Add-Content`**: Добавляет содержимое в конец файла.
   * **Синтаксис:** `Add-Content [путь] [параметры]`
       *  `-value` - текст для добавления

   *   **Пример:** `Add-Content myfile.txt "Еще текст"` - Добавить текст в конец `myfile.txt`

**2. Управление процессами:**

*   **`Get-Process` (или `gps`)**: Получает список запущенных процессов.
    *   **Синтаксис**: `Get-Process [параметры]`
    *   **Основные параметры:**
        *   `-Name`: Фильтровать по имени процесса.
        *   `-Id`: Фильтровать по идентификатору процесса.
        *    `-IncludeUserName`: Вывести пользователя запустившего процесс
    *   **Примеры:**
        *   `Get-Process`: Список всех запущенных процессов.
        *   `Get-Process -Name notepad`: Список процессов с именем `notepad`.
        *    `Get-Process -IncludeUserName`: Список всех запущенных процессов с пользователями.

*   **`Stop-Process`**: Завершает процесс.
    *   **Синтаксис**: `Stop-Process [параметры]`
     *  `-Id` - Указать id процесса
    *   `-Name` - Указать имя процесса
    *  `-Force` - Принудительно завершить процесс
    *   **Примеры:**
        *   `Stop-Process -Name notepad`: Завершить все процессы `notepad`.
         *    `Stop-Process -Id 1234` : Завершить процесс с идентификатором 1234.
        *    `Stop-Process -Name chrome -Force` : Принудительно завершить все процессы `chrome`.

**3. Управление службами:**

*   **`Get-Service`**: Получает список служб.
    *   **Синтаксис**: `Get-Service [параметры]`
    *   **Основные параметры:**
         * `-Name`: Вывести только службы с указанным именем
         * `-DisplayName`: Вывести только службы с указанным отображаемым именем
        *   `-Status`: Фильтрует по статусу (Running, Stopped).
    *   **Примеры:**
        *   `Get-Service`: Список всех служб.
        *   `Get-Service -Name Spooler`: Вывести службу Spooler.
       *   `Get-Service -Status Running`: Показать запущенные службы.
*  **`Start-Service`**: Запускает службу.
   *   **Синтаксис**: `Start-Service [имя_службы]`
   *   **Пример:** `Start-Service Spooler` - Запустить службу Spooler

*   **`Stop-Service`**: Останавливает службу.
    *   **Синтаксис**: `Stop-Service [имя_службы]`
        *  `-Force` - Остановить службу принудительно
    *   **Пример:** `Stop-Service Spooler`: Остановить службу Spooler.
        *   `Stop-Service Spooler -Force` - Остановить службу Spooler принудительно.

*  **`Restart-Service`**: Перезапускает службу.
   *   **Синтаксис:** `Restart-Service [имя_службы]`
   *   **Пример:** `Restart-Service Spooler` - Перезапустить службу Spooler.

**4. Работа с сетью**

*   **`Test-NetConnection`**: Проверяет сетевое соединение.
    *   **Синтаксис**: `Test-NetConnection [имя_хоста_или_ip-адрес] [параметры]`
    *  `-Port` - Номер порта
    *   **Примеры:**
        *   `Test-NetConnection google.com`: Проверить соединение с `google.com`.
        * `Test-NetConnection google.com -Port 80`: Проверить соединение с google.com на порту 80
*   **`Get-NetIPConfiguration`**: Получает конфигурацию сети.
    *   **Синтаксис**: `Get-NetIPConfiguration`
    *   **Пример:**
        *   `Get-NetIPConfiguration`: Отобразить конфигурацию сети.
*   **`Resolve-DnsName`**: Запрашивает информацию о DNS.
    *   **Синтаксис**: `Resolve-DnsName [имя_хоста]`
    *   **Пример:** `Resolve-DnsName google.com`: Запросить DNS-информацию для `google.com`.

**5. Работа с реестром**

*   **`Get-ItemProperty`**: Получает значение свойства из реестра.
    *   **Синтаксис**: `Get-ItemProperty -Path [путь_в_реестре]`
    *   **Пример:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: Устанавливает значение свойства в реестре.
    *   **Синтаксис**: `Set-ItemProperty -Path [путь_в_реестре] -Name [имя_свойства] -Value [значение]`
    *   **Пример:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. Прочее**

*   **`Clear-Host`**: Очищает экран консоли.
    *   **Синтаксис:** `Clear-Host`
*   **`Get-Date`**: Получает текущую дату и время.
    *   **Синтаксис:** `Get-Date`
*    **`Start-Process`**: Запускает программу или открывает файл.
    *   **Синтаксис:** `Start-Process [имя_программы_или_файла] [опции]`
   *   **Примеры:**
        *   `Start-Process notepad.exe`: Запустить Блокнот.
        *   `Start-Process myfile.txt`: Открыть файл `myfile.txt` программой по умолчанию.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - Открыть сайт в хроме

*   **`Get-Help`**: Показывает справку по команде.
    *   **Синтаксис**: `Get-Help [имя_команды]`
    *   **Пример:** `Get-Help Get-Process`: Показать справку по команде `Get-Process`.
*   **`Exit`**: Завершает сеанс PowerShell
    *   **Синтаксис:** `Exit`
*  **`Get-Variable`**: Показывает текущие переменные
    *  **Синтаксис**: `Get-Variable`
*  **`Get-Alias`**: Показывает алиасы команд
    *   **Синтаксис**: `Get-Alias`
*   **`Set-Alias`**: Создает псевдоним для команды
    *  **Синтаксис**: `Set-Alias [имя_псевдонима] [имя_команды]`
    *  **Пример**: `Set-Alias gci Get-ChildItem`

**Примечания:**

*   `PowerShell` команды (cmdlets) обычно имеют вид `Глагол-Существительное` (например, `Get-Process`, `Set-Location`).
*   `PowerShell` не чувствителен к регистру, поэтому ты можешь писать команды как `Get-ChildItem` или `get-childitem`.
*   `PowerShell` работает с объектами, поэтому ты можешь использовать оператор `|` для передачи вывода одной команды на ввод другой (например, `Get-Process | Sort-Object -Property CPU`).
*  Многие команды поддерживают использование wildcards (*) для работы с несколькими файлами (например `Get-ChildItem *.txt`).
*   Для работы с некоторыми командами требуются права администратора.

