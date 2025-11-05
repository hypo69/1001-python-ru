# Maussteuerung in Python: Übersicht und Vergleich von Bibliotheken

Die Automatisierung von Mausaktionen ist ein leistungsstarkes Werkzeug für Tests, wissenschaftliche Forschung, Geschäftsprozesse und die Entwicklung von assistiven Technologien. Innerhalb des Python-Ökosystems gibt es mehrere Bibliotheken für diese Zwecke, jede mit ihren eigenen Stärken und Anwendungsfällen. In diesem Artikel werden wir drei wichtige plattformübergreifende Bibliotheken detailliert betrachten: `PyAutoGUI`, `pynput` und `mouse`, und auch kurz andere spezialisierte Lösungen erwähnen.

## 1. PyAutoGUI-Bibliothek: Hochrangige GUI-Automatisierung

`PyAutoGUI` ist eine leistungsstarke und benutzerfreundliche plattformübergreifende Bibliothek, die es Python-Skripten ermöglicht, Maus und Tastatur zu steuern, Screenshots zu erstellen und andere GUI-Automatisierungsaufgaben durchzuführen. Sie ist ideal für die Automatisierung routinemäßiger Aufgaben, Softwaretests und die Erstellung von Bots. **Unterstützt Windows, macOS und Linux.**

### Installation

```bash
pip install pyautogui
```

### Hauptmerkmale

*   **Cursorbewegung**: `pyautogui.moveTo(x, y, duration=seconds)` für absolute Bewegung und `pyautogui.move(xOffset, yOffset, duration=seconds)` für relative Bewegung.
*   **Maustastenanschläge**: `pyautogui.click()`, `pyautogui.rightClick()`, `pyautogui.doubleClick()`, `pyautogui.tripleClick()`. Sie können Koordinaten und die Taste angeben.
*   **Drag and Drop**: `pyautogui.dragTo(x, y, duration=seconds)` oder `pyautogui.drag(xOffset, yOffset, duration=seconds)`.
*   **Mausrad-Scrollen**: `pyautogui.scroll(amount)` (positiver Wert scrollt nach oben, negativer Wert nach unten).
*   **Tastaturinteraktion**: `pyautogui.write()`, `pyautogui.press()`, `pyautogui.hotkey()`.
*   **Cursorposition abrufen**: `pyautogui.position()`.
*   **Failsafe**: Eine integrierte Sicherheitsfunktion, die das Skript stoppt, wenn der Mauszeiger in eine der vier Ecken des Bildschirms bewegt wird.

### Anwendungsbeispiele

```python
import pyautogui
import time

# Cursor bewegen
pyautogui.moveTo(100, 150, duration=1)
print(f"Cursor bewegt nach {pyautogui.position()}")

# Linksklick
pyautogui.click(200, 250)
print("Klick ausgeführt.")

# Ziehen
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.dragTo(600, 600, duration=1)
print("Ziehen ausgeführt.")

# Mausrad scrollen
pyautogui.scroll(-100)
print("Nach unten gescrollt.")

# Text eingeben
pyautogui.write('Hallo, PyAutoGUI!', interval=0.1)
print("Text eingegeben.")
```

### Wann sollte man PyAutoGUI verwenden?

✅ Ideal, wenn Sie eine schnelle und einfache Möglichkeit benötigen, Benutzeraktionen zu automatisieren, Eingaben zu simulieren und Screenshots zu erstellen. Es eignet sich hervorragend für hochrangige Automatisierungsskripte, bei denen keine detaillierte Kontrolle über Eingabeereignisse erforderlich ist.

❌ Nicht die beste Wahl für die Überwachung von Low-Level-Ereignissen oder die Eingabeblockierung.

## 2. pynput-Bibliothek: Flexible Steuerung und Überwachung

`pynput` ist ein modernes, aktiv gepflegtes Werkzeug zur umfassenden Überwachung und Steuerung von Eingabegeräten. Es bietet detaillierten Zugriff auf Maus- und Tastaturereignisse, einschließlich der Möglichkeit, diese in Echtzeit zu blockieren oder zu ändern. **Unterstützt Windows, macOS und Linux.**

### Installation

```bash
pip install pynput
```

### Hauptmerkmale

*   **Umfassende Ereignis-Listener**: `pynput.mouse.Listener` ermöglicht die Verfolgung von Bewegungen, Klicks und Scrollen mit Zugriff auf Koordinaten, Tastentyp und Zustand (gedrückt/losgelassen).
*   **Ereignisblockierung**: Wenn ein Ereignishandler `False` zurückgibt, wird das Ereignis nicht an das System weitergeleitet. Dies ist eine einzigartige und leistungsstarke Funktion.
*   **Maussteuerung über Controller**: `pynput.mouse.Controller` zur Emulation von Aktionen (Positionierung, relative Bewegung, Klicks, Scrollen).
*   **Einheitliche Tastaturarchitektur**: Einfache Kombination von Maus- und Tastaturaktionen.
*   **Thread-Sicherheit**: Listener arbeiten in separaten Threads und bieten eine flexible Verwaltung.

### Anwendungsbeispiele

```python
from pynput import mouse
from pynput.mouse import Controller, Button
import time

# Maussteuerung
mouse_ctrl = Controller()
print(f"Aktuelle Position: {mouse_ctrl.position}")
mouse_ctrl.position = (100, 200)
mouse_ctrl.move(50, -50)
mouse_ctrl.click(Button.left, 1)
mouse_ctrl.scroll(0, 2)
print("Mausaktionen ausgeführt.")

# Ereignis-Listener
def on_click(x, y, button, pressed):
    print(f"Klick bei ({x}, {y}) mit Taste {button}. Gedrückt: {pressed}")
    if not pressed:
        # Listener nach Loslassen der Taste stoppen
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
print("Listener aktiv. Klicken Sie mit der Maus.")
listener.join() # Warten, bis der Listener beendet ist
print("Listener beendet.")
```

### Wann sollte man pynput verwenden?

✅ Ideal, wenn Sie:
- Das **Benutzerverhalten analysieren** müssen (Koordinaten, Trajektorien, Klickfrequenz).
- **Hotkey-Systeme**, **Eingabefilter** oder **assistive Technologien** erstellen.
- Eingaben in Echtzeit **blockieren oder ändern** möchten.
- Ein **wissenschaftliches Experiment**, **Usability-Tests** oder ein **Sicherheitssystem** durchführen.
- Eine **Maus- und Tastaturintegration** in einem einzigen Skript benötigen.

❌ Nicht die schnellste Wahl, wenn Sie nur Aktionen ohne Analyse aufzeichnen und wiedergeben müssen.

## 3. mouse-Bibliothek: Einfachheit und Aktionsaufzeichnung

Die `mouse`-Bibliothek ist ein minimalistisches, aber effektives Werkzeug zum Emulieren und Aufzeichnen von Mausaktionssequenzen. Ihr Hauptmerkmal ist die integrierte Unterstützung für die Aufzeichnung und Wiedergabe, was sie ideal für das schnelle Prototyping von Makros. **Unterstützt Windows, macOS und Linux.**

### Installation

```bash
pip install mouse
```

### Hauptmerkmale

*   **Cursorbewegung**: `mouse.move(x, y, absolute=True/False)`.
*   **Maustastenanschläge**: `mouse.click('left'/'right'/'middle')`.
*   **Drag and Drop**: `mouse.drag(x1, y1, x2, y2, absolute=True)`.
*   **Mausrad**: `mouse.wheel(delta)`.
*   **Cursorposition abrufen**: `mouse.get_position()`.
*   **Tastenzustand prüfen**: `mouse.is_pressed(button)`.
*   **Ereignisse aufzeichnen und wiedergeben**: `mouse.record()` und `mouse.play()`. Dies ist eine einzigartige integrierte Funktion.
*   **Einfacher Klick-Handler**: `mouse.on_click(handler)`.

### Anwendungsbeispiele

```python
import mouse
import time

# Bewegen und klicken
mouse.move(200, 300, absolute=True, duration=0.2)
mouse.click('left')
print("Bewegung und Klick ausgeführt.")

# Aufzeichnen und wiedergeben (erfordert interaktive Eingabe)
print("Aufzeichnung starten. Rechte Maustaste drücken, um zu stoppen.")
# events = mouse.record()
# print("Aufzeichnung beendet. Wiedergabe...")
# mouse.play(events[:-1]) # Alle Ereignisse außer dem letzten (Loslassen der rechten Maustaste) wiedergeben
# print("Wiedergabe beendet.")

# Scrollen
mouse.wheel(-2)
print("Nach unten gescrollt.")
```

### Wann sollte man mouse verwenden?

✅ Ideal für:
- Aufzeichnen und Wiedergeben von Routineaktionen.
- Einfache Automatisierungsskripte ohne Feedback.
- Lehrbeispiele und Demonstrationen, bei denen maximale Einfachheit entscheidend ist.

❌ Nicht geeignet für:
- Analyse des Benutzerverhaltens (Handler erhalten keine Koordinaten).
- Erstellen von Eingabefiltern oder Blockern.
- Tastaturintegration.
- Das Projekt wurde seit 2021 nicht mehr aktualisiert, was ein Risiko für langfristige Projekte darstellen kann.

## 4. Andere bemerkenswerte Bibliotheken

Obwohl `PyAutoGUI`, `pynput` und `mouse` die vielseitigsten sind, gibt es andere Bibliotheken für spezifischere Aufgaben:

*   **PyDirectInput**: Eine spezialisierte Bibliothek, die als Alternative zu `PyAutoGUI` für die Spielautomatisierung entwickelt wurde. Sie kann Probleme umgehen, bei denen einige Spiele Eingaben von `PyAutoGUI` aufgrund ihrer spezifischen Eingabeverarbeitungsmechanismen nicht registrieren.
*   **pywinauto**: Konzentriert sich auf die Automatisierung der Windows-Benutzeroberfläche. Es interagiert mit Windows-Steuerelementen unter Verwendung von Barrierefreiheits- und UI-Automatisierungs-Frameworks, was es zu einer zuverlässigen Wahl für die Automatisierung nativer Windows-Anwendungen macht, indem es Elemente anstelle von Bildschirmkoordinaten anspricht.

## 5. Vergleichstabelle

| Funktion / Bibliothek    | PyAutoGUI | pynput | mouse |
|--------------------------|:---------:|:------:|:-----:|
| **Unterstützte Betriebssysteme** | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux |
|--------------------------|:---------:|:------:|:-----:|
| **Installation**         | `pip install pyautogui` | `pip install pynput` | `pip install mouse` |
| **Cursorbewegung**       | ✅ Abs./Rel. | ✅ Abs./Rel. | ✅ Abs./Rel. |
| **Maustastenanschläge**  | ✅ Alle Typen | ✅ Alle Typen | ✅ Alle Typen |
| **Drag and Drop**        | ✅ `dragTo()` | ⚠️ Manuell | ✅ `drag()` |
| **Mausrad-Scrollen**     | ✅ Ja       | ✅ Ja    | ✅ Ja   |
| **Position abrufen**     | ✅ Ja       | ✅ Ja    | ✅ Ja   |
| **Tastenzustand prüfen** | ❌ Nein     | ⚠️ Über Listener | ✅ Ja   |
| **Aufzeichnung/Wiedergabe** | ❌ Nein     | ❌ Nein (nur manuell) | ✅ Integriert |
| **Koordinaten im Handler** | ❌ Nein     | ✅ Ja    | ❌ Nein |
| **Ereignisblockierung**  | ❌ Nein     | ✅ Ja (`return False`) | ❌ Nein |
| **Tastaturintegration**  | ✅ Ja       | ✅ Ja    | ❌ Nein |
| **Aktive Unterstützung** | ✅ Ja       | ✅ Ja    | ❌ Nein (seit 2021) |
| **Failsafe**             | ✅ Ja       | ❌ Nein  | ❌ Nein |
| **API-Komplexität**      | Mittel      | Mittel/Hoch | Niedrig |

## Fazit

Die Wahl einer Python-Maussteuerungsbibliothek hängt von Ihren spezifischen Anforderungen ab:

*   **PyAutoGUI**: Ihre Standardwahl für die hochrangige GUI-Automatisierung, wenn Sie Benutzeraktionen, einschließlich Tastatur und Screenshots, ohne detaillierte Ereignisanalyse simulieren müssen.
*   **pynput**: Ideal für Projekte, die eine präzise Kontrolle über Maus- (und Tastatur-) Ereignisse, Überwachung, Analyse sowie die Möglichkeit erfordern, Eingaben in Echtzeit zu blockieren oder zu ändern. Es ist ein professionelles Werkzeug für komplexe Systeme.
*   **mouse**: Am besten geeignet für einfache Aufgaben der Makroaufzeichnung und -wiedergabe, bei denen maximale Einfachheit und minimaler Code wichtig sind. Die mangelnde aktive Unterstützung sollte jedoch berücksichtigt werden.

Für neue Projekte, die Flexibilität und langfristige Unterstützung erfordern, wird `pynput` empfohlen. Wenn Ihre Aufgabe die schnelle Automatisierung routinemäßiger Aktionen ist, ist `PyAutoGUI` eine ausgezeichnete Wahl.
