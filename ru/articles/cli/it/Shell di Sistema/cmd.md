# cmd

## Categoria: Shell di sistema

### Scopo: Prompt dei comandi classico di Windows.

### Introduzione
Il Prompt dei comandi di Windows (`cmd.exe`) è un interprete della riga di comando per i sistemi operativi Windows. Consente agli utenti di eseguire comandi per svolgere varie attività, gestire file e directory, configurare le impostazioni di sistema e altro ancora. Fornisce un'interfaccia basata su testo per interagire con il sistema operativo.

### Comandi importanti ed esempi

Ecco alcuni comandi `cmd` essenziali e il loro utilizzo:

#### 1. `dir` - Visualizza un elenco di file e sottodirectory

Il comando `dir` visualizza un elenco di file e sottodirectory all'interno di una directory specificata.

```cmd
dir [unità:][percorso][nomefile] [/A[[:]attributi]] [/B] [/C] [/D] [/L] [/N] [/O[[:]ordine_di_ordinamento]] [/P] [/Q] [/R] [/S] [/T[[:]campo_ora]] [/W] [/X] [/4]
```

**Flag/Parametri**:
*   `/A[[:]attributi]`: Visualizza i file con gli attributi specificati.
    *   `D`: Directory
    *   `R`: File di sola lettura
    *   `H`: File nascosti
    *   `A`: File pronti per l'archiviazione
    *   `S`: File di sistema
    *   `I`: File non indicizzati per il contenuto
    *   `L`: Punti di reparse
    *   `O`: File offline
    *   `-`: Prefisso che significa "non" (ad esempio, `/A:-H` per escludere i file nascosti).
*   `/B`: Utilizza il formato "bare" (senza informazioni di intestazione o riepilogo), elencando solo il nome della directory o il nome del file e l'estensione.
*   `/S`: Visualizza i file nella directory specificata e in tutte le sottodirectory.
*   `/P`: Mette in pausa dopo ogni schermata di informazioni.
*   `/O[[:]ordine_di_ordinamento]`: Ordina l'output.
    *   `N`: In ordine alfabetico per nome.
    *   `E`: In ordine alfabetico per estensione.
    *   `S`: Per dimensione, dal più piccolo al più grande.
    *   `D`: Per data/ora, dal più vecchio al più recente.
    *   `G`: Raggruppa prima le directory.
    *   `-`: Prefisso per invertire l'ordine di ordinamento.
*   `/W`: Utilizza il formato di elenco ampio.
*   `/?`: Visualizza l'aiuto per il comando.

**Esempi**:
*   `dir`: Elenca file e directory nella directory corrente.
*   `dir /S`: Elenca tutti i file e le sottodirectory nella directory corrente e nelle sue sottodirectory.
*   `dir *.txt`: Elenca tutti i file con estensione `.txt` nella directory corrente.
*   `dir /A:H`: Elenca i file nascosti.
*   `dir /S /B *.log > logs.txt`: Trova tutti i file `.log` nella directory corrente e nelle sottodirectory, li elenca in formato "bare" e reindirizza l'output a `logs.txt`.

**Condizioni di successo**:
*   Il comando viene eseguito e visualizza l'elenco della directory richiesta.
*   Non vengono visualizzati messaggi di errore.
*   Il comando restituisce tipicamente un codice di uscita di `0`.

**Condizioni di fallimento**:
*   "File non trovato": Se il percorso o il modello di nome file specificato non esiste.
*   "Accesso negato.": Se non si dispone delle autorizzazioni necessarie per accedere alla directory.
*   Se l'output viene reindirizzato a un file e la directory per il file di output non esiste, potrebbe risultare un "Errore di creazione file".

#### 2. `copy` - Copia uno o più file

Il comando `copy` duplica uno o più file da una posizione all'altra.

```cmd
copy [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B] origine [/A | /B] [+ origine [/A | /B] [+ ...]] [destinazione [/A | /B]] [/?]
```

**Flag/Parametri**:
*   `origine`: Specifica il/i file da copiare. È possibile utilizzare i caratteri jolly (`*`, `?`).
*   `destinazione`: Specifica la directory e/o il nome del file per il/i nuovo/i file.
*   `/V`: Verifica che i nuovi file siano scritti correttamente.
*   `/Y`: Sopprime le richieste di conferma per sovrascrivere un file di destinazione esistente.
*   `/-Y`: Forza la richiesta di conferma per sovrascrivere un file di destinazione esistente.
*   `/A`: Indica un file di testo ASCII.
*   `/B`: Indica un file binario.
*   `/Z`: Copia i file in modalità riavviabile, utile per file di grandi dimensioni su una rete.
*   `/?`: Visualizza l'aiuto per il comando.

**Esempi**:
*   `copy file.txt C:\backup`: Copia `file.txt` dalla directory corrente a `C:\backup`.
*   `copy *.doc C:\reports /V`: Copia tutti i file `.doc` dalla directory corrente a `C:\reports` e verifica la copia.
*   `copy C:\source\file1.txt + C:\source\file2.txt C:\destination\combined.txt`: Combina `file1.txt` e `file2.txt` in `combined.txt`.
*   `copy D:\readme.htm`: Copia `readme.htm` dall'unità D: alla directory corrente.

**Condizioni di successo**:
*   Il/i file vengono copiati nella destinazione senza messaggi di errore.
*   Viene visualizzato un messaggio come "1 file(s) copiato/i.".
*   L'`ERRORLEVEL` è `0`.

**Condizioni di fallimento**:
*   "Impossibile trovare il file specificato.": Se il file di origine non esiste.
*   "Accesso negato.": Se non si dispone delle autorizzazioni di scrittura per la directory di destinazione o delle autorizzazioni di lettura per il file di origine.
*   "Spazio insufficiente sul disco.": Se l'unità di destinazione è piena.
*   Se viene utilizzato `/V` e la verifica fallisce, verrà visualizzato un messaggio di errore.
*   L'`ERRORLEVEL` sarà diverso da zero (ad esempio, `1` per un errore generico).

#### 3. `ping` - Verifica la connettività a livello IP

Il comando `ping` invia messaggi di richiesta echo del Protocollo di controllo messaggi Internet (ICMP) a un host di destinazione per verificare la connettività a livello IP.

```cmd
ping [/t] [/a] [/n conteggio] [/l dimensione] [/f] [/i TTL] [/v TOS] [/r conteggio] [/s conteggio] [{/j elenco_host | /k elenco_host}] [/w timeout] [/R] [/S indirizzo_sorgente] [/4] [/6] nome_destinazione
```

**Flag/Parametri**:
*   `nome_destinazione`: Specifica il nome host o l'indirizzo IP della destinazione.
*   `/t`: Esegue il ping dell'host specificato fino all'interruzione (Ctrl+C per fermare, Ctrl+Break per visualizzare le statistiche).
*   `/a`: Risolve gli indirizzi in nomi host.
*   `/n conteggio`: Specifica il numero di richieste echo da inviare (il valore predefinito è 4).
*   `/l dimensione`: Specifica la dimensione del buffer di invio in byte (il valore predefinito è 32).
*   `/w timeout`: Specifica il timeout in millisecondi da attendere per ogni risposta (il valore predefinito è 4000ms).
*   `/?`: Visualizza l'aiuto per il comando.

**Esempi**:
*   `ping google.com`: Esegue il ping di `google.com` quattro volte.
*   `ping 192.168.1.1 -n 10`: Esegue il ping dell'indirizzo IP `192.168.1.1` dieci volte.
*   `ping localhost`: Esegue il ping della macchina locale.
*   `ping -t 8.8.8.8`: Esegue continuamente il ping del server DNS di Google fino all'arresto manuale.

**Condizioni di successo**:
*   "Risposta da <indirizzo IP>": Indica una risposta riuscita dal target.
*   "TTL=" nell'output.
*   Un riepilogo che mostra "Pacchetti: Inviati = X, Ricevuti = X, Persi = 0 (0% di perdita)".
*   Il comando restituisce un codice di uscita di `0`.

**Condizioni di fallimento**:
*   "Richiesta scaduta.": Il target non ha risposto entro il timeout specificato.
*   "Host di destinazione irraggiungibile.": Non è stato possibile trovare un percorso per l'host di destinazione.
*   "La richiesta ping non è riuscita a trovare l'host <nome_host>. Controllare il nome e riprovare.": Il nome host non è stato risolto in un indirizzo IP (problema DNS).
*   "Errore generico.": Indica un problema con l'interfaccia di rete locale.
*   Un riepilogo che mostra "Pacchetti: Inviati = X, Ricevuti = Y, Persi = Z (Z% di perdita)" dove Z > 0.
*   Il comando restituisce un codice di uscita diverso da zero (ad esempio, `1` se l'host è irraggiungibile).

#### 4. `mkdir` (o `md`) - Crea una directory

Il comando `mkdir` crea una nuova directory o sottodirectory.

```cmd
mkdir [unità:]percorso
```

**Flag/Parametri**:
*   `[unità:]percorso`: Specifica l'unità e il percorso della directory da creare.
*   `/?`: Visualizza l'aiuto per il comando.
*   (Nota: il flag `-p` per la creazione di directory padre, comune nei sistemi Unix-like, non è un flag `cmd` standard. Le estensioni dei comandi in Windows consentono di creare directory intermedie in un percorso specificato con un singolo comando `mkdir`, in modo effettivamente simile a `-p` in alcuni casi).

**Esempi**:
*   `mkdir nuova_cartella`: Crea una directory denominata `nuova_cartella` nella directory corrente.
*   `mkdir C:\projects\my_project`: Crea `il_mio_progetto` all'interno di `C:\projects`. Se `C:\projects` non esiste, `cmd` con le estensioni dei comandi abilitate lo creerà.
*   `md "I miei documenti"`: Crea una directory denominata "I miei documenti" (le virgolette sono necessarie a causa dello spazio).

**Condizioni di successo**:
*   La directory viene creata senza messaggi di errore.
*   Normalmente non viene visualizzato alcun output in caso di successo.
*   L'`ERRORLEVEL` è `0`.

**Condizioni di fallimento**:
*   "Esiste già una sottodirectory o un file <nome_directory>.": Se esiste già una directory con lo stesso nome nella posizione specificata.
*   "Impossibile trovare il percorso specificato.": Se una directory intermedia nel percorso non esiste e le estensioni dei comandi sono disabilitate (o se il percorso non è valido).
*   "Accesso negato.": Se non si dispone delle autorizzazioni di scrittura nella directory padre.
*   L'`ERRORLEVEL` è diverso da zero (ad esempio, `1`).

#### 5. `del` (o `erase`) - Elimina uno o più file

Il comando `del` elimina uno o più file.

```cmd
del [/p] [/f] [/s] [/q] [/a[:attributi]] nomi
```

**Flag/Parametri**:
*   `nomi`: Specifica un elenco di uno o più file da eliminare. È possibile utilizzare i caratteri jolly (`*`, `?`).
*   `/P`: Richiede conferma prima di eliminare ogni file.
*   `/F`: Forza l'eliminazione dei file di sola lettura.
*   `/S`: Elimina i file specificati da tutte le sottodirectory. Visualizza i nomi dei file mentre vengono eliminati.
*   `/Q`: Modalità silenziosa; sopprime le richieste di conferma dell'eliminazione.
*   `/A[:attributi]`: Elimina i file in base agli attributi.
    *   `R`: File di sola lettura
    *   `H`: File nascosti
    *   `S`: File di sistema
    *   `A`: File pronti per l'archiviazione
    *   `-`: Prefisso che significa "non"
*   `/?`: Visualizza l'aiuto per il comando.

**Esempi**:
*   `del vecchio_file.txt`: Elimina `vecchio_file.txt` dalla directory corrente.
*   `del *.bak /Q`: Elimina tutti i file con estensione `.bak` nella directory corrente senza chiedere conferma.
*   `del /S /Q C:\temp\*.*`: Elimina tutti i file in `C:\temp` e nelle sue sottodirectory senza chiedere conferma.
*   `del /F file_sola_lettura.txt`: Forza l'eliminazione di un file di sola lettura denominato `file_sola_lettura.txt`.

**Condizioni di successo**:
*   Il/i file vengono eliminati senza messaggi di errore.
*   Se `/P` non viene utilizzato, potrebbe non esserci alcun output in caso di successo, o un messaggio come "File eliminato - <nome_file>" se viene utilizzato `/S`.
*   L'`ERRORLEVEL` è `0`.

**Condizioni di fallimento**:
*   "Impossibile trovare <nome_file>": Se il file specificato non esiste.
*   "Accesso negato.": Se non si dispone delle autorizzazioni necessarie per eliminare il file, o se il file è in uso da un altro processo e `/F` non è sufficiente.
*   "Il processo non può accedere al file perché è utilizzato da un altro processo.": Se il file è bloccato da un'altra applicazione.
*   `del` eliminerà i file all'interno di una directory se viene specificato un nome di directory, ma non eliminerà la directory stessa. Per eliminare le directory, utilizzare `rmdir`.
*   L'`ERRORLEVEL` è diverso da zero.

### Ulteriori letture
Per informazioni più dettagliate, fare riferimento alla documentazione ufficiale di `cmd`.
