# So beheben Sie den SSLCertVerificationError in Python

    Ist Ihnen der Fehler `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` begegnet, als Sie versuchten, eine HTTPS-Anfrage in Python mit `requests` oder `urllib3` zu stellen?
In diesem Artikel zeige ich Ihnen, wie Sie dieses Problem diagnostizieren und beheben können.

Der Fehler bedeutet, dass Python das SSL/TLS-Zertifikat der Webseite, mit der Sie sich verbinden, nicht überprüfen konnte, weil es kein vertrauenswürdiges Stammzertifikat in seinem Speicher finden konnte.

## Schritt 1: Diagnose des Problems mit OpenSSL (Empfohlen)

    Bevor Sie den Python-Code ändern, überprüfen Sie die SSL-Verbindung mit dem `openssl`-Dienstprogramm. Dies hilft Ihnen zu verstehen, ob das Problem spezifisch für Python ist oder mit den Systemeinstellungen oder dem Server selbst zusammenhängt.

1.  **Installieren Sie OpenSSL**, falls Sie es nicht haben (oft auf Linux/macOS vorinstalliert; für Windows von der [offiziellen Website](https://www.openssl.org/source/) herunterladen oder Paketmanager wie Chocolatey/Scoop verwenden).
2.  **Führen Sie den Befehl** in Ihrem Terminal (Befehlszeile) aus, ersetzen Sie dabei `<hostname>` durch die Website-Adresse (ohne `https://`) und `<port>` durch den Port (normalerweise 443 für HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Beispiel für rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analysieren Sie die Ausgabe:** Achten Sie auf die Zeile `Verify return code`. Wenn sie einen Fehler wie `unable to get local issuer certificate` (Code 20) oder `certificate verify failed` (Code 21) enthält, bestätigt dies ein Problem mit dem Vertrauen in das Zertifikat auf Systemebene oder im von OpenSSL verwendeten Speicher.

## Schritt 2: Wählen Sie eine Lösungsmethode

    Es gibt mehrere Möglichkeiten, den `SSLCertVerificationError` zu beheben. Wählen Sie diejenige, die am besten zu Ihrer Situation passt.

### Methode 1: SSL-Verifizierung deaktivieren (Schnell, aber UNSICHER)

    Diese Methode deaktiviert die Zertifikatsprüfung vollständig. Verwenden Sie sie **nur** für temporäre Tests, einmalige Skripte und **nur** für Websites, denen Sie absolut vertrauen.

⚠️ **Warnung:** Das Deaktivieren der Überprüfung macht Ihre Verbindung anfällig für Man-in-the-Middle (MITM)-Angriffe. **Verwenden Sie `verify=False` niemals in Produktionscode oder bei der Arbeit mit sensiblen Daten!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Beispiel-URL

# SSL-Verifizierung deaktivieren
try:
    # Warnungen über unsichere Anfragen unterdrücken (optional)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Auf HTTP-Fehler prüfen (4xx, 5xx)

    # Ihr Code zur Verarbeitung der Antwort, z.B. Speichern einer Datei
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Datei erfolgreich heruntergeladen (mit deaktivierter SSL-Verifizierung).")

except requests.exceptions.RequestException as e:
    print(f"Fehler beim Herunterladen der Datei: {e}")

finally:
    # Wichtig: Wenn Sie Warnungen global deaktiviert haben,
    # möchten Sie diese möglicherweise nach Abschluss der Anfrage wieder aktivieren,
    # obwohl dies normalerweise nicht erforderlich ist, wenn das Skript beendet wird.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Methode 2: Zertifikate für Python installieren/aktualisieren (Plattformabhängig)

    Python kann mit Skripten geliefert werden, um den Satz von Stammzertifikaten aus dem `certifi`-Paket zu installieren oder zu aktualisieren.

*   **Unter macOS:**
    1.  Gehen Sie zum Python-Installationsordner (normalerweise `/Applications/Python <version>/`).
    2.  Suchen Sie die Datei `Install Certificates.command` und doppelklicken Sie darauf. Sie installiert/aktualisiert `certifi` und verknüpft das Standard-`ssl`-Modul mit diesen Zertifikaten.
*   **Unter Windows:**
    1.  Manchmal wird bei der Python-Installation ein Skript `install_certificates.bat` erstellt. Suchen Sie es im `Scripts`-Verzeichnis innerhalb des Python-Installationsordners (z.B. `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\`).
    2.  Wenn Sie es finden, führen Sie es aus.
    3.  Wenn das Skript nicht vorhanden ist, funktioniert diese Methode höchstwahrscheinlich nicht. Verwenden Sie Methode 3.

### Methode 3: Das `certifi`-Paket direkt verwenden (Empfohlen, plattformübergreifend)

    Dies ist der zuverlässigste Weg, Python explizit mitzuteilen, welchen Satz von Stammzertifikaten es verwenden soll.

1.  **Installieren Sie `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Verwenden Sie `certifi` in Ihrem Code:** Übergeben Sie den Pfad zur `certifi`-Zertifikatsdatei an den `verify`-Parameter der Funktion `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Beispiel-URL

    try:
        # Explizit angeben, dass Zertifikate von certifi verwendet werden sollen
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Ihr Code zur Verarbeitung der Antwort
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Datei erfolgreich mit certifi-Zertifikaten heruntergeladen.")

    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Herunterladen der Datei: {e}")
    ```
    Auch wenn `requests` `certifi` standardmäßig verwenden kann, garantiert die explizite Angabe von `verify=certifi.where()` dieses Verhalten.

### Methode 4: Systemspeicher oder Umgebungsvariablen verwenden (Fortgeschritten)

    Das Python-`ssl`-Modul kann auch in Systemspeichern oder in Pfaden nach Zertifikaten suchen, die in Umgebungsvariablen angegeben sind. Dies ist nützlich, z.B. in Unternehmensumgebungen mit eigenen Zertifizierungsstellen (CAs).

1.  **Systemspeicher:**
    *   **Linux/macOS:** Python verwendet oft automatisch Systemzertifikate (z.B. von `/etc/ssl/certs/`). Stellen Sie sicher, dass Ihr System über aktuelle Stammzertifikate verfügt (`sudo apt update && sudo apt install ca-certificates` für Debian/Ubuntu, `sudo yum update ca-certificates` für CentOS/RHEL).
    *   **Windows:** Python *kann* versuchen, den Windows-Systemspeicher zu verwenden, aber dies funktioniert nicht immer zuverlässig ohne zusätzliche Pakete (z.B. `python-certifi-win32`). Es wird empfohlen, `certifi` (Methode 3) zu verwenden.
2.  **Umgebungsvariablen:** Sie können den Pfad zu einer Datei oder einem Verzeichnis mit Zertifikaten explizit angeben:
    *   `SSL_CERT_FILE`: Geben Sie den Pfad zu einer *Datei* (im PEM-Format) an, die alle vertrauenswürdigen Stammzertifikate enthält.
    *   `SSL_CERT_DIR`: Geben Sie den Pfad zu einem *Verzeichnis* an, in dem sich jedes Zertifikat in einer separaten PEM-Datei mit einem Namen in Form eines Hashs befindet (verwenden Sie `c_rehash` von OpenSSL, um das Verzeichnis vorzubereiten).

    **So legen Sie Umgebungsvariablen fest:**

    *   **Linux/macOS (temporär, für die aktuelle Sitzung):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, temporär):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, temporär):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Um Ihre eigene (z.B. Unternehmens-) CA hinzuzufügen, müssen Sie deren Zertifikat zur Datei `SSL_CERT_FILE` oder zum Verzeichnis `SSL_CERT_DIR` hinzufügen.

## Schritt 3 (Bonus): So erstellen Sie ein selbstsigniertes Zertifikat für die lokale Entwicklung

    Wenn Sie einen lokalen Webserver (API, Website) entwickeln und diesen über HTTPS testen möchten, benötigen Sie ein SSL-Zertifikat. Da Sie keine öffentliche Domain haben, um ein Zertifikat von einer regulären CA zu erhalten, können Sie ein *selbstsigniertes* Zertifikat erstellen.

**Verwendung von OpenSSL (plattformübergreifend):**

1.  **Führen Sie den Befehl aus:** Dieser Befehl erstellt einen privaten Schlüssel (`key.pem`) und das Zertifikat selbst (`cert.pem`), gültig für 10 Jahre, für `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Erstellt einen Schlüssel ohne Passwort (praktisch für die Entwicklung).
    *   `-subj "/CN=localhost"`: Legt den Common Name fest.
    *   `-addext "subjectAltName = ..."`: Fügt Subject Alternative Names hinzu (wichtig für moderne Browser und Clients).

2.  **Verwenden Sie `key.pem` und `cert.pem`** in den Einstellungen Ihres lokalen Webservers (Flask, Django, Node.js usw.), um HTTPS zu aktivieren.

**Verwendung von PowerShell (Windows 10/11):**

1.  **Führen Sie den Befehl in PowerShell (mit Administratorrechten) aus:** Dieser Befehl erstellt ein Zertifikat und legt es im Zertifikatspeicher des Computers ab.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Möglicherweise müssen Sie dieses Zertifikat aus dem Speicher (`certlm.msc`) in `.pfx`- oder `.pem`-Dateien exportieren, damit Ihr Webserver es verwenden kann.

**Hinweis:** Browser und HTTP-Clients (einschließlich Python `requests` standardmäßig) vertrauen selbstsignierten Zertifikaten nicht. Beim Zugriff auf einen solchen Server erhalten Sie eine Warnung oder einen SSL-Fehler. Zum Testen müssen Sie entweder dieses Zertifikat zu den vertrauenswürdigen Stammzertifikaten Ihres Systems/Browsers hinzufügen oder `verify=False` (für `requests`) verwenden oder den Pfad zu Ihrer `cert.pem` über `verify='/path/to/cert.pem'` angeben.
