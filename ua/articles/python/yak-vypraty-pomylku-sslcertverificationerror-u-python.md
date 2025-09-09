# Як виправити помилку SSLCertVerificationError у Python

    Зіткнулися з помилкою `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` при спробі зробити HTTPS-запит у Python за допомогою `requests` або `urllib3`?
У цій статті я покажу, як діагностувати та виправити цю проблему.

Помилка означає, що Python не зміг перевірити SSL/TLS-сертифікат веб-сайту, до якого ви підключаєтеся, тому що не знайшов довірений кореневий сертифікат у своєму сховищі.

## Крок 1: Діагностика проблеми за допомогою OpenSSL (Рекомендується)

    Перш ніж змінювати код Python, перевірте SSL-з'єднання за допомогою утиліти `openssl`. Це допоможе зрозуміти, чи є проблема специфічною для Python або пов'язана з системними налаштуваннями чи самим сервером.

1.  **Встановіть OpenSSL**, якщо у вас його немає (часто попередньо встановлений у Linux/macOS; для Windows завантажте з [офіційного сайту](https://www.openssl.org/source/) або використовуйте менеджери пакетів на кшталт Chocolatey/Scoop).
2.  **Виконайте команду** у вашому терміналі (командному рядку), замінивши `<hostname>` на адресу сайту (без `https://`) та `<port>` на порт (зазвичай 443 для HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Приклад для rosstat.gov.ua:
    openssl s_client -connect rosstat.gov.ua:443 -showcerts
    ```
3.  **Проаналізуйте вивід:** Зверніть увагу на рядок `Verify return code`. Якщо він містить помилку на кшталт `unable to get local issuer certificate` (код 20) або `certificate verify failed` (код 21), це підтверджує проблему з довірою до сертифіката на рівні системи або сховища, яке використовує OpenSSL.

## Крок 2: Виберіть спосіб вирішення

    Існує кілька способів виправити помилку `SSLCertVerificationError`. Виберіть той, який найкраще підходить для вашої ситуації.

### Спосіб 1: Відключити перевірку SSL (Швидко, але НЕБЕЗПЕЧНО)

    Цей метод повністю відключає перевірку сертифіката. Використовуйте його **лише** для тимчасового тестування, одноразових скриптів і **лише** для сайтів, яким ви абсолютно довіряєте.

⚠️ **Увага:** Відключення перевірки робить ваше з'єднання вразливим для атак "людина посередині" (MITM). **Ніколи не використовуйте `verify=False` у продакшн-коді або при роботі з конфіденційними даними!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ua/storage/mediabank/tab5_v01.xlsx" # Приклад URL

# Відключаємо перевірку SSL
try:
    # Пригнічуємо попередження про небезпечний запит (опціонально)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Перевіряємо на помилки HTTP (4xx, 5xx)

    # Ваш код для обробки відповіді, наприклад, збереження файлу
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Файл успішно завантажено (з відключеною перевіркою SSL).")

except requests.exceptions.RequestException as e:
    print(f"Помилка при завантаженні файлу: {e}")

finally:
    # Важливо: Якщо ви відключали попередження глобально,
    # можливо, ви захочете їх знову включити після виконання запиту,
    # хоча зазвичай це не потрібно, якщо скрипт завершує роботу.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Спосіб 2: Встановити/Оновити сертифікати для Python (Залежить від платформи)

    Python може постачатися зі скриптами для встановлення або оновлення набору кореневих сертифікатів з пакета `certifi`.

*   **На macOS:**
    1.  Перейдіть до папки встановлення Python (зазвичай `/Applications/Python <версія>/`).
    2.  Знайдіть і двічі клацніть файл `Install Certificates.command`. Він встановить/оновить `certifi` та зв'яже стандартний модуль `ssl` з цими сертифікатами.
*   **На Windows:**
    1.  Іноді при встановленні Python створюється скрипт `install_certificates.bat`. Пошукайте його в директорії `Scripts` всередині папки встановлення Python (наприклад, `C:\Users\<ім'я_користувача>\AppData\Local\Programs\Python\Python<версія>\Scripts\`).
    2.  Якщо ви знайшли його, запустіть.
    3.  Якщо скрипта немає, цей метод, швидше за все, не спрацює. Використовуйте Спосіб 3.

### Спосіб 3: Використовувати пакет `certifi` безпосередньо (Рекомендується, крос-платформний)

    Це найнадійніший спосіб явно вказати Python, який набір кореневих сертифікатів використовувати.

1.  **Встановіть `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Використовуйте `certifi` у вашому коді:** Передайте шлях до файлу сертифікатів `certifi` у параметр `verify` функції `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ua/storage/mediabank/tab5_v01.xlsx" # Приклад URL

    try:
        # Явно вказуємо використовувати сертифікати з certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Ваш код для обробки відповіді
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Файл успішно завантажено з використанням сертифікатів certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні файлу: {e}")
    ```
    Навіть якщо `requests` може використовувати `certifi` за замовчуванням, явне вказання `verify=certifi.where()` гарантує цю поведінку.

### Спосіб 4: Використовувати системні сховища або змінні середовища (Просунутий)

    Модуль `ssl` Python також може шукати сертифікати в системних сховищах або за шляхами, вказаними в змінних середовища. Це корисно, наприклад, у корпоративних середовищах з власними центрами сертифікації (CA).

1.  **Системні сховища:**
    *   **Linux/macOS:** Python часто автоматично використовує системні сертифікати (наприклад, з `/etc/ssl/certs/`). Переконайтеся, що ваша система має актуальні кореневі сертифікати (`sudo apt update && sudo apt install ca-certificates` для Debian/Ubuntu, `sudo yum update ca-certificates` для CentOS/RHEL).
    *   **Windows:** Python *може* намагатися використовувати системне сховище Windows, але це не завжди працює надійно без додаткових пакетів (наприклад, `python-certifi-win32`). Рекомендується використовувати `certifi` (Спосіб 3).
2.  **Змінні середовища:** Ви можете явно вказати шлях до файлу або директорії з сертифікатами:
    *   `SSL_CERT_FILE`: Вкажіть шлях до *файлу* (у форматі PEM), що містить усі довірені кореневі сертифікати.
    *   `SSL_CERT_DIR`: Вкажіть шлях до *директорії*, де кожен сертифікат знаходиться в окремому файлі PEM з ім'ям у вигляді хешу (використовуйте `c_rehash` з OpenSSL для підготовки директорії).

    **Як встановити змінні середовища:**

    *   **Linux/macOS (тимчасово, для поточної сесії):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, тимчасово):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, тимчасово):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Щоб додати свій власний (наприклад, корпоративний) CA, вам потрібно додати його сертифікат до файлу `SSL_CERT_FILE` або до директорії `SSL_CERT_DIR`.

## Крок 3 (Бонус): Як створити самопідписаний сертифікат для локальної розробки

    Якщо ви розробляєте локальний веб-сервер (API, сайт) і хочете тестувати його по HTTPS, вам знадобиться SSL-сертифікат. Оскільки у вас немає публічного домену для отримання сертифіката від звичайного CA, ви можете створити *самопідписаний* сертифікат.

**Використання OpenSSL (крос-платформний):**

1.  **Виконайте команду:** Ця команда створить приватний ключ (`key.pem`) та сам сертифікат (`cert.pem`), дійсний 10 років, для `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Створює ключ без парольного захисту (зручно для розробки).
    *   `-subj "/CN=localhost"`: Встановлює Common Name.
    *   `-addext "subjectAltName = ..."`: Додає Subject Alternative Names (важливо для сучасних браузерів та клієнтів).

2.  **Використовуйте `key.pem` та `cert.pem`** у налаштуваннях вашого локального веб-сервера (Flask, Django, Node.js тощо) для увімкнення HTTPS.

**Використання PowerShell (Windows 10/11):**

1.  **Виконайте команду в PowerShell (з правами адміністратора):** Ця команда створить сертифікат і помістить його в сховище сертифікатів комп'ютера.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Можливо, вам знадобиться експортувати цей сертифікат зі сховища (`certlm.msc`) до файлів `.pfx` або `.pem` для використання вашим веб-сервером.

**Примітка:** Браузери та HTTP-клієнти (включаючи Python `requests` за замовчуванням) не довірятимуть самопідписаним сертифікатам. При доступі до такого сервера ви отримаєте попередження або помилку SSL. Для тестів вам потрібно буде або додати цей сертифікат до довірених кореневих сертифікатів вашої системи/браузера, або використовувати `verify=False` (для `requests`), або вказати шлях до вашого `cert.pem` через `verify='/path/to/cert.pem'`.
