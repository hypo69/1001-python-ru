# Как исправить ошибку SSLCertVerificationError в Python

Столкнулись с ошибкой `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` при попытке сделать HTTPS-запрос в Python с помощью `requests` или `urllib3`? 
В этой статье я покажу, как диагностировать и исправить эту проблему.

Ошибка означает, что Python не смог проверить SSL/TLS-сертификат веб-сайта, к которому вы подключаетесь, потому что не нашел доверенный корневой сертификат в своем хранилище.

## Шаг 1: Диагностика проблемы с помощью OpenSSL (Рекомендуется)

Прежде чем менять код Python, проверьте SSL-соединение с помощью утилиты `openssl`. Это поможет понять, является ли проблема специфичной для Python или связана с системными настройками или самим сервером.

1.  **Установите OpenSSL**, если у вас его нет (часто предустановлен в Linux/macOS; для Windows скачайте с [официального сайта](https://www.openssl.org/source/) или используйте менеджеры пакетов вроде Chocolatey/Scoop).
2.  **Выполните команду** в вашем терминале (командной строке), заменив `<hostname>` на адрес сайта (без `https://`) и `<port>` на порт (обычно 443 для HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Пример для rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Проанализируйте вывод:** Обратите внимание на строку `Verify return code`. Если она содержит ошибку вроде `unable to get local issuer certificate` (код 20) или `certificate verify failed` (код 21), это подтверждает проблему с доверием к сертификату на уровне системы или хранилища, которое использует OpenSSL.

## Шаг 2: Выберите способ решения

Существует несколько способов исправить ошибку `SSLCertVerificationError`. Выберите тот, который лучше всего подходит для вашей ситуации.

### Способ 1: Отключить проверку SSL (Быстро, но НЕБЕЗОПАСНО)

Этот метод полностью отключает проверку сертификата. Используйте его **только** для временного тестирования, одноразовых скриптов и **только** для сайтов, которым вы абсолютно доверяете.

⚠️ **Внимание:** Отключение проверки делает ваше соединение уязвимым для атак "человек посередине" (MITM). **Никогда не используйте `verify=False` в продакшн-коде или при работе с конфиденциальными данными!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Пример URL

# Отключаем проверку SSL
try:
    # Подавляем предупреждения о небезопасном запросе (опционально)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Проверяем на ошибки HTTP (4xx, 5xx)

    # Ваш код для обработки ответа, например, сохранение файла
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Файл успешно скачан (с отключенной проверкой SSL).")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при скачивании файла: {e}")

finally:
    # Важно: Если вы отключали предупреждения глобально,
    # возможно, вы захотите их снова включить после выполнения запроса,
    # хотя обычно это не требуется, если скрипт завершает работу.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Способ 2: Установить/Обновить сертификаты для Python (Зависит от платформы)

Python может поставляться со скриптами для установки или обновления набора корневых сертификатов из пакета `certifi`.

*   **На macOS:**
    1.  Перейдите в папку установки Python (обычно `/Applications/Python <версия>/`).
    2.  Найдите и дважды щелкните файл `Install Certificates.command`. Он установит/обновит `certifi` и свяжет стандартный модуль `ssl` с этими сертификатами.
*   **На Windows:**
    1.  Иногда при установке Python создается скрипт `install_certificates.bat`. Поищите его в директории `Scripts` внутри папки установки Python (например, `C:\Users\<имя_пользователя>\AppData\Local\Programs\Python\Python<версия>\Scripts\`).
    2.  Если вы нашли его, запустите.
    3.  Если скрипта нет, этот метод, скорее всего, не сработает. Используйте Способ 3.

### Способ 3: Использовать пакет `certifi` напрямую (Рекомендуется, кросс-платформенный)

Это самый надежный способ явно указать Python, какой набор корневых сертификатов использовать.

1.  **Установите `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Используйте `certifi` в вашем коде:** Передайте путь к файлу сертификатов `certifi` в параметр `verify` функции `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Пример URL

    try:
        # Явно указываем использовать сертификаты из certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Ваш код для обработки ответа
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Файл успешно скачан с использованием сертификатов certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании файла: {e}")
    ```
    Даже если `requests` может использовать `certifi` по умолчанию, явное указание `verify=certifi.where()` гарантирует это поведение.

### Способ 4: Использовать системные хранилища или переменные окружения (Продвинутый)

Модуль `ssl` Python также может искать сертификаты в системных хранилищах или по путям, указанным в переменных окружения. Это полезно, например, в корпоративных средах с собственными центрами сертификации (CA).

1.  **Системные хранилища:**
    *   **Linux/macOS:** Python часто автоматически использует системные сертификаты (например, из `/etc/ssl/certs/`). Убедитесь, что ваша система имеет актуальные корневые сертификаты (`sudo apt update && sudo apt install ca-certificates` для Debian/Ubuntu, `sudo yum update ca-certificates` для CentOS/RHEL).
    *   **Windows:** Python *может* пытаться использовать системное хранилище Windows, но это не всегда работает надежно без дополнительных пакетов (например, `python-certifi-win32`). Рекомендуется использовать `certifi` (Способ 3).
2.  **Переменные окружения:** Вы можете явно указать путь к файлу или директории с сертификатами:
    *   `SSL_CERT_FILE`: Укажите путь к *файлу* (в формате PEM), содержащему все доверенные корневые сертификаты.
    *   `SSL_CERT_DIR`: Укажите путь к *директории*, где каждый сертификат находится в отдельном файле PEM с именем в виде хеша (используйте `c_rehash` из OpenSSL для подготовки директории).

    **Как установить переменные окружения:**

    *   **Linux/macOS (временно, для текущей сессии):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, временно):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, временно):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Чтобы добавить свой собственный (например, корпоративный) CA, вам нужно добавить его сертификат в файл `SSL_CERT_FILE` или в директорию `SSL_CERT_DIR`.

## Шаг 3 (Бонус): Как создать самоподписанный сертификат для локальной разработки

Если вы разрабатываете локальный веб-сервер (API, сайт) и хотите тестировать его по HTTPS, вам понадобится SSL-сертификат. Так как у вас нет публичного домена для получения сертификата от обычного CA, вы можете создать *самоподписанный* сертификат.

**Использование OpenSSL (кросс-платформенный):**

1.  **Выполните команду:** Эта команда создаст приватный ключ (`key.pem`) и сам сертификат (`cert.pem`), действительный 10 лет, для `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Создает ключ без парольной защиты (удобно для разработки).
    *   `-subj "/CN=localhost"`: Устанавливает Common Name.
    *   `-addext "subjectAltName = ..."`: Добавляет Subject Alternative Names (важно для современных браузеров и клиентов).

2.  **Используйте `key.pem` и `cert.pem`** в настройках вашего локального веб-сервера (Flask, Django, Node.js и т.д.) для включения HTTPS.

**Использование PowerShell (Windows 10/11):**

1.  **Выполните команду в PowerShell (с правами администратора):** Эта команда создаст сертификат и поместит его в хранилище сертификатов компьютера.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Возможно, вам потребуется экспортировать этот сертификат из хранилища (`certlm.msc`) в файлы `.pfx` или `.pem` для использования вашим веб-сервером.

**Примечание:** Браузеры и HTTP-клиенты (включая Python `requests` по умолчанию) не будут доверять самоподписанным сертификатам. При доступе к такому серверу вы получите предупреждение или ошибку SSL. Для тестов вам нужно будет либо добавить этот сертификат в доверенные корневые сертификаты вашей системы/браузера, либо использовать `verify=False` (для `requests`), либо указать путь к вашему `cert.pem` через `verify='/path/to/cert.pem'`.
