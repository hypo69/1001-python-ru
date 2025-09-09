### Jak sprawdzić i naprawić błędy na dysku twardym w Windows: ściągawka CHKDSK i PowerShell

Z biegiem czasu na dysku twardym lub SSD mogą gromadzić się błędy logiczne, pojawiać się uszkodzone sektory, co prowadzi do spowolnienia działania systemu, awarii programów, a nawet utraty danych. Na szczęście w systemie Windows istnieją wbudowane narzędzia do diagnozowania i naprawiania takich problemów.

W tej ściągawce pokażę dwa sposoby kontroli stanu dysków: narzędzie `chkdsk` i polecenia PowerShell.

### Część 1: Narzędzie CHKDSK

**CHKDSK** (Check Disk) – to standardowe narzędzie wiersza poleceń, które sprawdza system plików woluminu pod kątem błędów logicznych i fizycznych.

#### Jak uruchomić CHKDSK

Aby wykonać polecenia, które wprowadzają zmiany w systemie, potrzebne będą uprawnienia administratora.

1.  Naciśnij `Win + S` lub przycisk „Start”.
2.  Wpisz `cmd` lub „Wiersz polecenia”.
3.  W wynikach wyszukiwania kliknij prawym przyciskiem myszy na „Wiersz polecenia” i wybierz **„Uruchom jako administrator”**.

#### Główne parametry (przełączniki) CHKDSK

Polecenie ma następującą składnię: `chkdsk [dysk:] [parametry]`

Często używane parametry:

*   `chkdsk C:`
    Uruchamia sprawdzanie dysku C: w trybie „tylko do odczytu”. Narzędzie zgłosi znalezione błędy, ale ich nie naprawi.

*   **/f**
    Naprawia błędy na dysku. Jeśli na dysku są otwarte pliki (co prawie zawsze ma miejsce w przypadku dysku systemowego), narzędzie zaproponuje wykonanie sprawdzania przy następnym ponownym uruchomieniu systemu.
    *Przykład:* `chkdsk D: /f`

*   **/r**
    Wyszukuje uszkodzone sektory (bad sectors) i próbuje odzyskać informacje, które można odczytać. Ten przełącznik **zawiera funkcjonalność przełącznika `/f`**, więc używanie ich razem nie jest konieczne, choć nie jest błędem. Sprawdzanie z `/r` zajmuje znacznie więcej czasu.
    *Przykład:* `chkdsk D: /r`

*   **/x**
    Wymusza odmontowanie woluminu przed sprawdzeniem, jeśli to konieczne. Wszystkie otwarte uchwyty do tego dysku staną się nieprawidłowe. Ten przełącznik również **zawiera funkcjonalność `/f`**.
    *Przykład:* `chkdsk D: /x`

*   **/b** (tylko dla systemu plików NTFS)
    Wykonuje ponowną ocenę uszkodzonych klastrów na dysku. Ten przełącznik jest najbardziej kompleksowy, ponieważ **zawiera funkcjonalność `/r`**.
    *Przykład:* `chkdsk C: /b`

*   **/scan** (tylko dla NTFS)
    Uruchamia sprawdzanie woluminu online. Oznacza to, że dysku nie trzeba odmontowywać i można kontynuować pracę w systemie podczas skanowania. Jednak naprawa znalezionych problemów będzie wymagała następnego przełącznika lub ponownego uruchomienia.
    *Przykład:* `chkdsk C: /scan`

*   **/spotfix** (tylko dla NTFS)
    Wykonuje punktową, bardzo szybką naprawę błędów na woluminie. Wymaga odmontowania dysku, podobnie jak przełącznik `/f`.
    *Przykład:* `chkdsk D: /spotfix`

#### Przykłady uruchamiania CHKDSK

*   **Szybkie sprawdzanie dysku D: bez naprawy:**
    ```
    chkdsk D:
    ```

*   **Sprawdzanie i naprawa błędów na dysku D:**
    ```
    chkdsk D: /f
    ```

*   **Najbardziej kompleksowe sprawdzanie dysku systemowego C: z wyszukiwaniem uszkodzonych sektorów i ich odzyskiwaniem:**
    ```
    chkdsk C: /f /r
    ```
    *lub po prostu:*
    ```
    chkdsk C: /r
    ```

#### Co zrobić, jeśli dysk jest używany?

Przy próbie uruchomienia sprawdzania z naprawą (`/f` lub `/r`) dla dysku systemowego (zazwyczaj `C:`), zobaczysz komunikat:

`Nie można wykonać polecenia CHKDSK, ponieważ określony wolumin jest używany przez inny proces. Czy chcesz zaplanować sprawdzenie tego woluminu przy następnym ponownym uruchomieniu systemu? (T/N)`

Naciśnij klawisz `T`, a następnie `Enter`. Sprawdzanie zostanie zaplanowane i automatycznie rozpocznie się przy następnym ponownym uruchomieniu komputera.

---

### Część 2: Polecenia PowerShell

PowerShell – to powłoka automatyzacji, która oferuje nowoczesne i elastyczne polecenia do zarządzania systemem.

#### Jak uruchomić PowerShell

Podobnie jak w przypadku wiersza poleceń, potrzebne będą uprawnienia administratora.

1.  Naciśnij `Win + S` lub przycisk „Start”.
2.  Wpisz `powershell`.
3.  W wynikach wyszukiwania kliknij prawym przyciskiem myszy na „Windows PowerShell” i wybierz **„Uruchom jako administrator”**.

#### Główne polecenie: `Repair-Volume`

W PowerShell do sprawdzania i naprawy dysków używa się polecenia `Repair-Volume`.

Najpierw może być przydatne wyświetlenie listy wszystkich woluminów w systemie za pomocą polecenia:
```powershell
Get-Volume
```

#### Główne parametry `Repair-Volume`

*   `-DriveLetter`
    Określa literę dysku, który ma zostać sprawdzony.

*   `-Scan`
    Skanuje wolumin w poszukiwaniu błędów i zgłasza je. Jest to analogia do `chkdsk` bez przełączników.
    *Przykład:* `Repair-Volume -DriveLetter D -Scan`

*   `-SpotFix`
    Wykonuje szybką naprawę online bez konieczności długotrwałego odmontowywania woluminu. Analogia do `chkdsk /spotfix`.
    *Przykład:* `Repair-Volume -DriveLetter D -SpotFix`

*   `-OfflineScanAndFix`
    Wykonuje pełne sprawdzanie i naprawę dysku w trybie offline. Jest to najbardziej kompletna analogia do polecenia `chkdsk /f /r`. System poprosi o ponowne uruchomienie, jeśli wolumin jest używany.
    *Przykład:* `Repair-Volume -DriveLetter C -OfflineScanAndFix`

#### Przykłady PowerShell

*   **Skanowanie dysku C: w poszukiwaniu błędów (bez naprawy):**
    ```powershell
    Repair-Volume -DriveLetter C -Scan
    ```
    Wynik zobaczysz w polu `HealthStatus` (np. `Healthy` lub `Needs-Repair`).

*   **Wykonanie szybkiej naprawy dla dysku D:**
    ```powershell
    Repair-Volume -DriveLetter D -SpotFix
    ```

*   **Zaplanowanie pełnego sprawdzania i naprawy dysku systemowego C: przy następnym ponownym uruchomieniu:**
    ```powershell
    Repair-Volume -DriveLetter C -OfflineScanAndFix
    ```
    PowerShell, podobnie jak `chkdsk`, powiadomi Cię o konieczności ponownego uruchomienia i zaplanuje zadanie.


Dla większości użytkowników wynik działania `chkdsk C: /r` i `Repair-Volume -DriveLetter C -OfflineScanAndFix` będzie taki sam. Wybór zależy od Twoich preferencji i zadań.

**Ważna uwaga:** Przed wykonaniem jakichkolwiek poważnych operacji na dysku, zwłaszcza jeśli podejrzewasz problemy fizyczne, **zawsze twórz kopię zapasową ważnych danych!** Narzędzia mogą naprawić błędy, ale nie mogą zagwarantować 100% integralności danych na uszkodzonym nośniku.