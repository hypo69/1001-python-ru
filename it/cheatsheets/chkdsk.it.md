### Come controllare e correggere gli errori del disco rigido in Windows: cheat sheet CHKDSK e PowerShell

Con il tempo, sul disco rigido o sull'SSD possono accumularsi errori logici e possono comparire settori danneggiati, portando a rallentamenti del sistema, crash di programmi e persino alla perdita di dati. Fortunatamente, Windows dispone di strumenti integrati per la diagnosi e la correzione di tali problemi.

In questa cheat sheet, mostrerò due modi per monitorare lo stato dei dischi: l'utility `chkdsk` e i comandi PowerShell.

### Parte 1: Utility CHKDSK

**CHKDSK** (Check Disk) è un'utility standard da riga di comando che controlla il file system di un volume per la presenza di errori logici e fisici.

#### Come eseguire CHKDSK

Per eseguire comandi che apportano modifiche al sistema, avrete bisogno dei diritti di amministratore.

1.  Premere `Win + S` o il pulsante "Start".
2.  Digitare `cmd` o "Prompt dei comandi".
3.  Nei risultati della ricerca, fare clic con il tasto destro su "Prompt dei comandi" e selezionare **"Esegui come amministratore"**.

#### Parametri principali (switch) di CHKDSK

Il comando ha la seguente sintassi: `chkdsk [unità:] [parametri]`

Parametri di uso frequente:

*   `chkdsk C:`
    Avvia il controllo dell'unità C: in modalità "sola lettura". L'utility segnalerà gli errori trovati ma non li correggerà.

*   **/f**
    Corregge gli errori sul disco. Se ci sono file aperti sul disco (il che è quasi sempre il caso per l'unità di sistema), l'utility proporrà di eseguire il controllo al prossimo riavvio del sistema.
    *Esempio:* `chkdsk D: /f`

*   **/r**
    Individua i settori danneggiati (bad sectors) e tenta di recuperare le informazioni leggibili. Questo switch **include la funzionalità dello switch `/f`**, quindi usarli insieme non è strettamente necessario, anche se non è un errore. Un controllo con `/r` richiede molto più tempo.
    *Esempio:* `chkdsk D: /r`

*   **/x**
    Forza lo smontaggio del volume prima del controllo, se necessario. Tutti gli handle aperti per questo disco diventeranno invalidi. Questo switch **include anche la funzionalità di `/f`**.
    *Esempio:* `chkdsk D: /x`

*   **/b** (solo per file system NTFS)
    Esegue una rivalutazione dei cluster danneggiati sul disco. Questo switch è il più completo, in quanto **include la funzionalità di `/r`**.
    *Esempio:* `chkdsk C: /b`

*   **/scan** (solo per NTFS)
    Esegue una scansione online del volume. Ciò significa che l'unità non deve essere smontata e si può continuare a lavorare sul sistema durante la scansione. Tuttavia, la correzione dei problemi trovati richiederà lo switch successivo o un riavvio.
    *Esempio:* `chkdsk C: /scan`

*   **/spotfix** (solo per NTFS)
    Esegue una correzione puntuale e molto rapida degli errori sul volume. Richiede lo smontaggio del disco, proprio come lo switch `/f`.
    *Esempio:* `chkdsk D: /spotfix`

#### Esempi di esecuzione di CHKDSK

*   **Controllo rapido dell'unità D: senza correzione:**
    ```
    chkdsk D:
    ```

*   **Controllo e correzione degli errori sull'unità D:**
    ```
    chkdsk D: /f
    ```

*   **Controllo più completo dell'unità di sistema C: con rilevamento e recupero dei settori danneggiati:**
    ```
    chkdsk C: /f /r
    ```
    *o semplicemente:*
    ```
    chkdsk C: /r
    ```

#### Cosa fare se il disco è in uso?

Quando si tenta di eseguire un controllo con correzione (`/f` o `/r`) per l'unità di sistema (di solito `C:`), verrà visualizzato un messaggio:

`Impossibile eseguire il comando CHKDSK perché il volume specificato è in uso da un altro processo. Si desidera pianificare il controllo di questo volume al prossimo riavvio del sistema? (S/N)`

Premere `S`, quindi `Invio`. Il controllo verrà pianificato e si avvierà automaticamente al prossimo riavvio del computer.

---

### Parte 2: Comandi PowerShell

PowerShell è una shell di automazione che offre comandi moderni e flessibili per la gestione del sistema.

#### Come eseguire PowerShell

Come per il Prompt dei comandi, avrete bisogno dei diritti di amministratore.

1.  Premere `Win + S` o il pulsante "Start".
2.  Digitare `powershell`.
3.  Nei risultati della ricerca, fare clic con il tasto destro su "Windows PowerShell" e selezionare **"Esegui come amministratore"**.

#### Comando principale: `Repair-Volume`

In PowerShell, il cmdlet `Repair-Volume` viene utilizzato per controllare e correggere i dischi.

Per prima cosa, potrebbe essere utile visualizzare un elenco di tutti i volumi sul sistema utilizzando il comando:
```powershell
Get-Volume
```

#### Parametri principali di `Repair-Volume`

*   `-DriveLetter`
    Specifica la lettera dell'unità da controllare.

*   `-Scan`
    Scansiona il volume per errori e li segnala. Questo è analogo a `chkdsk` senza switch.
    *Esempio:* `Repair-Volume -DriveLetter D -Scan`

*   `-SpotFix`
    Esegue una correzione rapida online senza la necessità di smontare il volume per molto tempo. Analogo a `chkdsk /spotfix`.
    *Esempio:* `Repair-Volume -DriveLetter D -SpotFix`

*   `-OfflineScanAndFix`
    Esegue un controllo e una correzione completa del disco offline. Questo è l'analogo più completo del comando `chkdsk /f /r`. Il sistema richiederà un riavvio se il volume è in uso.
    *Esempio:* `Repair-Volume -DriveLetter C -OfflineScanAndFix`

#### Esempi PowerShell

*   **Scansionare l'unità C: per errori (senza correzione):**
    ```powershell
    Repair-Volume -DriveLetter C -Scan
    ```
    Vedrete il risultato nel campo `HealthStatus` (ad esempio, `Healthy` o `Needs-Repair`).

*   **Eseguire una correzione rapida per l'unità D:**
    ```powershell
    Repair-Volume -DriveLetter D -SpotFix
    ```

*   **Pianificare un controllo e una correzione completa per l'unità di sistema C: al prossimo riavvio:**
    ```powershell
    Repair-Volume -DriveLetter C -OfflineScanAndFix
    ```
    PowerShell, come `chkdsk`, vi informerà della necessità di un riavvio e pianificherà l'attività.


Per la maggior parte degli utenti, il risultato di `chkdsk C: /r` e `Repair-Volume -DriveLetter C -OfflineScanAndFix` sarà lo stesso. La scelta dipende dalle vostre preferenze e attività.

**Nota importante:** Prima di eseguire qualsiasi operazione seria sul disco, soprattutto se si sospettano problemi fisici, **eseguire sempre il backup dei dati importanti!** Gli strumenti possono correggere gli errori, ma non possono garantire al 100% l'integrità dei dati su un supporto danneggiato.
