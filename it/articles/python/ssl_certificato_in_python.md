# Come risolvere l'errore SSLCertVerificationError in Python

    Hai riscontrato l'errore `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` quando hai provato a effettuare una richiesta HTTPS in Python usando `requests` o `urllib3`? 
In questo articolo ti mostrerò come diagnosticare e risolvere questo problema.

L'errore significa che Python non è riuscito a verificare il certificato SSL/TLS del sito web a cui ti stai connettendo, perché non ha trovato un certificato radice attendibile nel suo archivio.

## Passaggio 1: Diagnostica del problema con OpenSSL (Consigliato)

    Prima di modificare il codice Python, verifica la connessione SSL usando l'utilità `openssl`. Questo ti aiuterà a capire se il problema è specifico di Python o è correlato alle impostazioni di sistema o al server stesso.

1.  **Installa OpenSSL**, se non lo hai già (spesso preinstallato in Linux/macOS; per Windows scaricalo dal [sito ufficiale](https://www.openssl.org/source/) o usa gestori di pacchetti come Chocolatey/Scoop).
2.  **Esegui il comando** nel tuo terminale (prompt dei comandi), sostituendo `<hostname>` con l'indirizzo del sito (senza `https://`) e `<port>` con la porta (solitamente 443 per HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Esempio per rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analizza l'output:** Presta attenzione alla riga `Verify return code`. Se contiene un errore come `unable to get local issuer certificate` (codice 20) o `certificate verify failed` (codice 21), ciò conferma un problema di fiducia del certificato a livello di sistema o dell'archivio utilizzato da OpenSSL.

## Passaggio 2: Scegli il metodo di risoluzione

    Esistono diversi modi per risolvere l'errore `SSLCertVerificationError`. Scegli quello più adatto alla tua situazione.

### Metodo 1: Disabilitare la verifica SSL (Veloce, ma NON SICURO)

    Questo metodo disabilita completamente la verifica del certificato. Usalo **solo** per test temporanei, script monouso e **solo** per siti di cui ti fidi assolutamente.

⚠️ **Attenzione:** La disabilitazione della verifica rende la tua connessione vulnerabile agli attacchi "man-in-the-middle" (MITM). **Non usare mai `verify=False` nel codice di produzione o quando lavori con dati sensibili!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # URL di esempio

# Disabilita la verifica SSL
try:
    # Sopprimi gli avvisi di richiesta non sicura (opzionale)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Controlla gli errori HTTP (4xx, 5xx)

    # Il tuo codice per elaborare la risposta, ad esempio salvare il file
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("File scaricato con successo (con verifica SSL disabilitata).")

except requests.exceptions.RequestException as e:
    print(f"Errore durante il download del file: {e}")

finally:
    # Importante: Se hai disabilitato gli avvisi globalmente,
    # potresti volerli riabilitare dopo aver eseguito la richiesta,
    # anche se di solito non è necessario se lo script termina.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Metodo 2: Installare/Aggiornare i certificati per Python (Dipende dalla piattaforma)

    Python può essere fornito con script per installare o aggiornare il set di certificati radice dal pacchetto `certifi`.

*   **Su macOS:**
    1.  Vai alla cartella di installazione di Python (solitamente `/Applications/Python <versione>/`).
    2.  Trova e fai doppio clic sul file `Install Certificates.command`. Questo installerà/aggiornerà `certifi` e collegherà il modulo `ssl` standard a questi certificati.
*   **Su Windows:**
    1.  A volte, durante l'installazione di Python, viene creato uno script `install_certificates.bat`. Cercalo nella directory `Scripts` all'interno della cartella di installazione di Python (ad esempio, `C:\Users\<nome_utente>\AppData\Local\Programs\Python\Python<versione>\Scripts\`).
    2.  Se lo trovi, eseguilo.
    3.  Se lo script non esiste, questo metodo probabilmente non funzionerà. Usa il Metodo 3.

### Metodo 3: Usare il pacchetto `certifi` direttamente (Consigliato, multipiattaforma)

    Questo è il modo più affidabile per specificare esplicitamente a Python quale set di certificati radice utilizzare.

1.  **Installa `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Usa `certifi` nel tuo codice:** Passa il percorso del file di certificati `certifi` al parametro `verify` della funzione `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # URL di esempio

    try:
        # Specifica esplicitamente di usare i certificati da certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Il tuo codice per elaborare la risposta
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("File scaricato con successo usando i certificati certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Errore durante il download del file: {e}")
    ```
    Anche se `requests` può usare `certifi` per impostazione predefinita, specificare esplicitamente `verify=certifi.where()` garantisce questo comportamento.

### Metodo 4: Usare archivi di sistema o variabili d'ambiente (Avanzato)

    Il modulo `ssl` di Python può anche cercare certificati negli archivi di sistema o nei percorsi specificati nelle variabili d'ambiente. Questo è utile, ad esempio, in ambienti aziendali con le proprie autorità di certificazione (CA).

1.  **Archivi di sistema:**
    *   **Linux/macOS:** Python spesso utilizza automaticamente i certificati di sistema (ad esempio, da `/etc/ssl/certs/`). Assicurati che il tuo sistema abbia certificati radice aggiornati (`sudo apt update && sudo apt install ca-certificates` per Debian/Ubuntu, `sudo yum update ca-certificates` per CentOS/RHEL).
    *   **Windows:** Python *potrebbe* tentare di utilizzare l'archivio di sistema di Windows, ma questo non sempre funziona in modo affidabile senza pacchetti aggiuntivi (ad esempio, `python-certifi-win32`). Si consiglia di utilizzare `certifi` (Metodo 3).
2.  **Variabili d'ambiente:** Puoi specificare esplicitamente il percorso di un file o di una directory con i certificati:
    *   `SSL_CERT_FILE`: Specifica il percorso di un *file* (in formato PEM), contenente tutti i certificati radice attendibili.
    *   `SSL_CERT_DIR`: Specifica il percorso di una *directory* in cui ogni certificato si trova in un file PEM separato con un nome hash (usa `c_rehash` da OpenSSL per preparare la directory).

    **Come impostare le variabili d'ambiente:**

    *   **Linux/macOS (temporaneamente, per la sessione corrente):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, temporaneamente):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, temporaneamente):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Per aggiungere la tua CA (ad esempio, aziendale), devi aggiungere il suo certificato al file `SSL_CERT_FILE` o alla directory `SSL_CERT_DIR`.

## Passaggio 3 (Bonus): Come creare un certificato autofirmato per lo sviluppo locale

    Se stai sviluppando un server web locale (API, sito) e vuoi testarlo tramite HTTPS, avrai bisogno di un certificato SSL. Poiché non hai un dominio pubblico per ottenere un certificato da una CA normale, puoi creare un certificato *autofirmato*.

**Utilizzo di OpenSSL (multipiattaforma):**

1.  **Esegui il comando:** Questo comando creerà una chiave privata (`key.pem`) e il certificato stesso (`cert.pem`), valido per 10 anni, per `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Crea una chiave senza protezione con password (comodo per lo sviluppo).
    *   `-subj "/CN=localhost"`: Imposta il Common Name.
    *   `-addext "subjectAltName = ..."`: Aggiunge i Subject Alternative Names (importante per i browser e i client moderni).

2.  **Usa `key.pem` e `cert.pem`** nelle impostazioni del tuo server web locale (Flask, Django, Node.js, ecc.) per abilitare HTTPS.

**Utilizzo di PowerShell (Windows 10/11):**

1.  **Esegui il comando in PowerShell (con diritti di amministratore):** Questo comando creerà un certificato e lo inserirà nell'archivio certificati del computer.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Potrebbe essere necessario esportare questo certificato dall'archivio (`certlm.msc`) in file `.pfx` o `.pem` per l'utilizzo da parte del tuo server web.

**Nota:** I browser e i client HTTP (incluso Python `requests` per impostazione predefinita) non si fideranno dei certificati autofirmati. Quando accedi a un tale server, riceverai un avviso o un errore SSL. Per i test, dovrai aggiungere questo certificato ai certificati radice attendibili del tuo sistema/browser, oppure usare `verify=False` (per `requests`), oppure specificare il percorso del tuo `cert.pem` tramite `verify='/path/to/cert.pem'`.
