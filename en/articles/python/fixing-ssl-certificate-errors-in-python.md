# How to fix SSLCertVerificationError in Python

    Encountered `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` when trying to make an HTTPS request in Python using `requests` or `urllib3`?
In this article, I will show you how to diagnose and fix this problem.

The error means that Python could not verify the SSL/TLS certificate of the website you are connecting to because it did not find a trusted root certificate in its store.

## Step 1: Diagnose the problem with OpenSSL (Recommended)

    Before changing your Python code, check the SSL connection using the `openssl` utility. This will help you understand if the problem is specific to Python or related to system settings or the server itself.

1.  **Install OpenSSL** if you don't have it (often pre-installed in Linux/macOS; for Windows, download from the [official website](https://www.openssl.org/source/) or use package managers like Chocolatey/Scoop).
2.  **Execute the command** in your terminal (command prompt), replacing `<hostname>` with the website address (without `https://`) and `<port>` with the port (usually 443 for HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Example for rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analyze the output:** Pay attention to the `Verify return code` line. If it contains an error like `unable to get local issuer certificate` (code 20) or `certificate verify failed` (code 21), this confirms a problem with trust in the certificate at the system level or the store used by OpenSSL.

## Step 2: Choose a solution method

    There are several ways to fix the `SSLCertVerificationError`. Choose the one that best suits your situation.

### Method 1: Disable SSL verification (Fast, but UNSAFE)

    This method completely disables certificate verification. Use it **only** for temporary testing, one-time scripts, and **only** for sites you absolutely trust.

⚠️ **Warning:** Disabling verification makes your connection vulnerable to man-in-the-middle (MITM) attacks. **Never use `verify=False` in production code or when working with sensitive data!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Example URL

# Disable SSL verification
try:
    # Suppress insecure request warnings (optional)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Check for HTTP errors (4xx, 5xx)

    # Your code to process the response, e.g., saving the file
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("File successfully downloaded (with SSL verification disabled).")

except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")

finally:
    # Important: If you disabled warnings globally,
    # you might want to re-enable them after the request is complete,
    # although this is usually not required if the script exits.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Method 2: Install/Update certificates for Python (Platform-dependent)

    Python may come with scripts to install or update the set of root certificates from the `certifi` package.

*   **On macOS:**
    1.  Navigate to the Python installation folder (usually `/Applications/Python <version>/`).
    2.  Find and double-click the `Install Certificates.command` file. It will install/update `certifi` and link the standard `ssl` module to these certificates.
*   **On Windows:**
    1.  Sometimes, when installing Python, an `install_certificates.bat` script is created. Look for it in the `Scripts` directory within the Python installation folder (e.g., `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\`).
    2.  If you find it, run it.
    3.  If the script is not present, this method will likely not work. Use Method 3.

### Method 3: Use the `certifi` package directly (Recommended, cross-platform)

    This is the most reliable way to explicitly tell Python which set of root certificates to use.

1.  **Install `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Use `certifi` in your code:** Pass the path to the `certifi` certificate file to the `verify` parameter of the `requests.get()` function.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Example URL

    try:
        # Explicitly specify to use certificates from certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Your code to process the response
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("File successfully downloaded using certifi certificates.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    ```
    Even if `requests` can use `certifi` by default, explicitly specifying `verify=certifi.where()` guarantees this behavior.

### Method 4: Use system stores or environment variables (Advanced)

    Python's `ssl` module can also look for certificates in system stores or at paths specified in environment variables. This is useful, for example, in corporate environments with their own Certificate Authorities (CA).

1.  **System stores:**
    *   **Linux/macOS:** Python often automatically uses system certificates (e.g., from `/etc/ssl/certs/`). Make sure your system has up-to-date root certificates (`sudo apt update && sudo apt install ca-certificates` for Debian/Ubuntu, `sudo yum update ca-certificates` for CentOS/RHEL).
    *   **Windows:** Python *may* try to use the Windows system store, but this does not always work reliably without additional packages (e.g., `python-certifi-win32`). It is recommended to use `certifi` (Method 3).
2.  **Environment variables:** You can explicitly specify the path to a file or directory with certificates:
    *   `SSL_CERT_FILE`: Specify the path to a *file* (in PEM format) containing all trusted root certificates.
    *   `SSL_CERT_DIR`: Specify the path to a *directory* where each certificate is in a separate PEM file with a hash-like name (use `c_rehash` from OpenSSL to prepare the directory).

    **How to set environment variables:**

    *   **Linux/macOS (temporarily, for current session):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, temporarily):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, temporarily):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    To add your own (e.g., corporate) CA, you need to add its certificate to the `SSL_CERT_FILE` or `SSL_CERT_DIR`.

## Step 3 (Bonus): How to create a self-signed certificate for local development

    If you are developing a local web server (API, website) and want to test it over HTTPS, you will need an SSL certificate. Since you do not have a public domain to obtain a certificate from a regular CA, you can create a *self-signed* certificate.

**Using OpenSSL (cross-platform):**

1.  **Execute the command:** This command will create a private key (`key.pem`) and the certificate itself (`cert.pem`), valid for 10 years, for `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Creates a key without password protection (convenient for development).
    *   `-subj "/CN=localhost"`: Sets the Common Name.
    *   `-addext "subjectAltName = ..."`: Adds Subject Alternative Names (important for modern browsers and clients).

2.  **Use `key.pem` and `cert.pem`** in your local web server settings (Flask, Django, Node.js, etc.) to enable HTTPS.

**Using PowerShell (Windows 10/11):**

1.  **Execute the command in PowerShell (as administrator):** This command will create a certificate and place it in the computer's certificate store.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    You may need to export this certificate from the store (`certlm.msc`) to `.pfx` or `.pem` files for use by your web server.

**Note:** Browsers and HTTP clients (including Python `requests` by default) will not trust self-signed certificates. When accessing such a server, you will receive a warning or SSL error. For tests, you will need to either add this certificate to your system's/browser's trusted root certificates, or use `verify=False` (for `requests`), or specify the path to your `cert.pem` via `verify='/path/to/cert.pem'`.
