# Comment résoudre l'erreur SSLCertVerificationError en Python

    Avez-vous rencontré l'erreur `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` en essayant d'effectuer une requête HTTPS en Python à l'aide de `requests` ou `urllib3` ?
Dans cet article, je vais vous montrer comment diagnostiquer et résoudre ce problème.

L'erreur signifie que Python n'a pas pu vérifier le certificat SSL/TLS du site web auquel vous vous connectez, car il n'a pas trouvé de certificat racine de confiance dans son magasin.

## Étape 1 : Diagnostiquer le problème avec OpenSSL (Recommandé)

    Avant de modifier votre code Python, vérifiez la connexion SSL à l'aide de l'utilitaire `openssl`. Cela vous aidera à comprendre si le problème est spécifique à Python ou lié aux paramètres système ou au serveur lui-même.

1.  **Installez OpenSSL** si vous ne l'avez pas (souvent préinstallé sous Linux/macOS ; pour Windows, téléchargez-le depuis le [site officiel](https://www.openssl.org/source/) ou utilisez des gestionnaires de paquets comme Chocolatey/Scoop).
2.  **Exécutez la commande** dans votre terminal (invite de commande), en remplaçant `<hostname>` par l'adresse du site web (sans `https://`) et `<port>` par le port (généralement 443 pour HTTPS) :

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Exemple pour rosstat.gov.ru :
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analysez la sortie :** Faites attention à la ligne `Verify return code`. Si elle contient une erreur comme `unable to get local issuer certificate` (code 20) ou `certificate verify failed` (code 21), cela confirme un problème de confiance dans le certificat au niveau du système ou du magasin utilisé par OpenSSL.

## Étape 2 : Choisissez une méthode de résolution

    Il existe plusieurs façons de résoudre l'erreur `SSLCertVerificationError`. Choisissez celle qui convient le mieux à votre situation.

### Méthode 1 : Désactiver la vérification SSL (Rapide, mais DANGEREUX)

    Cette méthode désactive complètement la vérification du certificat. Utilisez-la **uniquement** pour des tests temporaires, des scripts à usage unique et **uniquement** pour les sites auxquels vous faites absolument confiance.

⚠️ **Attention :** La désactivation de la vérification rend votre connexion vulnérable aux attaques de l'homme du milieu (MITM). **N'utilisez jamais `verify=False` dans le code de production ou lorsque vous travaillez avec des données sensibles !**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Exemple dURL

# Désactiver la vérification SSL
try:
    # Supprimer les avertissements de requête non sécurisée (facultatif)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Vérifier les erreurs HTTP (4xx, 5xx)

    # Votre code pour traiter la réponse, par exemple, enregistrer le fichier
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Fichier téléchargé avec succès (avec vérification SSL désactivée).")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors du téléchargement du fichier : {e}")

finally:
    # Important : Si vous avez désactivé les avertissements globalement,
    # vous voudrez peut-être les réactiver après l'exécution de la requête,
    # bien que cela ne soit généralement pas nécessaire si le script se termine.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Méthode 2 : Installer/Mettre à jour les certificats pour Python (Dépend de la plateforme)

    Python peut être livré avec des scripts pour installer ou mettre à jour l'ensemble des certificats racine du paquet `certifi`.

*   **Sur macOS :**
    1.  Accédez au dossier d'installation de Python (généralement `/Applications/Python <version>/`).
    2.  Recherchez et double-cliquez sur le fichier `Install Certificates.command`. Il installera/mettra à jour `certifi` et liera le module `ssl` standard à ces certificats.
*   **Sous Windows :**
    1.  Parfois, lors de l'installation de Python, un script `install_certificates.bat` est créé. Recherchez-le dans le répertoire `Scripts` du dossier d'installation de Python (par exemple, `C:\Users\<nom_utilisateur>\AppData\Local\Programs\Python\Python<version>\Scripts\`).
    2.  Si vous le trouvez, exécutez-le.
    3.  Si le script n'est pas présent, cette méthode ne fonctionnera probablement pas. Utilisez la méthode 3.

### Méthode 3 : Utiliser directement le paquet `certifi` (Recommandé, multiplateforme)

    C'est le moyen le plus fiable d'indiquer explicitement à Python quel ensemble de certificats racine utiliser.

1.  **Installez `certifi` :**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Utilisez `certifi` dans votre code :** Passez le chemin du fichier de certificats `certifi` au paramètre `verify` de la fonction `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Exemple dURL

    try:
        # Indiquer explicitement d'utiliser les certificats de certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Votre code pour traiter la réponse
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Fichier téléchargé avec succès à l'aide des certificats certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement du fichier : {e}")
    ```
Même si `requests` peut utiliser `certifi` par défaut, l'indication explicite `verify=certifi.where()` garantit ce comportement.

### Méthode 4 : Utiliser les magasins système ou les variables d'environnement (Avancé)

    Le module `ssl` de Python peut également rechercher des certificats dans les magasins système ou aux chemins spécifiés dans les variables d'environnement. Ceci est utile, par exemple, dans les environnements d'entreprise avec leurs propres autorités de certification (CA).

1.  **Magasins système :**
    *   **Linux/macOS :** Python utilise souvent automatiquement les certificats système (par exemple, de `/etc/ssl/certs/`). Assurez-vous que votre système dispose de certificats racine à jour (`sudo apt update && sudo apt install ca-certificates` pour Debian/Ubuntu, `sudo yum update ca-certificates` pour CentOS/RHEL).
    *   **Windows :** Python *peut* essayer d'utiliser le magasin système de Windows, mais cela ne fonctionne pas toujours de manière fiable sans paquets supplémentaires (par exemple, `python-certifi-win32`). Il est recommandé d'utiliser `certifi` (Méthode 3).
2.  **Variables d'environnement :** Vous pouvez spécifier explicitement le chemin d'un fichier ou d'un répertoire avec des certificats :
    *   `SSL_CERT_FILE` : Spécifiez le chemin d'un *fichier* (au format PEM) contenant tous les certificats racine de confiance.
    *   `SSL_CERT_DIR` : Spécifiez le chemin d'un *répertoire* où chaque certificat se trouve dans un fichier PEM séparé avec un nom de hachage (utilisez `c_rehash` d'OpenSSL pour préparer le répertoire).

    **Comment définir les variables d'environnement :

    *   **Linux/macOS (temporairement, pour la session en cours) :**
        ```bash
        export SSL_CERT_FILE=/chemin/vers/votre/ca-bundle.pem
        python votre_script.py
        ```
    *   **Windows (cmd, temporairement) :**
        ```cmd
        set SSL_CERT_FILE=C:\chemin\vers\votre\ca-bundle.pem
        python votre_script.py
        ```
    *   **Windows (PowerShell, temporairement) :**
        ```powershell
        $env:SSL_CERT_FILE = "C:\chemin\vers\votre\ca-bundle.pem"
        python votre_script.py
        ```
Pour ajouter votre propre CA (par exemple, d'entreprise), vous devez ajouter son certificat au fichier `SSL_CERT_FILE` ou au répertoire `SSL_CERT_DIR`.

## Étape 3 (Bonus) : Comment créer un certificat auto-signé pour le développement local

    Si vous développez un serveur web local (API, site) et que vous souhaitez le tester via HTTPS, vous aurez besoin d'un certificat SSL. Comme vous n'avez pas de domaine public pour obtenir un certificat d'une CA normale, vous pouvez créer un certificat *auto-signé*.

**Utilisation d'OpenSSL (multiplateforme) :**

1.  **Exécutez la commande :** Cette commande créera une clé privée (`key.pem`) et le certificat lui-même (`cert.pem`), valable 10 ans, pour `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes` : Crée une clé sans protection par mot de passe (pratique pour le développement).
    *   `-subj "/CN=localhost"` : Définit le nom commun.
    *   `-addext "subjectAltName = ..."` : Ajoute des noms alternatifs de sujet (important pour les navigateurs et clients modernes).

2.  **Utilisez `key.pem` et `cert.pem`** dans les paramètres de votre serveur web local (Flask, Django, Node.js, etc.) pour activer HTTPS.

**Utilisation de PowerShell (Windows 10/11) :**

1.  **Exécutez la commande dans PowerShell (en tant qu'administrateur) :** Cette commande créera un certificat et le placera dans le magasin de certificats de l'ordinateur.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Vous devrez peut-être exporter ce certificat du magasin (`certlm.msc`) vers des fichiers `.pfx` ou `.pem` pour qu'il soit utilisé par votre serveur web.

**Remarque :** Les navigateurs et les clients HTTP (y compris `requests` de Python par défaut) ne feront pas confiance aux certificats auto-signés. Lors de l'accès à un tel serveur, vous recevrez un avertissement ou une erreur SSL. Pour les tests, vous devrez soit ajouter ce certificat aux certificats racine de confiance de votre système/navigateur, soit utiliser `verify=False` (pour `requests`), soit spécifier le chemin de votre `cert.pem` via `verify='/chemin/vers/cert.pem'`.
