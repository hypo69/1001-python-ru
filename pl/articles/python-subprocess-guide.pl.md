## Praca z biblioteką `subprocess` w Pythonie


### 1. **Czym jest `subprocess` i dlaczego jest potrzebny?**

Moduł `subprocess` w Pythonie zapewnia interfejs do tworzenia nowych procesów,
łączenia się z ich strumieniami wejścia/wyjścia/błędów i uzyskiwania ich kodów powrotu.
Pozwala skryptom Pythona uruchamiać i zarządzać innymi programami,
napisanymi w dowolnym języku, niezależnie od tego, czy są to narzędzia systemowe, skrypty powłoki, czy inne pliki wykonywalne.

**Kontekst historyczny:**

Przed pojawieniem się `subprocess` do uruchamiania procesów zewnętrznych używano funkcji z modułu `os`, takich jak `os.system()`, `os.spawn*()`, a także modułu `commands` (w Pythonie 2). Podejścia te miały szereg wad:
*   `os.system()`: Uruchamia polecenie za pośrednictwem powłoki systemowej, co jest niebezpieczne podczas pracy z danymi wejściowymi użytkownika i mniej elastyczne w zarządzaniu strumieniami.
*   `os.spawn*()`: Bardziej elastyczne, ale trudne w użyciu i zależne od platformy.
*   Moduł `popen2` (i jego warianty): Zapewniał dostęp do strumieni, ale był złożony i miał problemy z zakleszczeniami.

Moduł `subprocess` został wprowadzony w Pythonie 2.4 (PEP 324) jako ujednolicony i bezpieczniejszy sposób interakcji z procesami potomnymi. Kapsułkuje najlepsze funkcje poprzednich modułów i zapewnia czystsze API.

**Główne zadania rozwiązywane za pomocą `subprocess`:**

*   Wykonywanie poleceń systemu operacyjnego (np. `ls`, `dir`, `ping`).
*   Uruchamianie zewnętrznych narzędzi do przetwarzania danych (np. `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Integracja z systemami kontroli wersji (`git`, `svn`).
*   Uruchamianie kompilatorów lub interpreterów innych języków.
*   Automatyzacja administracji systemem.
*   Organizacja interakcji między różnymi programami.

--- 

### 2. Główne funkcje i klasy

Moduł `subprocess` oferuje kilka sposobów uruchamiania procesów:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Jest to **zalecane** API wysokiego poziomu, wprowadzone w Pythonie 3.5.
    *   Uruchamia polecenie, czeka na jego zakończenie i zwraca obiekt `CompletedProcess`.
    *   Nadaje się do większości przypadków, w których wystarczy wykonać polecenie i uzyskać wynik.

    ```python
    import subprocess

    # Proste uruchomienie
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Jeśli check=True i polecenie zwróciło wartość inną niż zero, zostanie zgłoszony CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Jest to główna klasa do tworzenia i zarządzania procesami potomnymi.
    *   Zapewnia maksymalną elastyczność: niewstrzymujące wykonanie, szczegółową kontrolę strumieni we/wy, możliwość wysyłania sygnałów do procesu.
    *   Funkcja `run()` używa `Popen` wewnętrznie.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Proces uruchomiony z PID: {process.pid}")
    # ... można wykonywać inne prace ...
    process.wait() # Czekaj na zakończenie
    print(f"Proces zakończony z kodem: {process.returncode}")
    ```

*   **Przestarzałe, ale nadal spotykane funkcje (były głównym API przed Pythonem 3.5):**
    *   `subprocess.call(args, ...)`: Wykonuje polecenie i czeka na jego zakończenie. Zwraca kod powrotu. Podobnie jak `os.system()`, ale bezpieczniejsze, jeśli `shell=False`.
    *   `subprocess.check_call(args, ...)`: Jak `call()`, ale zgłasza `CalledProcessError`, jeśli kod powrotu nie jest 0.
    *   `subprocess.check_output(args, ...)`: Wykonuje polecenie, czeka na zakończenie i zwraca jego standardowe wyjście (stdout) jako ciąg bajtów. Zgłasza `CalledProcessError`, jeśli kod powrotu nie jest 0.

    Chociaż te funkcje nadal działają, `subprocess.run()` zapewnia wygodniejszy i ujednolicony interfejs dla tych samych zadań.

--- 

### 3. Kluczowe argumenty funkcji `run()` i `Popen()`

Argumenty te pozwalają precyzyjnie dostosować uruchamianie i interakcję z procesem potomnym:

*   **`args`**: 
    *   Pierwszy i obowiązkowy argument.
    *   Może być listą ciągów (zalecane) lub pojedynczym ciągiem (jeśli `shell=True`).
    *   Pierwszym elementem listy jest nazwa pliku wykonywalnego, pozostałe to jego argumenty.
    *   Przykład: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**: 
    *   Definiują, jak będą obsługiwane standardowe strumienie wejścia, wyjścia i błędów procesu potomnego.
    *   Możliwe wartości:
        *   `None` (domyślnie): Dziedziczone z procesu nadrzędnego.
        *   `subprocess.PIPE`: Tworzony jest potok, przez który można wymieniać dane. `process.stdin`, `process.stdout`, `process.stderr` stają się obiektami podobnymi do plików.
        *   `subprocess.DEVNULL`: Przekierowuje strumień do "nikąd" (analogicznie do `/dev/null`).
        *   Otwarty deskryptor pliku (liczba całkowita).
        *   Istniejący obiekt pliku (np. otwarty plik `open('output.txt', 'w')`).

*   **`capture_output=True` (dla `run()`):**
    *   Wygodna opcja, równoważna ustawieniu `stdout=subprocess.PIPE` i `stderr=subprocess.PIPE`.
    *   Wynik będzie dostępny w `result.stdout` i `result.stderr`.

*   **`text=True` (lub `universal_newlines=True` dla kompatybilności):**
    *   Jeśli `True`, strumienie `stdout` i `stderr` (a także `stdin`, jeśli przekazano ciąg) zostaną otwarte w trybie tekstowym przy użyciu domyślnego kodowania (zazwyczaj UTF-8). Dekodowanie/kodowanie odbywa się automatycznie.
    *   Jeśli `False` (domyślnie), strumienie są traktowane jako bajty.
    *   Od Pythona 3.7 `text` jest preferowanym aliasem dla `universal_newlines`. Możesz również określić konkretne kodowanie za pomocą `encoding` i obsługę błędów za pomocą `errors`.

*   **`shell=False` (domyślnie):**
    *   Jeśli `False` (zalecane ze względów bezpieczeństwa i przewidywalności), `args` musi być listą. Polecenie jest uruchamiane bezpośrednio.
    *   Jeśli `True`, `args` jest przekazywany jako ciąg do powłoki systemowej (np. `/bin/sh` w systemie Unix, `cmd.exe` w systemie Windows) w celu interpretacji. Pozwala to na używanie funkcji powłoki (zmiennych, podstawień, potoków), ale jest **NIEBEZPIECZNE**, jeśli `args` zawiera niezaufane dane wejściowe użytkownika (ryzyko wstrzyknięcia poleceń).

*   **`cwd=None`:**
    *   Ustawia bieżący katalog roboczy dla procesu potomnego. Domyślnie jest dziedziczony z procesu nadrzędnego.

*   **`env=None`:**
    *   Słownik, który definiuje zmienne środowiskowe dla nowego procesu. Domyślnie dziedziczone jest środowisko procesu nadrzędnego. Jeśli określono, całkowicie zastępuje dziedziczone środowisko. Aby dodać/zmienić zmienne, zachowując resztę, należy najpierw skopiować `os.environ`, a następnie je zmodyfikować.

*   **`timeout=None`:**
    *   Maksymalny czas w sekundach przeznaczony na wykonanie polecenia. Jeśli proces nie zakończy się w tym czasie, zostanie zgłoszony wyjątek `subprocess.TimeoutExpired`. `Popen.communicate()` również akceptuje `timeout`.

*   **`check=False` (dla `run()`):**
    *   Jeśli `True` i proces zakończy się z niezerowym kodem powrotu, zostanie zgłoszony wyjątek `subprocess.CalledProcessError`.

--- 

### 4. Praca z wynikami i błędami

**Obiekt `CompletedProcess` (wynik `run()`):**

```python
import subprocess

try:
    # Próba wykonania polecenia, które może zakończyć się niepowodzeniem
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - literówka, aby zademonstrować błąd
        capture_output=True,
        text=True,
        check=True, # Zgłosi wyjątek, jeśli returncode != 0
        timeout=10
    )
    print("Polecenie wykonane pomyślnie.")
    print("Kod powrotu:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Zazwyczaj puste w przypadku sukcesu

except subprocess.CalledProcessError as e:
    print(f"Błąd wykonania polecenia (CalledProcessError):")
    print(f"  Polecenie: {e.cmd}")
    print(f"  Kod powrotu: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Może zawierać dane wyjściowe przed błędem
    print(f"  Stderr: {e.stderr}") # Zazwyczaj zawiera informacje o błędzie
except subprocess.TimeoutExpired as e:
    print(f"Polecenie nie zakończyło się w ciągu {e.timeout} sekund.")
    print(f"  Polecenie: {e.cmd}")
    if e.stdout: print(f"  Stdout (częściowy): {e.stdout.decode(errors='ignore')}") # stdout to bajty
    if e.stderr: print(f"  Stderr (częściowy): {e.stderr.decode(errors='ignore')}") # stderr to bajty
except FileNotFoundError:
    print("Błąd: nie znaleziono polecenia lub programu.")
except Exception as e:
    print(f"Wystąpił inny błąd: {e}")
```

**Atrybuty `CompletedProcess`:**
*   `args`: Argumenty użyte do uruchomienia procesu.
*   `returncode`: Kod powrotu procesu. 0 zazwyczaj oznacza sukces.
*   `stdout`: Standardowe wyjście procesu (bajty lub ciąg, jeśli `text=True` i `capture_output=True`).
*   `stderr`: Standardowy strumień błędów procesu (bajty lub ciąg, jeśli `text=True` i `capture_output=True`).

**Wyjątki:**
*   `subprocess.CalledProcessError`: Zgłaszany, jeśli `check=True` (dla `run()`) lub użyto `check_call()`, `check_output()` i polecenie zakończyło się kodem innym niż zero. Zawiera `returncode`, `cmd`, `output` (lub `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Jeśli upłynął limit czasu. Zawiera `cmd`, `timeout`, `stdout`, `stderr` (częściowe dane wyjściowe, jeśli istnieją).
*   `FileNotFoundError`: Jeśli plik wykonywalny nie zostanie znaleziony.

**Interakcja z obiektem `Popen`:**

Klasa `Popen` daje większą kontrolę:

```python
import subprocess
import time

# Uruchom proces w tle
process = subprocess.Popen(["sleep", "5"])
print(f"PID procesu: {process.pid} uruchomiony.")

# Niewstrzymujące sprawdzanie statusu
while process.poll() is None: # poll() zwraca None, jeśli proces nadal działa
    print("Proces nadal działa...")
    # Możesz odczytywać dane wyjściowe w miarę ich pojawiania się (uwaga, może to zablokować!)
    # line = process.stdout.readline()
    # if line: print(f"Wyjście: {line.strip()}")
    time.sleep(1)

# Czekaj na zakończenie i pobierz wszystkie dane wyjściowe/błędy
# stdout_data, stderr_data = process.communicate(timeout=10) # Bezpieczny sposób

# Jeśli communicate() nie było używane, po poll() != None możesz odczytać resztę
if process.stdout:
    for line in process.stdout:
        print(f"Końcowe wyjście: {line.strip()}")

print(f"Proces zakończony z kodem: {process.returncode}")

# Jeśli musisz wymusić zakończenie
# process.terminate() # Wysyła SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Jeśli nie zakończył się
#     process.kill()      # Wysyła SIGKILL
```

*   `process.poll()`: Sprawdza, czy proces potomny zakończył się. Zwraca kod powrotu lub `None`. Niewstrzymujące.
*   `process.wait(timeout=None)`: Czeka na zakończenie procesu potomnego. Zwraca kod powrotu. Wstrzymujące.
*   `process.communicate(input=None, timeout=None)`:
    *   Najbezpieczniejszy sposób interakcji z procesem podczas używania `PIPE`.
    *   Wysyła dane do `stdin` (jeśli określono `input`), odczytuje wszystkie dane z `stdout` i `stderr` do końca i czeka na zakończenie procesu.
    *   Zwraca krotkę `(stdout_data, stderr_data)`.
    *   Pomaga uniknąć zakleszczeń, które mogą wystąpić przy bezpośrednim odczycie/zapisie do `process.stdout`/`process.stdin`, jeśli bufory się przepełnią.
*   `process.terminate()`: Wysyła sygnał `SIGTERM` do procesu (miękkie zakończenie).
*   `process.kill()`: Wysyła sygnał `SIGKILL` do procesu (twarde zakończenie).
*   `process.send_signal(signal)`: Wysyła określony sygnał do procesu.
*   `process.stdin`, `process.stdout`, `process.stderr`: Obiekty podobne do plików dla potoków, jeśli zostały utworzone za pomocą `PIPE`.

--- 

### 5. Zaawansowane scenariusze użycia

**Przekierowanie wyjścia jednego polecenia na wejście drugiego (potoki):**

Emulacja `ps aux | grep python`:

```python
import subprocess

# Uruchom pierwsze polecenie, jego stdout będzie potokiem
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Uruchom drugie polecenie, jego stdin będzie stdout pierwszego polecenia
# Stdout drugiego polecenia jest również potokiem do odczytu wyniku
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Połącz stdout z ps do stdin dla grep
    stdout=subprocess.PIPE,
    text=True
)

# Ważne! Zamknij stdout pierwszego polecenia w procesie nadrzędnym,
# aby grep otrzymał EOF, gdy ps zakończy działanie.
if ps_process.stdout:
    ps_process.stdout.close()  

# Pobierz dane wyjściowe z grep
stdout_data, stderr_data = grep_process.communicate()

print("Wynik potoku:")
print(stdout_data)

if stderr_data:
    print("Błędy grep:", stderr_data)

# Upewnij się, że oba procesy zakończyły działanie
ps_process.wait() 
# grep_process.wait() # communicate() już czekał
print(f"kod powrotu ps: {ps_process.returncode}")
print(f"kod powrotu grep: {grep_process.returncode}")
```
*Uwaga:* W przypadku prostych potoków `subprocess.run("ps aux | grep python", shell=True, ...)` może być prostsze, ale mniej bezpieczne i elastyczne.

**Asynchroniczne wykonywanie procesów:**

`Popen` jest z natury niewstrzymujące. Możesz uruchomić wiele procesów i zarządzać nimi równolegle.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Polecenie z błędem
]

processes = []
for cmd_args in commands:
    print(f"Uruchamianie: {' '.join(cmd_args)}")
    # Dla asynchroniczności lepiej jest przekierować stdout/stderr,
    # aby nie kolidowały ze sobą ani z konsolą nadrzędną.
    # DEVNULL, jeśli wyjście nie jest potrzebne, PIPE, jeśli jest potrzebne później.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Wykonaj inne prace lub poczekaj na zakończenie
while any(p.poll() is None for p in processes):
    print("Czekam na zakończenie wszystkich procesów...")
    time.sleep(0.5)

print("\nWyniki:")
for i, p in enumerate(processes):
    print(f"Polecenie '{' '.join(commands[i])}' zakończyło się kodem: {p.returncode}")
```

**Interaktywna interakcja z procesem:**

Jest to złożone zadanie, które wymaga ostrożnego zarządzania strumieniami, aby uniknąć zakleszczeń. `communicate()` jest dobre do jednorazowej wymiany. W przypadku długiej sesji interaktywnej może być konieczne bezpośrednie odczytywanie/zapisywanie do `p.stdin`, `p.stdout`, `p.stderr` przy użyciu niewstrzymującego we/wy lub oddzielnych wątków.

```python
import subprocess

# Przykład: uruchamianie interaktywnej sesji Pythona
process = subprocess.Popen(
    ['python', '-i'], # -i dla trybu interaktywnego
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Buforowanie liniowe dla stdout/stderr (dla interaktywności)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Ważne!

def read_output():
    # Odczytywanie danych wyjściowych może być trudne, ponieważ trzeba wiedzieć, kiedy przestać.
    # To jest bardzo uproszczony przykład. W przypadku rzeczywistych zadań potrzebne są bardziej niezawodne rozwiązania.
    # Na przykład odczytywanie do określonego wzorca (monit wiersza poleceń).
    output = ""
    # Odczytaj stdout. W rzeczywistej aplikacji powinno to być wykonywane w sposób niewstrzymujący lub w osobnym wątku.
    # Tutaj zakładamy, że po poleceniu natychmiast pojawi się jakieś wyjście.
    # To bardzo kruche założenie dla ogólnego przypadku!
    try:
        # Popen nie ma readline z limitem czasu, to jedna z trudności
        # Możesz użyć select na process.stdout.fileno()
        # lub odczytywać znak po znaku/wiersz po wierszu w osobnym wątku
        # Dla uproszczenia, nie ma tego tutaj
        while True: # Uwaga, może to zablokować!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Prosty detektor monitu
                output += line
                break
            output += line
    except Exception as e:
        print(f"Błąd odczytu: {e}")
    return output.strip()

# Inicjalizacja: odczytaj początkowy monit
initial_output = ""
# Odczytywanie komunikatu powitalnego Pythona
# To jest bardzo uproszczone, ponieważ nie wiemy dokładnie, ile wierszy odczytać
for _ in range(5): # Spróbujmy odczytać kilka wierszy
    try:
        # Popen stdout nie ma limitu czasu, trzeba czytać ostrożnie
        # stdout.readline() może zablokować.
        # W rzeczywistych aplikacjach potrzebne są tutaj select lub wątki.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Znaleziono monit
    except BlockingIOError:
        break # Jeśli było odczytywanie niewstrzymujące
print(f"Początkowe wyjście:\n{initial_output.strip()}")


send_command("a = 10")
# W przypadku interaktywnej interakcji odczytywanie danych wyjściowych jest najtrudniejszą częścią.
# communicate() nie jest odpowiednie, ponieważ zamyka strumienie.
# Musisz ostrożnie odczytywać z process.stdout i process.stderr, 
# prawdopodobnie w osobnych wątkach, aby nie blokować głównego.
# Ten przykład NIE jest gotowy do produkcji dla złożonej interaktywności.
# print(read_output()) # Ten read_output jest bardzo prymitywny

send_command("print(a * 2)")
# print(read_output())

# Zakończ proces
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Czekaj na zakończenie i zbierz resztę

print("\nKońcowe standardowe wyjście:")
print(stdout_data)
if stderr_data:
    print("\nKońcowe standardowe wyjście błędów:")
    print(stderr_data)

print(f"Proces Pythona zakończył się kodem: {process.returncode}")

# W przypadku prawdziwej interaktywnej interakcji często używa się pty (pseudo-terminali)
# za pośrednictwem modułu `pty` w systemach uniksopodobnych lub bibliotek takich jak `pexpect`.
```
*Ostrzeżenie*: Bezpośrednia interaktywna interakcja z `Popen` za pośrednictwem `stdin`/`stdout`/`stderr` jest trudna ze względu na zakleszczenia i buforowanie. W celu zapewnienia niezawodnej interaktywności często używa się bibliotek takich jak `pexpect` (dla Uniksa) lub podobnych, które współpracują z pseudo-terminalami (pty).

**Praca z kodowaniami:**
*   Użyj `text=True` (lub `universal_newlines=True`) do automatycznego dekodowania/kodowania.
*   W razie potrzeby możesz określić `encoding="twoje-kodowanie"` i `errors="obsługa-błędów"` (np. `replace`, `ignore`).
*   Jeśli `text=False` (domyślnie), `stdout` i `stderr` będą ciągami bajtów. Będziesz musiał je ręcznie zdekodować: `result.stdout.decode('utf-8', errors='replace')`.

--- 

### 6. Bezpieczeństwo i najlepsze praktyki

*   **Ryzyka `shell=True` i wstrzyknięcia poleceń:**
    *   **Nigdy** nie używaj `shell=True` z poleceniami skonstruowanymi z niezaufanych danych wejściowych użytkownika. Otwiera to drogę do wstrzyknięcia poleceń.
    *   Przykład luki w zabezpieczeniach:
        ```python
        # NIEBEZPIECZNE!
        filename = input("Wprowadź nazwę pliku do usunięcia: ") # Użytkownik wprowadza "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Jeśli `shell=True` jest absolutnie konieczne (np. do użycia potoków `|` lub symboli wieloznacznych `*` bezpośrednio w wierszu poleceń), ostrożnie uciekaj wszystkie części polecenia utworzone z zewnątrz za pomocą `shlex.quote()` (od Pythona 3.3).

*   **Walidacja i ucieczka danych wejściowych użytkownika:**
    *   Nawet jeśli `shell=False`, jeśli argumenty polecenia są tworzone z danych wejściowych użytkownika, powinny zostać zweryfikowane. Na przykład, jeśli oczekiwana jest nazwa pliku, upewnij się, że jest to prawidłowa nazwa pliku, a nie coś w rodzaju `../../../etc/passwd`.

*   **Przekazywanie argumentów jako listy (gdy `shell=False`):**
    *   Jest to najbezpieczniejszy sposób. Każdy argument jest przekazywany jako oddzielny element listy, a system operacyjny obsługuje je poprawnie, nie próbując interpretować ich jako części polecenia powłoki.
    *   Przykład: `subprocess.run(["rm", filename_from_user])` — tutaj `filename_from_user` zawsze będzie traktowany jako pojedynczy argument (nazwa pliku), nawet jeśli zawiera spacje lub znaki specjalne.

*   **Obsługa błędów i kodów powrotu:**
    *   Zawsze sprawdzaj `returncode` lub używaj `check=True` (dla `run()`) / `check_call()` / `check_output()`, aby upewnić się, że polecenie zostało wykonane pomyślnie.
    *   Obsługuj możliwe wyjątki (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Zarządzanie zasobami:**
    *   Jeśli otwierasz potoki (`PIPE`), upewnij się, że zostaną one ostatecznie zamknięte. `Popen.communicate()` robi to automatycznie. Jeśli pracujesz bezpośrednio z `p.stdin`/`stdout`/`stderr`, może być konieczne ich jawne zamknięcie.
    *   W długo działających aplikacjach upewnij się, że procesy potomne kończą się prawidłowo i nie stają się "zombie". Użyj `p.wait()` lub `p.communicate()`. W razie potrzeby użyj `p.terminate()` lub `p.kill()`.

*   **Kodowania:** Zachowaj ostrożność przy kodowaniach podczas używania `text=True` lub ręcznego dekodowania ciągów bajtów. Problemy z kodowaniem są częstym źródłem błędów.

--- 

### 7. Praktyczne przykłady

**1. Wykonywanie prostego polecenia i sprawdzanie kodu powrotu:**
```python
import subprocess

try:
    # Wykonaj 'ls' dla istniejącego katalogu
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Polecenie 'ls /tmp' wykonane, kod powrotu: {result.returncode}")

    # Wykonaj 'ls' dla nieistniejącego katalogu
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Ten wiersz nie zostanie wykonany, jeśli check=True, ponieważ zostanie zgłoszony wyjątek
except subprocess.CalledProcessError as e:
    print(f"Błąd wykonania polecenia: {e.cmd}")
    print(f"Kod powrotu: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Przechwytywanie danych wyjściowych polecenia:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Określ bieżący katalog jako katalog roboczy dla git
    )
    print("Status Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Błąd: nie znaleziono polecenia 'git'. Czy Git jest zainstalowany i w PATH?")
except subprocess.CalledProcessError as e:
    print(f"Błąd Git: {e.stderr}")
```

**3. Wysyłanie danych do wejścia procesu (za pomocą `communicate`):**
```python
import subprocess

# Wyślij tekst do 'grep' w celu wyszukania
input_text = "hello world\npython is fun\nhello python"
try:
    process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout_data, stderr_data = process.communicate(input=input_text, timeout=5)

    if process.returncode == 0: # grep znalazł dopasowania
        print("Znalezione wiersze:")
        print(stdout_data)
    elif process.returncode == 1: # grep nie znalazł dopasowań
        print("Nie znaleziono dopasowań dla 'python'.")
    else: # inny błąd grep
        print(f"Błąd Grep (kod {process.returncode}):")
        if stderr_data:
            print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep nie odpowiedział na czas.")
    process.kill() # Zabij proces, jeśli się zawiesi
    process.communicate() # Zbierz pozostałe dane wyjściowe/błędy
```

**4. Tworzenie potoku (`ls -l | wc -l`) bez `shell=True`:**
(Bardziej szczegółowy przykład znajdował się w sekcji 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Upewnij się, że stdout istnieje
    ls_proc.stdout.close()  # Pozwala wc_proc otrzymać EOF, gdy ls_proc zakończy działanie

output, _ = wc_proc.communicate()
print(f"Liczba plików/katalogów: {output.strip()}")
```

**5. Używanie `timeout`:**
```python
import subprocess

try:
    # Polecenie, które będzie działać przez 5 sekund
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Polecenie 'sleep 5' zakończyło się (nie powinno było z timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Polecenie '{e.cmd}' nie zakończyło się w ciągu {e.timeout} sekund.")
```

--- 

### 8. Podsumowanie i przydatne zasoby

Moduł `subprocess` jest niezastąpionym narzędziem dla każdego programisty Pythona, który musi wchodzić w interakcje z programami zewnętrznymi lub środowiskiem systemowym. Oferuje równowagę między łatwością użycia (za pośrednictwem `subprocess.run()`) a potężną elastycznością (za pośrednictwem `subprocess.Popen()`).

**Kluczowe punkty:**
*   Preferuj `subprocess.run()` dla większości zadań.
*   Używaj `subprocess.Popen()` do asynchronicznego wykonywania lub złożonego zarządzania strumieniami.
*   **Unikaj `shell=True`**, zwłaszcza z danymi wejściowymi użytkownika, ze względu na ryzyko bezpieczeństwa. Przekazuj polecenia jako listę argumentów.
*   Zawsze obsługuj kody powrotu i możliwe wyjątki.
*   Zachowaj ostrożność przy kodowaniach podczas pracy z danymi wyjściowymi tekstowymi (`text=True` lub ręczne dekodowanie).
*   `communicate()` to Twój przyjaciel do bezpiecznej wymiany danych za pośrednictwem `PIPE`.

**Przydatne zasoby:**
*   Oficjalna dokumentacja Pythona dla modułu `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - Nowy moduł procesów: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)
