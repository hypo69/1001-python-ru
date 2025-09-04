# Jak naprawić błąd SSLCertVerificationError w Pythonie

    Czy napotkałeś błąd `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` podczas próby wykonania żądania HTTPS w Pythonie za pomocą `requests` lub `urllib3`?
W tym artykule pokażę Ci, jak zdiagnozować i naprawić ten problem.

Błąd oznacza, że Python nie mógł zweryfikować certyfikatu SSL/TLS witryny, z którą się łączysz, ponieważ nie mógł znaleźć zaufanego certyfikatu głównego w swoim magazynie.

## Krok 1: Diagnozowanie problemu za pomocą OpenSSL (zalecane)

    Przed zmianą kodu Pythona sprawdź połączenie SSL za pomocą narzędzia `openssl`. Pomoże to zrozumieć, czy problem jest specyficzny dla Pythona, czy związany z ustawieniami systemowymi lub samym serwerem.

1.  **Zainstaluj OpenSSL**, jeśli go nie masz (często preinstalowany na Linuxie/macOS; dla Windows pobierz z [oficjalnej strony](https://www.openssl.org/source/) lub użyj menedżerów pakietów, takich jak Chocolatey/Scoop).
2.  **Uruchom polecenie** w swoim terminalu (wierszu poleceń), zastępując `<hostname>` adresem witryny (bez `https://`) i `<port>` portem (zazwyczaj 443 dla HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Przykład dla rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Przeanalizuj dane wyjściowe:** Zwróć uwagę na wiersz `Verify return code`. Jeśli zawiera błąd, taki jak `unable to get local issuer certificate` (kod 20) lub `certificate verify failed` (kod 21), potwierdza to problem z zaufaniem do certyfikatu na poziomie systemu lub magazynu używanego przez OpenSSL.

## Krok 2: Wybierz metodę rozwiązania

    Istnieje kilka sposobów naprawienia błędu `SSLCertVerificationError`. Wybierz ten, który najlepiej odpowiada Twojej sytuacji.

### Metoda 1: Wyłącz weryfikację SSL (szybka, ale NIEBEZPIECZNA)

    Ta metoda całkowicie wyłącza weryfikację certyfikatu. Używaj jej **tylko** do tymczasowych testów, jednorazowych skryptów i **tylko** dla witryn, którym absolutnie ufasz.

⚠️ **Ostrzeżenie:** Wyłączenie weryfikacji sprawia, że Twoje połączenie jest podatne na ataki typu man-in-the-middle (MITM). **Nigdy nie używaj `verify=False` w kodzie produkcyjnym ani podczas pracy z danymi wrażliwymi!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Przykładowy URL

# Wyłącz weryfikację SSL
try:
    # Pomiń ostrzeżenia o niezabezpieczonych żądaniach (opcjonalnie)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Sprawdź błędy HTTP (4xx, 5xx)

    # Twój kod do obsługi odpowiedzi, na przykład zapisywanie pliku
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Plik pobrany pomyślnie (z wyłączoną weryfikacją SSL).")

except requests.exceptions.RequestException as e:
    print(f"Błąd pobierania pliku: {e}")

finally:
    # Ważne: Jeśli wyłączyłeś ostrzeżenia globalnie,
    # możesz chcieć je ponownie włączyć po zakończeniu żądania,
    # chociaż zazwyczaj nie jest to konieczne, jeśli skrypt się kończy.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Metoda 2: Zainstaluj/Zaktualizuj certyfikaty dla Pythona (zależne od platformy)

    Python może być dostarczany ze skryptami do instalacji lub aktualizacji zestawu certyfikatów głównych z pakietu `certifi`.

*   **Na macOS:**
    1.  Przejdź do folderu instalacyjnego Pythona (zazwyczaj `/Applications/Python <version>/`).
    2.  Znajdź i kliknij dwukrotnie plik `Install Certificates.command`. Zainstaluje/zaktualizuje `certifi` i połączy standardowy moduł `ssl` z tymi certyfikatami.
*   **Na Windows:**
    1.  Czasami podczas instalacji Pythona tworzony jest skrypt `install_certificates.bat`. Poszukaj go w katalogu `Scripts` w folderze instalacyjnym Pythona (np. `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\`).
    2.  Jeśli go znajdziesz, uruchom go.
    3.  Jeśli skryptu nie ma, ta metoda najprawdopodobniej nie zadziała. Użyj Metody 3.

### Metoda 3: Użyj pakietu `certifi` bezpośrednio (zalecane, wieloplatformowe)

    Jest to najbardziej niezawodny sposób na jawne poinformowanie Pythona, którego zestawu certyfikatów głównych ma użyć.

1.  **Zainstaluj `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Użyj `certifi` w swoim kodzie:** Przekaż ścieżkę do pliku certyfikatu `certifi` do parametru `verify` funkcji `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Przykładowy URL

    try:
        # Jawnie określ, aby używać certyfikatów z certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Twój kod do obsługi odpowiedzi
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Plik pobrany pomyślnie przy użyciu certyfikatów certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania pliku: {e}")
    ```
    Nawet jeśli `requests` może używać `certifi` domyślnie, jawne określenie `verify=certifi.where()` gwarantuje to zachowanie.

### Metoda 4: Użyj magazynów systemowych lub zmiennych środowiskowych (zaawansowane)

    Moduł `ssl` Pythona może również szukać certyfikatów w magazynach systemowych lub w ścieżkach określonych w zmiennych środowiskowych. Jest to przydatne, na przykład, w środowiskach korporacyjnych z własnymi urzędami certyfikacji (CA).

1.  **Magazyny systemowe:**
    *   **Linux/macOS:** Python często automatycznie używa certyfikatów systemowych (np. z `/etc/ssl/certs/`). Upewnij się, że Twój system ma aktualne certyfikaty główne (`sudo apt update && sudo apt install ca-certificates` dla Debiana/Ubuntu, `sudo yum update ca-certificates` dla CentOS/RHEL).
    *   **Windows:** Python *może* próbować używać magazynu systemowego Windows, ale nie zawsze działa to niezawodnie bez dodatkowych pakietów (np. `python-certifi-win32`). Zaleca się użycie `certifi` (Metoda 3).
2.  **Zmienne środowiskowe:** Możesz jawnie określić ścieżkę do pliku lub katalogu z certyfikatami:
    *   `SSL_CERT_FILE`: Określ ścieżkę do *pliku* (w formacie PEM) zawierającego wszystkie zaufane certyfikaty główne.
    *   `SSL_CERT_DIR`: Określ ścieżkę do *katalogu*, w którym każdy certyfikat znajduje się w osobnym pliku PEM z nazwą w postaci hasha (użyj `c_rehash` z OpenSSL, aby przygotować katalog).

    **Jak ustawić zmienne środowiskowe:**

    *   **Linux/macOS (tymczasowo, dla bieżącej sesji):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, tymczasowo):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, tymczasowo):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Aby dodać własny (np. korporacyjny) CA, musisz dodać jego certyfikat do pliku `SSL_CERT_FILE` lub do katalogu `SSL_CERT_DIR`.

## Krok 3 (Bonus): Jak stworzyć certyfikat samopodpisany do lokalnego rozwoju

    Jeśli rozwijasz lokalny serwer WWW (API, stronę internetową) i chcesz go przetestować przez HTTPS, będziesz potrzebował certyfikatu SSL. Ponieważ nie masz domeny publicznej, aby uzyskać certyfikat od zwykłego CA, możesz stworzyć certyfikat *samopodpisany*.

**Używanie OpenSSL (wieloplatformowe):**

1.  **Uruchom polecenie:** To polecenie utworzy klucz prywatny (`key.pem`) i sam certyfikat (`cert.pem`), ważny przez 10 lat, dla `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Tworzy klucz bez hasła (wygodne do rozwoju).
    *   `-subj "/CN=localhost"`: Ustawia nazwę pospolitą.
    *   `-addext "subjectAltName = ..."`: Dodaje alternatywne nazwy podmiotu (ważne dla nowoczesnych przeglądarek i klientów).

2.  **Użyj `key.pem` i `cert.pem`** w ustawieniach swojego lokalnego serwera WWW (Flask, Django, Node.js itp.), aby włączyć HTTPS.

**Używanie PowerShell (Windows 10/11):**

1.  **Uruchom polecenie w PowerShell (z uprawnieniami administratora):** To polecenie utworzy certyfikat i umieści go w magazynie certyfikatów komputera.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Może być konieczne wyeksportowanie tego certyfikatu z magazynu (`certlm.msc`) do plików `.pfx` lub `.pem` w celu użycia przez serwer WWW.

**Uwaga:** Przeglądarki i klienci HTTP (w tym `requests` Pythona domyślnie) nie będą ufać certyfikatom samopodpisany. Podczas uzyskiwania dostępu do takiego serwera otrzymasz ostrzeżenie lub błąd SSL. Do testowania będziesz musiał albo dodać ten certyfikat do zaufanych certyfikatów głównych swojego systemu/przeglądarki, albo użyć `verify=False` (dla `requests`), albo określić ścieżkę do swojego `cert.pem` za pomocą `verify='/path/to/cert.pem'`.
