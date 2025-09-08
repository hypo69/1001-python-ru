# Guida completa all'uso dei file multimediali su GitHub

## Introduzione

GitHub supporta vari tipi di file multimediali in `README.md` e altri documenti Markdown. Comprendere come lavorare correttamente con i media aiuterà a creare una documentazione più accattivante e informativa per i vostri progetti.

-----

## Immagini

### Sintassi di base

Per inserire immagini si utilizza la sintassi Markdown standard.

```markdown
![Testo alternativo](percorso/all/immagine.png)
![Logo del progetto](assets/logo.png)
```

### Immagini con link

Per rendere un'immagine cliccabile, racchiudetela in un link Markdown.

```markdown
[![Descrizione](image.png)](https://example.com)
```

### Immagini dal repository

  * **Percorso relativo:**
    Questo è il modo più affidabile se il file si trova nel vostro repository. Il link funzionerà anche se il progetto viene spostato.
    ```markdown
    ![Schema](docs/images/architecture.png)
    ```
  * **Link diretto:**
    Per inserire un'immagine tramite un link diretto a un file nel repository, utilizzate il dominio `raw.githubusercontent.com`. Questo è il metodo più consigliato, poiché fornisce la consegna diretta del file senza l'interfaccia di GitHub.
    ```markdown
    # Tramite raw.githubusercontent.com (consigliato)
    ![Schema](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    È anche possibile utilizzare il parametro `?raw=true` negli URL dei file.
    ```markdown
    # Link diretto al file nel repository
    ![Schema](https://github.com/username/repo/blob/main/docs/images/architecture.png?raw=true)
    ```

### HTML per immagini con parametri aggiuntivi

Se avete bisogno di regolare le dimensioni, il centraggio o aggiungere una didascalia a un'immagine, utilizzate il tag HTML `<img>`.

```html
<img src="image.png" alt="Descrizione" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Logo" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Screenshot" width="600">
  <figcaption>Fig. 1: Interfaccia principale dell'applicazione</figcaption>
</figure>
```

-----

## Video

GitHub non supporta l'incorporamento diretto di video nei file Markdown. Tuttavia, esistono metodi comprovati per visualizzarli.

### Metodo 1: Caricamento tramite GitHub Issues/Releases (Consigliato)

Questo metodo è il più affidabile, specialmente per file di grandi dimensioni e file con nomi in cirillico, poiché GitHub genera automaticamente link corretti per essi.

**Passaggi:**

1.  Aprite una nuova Issue nel vostro repository.
2.  Trascinate il file video (.mp4, .mov, .webm, .avi) nel campo dei commenti.
3.  GitHub caricherà il file e creerà un link diretto, che apparirà all'incirca così: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Copiate questo link per usarlo nel tag HTML `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Il tuo browser non supporta la riproduzione video.
</video>
```

### Metodo 2: Anteprima con link al video

Potete usare un'immagine come anteprima che porterà al download o alla visualizzazione del video.

```markdown
[![Dimostrazione](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)
*Clicca sull'immagine per vedere il video*

**[⬇️ Scarica video](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Guarda nel browser](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Metodo 3: Integrazione YouTube

Questo metodo è ideale se il vostro video è già ospitato su YouTube.

```markdown
[![Titolo del video](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![Il mio video](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Metodo 4: Video tramite GitHub Pages

Create una pagina HTML con il video nel ramo `gh-pages` e fate riferimento ad essa dal vostro `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dimostrazione video</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Quindi in `README.md`:

```markdown
[📺 Guarda il video](https://username.github.io/repo-name/video.html)
```

-----

## File audio

GitHub non supporta l'incorporamento diretto di audio, ma potete fornire link per il download o utilizzare servizi esterni.

### Link per il download

```markdown
🎵 [Scarica il file audio](assets/audio/soundtrack.mp3)
```

### Audio HTML5 (funziona in modo limitato)

L'uso di `<audio>` in Markdown potrebbe non funzionare in tutti i browser e su tutte le piattaforme.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Il tuo browser non supporta la riproduzione audio.
</audio>
```

### Servizi esterni

Utilizzate badge o link a servizi esterni come SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## Animazioni GIF

I file GIF funzionano come le normali immagini.

### Creazione di GIF da video

Potete utilizzare strumenti da riga di comando, come **FFmpeg**, o convertitori online.

#### Con FFmpeg:

```bash
# Conversione video in GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Convertitori online:

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### Utilizzo di GIF in README

```markdown
![Dimostrazione](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Dimostrazione del funzionamento" width="600">
  <p><em>Dimostrazione delle funzionalità principali</em></p>
</div>
```

-----

## Migliori pratiche

### Organizzazione dei file

Create cartelle separate per i media per mantenere l'ordine nel repository.

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

### Ottimizzazione delle dimensioni

  * **Immagini:** Utilizzate formati con buona compressione (PNG, JPEG, WebP) e strumenti di ottimizzazione (ad esempio, TinyPNG).
  * **Video:** Dimensione consigliata — fino a **100 MB**. Utilizzate una risoluzione di 720p o 1080p.
  * **GIF:** Dimensione ottimale — fino a **5 MB**.

### Accessibilità

  * Specificate sempre il `testo alt` per le immagini.
  * Fornite alternative per i file multimediali. Ad esempio, un link a un video per coloro che non possono visualizzare una GIF.

-----

## Tecniche avanzate

### Immagini responsive

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Immagine responsive">
</picture>
```

### Caricamento lazy

```html
<img src="image.png" alt="Descrizione" loading="lazy" width="600">
```

### Galleria di immagini

```markdown
## Screenshot

<div align="center">
  <img src="screenshot1.png" width="250" alt="Pagina principale">
  <img src="screenshot2.png" width="250" alt="Impostazioni">
  <img src="screenshot3.png" width="250" alt="Profilo">
</div>
```

### Badge e icone

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Elementi interattivi

Utilizzate il tag `<details>` per creare blocchi espandibili.

```markdown
<details>
<summary>📸 Guarda gli screenshot</summary>

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

</details>
```

-----

## Risoluzione dei problemi

### Il video non viene riprodotto

**Problema:** Il tag video HTML non funziona con i file del repository.

**Soluzione:** Utilizzate il metodo di caricamento tramite GitHub Issues/Releases.

### Le immagini non vengono visualizzate

**Problema:** Tipo di link errato.
**Soluzione:** Assicuratevi di utilizzare un link diretto (`raw.githubusercontent.com`), non un link alla pagina del file (`github.com/blob`).

```markdown
![Sbagliato](https://github.com/user/repo/blob/main/image.png)

![Corretto](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### File multimediali troppo grandi

**Soluzioni:**

  * Ottimizzate immagini e video.
  * Utilizzate **Git LFS** (Large File Storage) per file di grandi dimensioni.
  * Ospitate i media su CDN o utilizzate il metodo con le Issues.

-----

### Esempi di utilizzo

### README con un set completo di media

```markdown
# Il mio Progetto

<div align="center">
  <img src="assets/logo.png" alt="Logo" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Dimostrazione

[![Video demo](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Screenshot

<details>
<summary>Guarda gli screenshot</summary>

![Pagina principale](assets/screenshots/main.png)
![Impostazioni](assets/screenshots/settings.png)

</details>

## 🎯 Funzionalità

![Demo funzionalità](assets/gifs/feature-demo.gif)

- ✅ Funzionalità 1
- ✅ Funzionalità 2
- ✅ Funzionalità 3

## 🏗️ Architettura

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Architettura" width="600">
</div>
```
