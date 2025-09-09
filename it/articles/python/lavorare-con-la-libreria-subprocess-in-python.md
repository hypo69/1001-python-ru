## Lavorare con la libreria `subprocess` in Python


### 1. **Cos'è `subprocess` e a cosa serve?**

Il modulo `subprocess` in Python fornisce un'interfaccia per creare nuovi processi,
collegarsi ai loro flussi di input/output/errore e ottenere i loro codici di ritorno.
Consente agli script Python di avviare e gestire altri programmi,
scritti in qualsiasi linguaggio, che si tratti di utilità di sistema, script di shell o altri eseguibili.

**Contesto storico:**

Prima di `subprocess`, per avviare processi esterni venivano utilizzate funzioni del modulo `os`, come `os.system()`, `os.spawn*()`, nonché il modulo `commands` (in Python 2). Questi approcci presentavano una serie di svantaggi:
*   `os.system()`: Esegue un comando tramite la shell di sistema, il che è insicuro quando si lavora con input utente e meno flessibile nella gestione dei flussi.
*   `os.spawn*()`: Più flessibili, ma complessi da usare e dipendenti dalla piattaforma.
*   Il modulo `popen2` (e le sue varianti): Forniva accesso ai flussi, ma era complesso e presentava problemi di blocco.

Il modulo `subprocess` è stato introdotto in Python 2.4 (PEP 324) come un modo unificato e più sicuro per interagire con i processi figli. Incapsula le migliori funzionalità dei moduli precedenti e fornisce un'API più pulita.

**Principali attività risolte con `subprocess`:**

*   Esecuzione di comandi del sistema operativo (ad esempio, `ls`, `dir`, `ping`).
*   Avvio di utilità esterne per l'elaborazione dei dati (ad esempio, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Integrazione con sistemi di controllo versione (`git`, `svn`).
*   Avvio di compilatori o interpreti di altri linguaggi.
*   Automazione dell'amministrazione di sistema.
*   Organizzazione dell'interazione tra diversi programmi.

--- 

### 2. Funzioni e classi principali

Il modulo `subprocess` offre diversi modi per avviare processi:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Questa è l'API di alto livello **consigliata**, introdotta in Python 3.5.
    *   Esegue un comando, attende il suo completamento e restituisce un oggetto `CompletedProcess`.
    *   Adatto per la maggior parte dei casi in cui è necessario semplicemente eseguire un comando e ottenere il risultato.

    ```python
    import subprocess

    # Esecuzione semplice
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Se check=True e il comando restituisce un valore diverso da 0, verrà sollevato CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Questa è la classe principale per la creazione e la gestione dei processi figli.
    *   Fornisce la massima flessibilità: avvio non bloccante, controllo dettagliato dei flussi I/O, possibilità di inviare segnali al processo.
    *   La funzione `run()` utilizza `Popen` internamente.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Processo avviato con PID: {process.pid}")
    # ... può fare altro lavoro ...
    process.wait() # Attendi il completamento
    print(f"Processo terminato con codice: {process.returncode}")
    ```

*   **Funzioni deprecate, ma ancora presenti (prima di Python 3.5 erano l'API principale):**
    *   `subprocess.call(args, ...)`: Esegue un comando e attende il suo completamento. Restituisce il codice di ritorno. Simile a `os.system()`, ma più sicuro se `shell=False`.
    *   `subprocess.check_call(args, ...)`: Come `call()`, ma solleva `CalledProcessError` se il codice di ritorno non è 0.
    *   `subprocess.check_output(args, ...)`: Esegue un comando, attende il suo completamento e restituisce la sua output standard (stdout) come stringa di byte. Solleva `CalledProcessError` se il codice di ritorno non è 0.

    Sebbene queste funzioni funzionino ancora, `subprocess.run()` fornisce un'interfaccia più comoda e unificata per le stesse attività.

--- 

### 3. Argomenti chiave delle funzioni `run()` e `Popen()`

Questi argomenti consentono di configurare finemente l'avvio e l'interazione con il processo figlio:

*   **`args`**:
    *   Primo e obbligatorio argomento.
    *   Può essere un elenco di stringhe (consigliato) o una singola stringa (se `shell=True`).
    *   Il primo elemento dell'elenco è il nome dell'eseguibile, gli altri sono i suoi argomenti.
    *   Esempio: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**:
    *   Determinano come verranno gestiti l'input, l'output e i flussi di errore standard del processo figlio.
    *   Valori possibili:
        *   `None` (predefinito): Ereditati dal processo padre.
        *   `subprocess.PIPE`: Viene creata una pipe, attraverso la quale è possibile scambiare dati. `process.stdin`, `process.stdout`, `process.stderr` diventano oggetti simili a file.
        *   `subprocess.DEVNULL`: Reindirizza il flusso a "nessun luogo" (analogo a `/dev/null`).
        *   Un descrittore di file aperto (un numero intero).
        *   Un oggetto file esistente (ad esempio, un file aperto `open('output.txt', 'w')`).

*   **`capture_output=True` (per `run()`):**
    *   Un'opzione comoda, equivalente all'impostazione di `stdout=subprocess.PIPE` e `stderr=subprocess.PIPE`.
    *   Il risultato sarà disponibile in `result.stdout` e `result.stderr`.

*   **`text=True` (o `universal_newlines=True` per compatibilità):**
    *   Se `True`, i flussi `stdout` e `stderr` (così come `stdin`, se viene passata una stringa) verranno aperti in modalità testo utilizzando la codifica predefinita (solitamente UTF-8). La decodifica/codifica avviene automaticamente.
    *   Se `False` (predefinito), i flussi vengono trattati come byte.
    *   A partire da Python 3.7, `text` è l'alias preferito per `universal_newlines`. Puoi anche specificare una codifica specifica tramite `encoding` e un gestore di errori tramite `errors`.

*   **`shell=False` (predefinito):**
    *   Se `False` (consigliato per motivi di sicurezza e prevedibilità), `args` deve essere un elenco. Il comando viene avviato direttamente.
    *   Se `True`, `args` viene passato come stringa alla shell di sistema (ad esempio, `/bin/sh` su Unix, `cmd.exe` su Windows) per l'interpretazione. Ciò consente di utilizzare le funzionalità della shell (variabili, sostituzioni, pipe), ma è **PERICOLOSO** se `args` contiene input utente non attendibile (rischio di iniezione di comandi).

*   **`cwd=None`:**
    *   Imposta la directory di lavoro corrente per il processo figlio. Per impostazione predefinita, eredita dal processo padre.

*   **`env=None`:**
    *   Un dizionario che definisce le variabili d'ambiente per il nuovo processo. Per impostazione predefinita, l'ambiente del processo padre viene ereditato. Se specificato, sostituisce completamente l'ambiente ereditato. Per aggiungere/modificare variabili mantenendo le altre, è necessario prima copiare `os.environ` e quindi modificarlo.

*   **`timeout=None`:**
    *   Tempo massimo in secondi consentito per l'esecuzione del comando. Se il processo non si completa entro questo tempo, verrà sollevata un'eccezione `subprocess.TimeoutExpired`. `Popen.communicate()` accetta anche `timeout`.

*   **`check=False` (per `run()`):**
    *   Se `True` e il processo termina con un codice di ritorno diverso da zero, verrà sollevata un'eccezione `subprocess.CalledProcessError`.

--- 

### 4. Lavorare con risultati ed errori

**Oggetto `CompletedProcess` (risultato di `run()`):**

```python
import subprocess

try:
    # Tenta di eseguire un comando che potrebbe fallire
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - errore di battitura per dimostrazione
        capture_output=True,
        text=True,
        check=True, # Solleverà un'eccezione se returncode != 0
        timeout=10
    )
    print("Comando eseguito con successo.")
    print("Codice di ritorno:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Solitamente vuoto in caso di successo

except subprocess.CalledProcessError as e:
    print(f"Errore di esecuzione del comando (CalledProcessError):")
    print(f"  Comando: {e.cmd}")
    print(f"  Codice di ritorno: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Potrebbe contenere output prima dell'errore
    print(f"  Stderr: {e.stderr}") # Solitamente qui le informazioni sull'errore
except subprocess.TimeoutExpired as e:
    print(f"Il comando non è stato completato entro {e.timeout} secondi.")
    print(f"  Comando: {e.cmd}")
    if e.stdout: print(f"  Stdout (parziale): {e.stdout.decode(errors='ignore')}") # stdout è in byte
    if e.stderr: print(f"  Stderr (parziale): {e.stderr.decode(errors='ignore')}") # stderr è in byte
except FileNotFoundError:
    print("Errore: comando o programma non trovato.")
except Exception as e:
    print(f"Si è verificato un altro errore: {e}")
```

**Attributi di `CompletedProcess`:**
*   `args`: Argomenti usati per avviare il processo.
*   `returncode`: Codice di ritorno del processo. 0 di solito significa successo.
*   `stdout`: Output standard del processo (byte o stringa, se `text=True` e `capture_output=True`).
*   `stderr`: Flusso di errore standard del processo (byte o stringa, se `text=True` e `capture_output=True`).

**Eccezioni:**
*   `subprocess.CalledProcessError`: Sollevata se `check=True` (per `run()`) o se vengono usati `check_call()`, `check_output()` e il comando è terminato con un codice diverso da zero. Contiene `returncode`, `cmd`, `output` (o `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Se si è verificato un timeout. Contiene `cmd`, `timeout`, `stdout`, `stderr` (output parziale, se presente).
*   `FileNotFoundError`: Se l'eseguibile non viene trovato.

**Interazione con l'oggetto `Popen`:**

La classe `Popen` offre maggiore controllo:

```python
import subprocess
import time

# Avvia il processo in background
process = subprocess.Popen(["sleep", "5"])
print(f"Processo PID: {process.pid} avviato.")

# Controllo dello stato non bloccante
while process.poll() is None: # poll() restituisce None se il processo è ancora in esecuzione
    print("Processo ancora in esecuzione...")
    # Può leggere l'output man mano che arriva (attenzione, può bloccare!)
    # line = process.stdout.readline()
    # if line: print(f"Output: {line.strip()}")
    time.sleep(1)

# Attendi il completamento e ottieni tutto l'output/errori
# stdout_data, stderr_data = process.communicate(timeout=10) # Modo sicuro

# Se communicate() non è stato usato, dopo poll() != None, è possibile leggere il resto
if process.stdout:
    for line in process.stdout:
        print(f"Output finale: {line.strip()}")

print(f"Processo terminato con codice: {process.returncode}")

# Se è necessaria la terminazione forzata
# process.terminate() # Invia SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Se non terminato
#     process.kill()      # Invia SIGKILL
```

*   `process.poll()`: Controlla se il processo figlio è terminato. Restituisce il codice di ritorno o `None`. Non bloccante.
*   `process.wait(timeout=None)`: Attende che il processo figlio termini. Restituisce il codice di ritorno. Bloccante.
*   `process.communicate(input=None, timeout=None)`:
    *   Il modo più sicuro per interagire con un processo quando vengono usati `PIPE`.
    *   Invia dati a `stdin` (se `input` è specificato), legge tutti i dati da `stdout` e `stderr` fino alla fine e attende che il processo termini.
    *   Restituisce una tupla `(stdout_data, stderr_data)`.
    *   Aiuta a evitare deadlock che possono verificarsi con la lettura/scrittura diretta in `process.stdout`/`process.stdin` se i buffer si riempiono.
*   `process.terminate()`: Invia un segnale `SIGTERM` al processo (terminazione graziosa).
*   `process.kill()`: Invia un segnale `SIGKILL` al processo (terminazione forzata).
*   `process.send_signal(signal)`: Invia il segnale specificato al processo.
*   `process.stdin`, `process.stdout`, `process.stderr`: Oggetti simili a file per le pipe, se sono stati creati con `PIPE`.

--- 

### 5. Scenari di utilizzo avanzati

**Reindirizzamento dell'output di un comando all'input di un altro (pipeline):**

Emulazione di `ps aux | grep python`:

```python
import subprocess

# Avvia il primo comando, il suo stdout sarà PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Avvia il secondo comando, il suo stdin sarà stdout del primo comando
# stdout del secondo comando anche PIPE, per leggere il risultato
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Collega stdout da ps a stdin per grep
    stdout=subprocess.PIPE,
    text=True
)

# Importante! Chiudi stdout del primo comando nel processo padre,
# in modo che grep riceva EOF quando ps termina.
if ps_process.stdout:
    ps_process.stdout.close()

# Ottieni l'output da grep
stdout_data, stderr_data = grep_process.communicate()

print("Risultato della pipeline:")
print(stdout_data)

if stderr_data:
    print("Errori grep:", stderr_data)

# Assicurati che entrambi i processi siano terminati
ps_process.wait() 
# grep_process.wait() # communicate() ha già atteso
print(f"Codice di ritorno ps: {ps_process.returncode}")
print(f"Codice di ritorno grep: {grep_process.returncode}")
```
*Nota:* Per pipeline semplici, `subprocess.run("ps aux | grep python", shell=True, ...)` potrebbe essere più semplice, ma meno sicuro e flessibile.

**Avvio di processi asincroni:**

`Popen` è intrinsecamente non bloccante. Puoi avviare più processi e gestirli in parallelo.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Comando con errore
]

processes = []
for cmd_args in commands:
    print(f"Avvio: {' '.join(cmd_args)}")
    # Per l'asincronia, stdout/stderr è meglio reindirizzarli,
    # per evitare di interferire tra loro o con la console del padre.
    # DEVNULL se l'output non è necessario, PIPE se necessario in seguito.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Fai altro lavoro o attendi il completamento
while any(p.poll() is None for p in processes):
    print("In attesa del completamento di tutti i processi...")
    time.sleep(0.5)

print("\nRisultati:")
for i, p in enumerate(processes):
    print(f"Comando '{' '.join(commands[i])}' completato con codice: {p.returncode}")
```

**Interazione interattiva con il processo:**

Questo è un compito complesso, che richiede un'attenta gestione dei flussi per evitare deadlock. `communicate()` è buono per lo scambio una tantum. Per una sessione interattiva prolungata, potrebbe essere necessaria la lettura/scrittura diretta in `p.stdin`, `p.stdout`, `p.stderr` utilizzando I/O non bloccante o thread separati.

```python
import subprocess

# Esempio: avvio di una sessione python interattiva
process = subprocess.Popen(
    ['python', '-i'], # -i per la modalità interattiva
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Buffering di linea per stdout/stderr (per l'interattività)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Importante!

def read_output():
    # La lettura dell'output può essere complessa, poiché è necessario sapere quando fermarsi.
    # Questo è un esempio molto semplificato. Per compiti reali sono necessarie soluzioni più robuste.
    # Ad esempio, leggere fino a un certo pattern (prompt della riga di comando).
    output = ""
    # Leggi stdout. In un'applicazione reale, questo dovrebbe essere fatto in modo non bloccante o in un thread separato.
    # Qui si presume che dopo un comando ci sarà un output immediato.
    # Questa è un'ipotesi molto fragile per il caso generale!
    try:
        # Popen non ha readline con timeout, questa è una delle difficoltà
        # Può usare select su process.stdout.fileno()
        # o leggere carattere per carattere/riga per riga in un thread separato
        # Per semplicità, questo non è incluso qui
        while True: # Attenzione, può bloccare!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Rilevatore di prompt primitivo
                output += line
                break
            output += line
    except Exception as e:
        print(f"Errore di lettura: {e}")
    return output.strip()

# Inizializzazione: leggi il prompt iniziale
initial_output = ""
# Leggi il saluto di Python
# Questo è molto semplificato, poiché non sappiamo esattamente quante righe leggere
for _ in range(5): # Prova a leggere alcune righe
    try:
        # Popen stdout non ha timeout, è necessario leggere attentamente
        # stdout.readline() può bloccare.
        # Nelle applicazioni reali, qui sono necessari select o thread.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Prompt trovato
    except BlockingIOError:
        break # Se è stata usata la lettura non bloccante
print(f"Output iniziale:\n{initial_output.strip()}")


send_command("a = 10")
# Per l'interazione interattiva, la lettura dell'output è la parte più complessa.
# communicate() non è adatto, poiché chiude i flussi.
# È necessario leggere attentamente da process.stdout e process.stderr, 
# possibilmente in thread separati, per evitare di bloccare quello principale.
# Questo esempio NON è production-ready per interattività complessa.
# print(read_output()) # Questo read_output è molto primitivo

send_command("print(a * 2)")
# print(read_output())

# Termina il processo
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Attendi il completamento e raccogli il resto

print("\nStdout finale:")
print(stdout_data)
if stderr_data:
    print("\nStderr finale:")
    print(stderr_data)

print(f"Processo Python terminato con codice: {process.returncode}")

# Per una vera interazione interattiva, vengono spesso usati pty (pseudo-terminali)
# tramite il modulo `pty` nei sistemi Unix-like, o librerie come `pexpect`.
```
*Avvertenza*: L'interazione interattiva diretta con `Popen` tramite `stdin`/`stdout`/`stderr` è complessa a causa del blocco e del buffering. Per un'interattività affidabile, vengono spesso utilizzate librerie come `pexpect` (per Unix) o equivalenti che lavorano con pseudo-terminali (pty).

**Lavorare con le codifiche:**
*   Usa `text=True` (o `universal_newlines=True`) per la decodifica/codifica automatica.
*   Se necessario, puoi specificare `encoding="la_tua_codifica"` e `errors="gestore_errori"` (ad esempio, `replace`, `ignore`).
*   Se `text=False` (predefinito), `stdout` e `stderr` saranno stringhe di byte. Dovrai decodificarle manualmente: `result.stdout.decode('utf-8', errors='replace')`.

--- 

### 6. Sicurezza e migliori pratiche

*   **Rischi di `shell=True` e iniezione di comandi:**
    *   **Non usare mai** `shell=True` con comandi costruiti da input utente non attendibile. Ciò apre la porta all'iniezione di comandi.
    *   Esempio di vulnerabilità:
        ```python
        # PERICOLOSO!
        filename = input("Inserisci il nome del file da eliminare: ") # L'utente inserisce "il_mio_file_innocente.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Se `shell=True` è assolutamente necessario (ad esempio, per usare pipe `|` o sostituzioni `*` direttamente nella stringa di comando), escapa attentamente tutte le parti del comando formate da input esterno usando `shlex.quote()` (a partire da Python 3.3).

*   **Validazione ed escaping dell'input utente:**
    *   Anche se `shell=False`, se gli argomenti del comando sono formati da input utente, devono essere validati. Ad esempio, se si prevede un nome file, assicurati che sia effettivamente un nome file valido e non qualcosa come `../../../etc/passwd`.

*   **Passare gli argomenti come elenco (quando `shell=False`):**
    *   Questo è il modo più sicuro. Ogni argomento viene passato come un elemento di elenco separato e il sistema operativo li gestisce correttamente, senza cercare di interpretarli come parte del comando della shell.
    *   Esempio: `subprocess.run(["rm", filename_from_user])` — qui `filename_from_user` sarà sempre trattato come un singolo argomento (nome file), anche se contiene spazi o caratteri speciali.

*   **Gestione degli errori e dei codici di ritorno:**
    *   Controlla sempre `returncode` o usa `check=True` (per `run()`) / `check_call()` / `check_output()` per assicurarti che il comando sia stato eseguito correttamente.
    *   Gestisci le possibili eccezioni (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Gestione delle risorse:**
    *   Se apri pipe (`PIPE`), assicurati che vengano chiuse alla fine. `Popen.communicate()` lo fa automaticamente. Se lavori direttamente con `p.stdin/stdout/stderr`, potrebbe essere necessaria la loro chiusura esplicita.
    *   Nelle applicazioni a lunga esecuzione, assicurati che i processi figli terminino correttamente e non diventino "zombie". Usa `p.wait()` o `p.communicate()`. Se necessario, usa `p.terminate()` o `p.kill()`.

*   **Codifiche:** Fai attenzione alle codifiche quando usi `text=True` o quando decodifichi manualmente stringhe di byte. I problemi di codifica sono una fonte comune di errori.

--- 

### 7. Esempi pratici

**1. Esecuzione di un comando semplice e controllo del codice di ritorno:**
```python
import subprocess

try:
    # Esegui 'ls' per una directory esistente
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Comando 'ls /tmp' eseguito, codice di ritorno: {result.returncode}")

    # Esegui 'ls' per una directory inesistente
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Questa riga non verrà eseguita se check=True, poiché verrà sollevata un'eccezione
except subprocess.CalledProcessError as e:
    print(f"Errore di esecuzione del comando: {e.cmd}")
    print(f"Codice di ritorno: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Acquisizione dell'output del comando:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Specifica la directory corrente come directory di lavoro per git
    )
    print("Stato Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Errore: comando 'git' non trovato. Git è installato e nel PATH?")
except subprocess.CalledProcessError as e:
    print(f"Errore Git: {e.stderr}")
```

**3. Invio di dati all'input del processo (usando `communicate`):**
```python
import subprocess

# Invia testo a 'grep' per la ricerca
input_text = "hello world\npython è divertente\nhello python"
try:
    process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout_data, stderr_data = process.communicate(input=input_text, timeout=5)

    if process.returncode == 0: # grep ha trovato corrispondenze
        print("Righe trovate:")
        print(stdout_data)
    elif process.returncode == 1: # grep non ha trovato corrispondenze
        print("Nessuna corrispondenza 'python' trovata.")
    else: # altro errore grep
        print(f"Errore grep (codice {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep non ha risposto in tempo.")
    process.kill() # Uccidi il processo se si è bloccato
    process.communicate() # Raccogli l'output/errori rimanenti
```

**4. Creazione di una pipeline (`ls -l | wc -l`) senza `shell=True`:**
(Un esempio più dettagliato era nella sezione 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Assicurati che stdout esista
    ls_proc.stdout.close()  # Consente a wc_proc di ricevere EOF quando ls_proc termina

output, _ = wc_proc.communicate()
print(f"Numero di file/directory: {output.strip()}")
```

**5. Utilizzo di `timeout`:**
```python
import subprocess

try:
    # Comando che verrà eseguito per 5 secondi
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Comando 'sleep 5' completato (non avrebbe dovuto con timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Comando '{e.cmd}' non completato entro {e.timeout} secondi.")
```

--- 

### 8. Conclusione e risorse utili

Il modulo `subprocess` è uno strumento indispensabile per qualsiasi sviluppatore Python che abbia bisogno di interagire con programmi esterni o l'ambiente di sistema. Offre un equilibrio tra facilità d'uso (tramite `subprocess.run()`) e potente flessibilità (tramite `subprocess.Popen()`).

**Punti chiave:**
*   Preferisci `subprocess.run()` per la maggior parte dei compiti.
*   Usa `subprocess.Popen()` per l'esecuzione asincrona o la gestione complessa dei flussi.
*   **Evita `shell=True`**, specialmente con input utente, a causa dei rischi di sicurezza. Passa i comandi come un elenco di argomenti.
*   Gestisci sempre i codici di ritorno e le possibili eccezioni.
*   Fai attenzione alle codifiche quando lavori con l'output di testo (`text=True` o decodifica manuale).
*   `communicate()` è il tuo amico per lo scambio sicuro di dati tramite `PIPE`.

**Risorse utili:**
*   Documentazione ufficiale di Python per il modulo `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - Un nuovo modulo di processo: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)
