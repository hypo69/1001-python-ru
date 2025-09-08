# Guía completa para trabajar con archivos multimedia en GitHub

## Introducción

GitHub admite varios tipos de archivos multimedia en `README.md` y otros documentos Markdown. Comprender cómo trabajar correctamente con los medios le ayudará a crear una documentación más atractiva e informativa para sus proyectos.

-----

## Imágenes

### Sintaxis básica

Para insertar imágenes, se utiliza la sintaxis estándar de Markdown.

```markdown
![Texto alternativo](ruta/a/imagen.png)
![Logotipo del proyecto](assets/logo.png)
```

### Imágenes con enlaces

Para que una imagen sea clicable, envuélvala en un enlace Markdown.

```markdown
[![Descripción](image.png)](https://example.com)
```

### Imágenes desde el repositorio

  * **Ruta relativa:**
    Esta es la forma más fiable si el archivo se encuentra en su repositorio. El enlace funcionará incluso si el proyecto se mueve.
    ```markdown
    ![Esquema](docs/images/architecture.png)
    ```
  * **Enlace directo:**
    Para insertar una imagen mediante un enlace directo al archivo en el repositorio, utilice el dominio `raw.githubusercontent.com`. Este es el método más recomendado, ya que proporciona una entrega directa del archivo sin la interfaz de GitHub.
    ```markdown
    # A través de raw.githubusercontent.com (recomendado)
    ![Esquema](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    También puede utilizar el parámetro `?raw=true` en las URL del archivo.
    ```markdown
    # Enlace directo al archivo en el repositorio
    ![Esquema](https://github.com/username/repo/blob/main/docs/images/architecture.png?raw=true)
    ```

### HTML para imágenes con parámetros adicionales

Si necesita ajustar el tamaño, centrar o añadir una leyenda a una imagen, utilice la etiqueta HTML `<img>`.

```html
<img src="image.png" alt="Descripción" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Logotipo" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Captura de pantalla" width="600">
  <figcaption>Fig. 1: Interfaz principal de la aplicación</figcaption>
</figure>
```

-----

## Vídeos

GitHub no admite la incrustación directa de vídeos en archivos Markdown. Sin embargo, existen métodos probados para mostrarlos.

### Método 1: Carga a través de GitHub Issues/Releases (Recomendado)

Este método es el más fiable, especialmente para archivos grandes y archivos con nombres cirílicos, ya que GitHub genera automáticamente enlaces correctos para ellos.

**Pasos:**

1.  Abra un nuevo Issue en su repositorio.
2.  Arrastre el archivo de vídeo (.mp4, .mov, .webm, .avi) al campo de comentario.
3.  GitHub cargará el archivo y creará un enlace directo, que se verá aproximadamente así: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Copie este enlace para usarlo en la etiqueta HTML `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Su navegador no soporta la reproducción de vídeo.
</video>
```

### Método 2: Vista previa con enlace al vídeo

Puede utilizar una imagen como vista previa que conducirá a la descarga o visualización del vídeo.

```markdown
[![Demostración de funcionamiento](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)
*Haga clic en la imagen para ver el vídeo*

**[⬇️ Descargar vídeo](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Ver en el navegador](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Método 3: Integración con YouTube

Este método es ideal si su vídeo ya está alojado en YouTube.

```markdown
[![Título del vídeo](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![Mi vídeo](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Método 4: Vídeo a través de GitHub Pages

Cree una página HTML con el vídeo en la rama `gh-pages` y enlácela desde su `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Demostración de vídeo</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Luego en `README.md`:

```markdown
[📺 Ver vídeo](https://username.github.io/repo-name/video.html)
```

-----

## Archivos de audio

GitHub no admite la incrustación directa de audio, pero puede proporcionar enlaces de descarga o utilizar servicios externos.

### Enlace de descarga

```markdown
🎵 [Descargar archivo de audio](assets/audio/soundtrack.mp3)
```

### Audio HTML5 (funciona de forma limitada)

El uso de `<audio>` en Markdown puede no funcionar en todos los navegadores y plataformas.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Su navegador no soporta la reproducción de audio.
</audio>
```

### Servicios externos

Utilice insignias o enlaces a servicios externos como SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## Animación GIF

Los archivos GIF funcionan igual que las imágenes normales.

### Creación de GIF a partir de vídeo

Puede utilizar herramientas de línea de comandos como **FFmpeg** o convertidores en línea.

#### Con FFmpeg:

```bash
# Conversión de vídeo a GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Convertidores en línea:

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### Uso de GIF en README

```markdown
![Demostración](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Demostración de funcionamiento" width="600">
  <p><em>Demostración de la funcionalidad principal</em></p>
</div>
```

-----

## Mejores prácticas

### Organización de archivos

Cree carpetas separadas para los medios para mantener el orden en el repositorio.

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

### Optimización de tamaños

  * **Imágenes:** Utilice formatos con buena compresión (PNG, JPEG, WebP) y herramientas de optimización (por ejemplo, TinyPNG).
  * **Vídeos:** El tamaño recomendado es de hasta **100 MB**. Utilice una resolución de 720p o 1080p.
  * **GIF:** El tamaño óptimo es de hasta **5 MB**.

### Accesibilidad

  * Siempre especifique `alt-text` para las imágenes.
  * Proporcione alternativas para los archivos multimedia. Por ejemplo, un enlace a un vídeo para aquellos que no pueden ver un GIF.

-----

## Técnicas avanzadas

### Imágenes adaptables

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Imagen adaptable">
</picture>
```

### Carga diferida (Lazy loading)

```html
<img src="image.png" alt="Descripción" loading="lazy" width="600">
```

### Galería de imágenes

```markdown
## Capturas de pantalla

<div align="center">
  <img src="screenshot1.png" width="250" alt="Página principal">
  <img src="screenshot2.png" width="250" alt="Configuración">
  <img src="screenshot3.png" width="250" alt="Perfil">
</div>
```

### Insignias e iconos

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Elementos interactivos

Utilice la etiqueta `<details>` para crear bloques expandibles.

```markdown
<details>
<summary>📸 Ver capturas de pantalla</summary>

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

</details>
```

-----

## Solución de problemas

### El vídeo no se reproduce

**Problema:** La etiqueta de vídeo HTML no funciona con archivos del repositorio.

**Solución:** Utilice el método de carga a través de GitHub Issues/Releases.

### Las imágenes no se muestran

**Problema:** Tipo de enlace incorrecto.
**Solución:** Asegúrese de que está utilizando un enlace directo (`raw.githubusercontent.com`), y no un enlace a la página del archivo (`github.com/blob`).

```markdown
![Wrong](https://github.com/user/repo/blob/main/image.png)

![Correct](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### Archivos multimedia demasiado grandes

**Soluciones:**

  * Optimice imágenes y vídeos.
  * Utilice **Git LFS** (Large File Storage) para archivos grandes.
  * Aloje los medios en un CDN o utilice el método con Issues.

-----

### Ejemplos de uso

### README con un conjunto completo de medios

```markdown
# Mi Proyecto

<div align="center">
  <img src="assets/logo.png" alt="Logotipo" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Demostración

[![Demo vídeo](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Capturas de pantalla

<details>
<summary>Ver capturas de pantalla</summary>

![Página principal](assets/screenshots/main.png)
![Configuración](assets/screenshots/settings.png)

</details>

## 🎯 Características

![Feature Demo](assets/gifs/feature-demo.gif)

- ✅ Característica 1
- ✅ Característica 2
- ✅ Característica 3

## 🏗️ Arquitectura

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Arquitectura" width="600">
</div>
```
