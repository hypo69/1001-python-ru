# Pełny przewodnik po pracy z plikami multimedialnymi w GitHub

## Wprowadzenie

GitHub obsługuje różne typy plików multimedialnych w `README.md` i innych dokumentach Markdown. Zrozumienie, jak prawidłowo pracować z mediami, pomoże stworzyć bardziej atrakcyjną i informacyjną dokumentację dla Twoich projektów.

-----

## Obrazy

### Podstawowa składnia

Do wstawiania obrazów używa się standardowej składni Markdown.

```markdown
![Tekst alternatywny](ścieżka/do/obrazu.png)
![Logo projektu](assets/logo.png)
```

### Obrazy z linkami

Aby obraz był klikalny, owiń go w link Markdown.

```markdown
[![Opis](image.png)](https://example.com)
```

### Obrazy z repozytorium

  * **Ścieżka względna:**
    To najbardziej niezawodny sposób, jeśli plik znajduje się w Twoim repozytorium. Link będzie działać nawet po przeniesieniu projektu.
    ```markdown
    ![Schemat](docs/images/architecture.png)
    ```
  * **Bezpośredni link:**
    Aby wstawić obraz za pomocą bezpośredniego linku do pliku w repozytorium, użyj domeny `raw.githubusercontent.com`. Jest to najbardziej zalecana metoda, ponieważ zapewnia bezpośrednie dostarczanie pliku bez interfejsu GitHub.
    ```markdown
    # Przez raw.githubusercontent.com (zalecane)
    ![Schemat](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    Można również użyć parametru `?raw=true` w adresie URL pliku.
    ```markdown
    # Bezpośredni link do pliku w repozytorium
    ![Schemat](https://github.com/username/repo/blob/main/docs/images/architecture.png?raw=true)
    ```

### HTML dla obrazów z dodatkowymi parametrami

Jeśli potrzebujesz dostosować rozmiar, wyśrodkowanie lub dodać podpis do obrazu, użyj tagu HTML `<img>`.

```html
<img src="image.png" alt="Opis" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Logo" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Zrzut ekranu" width="600">
  <figcaption>Rys. 1: Główny interfejs aplikacji</figcaption>
</figure>
```

-----

## Wideo

GitHub nie obsługuje bezpośredniego osadzania wideo w plikach Markdown. Istnieją jednak sprawdzone metody ich wyświetlania.

### Metoda 1: Przesyłanie przez GitHub Issues/Releases (Zalecane)

Ten sposób jest najbardziej niezawodny, zwłaszcza dla dużych plików i plików z nazwami w cyrylicy, ponieważ GitHub automatycznie generuje dla nich poprawne linki.

**Kroki:**

1.  Otwórz nowy Issue w swoim repozytorium.
2.  Przeciągnij plik wideo (.mp4, .mov, .webm, .avi) do pola komentarza.
3.  GitHub załaduje plik i utworzy bezpośredni link, który będzie wyglądał mniej więcej tak: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Skopiuj ten link do użycia w tagu HTML `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Twoja przeglądarka nie obsługuje odtwarzania wideo.
</video>
```

### Metoda 2: Podgląd z linkiem do wideo

Możesz użyć obrazu jako podglądu, który będzie prowadził do pobrania lub obejrzenia wideo.

```markdown
[![Demonstracja działania](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)
*Kliknij obraz, aby obejrzeć wideo*

**[⬇️ Pobierz wideo](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Obejrzyj w przeglądarce](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Metoda 3: Integracja z YouTube

Ta metoda jest idealna, jeśli Twoje wideo jest już hostowane na YouTube.

```markdown
[![Nazwa wideo](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![Moje wideo](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Metoda 4: Wideo przez GitHub Pages

Utwórz stronę HTML z wideo w gałęzi `gh-pages` i odwołaj się do niej z Twojego `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Demonstracja wideo</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Następnie w `README.md`:

```markdown
[📺 Obejrzyj wideo](https://username.github.io/repo-name/video.html)
```

-----

## Pliki audio

GitHub nie obsługuje bezpośredniego osadzania audio, ale możesz udostępnić linki do pobrania lub użyć zewnętrznych usług.

### Link do pobrania

```markdown
🎵 [Pobierz plik audio](assets/audio/soundtrack.mp3)
```

### HTML5 audio (działa ograniczono)

Użycie `<audio>` w Markdown może nie działać we wszystkich przeglądarkach i na wszystkich platformach.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Twoja przeglądarka nie obsługuje odtwarzania audio.
</audio>
```

### Zewnętrzne usługi

Użyj plakietek lub linków do zewnętrznych usług, takich jak SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## Animacja GIF

Pliki GIF działają tak samo jak zwykłe obrazy.

### Tworzenie GIF z wideo

Możesz użyć narzędzi wiersza poleceń, takich jak **FFmpeg**, lub konwerterów online.

#### Za pomocą FFmpeg:

```bash
# Konwersja wideo na GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Konwertery online:

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### Użycie GIF w README

```markdown
![Demonstracja](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Demonstracja działania" width="600">
  <p><em>Demonstracja podstawowej funkcjonalności</em></p>
</div>
```

-----

## Najlepsze praktyki

### Organizacja plików

Twórz oddzielne foldery dla mediów, aby utrzymać porządek w repozytorium.

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

### Optymalizacja rozmiarów

  * **Obrazy:** Używaj formatów z dobrą kompresją (PNG, JPEG, WebP) i narzędzi do optymalizacji (np. TinyPNG).
  * **Wideo:** Zalecany rozmiar — do **100 MB**. Używaj rozdzielczości 720p lub 1080p.
  * **GIF:** Optymalny rozmiar — do **5 MB**.

### Dostępność

  * Zawsze podawaj `alt-tekst` dla obrazów.
  * Zapewnij alternatywy dla plików multimedialnych. Na przykład, link do wideo dla tych, którzy nie mogą obejrzeć GIF-a.

-----

## Zaawansowane techniki

### Adaptacyjne obrazy

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Adaptacyjny obraz">
</picture>
```

### Leniwe ładowanie

```html
<img src="image.png" alt="Opis" loading="lazy" width="600">
```

### Galeria obrazów

```markdown
## Zrzuty ekranu

<div align="center">
  <img src="screenshot1.png" width="250" alt="Strona główna">
  <img src="screenshot2.png" width="250" alt="Ustawienia">
  <img src="screenshot3.png" width="250" alt="Profil">
</div>
```

### Plakietki i ikony

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Interaktywne elementy

Użyj tagu `<details>` do tworzenia zwijanych bloków.

```markdown
<details>
<summary>📸 Zobacz zrzuty ekranu</summary>

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

</details>
```

-----

## Rozwiązywanie problemów

### Wideo nie odtwarza się

**Problem:** Tag wideo HTML nie działa z plikami z repozytorium.

**Rozwiązanie:** Użyj metody przesyłania przez GitHub Issues/Releases.

### Obrazy nie wyświetlają się

**Problem:** Nieprawidłowy typ linku.
**Rozwiązanie:** Upewnij się, że używasz bezpośredniego linku (`raw.githubusercontent.com`), a nie linku do strony pliku (`github.com/blob`).

```markdown
![Wrong](https://github.com/user/repo/blob/main/image.png)

![Correct](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### Pliki multimedialne są zbyt duże

**Rozwiązania:**

  * Zoptymalizuj obrazy i wideo.
  * Użyj **Git LFS** (Large File Storage) dla dużych plików.
  * Hostuj media na CDN lub skorzystaj z metody z Issues.

-----

### Przykłady użycia

### README z pełnym zestawem mediów

```markdown
# Mój Projekt

<div align="center">
  <img src="assets/logo.png" alt="Logo" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Demonstracja

[![Demo wideo](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Zrzuty ekranu

<details>
<summary>Zobacz zrzuty ekranu</summary>

![Strona główna](assets/screenshots/main.png)
![Ustawienia](assets/screenshots/settings.png)

</details>

## 🎯 Możliwości

![Feature Demo](assets/gifs/feature-demo.gif)

- ✅ Funkcja 1
- ✅ Funkcja 2
- ✅ Funkcja 3

## 🏗️ Architektura

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Architektura" width="600">
</div>
```
