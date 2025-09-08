# Vollständige Anleitung zur Arbeit mit Mediendateien auf GitHub

## Einführung

GitHub unterstützt verschiedene Arten von Mediendateien in `README.md` und anderen Markdown-Dokumenten. Das Verständnis, wie man richtig mit Medien umgeht, hilft Ihnen, eine ansprechendere und informativere Dokumentation für Ihre Projekte zu erstellen.

-----

## Bilder

### Grundlegende Syntax

Zum Einfügen von Bildern wird die Standard-Markdown-Syntax verwendet.

```markdown
![Alternativtext](pfad/zum/bild.png)
![Projektlogo](assets/logo.png)
```

### Bilder mit Links

Um ein Bild anklickbar zu machen, umschließen Sie es mit einem Markdown-Link.

```markdown
[![Beschreibung](image.png)](https://example.com)
```

### Bilder aus dem Repository

  * **Relativer Pfad:**
    Dies ist die zuverlässigste Methode, wenn sich die Datei in Ihrem Repository befindet. Der Link funktioniert auch, wenn das Projekt verschoben wird.
    ```markdown
    ![Schema](docs/images/architecture.png)
    ```
  * **Direkter Link:**
    Um ein Bild über einen direkten Link zu einer Datei im Repository einzufügen, verwenden Sie die Domain `raw.githubusercontent.com`. Dies ist die am meisten empfohlene Methode, da sie eine direkte Bereitstellung der Datei ohne die GitHub-Oberfläche gewährleistet.
    ```markdown
    # Über raw.githubusercontent.com (empfohlen)
    ![Schema](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    Sie können auch den Parameter `?raw=true` in der URL der Datei verwenden.
    ```markdown
    # Direkter Link zur Datei im Repository
    ![Schema](https://github.com/username/repo/blob/main/docs/images/architecture.png?raw=true)
    ```

### HTML für Bilder mit zusätzlichen Parametern

Wenn Sie die Größe anpassen, zentrieren oder eine Bildunterschrift zu einem Bild hinzufügen möchten, verwenden Sie das HTML-Tag `<img>`.

```html
<img src="image.png" alt="Beschreibung" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Logo" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Screenshot" width="600">
  <figcaption>Abb. 1: Hauptoberfläche der Anwendung</figcaption>
</figure>
```

-----

## Videos

GitHub unterstützt das direkte Einbetten von Videos in Markdown-Dateien nicht. Es gibt jedoch bewährte Methoden, um sie anzuzeigen.

### Methode 1: Hochladen über GitHub Issues/Releases (Empfohlen)

Diese Methode ist die zuverlässigste, insbesondere für große Dateien und Dateien mit kyrillischen Namen, da GitHub automatisch korrekte Links dafür generiert.

**Schritte:**

1.  Öffnen Sie ein neues Issue in Ihrem Repository.
2.  Ziehen Sie die Videodatei (.mp4, .mov, .webm, .avi) in das Kommentarfeld.
3.  GitHub lädt die Datei hoch und erstellt einen direkten Link, der etwa so aussieht: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Kopieren Sie diesen Link zur Verwendung im HTML-Tag `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Ihr Browser unterstützt die Videowiedergabe nicht.
</video>
```

### Methode 2: Vorschau mit Videolink

Sie können ein Bild als Vorschau verwenden, das zum Herunterladen oder Ansehen des Videos führt.

```markdown
[![Arbeitsdemonstration](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)

*Klicken Sie auf das Bild, um das Video anzusehen*

**[⬇️ Video herunterladen](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Im Browser ansehen](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Methode 3: YouTube-Integration

Diese Methode ist ideal, wenn Ihr Video bereits auf YouTube gehostet wird.

```markdown
[![Videotitel](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![Mein Video](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Methode 4: Video über GitHub Pages

Erstellen Sie eine HTML-Seite mit dem Video im `gh-pages`-Branch und verlinken Sie darauf von Ihrer `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Videodemonstration</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Dann in `README.md`:

```markdown
[📺 Video ansehen](https://username.github.io/repo-name/video.html)
```

-----

## Audiodateien

GitHub unterstützt das direkte Einbetten von Audio nicht, aber Sie können Links zum Herunterladen bereitstellen oder externe Dienste nutzen.

### Download-Link

```markdown
🎵 [Audiodatei herunterladen](assets/audio/soundtrack.mp3)
```

### HTML5-Audio (eingeschränkt funktionsfähig)

Die Verwendung von `<audio>` in Markdown funktioniert möglicherweise nicht in allen Browsern und auf allen Plattformen.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Ihr Browser unterstützt die Audiowiedergabe nicht.
</audio>
```

### Externe Dienste

Verwenden Sie Badges oder Links zu externen Diensten wie SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## GIF-Animation

GIF-Dateien funktionieren genauso wie normale Bilder.

### GIF aus Video erstellen

Sie können Befehlszeilentools wie **FFmpeg** oder Online-Konverter verwenden.

#### Mit FFmpeg:

```bash
# Video in GIF konvertieren
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Online-Konverter:

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### GIF in README verwenden

```markdown
![Demonstration](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Arbeitsdemonstration" width="600">
  <p><em>Demonstration der Hauptfunktionalität</em></p>
</div>
```

-----

## Best Practices

### Dateiorganisation

Erstellen Sie separate Ordner für Medien, um die Ordnung im Repository zu wahren.

```
project/
├── README.md
├── assets/
│   ├── images/
│   │   ├── logo.png
│   │   └── screenshots/
│   ├── videos/
│   │   └── demo.mp4
│   └── gifs/
│       └── feature1.gif
```

### Größenoptimierung

  * **Bilder:** Verwenden Sie Formate mit guter Komprimierung (PNG, JPEG, WebP) und Optimierungstools (z.B. TinyPNG).
  * **Videos:** Empfohlene Größe – bis zu **100 MB**. Verwenden Sie eine Auflösung von 720p oder 1080p.
  * **GIF:** Optimale Größe – bis zu **5 MB**.

### Barrierefreiheit

  * Geben Sie immer `alt-Text` für Bilder an.
  * Bieten Sie Alternativen für Mediendateien an. Zum Beispiel einen Videolink für diejenigen, die ein GIF nicht ansehen können.

-----

## Fortgeschrittene Techniken

### Responsive Bilder

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Responsives Bild">
</picture>
```

### Lazy Loading

```html
<img src="image.png" alt="Beschreibung" loading="lazy" width="600">
```

### Bildergalerie

```markdown
## Screenshots

<div align="center">
  <img src="screenshot1.png" width="250" alt="Startseite">
  <img src="screenshot2.png" width="250" alt="Einstellungen">
  <img src="screenshot3.png" width="250" alt="Profil">
</div>
```

### Badges und Icons

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Interaktive Elemente

Verwenden Sie das `<details>`-Tag, um einklappbare Blöcke zu erstellen.

```markdown
<details>
<summary>📸 Screenshots ansehen</summary>

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

</details>
```

-----

## Fehlerbehebung

### Video wird nicht abgespielt

**Problem:** Das HTML-Video-Tag funktioniert nicht mit Dateien aus dem Repository.

**Lösung:** Verwenden Sie die Upload-Methode über GitHub Issues/Releases.

### Bilder werden nicht angezeigt

**Problem:** Falscher Linktyp.
**Lösung:** Stellen Sie sicher, dass Sie einen direkten Link (`raw.githubusercontent.com`) verwenden und nicht einen Link zur Dateiseite (`github.com/blob`).

```markdown
![Wrong](https://github.com/user/repo/blob/main/image.png)

![Correct](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### Mediendateien sind zu groß

**Lösungen:**

  * Optimieren Sie Bilder und Videos.
  * Verwenden Sie **Git LFS** (Large File Storage) für große Dateien.
  * Hosten Sie Medien auf einem CDN oder verwenden Sie die Methode mit Issues.

-----

### Anwendungsbeispiele

### README mit vollständigem Mediensatz

```markdown
# Mein Projekt

<div align="center">
  <img src="assets/logo.png" alt="Logo" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Demonstration

[![Demo Video](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Screenshots

<details>
<summary>Screenshots ansehen</summary>

![Startseite](assets/screenshots/main.png)
![Einstellungen](assets/screenshots/settings.png)

</details>

## 🎯 Funktionen

![Feature Demo](assets/gifs/feature-demo.gif)

- ✅ Funktion 1
- ✅ Funktion 2
- ✅ Funktion 3

## 🏗️ Architektur

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Architektur" width="600">
</div>
```
