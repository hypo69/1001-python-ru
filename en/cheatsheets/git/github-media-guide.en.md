# Complete Guide to Working with Media Files on GitHub

## Introduction

GitHub supports various types of media files in `README.md` and other Markdown documents. Understanding how to properly work with media will help you create more engaging and informative documentation for your projects.

-----

## Images

### Basic Syntax

Standard Markdown syntax is used for embedding images.

```markdown
![Alternative text](path/to/image.png)
![Project Logo](assets/logo.png)
```

### Images with Links

To make an image clickable, wrap it in a Markdown link.

```markdown
[![Description](image.png)](https://example.com)
```

### Images from Repository

  * **Relative path:**
    This is the most reliable method if the file is in your repository. The link will work even if the project is moved.
    ```markdown
    ![Diagram](docs/images/architecture.png)
    ```
  * **Direct link:**
    To embed an image using a direct link to a file in the repository, use the `raw.githubusercontent.com` domain. This is the most recommended method as it provides direct file delivery without the GitHub interface.
    ```markdown
    # Via raw.githubusercontent.com (recommended)
    ![Diagram](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    You can also use the `?raw=true` parameter in the file URL.
    ```markdown
    # Direct link to a file in the repository
    ![Diagram](https://github.com/username/repo/blob/main/docs/images/architecture.png?raw=true)
    ```

### HTML for Images with Additional Parameters

If you need to adjust the size, centering, or add a caption to an image, use the HTML `<img>` tag.

```html
<img src="image.png" alt="Description" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Logo" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Screenshot" width="600">
  <figcaption>Fig. 1: Main application interface</figcaption>
</figure>
```

-----

## Videos

GitHub does not support direct embedding of videos in Markdown files. However, there are proven methods for displaying them.

### Method 1: Upload via GitHub Issues/Releases (Recommended)

This method is the most reliable, especially for large files and files with Cyrillic names, as GitHub automatically generates correct links for them.

**Steps:**

1.  Open a new Issue in your repository.
2.  Drag and drop the video file (.mp4, .mov, .webm, .avi) into the comment field.
3.  GitHub will upload the file and create a direct link, which will look something like this: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Copy this link for use in the HTML `<video>` tag.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Your browser does not support video playback.
</video>
```

### Method 2: Preview with Video Link

You can use an image as a preview that will lead to downloading or viewing the video.

```markdown
[![Demonstration of work](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)

*Click on the image to watch the video*

**[⬇️ Download video](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Watch in browser](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Method 3: YouTube Integration

This method is ideal if your video is already hosted on YouTube.

```markdown
[![Video Title](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![My Video](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Method 4: Video via GitHub Pages

Create an HTML page with the video in the `gh-pages` branch and link to it from your `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Video Demonstration</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Then in `README.md`:

```markdown
[📺 Watch video](https://username.github.io/repo-name/video.html)
```

-----

## Audio Files

GitHub does not support direct audio embedding, but you can provide download links or use external services.

### Download Link

```markdown
🎵 [Download audio file](assets/audio/soundtrack.mp3)
```

### HTML5 audio (limited functionality)

Using `<audio>` in Markdown may not work in all browsers and on all platforms.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Your browser does not support audio playback.
</audio>
```

### External Services

Use badges or links to external services like SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## GIF Animation

GIF files work just like regular images.

### Creating GIF from Video

You can use command-line tools like **FFmpeg** or online converters.

#### Using FFmpeg:

```bash
# Convert video to GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Online Converters:

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### Using GIF in README

```markdown
![Demonstration](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Demonstration of work" width="600">
  <p><em>Demonstration of core functionality</em></p>
</div>
```

-----

## Best Practices

### File Organization

Create separate folders for media to keep your repository organized.

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

### Size Optimization

  * **Images:** Use formats with good compression (PNG, JPEG, WebP) and optimization tools (e.g., TinyPNG).
  * **Videos:** Recommended size is up to **100 MB**. Use 720p or 1080p resolution.
  * **GIF:** Optimal size is up to **5 MB**.

### Accessibility

  * Always provide `alt-text` for images.
  * Provide alternatives for media files. For example, a video link for those who cannot view a GIF.

-----

## Advanced Techniques

### Responsive Images

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Responsive image">
</picture>
```

### Lazy Loading

```html
<img src="image.png" alt="Description" loading="lazy" width="600">
```

### Image Gallery

```markdown
## Screenshots

<div align="center">
  <img src="screenshot1.png" width="250" alt="Home page">
  <img src="screenshot2.png" width="250" alt="Settings">
  <img src="screenshot3.png" width="250" alt="Profile">
</div>
```

### Badges and Icons

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Interactive Elements

Use the `<details>` tag to create collapsible blocks.

```markdown
<details>
<summary>📸 View screenshots</summary>

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

</details>
```

-----

## Troubleshooting

### Video not playing

**Problem:** HTML video tag does not work with files from the repository.

**Solution:** Use the upload method via GitHub Issues/Releases.

### Images not displaying

**Problem:** Incorrect link type.
**Solution:** Make sure you are using a direct link (`raw.githubusercontent.com`), not a link to the file page (`github.com/blob`).

```markdown
![Wrong](https://github.com/user/repo/blob/main/image.png)

![Correct](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### Media files too large

**Solutions:**

  * Optimize images and videos.
  * Use **Git LFS** (Large File Storage) for large files.
  * Host media on a CDN or use the Issues method.

-----

### Usage Examples

### README with full set of media

```markdown
# My Project

<div align="center">
  <img src="assets/logo.png" alt="Logo" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Demo

[![Demo video](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Screenshots

<details>
<summary>View screenshots</summary>

![Home page](assets/screenshots/main.png)
![Settings](assets/screenshots/settings.png)

</details>

## 🎯 Features

![Feature Demo](assets/gifs/feature-demo.gif)

- ✅ Feature 1
- ✅ Feature 2
- ✅ Feature 3

## 🏗️ Architecture

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Architecture" width="600">
</div>
```
