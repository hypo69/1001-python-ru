Sie haben absolut Recht. Vielen Dank für die Klarstellung. Die Verwendung von „Anführungszeichen“ ist Standard in der russischen Typografie.

Hier ist die korrigierte Version des Artikels mit den richtigen Anführungszeichen:

***

### So aktualisieren Sie Programme automatisch mit Ninite und der Windows-Aufgabenplanung

Software auf dem neuesten Stand zu halten, ist der Schlüssel zur Sicherheit und Stabilität Ihres Systems. Das manuelle Überprüfen und Installieren von Updates für jede Anwendung kann jedoch zeitaufwändig sein. In diesem Artikel erfahren Sie, wie Sie diesen Prozess mithilfe des Dienstes Ninite.com und der integrierten Windows-Aufgabenplanung automatisieren können.

### Teil 1: Einführung in Ninite und Erstellung eines Installers

Ninite ist ein Dienst, der für die gleichzeitige Installation und Aktualisierung mehrerer beliebter Anwendungen entwickelt wurde. Er soll Ihnen Zeit sparen, indem er die manuelle Installation jeder Anwendung, das Durchblättern von Installationsassistenten und das Ablehnen von Angeboten zur Installation von Symbolleisten oder anderer unerwünschter Software überflüssig macht.

**Hauptmerkmale und Vorteile von Ninite:**

*   **Installation ohne unnötige Aktionen:** Sie müssen nicht auf „Weiter“ klicken oder Symbolleisten und zusätzlichen Müll ablehnen. Wählen Sie einfach die gewünschten Anwendungen aus und führen Sie den Installer aus.
*   **Immer aktuelle Versionen:** Ninite verwendet Bots, um Updates zu verfolgen, sodass Sie immer die neuesten stabilen Versionen von Anwendungen erhalten.
*   **Prozessautomatisierung:** Ninite arbeitet im Hintergrund und installiert Anwendungen an Standardstandorten und in der Sprache Ihres Systems. Es überspringt bereits aktualisierte Anwendungen und ignoriert Neustartanforderungen von Installern.
*   **Sicherheit:** Anwendungen werden direkt von den offiziellen Websites der Herausgeber heruntergeladen, und ihre digitalen Signaturen oder Hashes werden vor dem Start überprüft, um die Authentizität sicherzustellen.
*   **Systemunterstützung:** Ninite funktioniert unter Windows 11, 10, 8.x, 7 und entsprechenden Serverversionen.
*   **Kostenlos für den Heimgebrauch:** Die Website ist für den persönlichen Gebrauch kostenlos (keine Werbung oder unerwünschte Software). Die kostenpflichtige Version von Ninite Pro bietet erweiterte Funktionen für die Softwareverwaltung in Organisationen.

**Anwendungsbereiche (Kategorien), aus denen Sie wählen können:**

Ninite bietet eine breite Palette von Programmen, gruppiert nach Kategorien:

*   **Webbrowser (Web Browsers):** Chrome, Opera, Firefox, Edge, Brave.
*   **Messaging:** Zoom, Discord, Teams, Pidgin, Thunderbird.
*   **Medien (Media):** iTunes, VLC, AIMP, foobar2000, Audacity, K-Lite Codecs, Spotify, HandBrake.
*   **Bildbearbeitung (Imaging):** Krita, Blender, Paint.NET, GIMP, IrfanView, Inkscape, Greenshot, ShareX.
*   **Dokumente (Documents):** Foxit Reader, LibreOffice, SumatraPDF, OpenOffice.
*   **Sicherheit (Security):** Malwarebytes, Avast, AVG, Avira.
*   **Online-Speicher (Online Storage):** Dropbox, Google Drive, OneDrive.
*   **Dienstprogramme (Utilities):** TeamViewer, ImgBurn, TeraCopy, Revo, WinDirStat, CCleaner.
*   **Komprimierung (Compression):** 7-Zip, PeaZip, WinRAR.
*   **Entwicklertools (Developer Tools):** Python, Git, FileZilla, Notepad++, WinSCP, PuTTY, Visual Studio Code.
*   **Und vieles mehr:** einschließlich .NET, Java, Dienstprogramme und andere nützliche Tools.

**So wählen und laden Sie die Installationsdatei herunter:**

1.  **Anwendungen auswählen:** Auf der Hauptseite von ninite.com sehen Sie eine Liste von Kategorien mit Anwendungen. Aktivieren Sie die Kontrollkästchen neben den Programmen, die Sie installieren oder auf dem neuesten Stand halten möchten.
2.  **Installer herunterladen:** Nachdem Sie die Anwendungen ausgewählt haben, klicken Sie auf die Schaltfläche **„Get Your Ninite“**. Die Website generiert und bietet Ihnen den Download einer persönlichen ausführbaren Datei an. Diese kleine Datei ist Ihr universeller Installer/Updater.

### Teil 2: Automatische Updates einrichten

Nachdem Sie nun einen konfigurierten Ninite-Installer haben, wollen wir uns ansehen, wo Sie ihn am besten platzieren und wie Sie den automatischen Start einrichten.

**Wo die Ninite-Datei platziert werden soll**

Damit das System Ihre Ninite-Datei problemlos finden und ausführen kann, empfiehlt es sich, einen separaten Ordner dafür zu erstellen. Dies verhindert ein versehentliches Löschen oder Verschieben der Datei.

**Platzierungsempfehlungen:**

*   **Systemordner vermeiden:** Speichern Sie die Datei nicht im Stammverzeichnis des Laufwerks `C:` oder im Ordner `C:\Windows`.
*   **Einen dedizierten Ordner erstellen:** Eine gute Praxis wäre es, einen Ordner zu erstellen, z.B. `C:\NiniteUpdater`. Dies vereinfacht die Dateiverwaltung und die zukünftige Suche.

Verschieben Sie die von der Ninite-Website heruntergeladene Datei (z.B. `Ninite-Software-Paket.exe`) in den zuvor erstellten Ordner `C:\NiniteUpdater`.

**Automatisches Starten über die Windows-Aufgabenplanung einrichten**

Um sicherzustellen, dass Programme jeden Sonntag automatisch überprüft und aktualisiert werden, verwenden wir das integrierte Windows-Tool – die **Aufgabenplanung**.

**1. Aufgabenplanung öffnen:**

*   Drücken Sie die Tasten `Win + R`, geben Sie `taskschd.msc` ein und drücken Sie die Eingabetaste.

**2. Neue Aufgabe erstellen:**

Im Fenster der Aufgabenplanung wählen Sie im rechten Bereich „Aktionen“ die Option **„Einfache Aufgabe erstellen...“**.

*   **Name und Beschreibung:** Geben Sie einen aussagekräftigen Namen für Ihre Aufgabe ein, z.B. „Wöchentliches Ninite-Update“. Klicken Sie auf „Weiter“.
*   **Trigger (Startzeit):** In diesem Schritt müssen Sie angeben, wie oft die Aufgabe ausgeführt werden soll.
    *   Wählen Sie „Wöchentlich“ und klicken Sie auf „Weiter“.
    *   Geben Sie den Wochentag an – „Sonntag“. Sie können auch eine für Sie passende Startzeit wählen, z.B. wenn der Computer normalerweise eingeschaltet, aber nicht aktiv genutzt wird. Klicken Sie auf „Weiter“.
*   **Aktion:** Hier geben wir an, welches Programm ausgeführt werden soll.
    *   Wählen Sie „Programm starten“ und klicken Sie auf „Weiter“.
    *   Klicken Sie im Feld „Programm oder Skript“ auf die Schaltfläche „Durchsuchen...“ und suchen Sie Ihre Ninite-Datei in dem zuvor erstellten Ordner (`C:\NiniteUpdater\Ninite-Software-Paket.exe`).
    *   Klicken Sie auf „Weiter“.
*   **Abschluss:** Im letzten Schritt überprüfen Sie alle angegebenen Parameter. Wenn alles korrekt ist, klicken Sie auf „Fertig stellen“.

Die Aufgabenplanung wird nun Ihre Ninite-Datei jeden Sonntag zur angegebenen Zeit automatisch ausführen. Wenn Ninite im Hintergrund läuft, überprüft es die Versionen der von Ihnen ausgewählten Programme und lädt und installiert Updates, falls welche gefunden werden, ohne Ihr Zutun. So erhalten Sie ein einfaches und zuverlässiges System, um Ihre Software auf dem neuesten Stand zu halten.
