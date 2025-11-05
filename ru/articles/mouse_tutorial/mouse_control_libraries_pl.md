# Sterowanie myszą w Pythonie: Przegląd i porównanie bibliotek

Automatyzacja działań myszy to potężne narzędzie do testowania, badań naukowych, procesów biznesowych i tworzenia technologii wspomagających. W ekosystemie Pythona istnieje kilka bibliotek do tych celów, każda z własnymi mocnymi stronami i przypadkami użycia. W tym artykule szczegółowo omówimy trzy główne biblioteki wieloplatformowe: `PyAutoGUI`, `pynput` i `mouse`, a także krótko wspomnimy o innych wyspecjalizowanych rozwiązaniach.

## 1. Biblioteka PyAutoGUI: Wysokopoziomowa automatyzacja GUI

`PyAutoGUI` to potężna i łatwa w użyciu biblioteka wieloplatformowa, która umożliwia skryptom Pythona sterowanie myszą i klawiaturą, robienie zrzutów ekranu i wykonywanie innych zadań automatyzacji graficznego interfejsu użytkownika (GUI). Jest idealna do automatyzacji rutynowych zadań, testowania oprogramowania i tworzenia botów. **Obsługuje Windows, macOS i Linux.**

### Instalacja

```bash
pip install pyautogui
```

### Kluczowe cechy

*   **Ruch kursora**: `pyautogui.moveTo(x, y, duration=seconds)` dla ruchu absolutnego i `pyautogui.move(xOffset, yOffset, duration=seconds)` dla ruchu względnego.
*   **Kliknięcia myszy**: `pyautogui.click()`, `pyautogui.rightClick()`, `pyautogui.doubleClick()`, `pyautogui.tripleClick()`. Możesz określić współrzędne i przycisk.
*   **Przeciągnij i upuść (Drag and Drop)**: `pyautogui.dragTo(x, y, duration=seconds)` lub `pyautogui.drag(xOffset, yOffset, duration=seconds)`.
*   **Przewijanie kółkiem myszy**: `pyautogui.scroll(amount)` (wartość dodatnia przewija w górę, ujemna w dół).
*   **Interakcja z klawiaturą**: `pyautogui.write()`, `pyautogui.press()`, `pyautogui.hotkey()`.
*   **Pobieranie pozycji kursora**: `pyautogui.position()`.
*   **Failsafe**: Wbudowana funkcja bezpieczeństwa, która zatrzymuje skrypt, gdy kursor myszy zostanie przesunięty do jednego z czterech rogów ekranu.

### Przykłady użycia

```python
import pyautogui
import time

# Przesuń kursor
pyautogui.moveTo(100, 150, duration=1)
print(f"Kursor przesunięty do {pyautogui.position()}")

# Lewy klik
pyautogui.click(200, 250)
print("Kliknięcie wykonane.")

# Przeciągnij
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.dragTo(600, 600, duration=1)
print("Przeciągnięcie wykonane.")

# Przewiń kółkiem
pyautogui.scroll(-100)
print("Przewinięto w dół.")

# Wpisz tekst
pyautogui.write('Witaj, PyAutoGUI!', interval=0.1)
print("Tekst wpisany.")
```

### Kiedy używać PyAutoGUI?

✅ Idealne, jeśli potrzebujesz szybkiego i łatwego sposobu na automatyzację działań użytkownika, symulowanie wprowadzania danych i robienie zrzutów ekranu. Jest doskonałe do wysokopoziomowych skryptów automatyzacji, gdzie nie jest wymagana szczegółowa kontrola nad zdarzeniami wejściowymi.

❌ Nie jest najlepszym wyborem do niskopoziomowego monitorowania zdarzeń lub blokowania wprowadzania danych.

## 2. Biblioteka pynput: Elastyczna kontrola i monitorowanie

`pynput` to nowoczesne, aktywnie rozwijane narzędzie do kompleksowego monitorowania i sterowania urządzeniami wejściowymi. Zapewnia szczegółowy dostęp do zdarzeń myszy i klawiatury, w tym możliwość blokowania lub modyfikowania ich w czasie rzeczywistym. **Obsługuje Windows, macOS i Linux.**

### Instalacja

```bash
pip install pynput
```

### Kluczowe cechy

*   **Kompleksowe słuchacze zdarzeń**: `pynput.mouse.Listener` umożliwia śledzenie ruchów, kliknięć i przewijania z dostępem do współrzędnych, typu przycisku i stanu (naciśnięty/zwolniony).
*   **Blokowanie zdarzeń**: Jeśli program obsługi zdarzeń zwróci `False`, zdarzenie nie jest przekazywane dalej do systemu. Jest to unikalna i potężna funkcja.
*   **Sterowanie myszą za pomocą kontrolera**: `pynput.mouse.Controller` do emulacji działań (pozycjonowanie, ruch względny, kliknięcia, przewijanie).
*   **Ujednolicona architektura klawiatury**: Łatwe łączenie działań myszy i klawiatury.
*   **Bezpieczeństwo wątków**: Słuchacze działają w oddzielnych wątkach, zapewniając elastyczne zarządzanie.

### Przykłady użycia

```python
from pynput import mouse
from pynput.mouse import Controller, Button
import time

# Sterowanie myszą
mouse_ctrl = Controller()
print(f"Aktualna pozycja: {mouse_ctrl.position}")
mouse_ctrl.position = (100, 200)
mouse_ctrl.move(50, -50)
mouse_ctrl.click(Button.left, 1)
mouse_ctrl.scroll(0, 2)
print("Wykonano działania myszy.")

# Słuchacz zdarzeń
def on_click(x, y, button, pressed):
    print(f"Kliknięcie w ({x}, {y}) przyciskiem {button}. Naciśnięty: {pressed}")
    if not pressed:
        # Zatrzymaj słuchacza po zwolnieniu przycisku
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
print("Słuchacz aktywny. Kliknij myszą.")
listener.join() # Poczekaj na zakończenie słuchacza
print("Słuchacz zakończony.")
```

### Kiedy używać pynput?

✅ Idealne, jeśli:
- Potrzebujesz **analizować zachowanie użytkownika** (współrzędne, trajektorie, częstotliwość kliknięć).
- Tworzysz **systemy skrótów klawiszowych**, **filtry wejścia** lub **technologie wspomagające**.
- Chcesz **blokować lub modyfikować dane wejściowe** w czasie rzeczywistym.
- Przeprowadzasz **eksperyment naukowy**, **testy użyteczności** lub **system bezpieczeństwa**.
- Wymagana jest **integracja myszy i klawiatury** w jednym skrypcie.

❌ Nie jest to najszybszy wybór, jeśli potrzebujesz tylko nagrywać i odtwarzać działania bez analizy.

## 3. Biblioteka mouse: Prostota i nagrywanie działań

Biblioteka `mouse` to minimalistyczne, ale skuteczne narzędzie do emulacji i nagrywania sekwencji działań myszy. Jej główną cechą jest wbudowana obsługa nagrywania i odtwarzania, co czyni ją idealną do szybkiego prototypowania makr. **Obsługuje Windows, macOS i Linux.**

### Instalacja

```bash
pip install mouse
```

### Kluczowe cechy

*   **Ruch kursora**: `mouse.move(x, y, absolute=True/False)`.
*   **Kliknięcia myszy**: `mouse.click('left'/'right'/'middle')`.
*   **Przeciągnij i upuść**: `mouse.drag(x1, y1, x2, y2, absolute=True)`.
*   **Kółko przewijania**: `mouse.wheel(delta)`.
*   **Pobieranie pozycji kursora**: `mouse.get_position()`.
*   **Sprawdzanie stanu przycisku**: `mouse.is_pressed(button)`.
*   **Nagrywanie i odtwarzanie zdarzeń**: `mouse.record()` i `mouse.play()`. Jest to unikalna wbudowana funkcja.
*   **Prosty program obsługi kliknięć**: `mouse.on_click(handler)`.

### Przykłady użycia

```python
import mouse
import time

# Przesuń i kliknij
mouse.move(200, 300, absolute=True, duration=0.2)
mouse.click('left')
print("Przesunięcie i kliknięcie wykonane.")

# Nagrywanie i odtwarzanie (wymaga interaktywnego wprowadzania)
print("Rozpocznij nagrywanie. Naciśnij prawy przycisk, aby zatrzymać.")
# events = mouse.record()
# print("Nagrywanie zakończone. Odtwarzanie...")
# mouse.play(events[:-1]) # Odtwórz wszystkie zdarzenia oprócz ostatniego (zwolnienie prawego przycisku)
# print("Odtwarzanie zakończone.")

# Przewiń
mouse.wheel(-2)
print("Przewinięto w dół.")
```

### Kiedy używać mouse?

✅ Idealne do:
- Nagrywania i odtwarzania rutynowych działań.
- Prostych skryptów automatyzacji bez informacji zwrotnej.
- Przykładów edukacyjnych i demonstracji, gdzie kluczowa jest maksymalna prostota.

❌ Nie nadaje się do:
- Analizy zachowania użytkownika (programy obsługi nie otrzymują współrzędnych).
- Tworzenia filtrów wejścia lub blokad.
- Integracji z klawiaturą.
- Projekt nie był aktualizowany od 2021 roku, co może stanowić ryzyko dla długoterminowych projektów.

## 4. Inne godne uwagi biblioteki

Chociaż `PyAutoGUI`, `pynput` i `mouse` są najbardziej wszechstronne, istnieją inne biblioteki do bardziej specyficznych zadań:

*   **PyDirectInput**: Wyspecjalizowana biblioteka zaprojektowana jako alternatywa dla `PyAutoGUI` do automatyzacji gier. Może omijać problemy, w których niektóre gry mogą nie rejestrować danych wejściowych z `PyAutoGUI` ze względu na ich specyficzne mechanizmy obsługi wejścia.
*   **pywinauto**: Skoncentrowana na automatyzacji interfejsu użytkownika systemu Windows. Współpracuje z kontrolkami systemu Windows, wykorzystując struktury dostępności i automatyzacji interfejsu użytkownika, co czyni ją niezawodnym wyborem do automatyzacji natywnych aplikacji systemu Windows poprzez celowanie w elementy, a nie w współrzędne ekranu.

## 5. Tabela porównawcza

| Funkcja / Biblioteka     | PyAutoGUI | pynput | mouse |
|--------------------------|:---------:|:------:|:-----:|
| **Obsługiwane systemy operacyjne** | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux |
|--------------------------|:---------:|:------:|:-----:|
| **Instalacja**           | `pip install pyautogui` | `pip install pynput` | `pip install mouse` |
| **Ruch kursora**         | ✅ Abs./Wzgl. | ✅ Abs./Wzgl. | ✅ Abs./Wzgl. |
| **Kliknięcia myszy**     | ✅ Wszystkie typy | ✅ Wszystkie typy | ✅ Wszystkie typy |
| **Przeciągnij i upuść**  | ✅ `dragTo()` | ⚠️ Ręcznie | ✅ `drag()` |
| **Przewijanie kółkiem**  | ✅ Tak      | ✅ Tak   | ✅ Tak  |
| **Pobieranie pozycji**   | ✅ Tak      | ✅ Tak   | ✅ Tak  |
| **Sprawdzanie stanu przycisku** | ❌ Nie      | ⚠️ Przez Listener | ✅ Tak  |
| **Nagrywanie/Odtwarzanie** | ❌ Nie      | ❌ Nie (tylko ręcznie) | ✅ Wbudowane |
| **Współrzędne w programie obsługi** | ❌ Nie      | ✅ Tak   | ❌ Nie  |
| **Blokowanie zdarzeń**   | ❌ Nie      | ✅ Tak (`return False`) | ❌ Nie  |
| **Integracja z klawiaturą** | ✅ Tak      | ✅ Tak   | ❌ Nie  |
| **Aktywne wsparcie**     | ✅ Tak      | ✅ Tak   | ❌ Nie (od 2021) |
| **Failsafe**             | ✅ Tak      | ❌ Nie   | ❌ Nie  |
| **Złożoność API**        | Średnia     | Średnia/Wysoka | Niska |

## Podsumowanie

Wybór biblioteki do sterowania myszą w Pythonie zależy od konkretnych potrzeb:

*   **PyAutoGUI**: Twój domyślny wybór do wysokopoziomowej automatyzacji GUI, gdy musisz symulować działania użytkownika, w tym klawiaturę i zrzuty ekranu, bez głębokiej analizy zdarzeń.
*   **pynput**: Idealny do projektów wymagających precyzyjnej kontroli nad zdarzeniami myszy (i klawiatury), monitorowania, analizy, a także możliwości blokowania lub modyfikowania danych wejściowych w czasie rzeczywistym. Jest to profesjonalne narzędzie do złożonych systemów.
*   **mouse**: Najlepiej nadaje się do prostych zadań nagrywania i odtwarzania makr, gdzie ważna jest maksymalna prostota i minimalny kod. Należy jednak wziąć pod uwagę brak aktywnego wsparcia.

Do nowych projektów wymagających elastyczności i długoterminowego wsparcia zaleca się `pynput`. Jeśli Twoim zadaniem jest szybka automatyzacja rutynowych działań, `PyAutoGUI` będzie doskonałym wyborem.
