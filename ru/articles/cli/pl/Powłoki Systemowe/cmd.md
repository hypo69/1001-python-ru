# cmd

## Kategoria: Powłoki systemowe

### Cel: Klasyczny wiersz poleceń systemu Windows.

### Wprowadzenie
Wiersz poleceń systemu Windows (`cmd.exe`) to interpreter linii poleceń dla systemów operacyjnych Windows. Umożliwia użytkownikom wykonywanie poleceń w celu realizacji różnych zadań, zarządzania plikami i katalogami, konfigurowania ustawień systemowych i wielu innych. Zapewnia tekstowy interfejs do interakcji z systemem operacyjnym.

### Ważne polecenia i przykłady

Oto kilka podstawowych poleceń `cmd` i ich zastosowanie:

#### 1. `dir` - Wyświetla listę plików i podkatalogów

Polecenie `dir` wyświetla listę plików i podkatalogów w określonym katalogu.

```cmd
dir [dysk:][ścieżka][nazwa_pliku] [/A[[:]atrybuty]] [/B] [/C] [/D] [/L] [/N] [/O[[:]kolejność_sortowania]] [/P] [/Q] [/R] [/S] [/T[[:]pole_czasu]] [/W] [/X] [/4]
```

**Flagi/Parametry**:
*   `/A[[:]atrybuty]`: Wyświetla pliki z określonymi atrybutami.
    *   `D`: Katalogi
    *   `R`: Pliki tylko do odczytu
    *   `H`: Pliki ukryte
    *   `A`: Pliki gotowe do archiwizacji
    *   `S`: Pliki systemowe
    *   `I`: Pliki nieindeksowane zawartością
    *   `L`: Punkty ponownej analizy
    *   `O`: Pliki offline
    *   `-`: Prefiks oznaczający "nie" (np. `/A:-H` aby wykluczyć pliki ukryte).
*   `/B`: Używa formatu uproszczonego (bez nagłówka i podsumowania), wyświetlając tylko nazwę katalogu lub nazwę pliku i rozszerzenie.
*   `/S`: Wyświetla pliki w określonym katalogu i wszystkich podkatalogach.
*   `/P`: Wstrzymuje wyświetlanie po każdym ekranie informacji.
*   `/O[[:]kolejność_sortowania]`: Sortuje dane wyjściowe.
    *   `N`: Alfabetycznie według nazwy.
    *   `E`: Alfabetycznie według rozszerzenia.
    *   `S`: Według rozmiaru, najmniejsze najpierw.
    *   `D`: Według daty/godziny, najstarsze najpierw.
    *   `G`: Najpierw grupuje katalogi.
    *   `-`: Prefiks odwracający kolejność sortowania.
*   `/W`: Używa szerokiego formatu listy.
*   `/?`: Wyświetla pomoc dla polecenia.

**Przykłady**:
*   `dir`: Wyświetla pliki i katalogi w bieżącym katalogu.
*   `dir /S`: Wyświetla wszystkie pliki i podkatalogi w bieżącym katalogu i jego podkatalogach.
*   `dir *.txt`: Wyświetla wszystkie pliki z rozszerzeniem `.txt` w bieżącym katalogu.
*   `dir /A:H`: Wyświetla pliki ukryte.
*   `dir /S /B *.log > logs.txt`: Znajduje wszystkie pliki `.log` w bieżącym katalogu i podkatalogach, wyświetla je w formacie uproszczonym i przekierowuje wynik do `logs.txt`.

**Warunki sukcesu**:
*   Polecenie wykonuje się i wyświetla żądaną listę katalogów.
*   Nie są wyświetlane żadne komunikaty o błędach.
*   Polecenie zazwyczaj zwraca kod wyjścia `0`.

**Warunki niepowodzenia**:
*   "Nie znaleziono pliku": Jeśli określona ścieżka lub wzorzec nazwy pliku nie istnieje.
*   "Odmowa dostępu.": Jeśli nie masz niezbędnych uprawnień do dostępu do katalogu.
*   Jeśli dane wyjściowe są przekierowywane do pliku, a katalog dla pliku wyjściowego nie istnieje, może to spowodować błąd "Błąd tworzenia pliku".

#### 2. `copy` - Kopiuje jeden lub więcej plików

Polecenie `copy` duplikuje jeden lub więcej plików z jednej lokalizacji do drugiej.

```cmd
copy [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B] źródło [/A | /B] [+ źródło [/A | /B] [+ ...]] [miejsce_docelowe [/A | /B]] [/?]
```

**Flagi/Parametry**:
*   `źródło`: Określa plik(i) do skopiowania. Można używać symboli wieloznacznych (`*`, `?`).
*   `miejsce_docelowe`: Określa katalog i/lub nazwę pliku dla nowego(ych) pliku(ów).
*   `/V`: Weryfikuje, czy nowe pliki zostały poprawnie zapisane.
*   `/Y`: Pomija monity o potwierdzenie nadpisania istniejącego pliku docelowego.
*   `/-Y`: Wymusza monit o potwierdzenie nadpisania istniejącego pliku docelowego.
*   `/A`: Wskazuje plik tekstowy ASCII.
*   `/B`: Wskazuje plik binarny.
*   `/Z`: Kopiuje pliki w trybie restartowalnym, przydatne dla dużych plików w sieci.
*   `/?`: Wyświetla pomoc dla polecenia.

**Przykłady**:
*   `copy plik.txt C:\backup`: Kopiuje `plik.txt` z bieżącego katalogu do `C:\backup`.
*   `copy *.doc C:\reports /V`: Kopiuje wszystkie pliki `.doc` z bieżącego katalogu do `C:\reports` i weryfikuje kopiowanie.
*   `copy C:\source\plik1.txt + C:\source\plik2.txt C:\cel\połączony.txt`: Łączy `plik1.txt` i `plik2.txt` w `połączony.txt`.
*   `copy D:\readme.htm`: Kopiuje `readme.htm` z dysku D: do bieżącego katalogu.

**Warunki sukcesu**:
*   Plik(i) są kopiowane do miejsca docelowego bez komunikatów o błędach.
*   Wyświetlany jest komunikat typu "Skopiowano 1 plik(ów).".
*   `ERRORLEVEL` wynosi `0`.

**Warunki niepowodzenia**:
*   "System nie może odnaleźć określonego pliku.": Jeśli plik źródłowy nie istnieje.
*   "Odmowa dostępu.": Jeśli nie masz uprawnień do zapisu w katalogu docelowym lub uprawnień do odczytu pliku źródłowego.
*   "Brak wystarczającej ilości miejsca na dysku.": Jeśli dysk docelowy jest pełny.
*   Jeśli użyto `/V` i weryfikacja nie powiedzie się, pojawi się komunikat o błędzie.
*   `ERRORLEVEL` będzie różny od zera (np. `1` dla ogólnego błędu).

#### 3. `ping` - Weryfikuje łączność na poziomie IP

Polecenie `ping` wysyła komunikaty żądania echa protokołu ICMP (Internet Control Message Protocol) do hosta docelowego w celu weryfikacji łączności na poziomie IP.

```cmd
ping [/t] [/a] [/n liczba] [/l rozmiar] [/f] [/i TTL] [/v TOS] [/r liczba] [/s liczba] [{/j lista_hostów | /k lista_hostów}] [/w limit_czasu] [/R] [/S adres_źródłowy] [/4] [/6] nazwa_docelowa
```

**Flagi/Parametry**:
*   `nazwa_docelowa`: Określa nazwę hosta lub adres IP miejsca docelowego.
*   `/t`: Pingowanie określonego hosta do momentu przerwania (Ctrl+C aby zatrzymać, Ctrl+Break aby wyświetlić statystyki).
*   `/a`: Rozwiązuje adresy na nazwy hostów.
*   `/n liczba`: Określa liczbę żądań echa do wysłania (domyślnie 4).
*   `/l rozmiar`: Określa rozmiar bufora wysyłania w bajtach (domyślnie 32).
*   `/w limit_czasu`: Określa limit czasu w milisekundach na oczekiwanie na każdą odpowiedź (domyślnie 4000ms).
*   `/?`: Wyświetla pomoc dla polecenia.

**Przykłady**:
*   `ping google.com`: Pingowanie `google.com` cztery razy.
*   `ping 192.168.1.1 -n 10`: Pingowanie adresu IP `192.168.1.1` dziesięć razy.
*   `ping localhost`: Pingowanie lokalnej maszyny.
*   `ping -t 8.8.8.8`: Ciągłe pingowanie serwera DNS Google do momentu ręcznego zatrzymania.

**Warunki sukcesu**:
*   "Odpowiedź z <adres IP>": Wskazuje na pomyślną odpowiedź od celu.
*   "TTL=" w danych wyjściowych.
*   Podsumowanie pokazujące "Pakiety: Wysłane = X, Odebrane = X, Utracone = 0 (0% strat)".
*   Polecenie zwraca kod wyjścia `0`.

**Warunki niepowodzenia**:
*   "Upłynął limit czasu żądania.": Cel nie odpowiedział w określonym limicie czasu.
*   "Host docelowy nieosiągalny.": Nie można znaleźć trasy do hosta docelowego.
*   "Żądanie ping nie mogło znaleźć hosta <nazwa_hosta>. Sprawdź nazwę i spróbuj ponownie.": Nie można rozwiązać nazwy hosta na adres IP (problem DNS).
*   "Ogólny błąd.": Wskazuje na problem z lokalnym interfejsem sieciowym.
*   Podsumowanie pokazujące "Pakiety: Wysłane = X, Odebrane = Y, Utracone = Z (Z% strat)", gdzie Z > 0.
*   Polecenie zwraca kod wyjścia różny od zera (np. `1`, jeśli host jest nieosiągalny).

#### 4. `mkdir` (lub `md`) - Tworzy katalog

Polecenie `mkdir` tworzy nowy katalog lub podkatalog.

```cmd
mkdir [dysk:]ścieżka
```

**Flagi/Parametry**:
*   `[dysk:]ścieżka`: Określa dysk i ścieżkę katalogu do utworzenia.
*   `/?`: Wyświetla pomoc dla polecenia.
*   (Uwaga: Flaga `-p` do tworzenia katalogów nadrzędnych, powszechna w systemach uniksowych, nie jest standardową flagą `cmd`. Rozszerzenia poleceń w systemie Windows umożliwiają tworzenie pośrednich katalogów w określonej ścieżce za pomocą pojedynczego polecenia `mkdir`, co w niektórych przypadkach jest podobne do `-p`).

**Przykłady**:
*   `mkdir nowy_folder`: Tworzy katalog o nazwie `nowy_folder` w bieżącym katalogu.
*   `mkdir C:\projekty\mój_projekt`: Tworzy `mój_projekt` wewnątrz `C:\projekty`. Jeśli `C:\projekty` nie istnieje, `cmd` z włączonymi rozszerzeniami poleceń utworzy go.
*   `md "Moje Dokumenty"`: Tworzy katalog o nazwie "Moje Dokumenty" (cudzysłowy są potrzebne ze względu na spację).

**Warunki sukcesu**:
*   Katalog jest tworzony bez żadnych komunikatów o błędach.
*   W przypadku sukcesu zazwyczaj nie jest wyświetlany żaden wynik.
*   `ERRORLEVEL` wynosi `0`.

**Warunki niepowodzenia**:
*   "Podkatalog lub plik <nazwa_katalogu> już istnieje.": Jeśli katalog o tej samej nazwie już istnieje w określonej lokalizacji.
*   "System nie może odnaleźć określonej ścieżki.": Jeśli pośredni katalog w ścieżce nie istnieje, a rozszerzenia poleceń są wyłączone (lub jeśli ścieżka jest nieprawidłowa).
*   "Odmowa dostępu.": Jeśli nie masz uprawnień do zapisu w katalogu nadrzędnym.
*   `ERRORLEVEL` jest różny od zera (np. `1`).

#### 5. `del` (lub `erase`) - Usuwa jeden lub więcej plików

Polecenie `del` usuwa jeden lub więcej plików.

```cmd
del [/p] [/f] [/s] [/q] [/a[:atrybuty]] nazwy
```

**Flagi/Parametry**:
*   `nazwy`: Określa listę jednego lub więcej plików do usunięcia. Można używać symboli wieloznacznych (`*`, `?`).
*   `/P`: Monituje o potwierdzenie przed usunięciem każdego pliku.
*   `/F`: Wymusza usunięcie plików tylko do odczytu.
*   `/S`: Usuwa określone pliki ze wszystkich podkatalogów. Wyświetla nazwy usuwanych plików.
*   `/Q`: Tryb cichy; pomija monity o potwierdzenie usunięcia.
*   `/A[:atrybuty]`: Usuwa pliki na podstawie atrybutów.
    *   `R`: Pliki tylko do odczytu
    *   `H`: Pliki ukryte
    *   `S`: Pliki systemowe
    *   `A`: Pliki gotowe do archiwizacji
    *   `-`: Prefiks oznaczający "nie"
*   `/?`: Wyświetla pomoc dla polecenia.

**Przykłady**:
*   `del stary_plik.txt`: Usuwa `stary_plik.txt` z bieżącego katalogu.
*   `del *.bak /Q`: Usuwa wszystkie pliki z rozszerzeniem `.bak` w bieżącym katalogu bez monitowania.
*   `del /S /Q C:\temp\*.*`: Usuwa wszystkie pliki w `C:\temp` i jego podkatalogach bez monitowania.
*   `del /F tylko_do_odczytu.txt`: Wymusza usunięcie pliku tylko do odczytu o nazwie `tylko_do_odczytu.txt`.

**Warunki sukcesu**:
*   Plik(i) są usuwane bez komunikatów o błędach.
*   Jeśli nie użyto `/P`, w przypadku sukcesu może nie być żadnego wyniku, lub komunikat typu "Usunięto plik - <nazwa_pliku>", jeśli użyto `/S`.
*   `ERRORLEVEL` wynosi `0`.

**Warunki niepowodzenia**:
*   "Nie można odnaleźć <nazwa_pliku>": Jeśli określony plik nie istnieje.
*   "Odmowa dostępu.": Jeśli nie masz niezbędnych uprawnień do usunięcia pliku, lub jeśli plik jest używany przez inny proces, a `/F` nie jest wystarczające.
*   "Proces nie może uzyskać dostępu do pliku, ponieważ jest on używany przez inny proces.": Jeśli plik jest zablokowany przez inną aplikację.
*   `del` usunie pliki w katalogu, jeśli podano nazwę katalogu, ale nie usunie samego katalogu. Do usuwania katalogów użyj `rmdir`.
*   `ERRORLEVEL` jest różny od zera.

### Dalsze czytanie
Aby uzyskać bardziej szczegółowe informacje, zapoznaj się z oficjalną dokumentacją `cmd`.

