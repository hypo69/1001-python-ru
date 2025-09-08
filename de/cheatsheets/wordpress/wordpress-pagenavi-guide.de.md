# Vollständige Anleitung zu Variablen in WP-PageNavi für WordPress

Die Seitennavigation ist ein wichtiger Bestandteil jedes Blogs oder jeder Nachrichten-Website in WordPress. Eines der beliebtesten Tools für eine bequeme Seitennavigation ist das Plugin **WP-PageNavi**. Es ermöglicht, die Standardlinks „Vorherige / Nächste“ durch eine flexiblere und ansprechendere Paginierung zu ersetzen.

Eine der Hauptfunktionen ist die Anpassung des Linktextes über **Variablen**, die automatisch die aktuelle Seitenzahl, die Gesamtseitenzahl und andere Informationen einfügen.

In diesem Artikel werden **alle verfügbaren Variablen** und Beispiele für deren Verwendung erläutert und anhand von Screenshots gezeigt, wo sie eingefügt werden müssen.

---

## Wo sich die WP-PageNavi-Einstellungen befinden

Nach der Installation des Plugins gehen Sie im WordPress-Adminbereich zu:

**Einstellungen → PageNavi**

Dort sehen Sie das Menü zur Einstellung des Linktextes (Beispiel im Screenshot unten):

![WP-PageNavi-Einstellungen in WordPress](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 In jedem Feld können Variablen verwendet werden, um die aktuelle Seite, die Gesamtseitenzahl und andere Navigationselemente dynamisch anzuzeigen.

---

## Verfügbare WP-PageNavi-Variablen

Das Plugin bietet eine Reihe von Platzhaltern (Vorlagenvariablen), die in den Einstellungen verwendet werden können:

### 🔹 %CURRENT_PAGE%
Zeigt die **Nummer der aktuellen Seite** an.

Beispiel:
```
Sie sind auf Seite %CURRENT_PAGE%
```
👉 Wenn Sie sich auf Seite 3 befinden, lautet das Ergebnis:
```
Sie sind auf Seite 3
```

---

### 🔹 %TOTAL_PAGES%
Zeigt die **Gesamtanzahl der Seiten** an.

Beispiel:
```
Gesamtseiten: %TOTAL_PAGES%
```
👉 Wenn es insgesamt 10 Seiten gibt, lautet die Ausgabe:
```
Gesamtseiten: 10
```

---

### 🔹 %PAGE_NUMBER%
Wird verwendet, um die **Nummer jeder Seite** in der Liste anzuzeigen.

Beispiel:
```
Seite %PAGE_NUMBER%
```
👉 In der Navigation erscheinen Links:
```
Seite 1 | Seite 2 | Seite 3 | ...
```

---

## WP-PageNavi-Variablentabelle

| Variable          | Beschreibung                          | Einstellungsbeispiel                | Ergebnis (wenn 3. Seite von 10)      |
|-------------------|---------------------------------------|-------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Nummer der aktuellen Seite            | `Sie sind jetzt auf Seite %CURRENT_PAGE%` | `Sie sind jetzt auf Seite 3`         |
| **%TOTAL_PAGES%**  | Gesamtanzahl der Seiten               | `Gesamtseiten: %TOTAL_PAGES%`       | `Gesamtseiten: 10`                   |
| **%PAGE_NUMBER%**  | Nummer jeder Seite in der Liste       | `Seite %PAGE_NUMBER%`               | `Seite 1 | Seite 2 | Seite 3 …`      |
| **1 (statisch)**   | Erste Seite (keine Variable)          | `Erste` oder `Seite 1`              | `Erste`                              |
| **%TOTAL_PAGES%**  | Letzte Seite                          | `Seite %TOTAL_PAGES%`               | `Seite 10`                           |
| **← / → / …**      | Symbole für Pfeile und Abkürzungen    | `← Zurück`, `Weiter →`, `…`         | `← Zurück | 1 | 2 | 3 | … | 10 | Weiter →` |

---

## Beispiel für eine vollständige Konfiguration

Im obigen Screenshot können die Felder wie folgt ausgefüllt werden:

- **Text For Number Of Pages**:
  `Seite %CURRENT_PAGE% von %TOTAL_PAGES%`

- **Text For Current Page**:
  `%PAGE_NUMBER%`

- **Text For Page**:
  `%PAGE_NUMBER%`

- **Text For First Page**:
  `Erste`

- **Text For Last Page**:
  `Seite %TOTAL_PAGES%`

- **Text For Previous Page**:
  `← Zurück`

- **Text For Next Page**:
  `Weiter →`

- **Text For Previous …**:
  `…`

- **Text For Next …**:
  `…`

👉 Am Ende sehen die Besucher eine Navigation, die ungefähr so aussieht:
```
← Zurück | Erste | 1 | 2 | 3 | … | Seite 10 | Weiter →
```

---

## Zusammenfassung

Die Variablen in WP-PageNavi sind einfach, bieten aber Flexibilität bei der Navigationseinstellung:

- `%CURRENT_PAGE%` — aktuelle Seite
- `%TOTAL_PAGES%` — Gesamtseiten
- `%PAGE_NUMBER%` — Nummer der spezifischen Seite

Für die erste Seite verwenden Sie `1`, und für die letzte Seite `%TOTAL_PAGES%`.

Dank dieser Einstellungen kann die Navigation auf der Website für Besucher verständlicher und bequemer gestaltet werden.
