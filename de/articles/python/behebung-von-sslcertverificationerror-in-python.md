# Wie man den SSLCertVerificationError in Python behebt

    Sind Sie auf den Fehler `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` gestoßen, wenn Sie versuchen, eine HTTPS-Anfrage in Python mit `requests` oder `urllib3` zu stellen?
In diesem Artikel zeige ich Ihnen, wie Sie dieses Problem diagnostizieren und beheben können.

Der Fehler bedeutet, dass Python das SSL/TLS-Zertifikat der Webseite, mit der Sie sich verbinden, nicht überprüfen konnte, weil es kein vertrauenswürdiges Stammzertifikat in seinem Speicher gefunden hat.

## Schritt 1: Diagnose des Problems mit OpenSSL (Empfohlen)

    Bevor Sie Ihren Python-Code ändern, überprüfen Sie die SSL-Verbindung mit dem Dienstprogramm `openssl`. Dies hilft Ihnen zu verstehen, ob das Problem spezifisch für Python ist oder mit den Systemeinstellungen oder dem Server selbst zusammenhängt.

1.  **Installieren Sie OpenSSL**, falls Sie es nicht haben (oft vorinstalliert unter Linux/macOS; für Windows laden Sie es von der [offiziellen Website](https://www.openssl.org/source/) herunter oder verwenden Sie Paketmanager wie Chocolatey/Scoop).
2.  **Führen Sie den Befehl** in Ihrem Terminal (Eingabeaufforderung) aus, wobei Sie `<hostname>` durch die Webseitenadresse (ohne `https://`) und `<port>` durch den Port (normalerweise 443 für HTTPS) ersetzen:

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Beispiel für rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analysieren Sie die Ausgabe:** Achten Sie auf die Zeile `Verify return code`. Wenn sie einen Fehler wie `unable to get local issuer certificate` (Code 20) oder `certificate verify failed` (Code 21) enthält, bestätigt dies ein Problem mit dem Vertrauen in das Zertifikat auf Systemebene oder im von OpenSSL verwendeten Speicher.

## Schritt 2: Wählen Sie eine Lösungsmethode

    Es gibt mehrere Möglichkeiten, den Fehler `SSLCertVerificationError` zu beheben. Wählen Sie diejenige, die am besten zu Ihrer Situation passt.

### Methode 1: SSL-Überprüfung deaktivieren (Schnell, aber UNSICHER)

    Diese Methode deaktiviert die Zertifikatsüberprüfung vollständig. Verwenden Sie sie **nur** für temporäre Tests, einmalige Skripte und **nur** für Websites, denen Sie absolut vertrauen.

⚠️ **Warnung:** Das Deaktivieren der Überprüfung macht Ihre Verbindung anfällig für Man-in-the-Middle (MITM)-Angriffe. **Verwenden Sie niemals `verify=False` in Produktionscode oder bei der Arbeit mit sensiblen Daten!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Beispiel-URL

# SSL-Überprüfung deaktivieren
try:
    # Warnungen vor unsicheren Anfragen unterdrücken (optional)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Auf HTTP-Fehler prüfen (4xx, 5xx)

    # Ihr Code zur Verarbeitung der Antwort, z.B. Speichern der Datei
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Datei erfolgreich heruntergeladen (mit deaktivierter SSL-Überprüfung).")

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
    1.  Navigieren Sie zum Python-Installationsordner (normalerweise `/Applications/Python <Version>/`).
    2.  Suchen Sie die Datei `Install Certificates.command` und doppelklicken Sie darauf. Sie installiert/aktualisiert `certifi` und verknüpft das Standardmodul `ssl` mit diesen Zertifikaten.
*   **Unter Windows:**
    1.  Manchmal wird bei der Installation von Python ein Skript `install_certificates.bat` erstellt. Suchen Sie es im Verzeichnis `Scripts` innerhalb des Python-Installationsordners (z. B. `C:\Users\<Benutzername>\AppData\Local\Programs\Python\Python<Version>\Scripts\`).
    2.  Wenn Sie es finden, führen Sie es aus.
    3.  Wenn das Skript nicht vorhanden ist, funktioniert diese Methode wahrscheinlich nicht. Verwenden Sie Methode 3.

### Methode 3: Das `certifi`-Paket direkt verwenden (Empfohlen, plattformübergreifend)

    Dies ist die zuverlässigste Methode, um Python explizit mitzuteilen, welchen Satz von Stammzertifikaten es verwenden soll.

1.  **`certifi` installieren:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **`certifi` in Ihrem Code verwenden:** Übergeben Sie den Pfad zur `certifi`-Zertifikatsdatei an den `verify`-Parameter der `requests.get()`-Funktion.

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

    Das `ssl`-Modul von Python kann auch nach Zertifikaten in Systemspeichern oder unter Pfaden suchen, die in Umgebungsvariablen angegeben sind. Dies ist beispielsweise in Unternehmensumgebungen mit eigenen Zertifizierungsstellen (CA) nützlich.

1.  **Systemspeicher:**
    *   **Linux/macOS:** Python verwendet oft automatisch Systemzertifikate (z. B. aus `/etc/ssl/certs/`). Stellen Sie sicher, dass Ihr System über aktuelle Stammzertifikate verfügt (`sudo apt update && sudo apt install ca-certificates` für Debian/Ubuntu, `sudo yum update ca-certificates` für CentOS/RHEL).
    *   **Windows:** Python *kann* versuchen, den Windows-Systemspeicher zu verwenden, aber dies funktioniert nicht immer zuverlässig ohne zusätzliche Pakete (z. B. `python-certifi-win32`). Es wird empfohlen, `certifi` (Methode 3) zu verwenden.
2.  **Umgebungsvariablen:** Sie können den Pfad zu einer Datei oder einem Verzeichnis mit Zertifikaten explizit angeben:
    *   `SSL_CERT_FILE`: Geben Sie den Pfad zu einer *Datei* (im PEM-Format) an, die alle vertrauenswürdigen Stammzertifikate enthält.
    *   `SSL_CERT_DIR`: Geben Sie den Pfad zu einem *Verzeichnis* an, in dem sich jedes Zertifikat in einer separaten PEM-Datei mit einem Hash-ähnlichen Namen befindet (verwenden Sie `c_rehash` von OpenSSL, um das Verzeichnis vorzubereiten).

    **So legen Sie Umgebungsvariablen fest:**

    *   **Linux/macOS (temporär, für die aktuelle Sitzung):**
        ```bash
        export SSL_CERT_FILE=/pfad/zu/ihrem/ca-bundle.pem
        python ihr_skript.py
        ```
    *   **Windows (cmd, temporär):**
        ```cmd
        set SSL_CERT_FILE=C:\pfad\zu\ihrem\ca-bundle.pem
        python ihr_skript.py
        ```
    *   **Windows (PowerShell, temporär):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\pfad\zu\ihrem\ca-bundle.pem"
        python ihr_skript.py
        ```
    Um Ihre eigene (z. B. Unternehmens-) CA hinzuzufügen, müssen Sie deren Zertifikat zur Datei `SSL_CERT_FILE` oder zum Verzeichnis `SSL_CERT_DIR` hinzufügen.

## Schritt 3 (Bonus): Wie man ein selbstsigniertes Zertifikat für die lokale Entwicklung erstellt

    Wenn Sie einen lokalen Webserver (API, Website) entwickeln und diesen über HTTPS testen möchten, benötigen Sie ein SSL-Zertifikat. Da Sie keine öffentliche Domain haben, um ein Zertifikat von einer regulären CA zu erhalten, können Sie ein *selbstsigniertes* Zertifikat erstellen.

**Verwendung von OpenSSL (plattformübergreifend):**

1.  **Führen Sie den Befehl aus:** Dieser Befehl erstellt einen privaten Schlüssel (`key.pem`) und das Zertifikat selbst (`cert.pem`), gültig für 10 Jahre, für `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Erstellt einen Schlüssel ohne Passwortschutz (praktisch für die Entwicklung).
    *   `-subj "/CN=localhost"`: Legt den Common Name fest.
    *   `-addext "subjectAltName = ..."`: Fügt Subject Alternative Names hinzu (wichtig für moderne Browser und Clients).

2.  **Verwenden Sie `key.pem` und `cert.pem`** in den Einstellungen Ihres lokalen Webservers (Flask, Django, Node.js usw.), um HTTPS zu aktivieren.

**Verwendung von PowerShell (Windows 10/11):**

1.  **Führen Sie den Befehl in PowerShell (als Administrator) aus:** Dieser Befehl erstellt ein Zertifikat und legt es im Zertifikatsspeicher des Computers ab.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Möglicherweise müssen Sie dieses Zertifikat aus dem Speicher (`certlm.msc`) in `.pfx`- oder `.pem`-Dateien exportieren, damit Ihr Webserver es verwenden kann.

**Hinweis:** Browser und HTTP-Clients (einschließlich Python `requests` standardmäßig) vertrauen selbstsignierten Zertifikaten nicht. Beim Zugriff auf einen solchen Server erhalten Sie eine Warnung oder einen SSL-Fehler. Für Tests müssen Sie entweder dieses Zertifikat zu den vertrauenswürdigen Stammzertifikaten Ihres Systems/Browsers hinzufügen oder `verify=False` (für `requests`) verwenden oder den Pfad zu Ihrer `cert.pem` über `verify='/pfad/zu/cert.pem'` angeben.
