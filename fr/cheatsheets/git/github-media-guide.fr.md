# Guide complet pour travailler avec les fichiers multimédias sur GitHub

## Introduction

GitHub prend en charge différents types de fichiers multimédias dans `README.md` et d'autres documents Markdown. Comprendre comment travailler correctement avec les médias vous aidera à créer une documentation plus attrayante et informative pour vos projets.

-----

## Images

### Syntaxe de base

Pour insérer des images, utilisez la syntaxe Markdown standard.

```markdown
![Texte alternatif](chemin/vers/image.png)
![Logo du projet](assets/logo.png)
```

### Images avec liens

Pour rendre une image cliquable, enveloppez-la dans un lien Markdown.

```markdown
[![Description](image.png)](https://example.com)
```

### Images depuis le dépôt

  * **Chemin relatif :**
    C'est la méthode la plus fiable si le fichier se trouve dans votre dépôt. Le lien fonctionnera même si le projet est déplacé.
    ```markdown
    ![Schéma](docs/images/architecture.png)
    ```
  * **Lien direct :**
    Pour insérer une image via un lien direct vers le fichier dans le dépôt, utilisez le domaine `raw.githubusercontent.com`. C'est la méthode la plus recommandée, car elle assure une livraison directe du fichier sans l'interface GitHub.
    ```markdown
    # Via raw.githubusercontent.com (recommandé)
    ![Schéma](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    Vous pouvez également utiliser le paramètre `?raw=true` dans l'URL du fichier.
    ```markdown
    # Lien direct vers le fichier dans le dépôt
    ![Schéma](https://github.com/username/repo/blob/main/docs/images/architecture.png?raw=true)
    ```

### HTML pour les images avec paramètres supplémentaires

Si vous avez besoin de configurer la taille, le centrage ou d'ajouter une légende à une image, utilisez la balise HTML `<img>`.

```html
<img src="image.png" alt="Description" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Logo" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Capture d'écran" width="600">
  <figcaption>Fig. 1 : Interface principale de l'application</figcaption>
</figure>
```

-----

## Vidéos

GitHub ne prend pas en charge l'intégration directe de vidéos dans les fichiers Markdown. Cependant, il existe des méthodes éprouvées pour les afficher.

### Méthode 1 : Téléchargement via GitHub Issues/Releases (Recommandé)

Cette méthode est la plus fiable, surtout pour les fichiers volumineux et les fichiers avec des noms en cyrillique, car GitHub génère automatiquement des liens corrects pour eux.

**Étapes :**

1.  Ouvrez une nouvelle Issue dans votre dépôt.
2.  Faites glisser le fichier vidéo (.mp4, .mov, .webm, .avi) dans le champ de commentaire.
3.  GitHub téléchargera le fichier et créera un lien direct, qui ressemblera à ceci : `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Copiez ce lien pour l'utiliser dans la balise HTML `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la lecture de vidéos.
</video>
```

### Méthode 2 : Aperçu avec un lien vers la vidéo

Vous pouvez utiliser une image comme aperçu qui mènera au téléchargement ou à la visualisation de la vidéo.

```markdown
[![Démonstration de fonctionnement](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)
*Cliquez sur l'image pour regarder la vidéo*

**[⬇️ Télécharger la vidéo](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Regarder dans le navigateur](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Méthode 3 : Intégration YouTube

Cette méthode est idéale si votre vidéo est déjà hébergée sur YouTube.

```markdown
[![Titre de la vidéo](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![Ma vidéo](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Méthode 4 : Vidéo via GitHub Pages

Créez une page HTML avec la vidéo dans la branche `gh-pages` et référencez-la depuis votre `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Démonstration vidéo</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Ensuite, dans `README.md` :

```markdown
[📺 Regarder la vidéo](https://username.github.io/repo-name/video.html)
```

-----

## Fichiers audio

GitHub ne prend pas en charge l'intégration directe d'audio, mais vous pouvez fournir des liens de téléchargement ou utiliser des services externes.

### Lien de téléchargement

```markdown
🎵 [Télécharger le fichier audio](assets/audio/soundtrack.mp3)
```

### Audio HTML5 (fonctionne de manière limitée)

L'utilisation de `<audio>` dans Markdown peut ne pas fonctionner dans tous les navigateurs et sur toutes les plateformes.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Votre navigateur ne prend pas en charge la lecture audio.
</audio>
```

### Services externes

Utilisez des badges ou des liens vers des services externes comme SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## Animation GIF

Les fichiers GIF fonctionnent de la même manière que les images normales.

### Création de GIF à partir de vidéos

Vous pouvez utiliser des outils en ligne de commande, tels que **FFmpeg**, ou des convertisseurs en ligne.

#### Avec FFmpeg :

```bash
# Conversion vidéo en GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Convertisseurs en ligne :

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### Utilisation de GIF dans README

```markdown
![Démonstration](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Démonstration de fonctionnement" width="600">
  <p><em>Démonstration des fonctionnalités principales</em></p>
</div>
```

-----

## Bonnes pratiques

### Organisation des fichiers

Créez des dossiers séparés pour les médias afin de maintenir l'ordre dans le dépôt.

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

### Optimisation des tailles

  * **Images :** Utilisez des formats avec une bonne compression (PNG, JPEG, WebP) et des outils d'optimisation (par exemple, TinyPNG).
  * **Vidéos :** La taille recommandée est jusqu'à **100 Mo**. Utilisez une résolution de 720p ou 1080p.
  * **GIF :** La taille optimale est jusqu'à **5 Mo**.

### Accessibilité

  * Spécifiez toujours un `alt-text` для изображений.
  * Fournissez des alternatives pour les fichiers multimédias. Par exemple, un lien vers la vidéo pour ceux qui ne peuvent pas visualiser le GIF.

-----

## Techniques avancées

### Images adaptatives

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Image adaptative">
</picture>
```

### Chargement paresseux (Lazy loading)

```html
<img src="image.png" alt="Description" loading="lazy" width="600">
```

### Galerie d'images

```markdown
## Captures d'écran

<div align="center">
  <img src="screenshot1.png" width="250" alt="Page d'accueil">
  <img src="screenshot2.png" width="250" alt="Paramètres">
  <img src="screenshot3.png" width="250" alt="Profil">
</div>
```

### Badges et icônes

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Éléments interactifs

Utilisez la balise `<details>` pour créer des blocs dépliables.

```markdown
<details>
<summary>📸 Voir les captures d'écran</summary>

![Capture d'écran 1](screenshot1.png)
![Capture d'écran 2](screenshot2.png)

</details>
```

-----

## Résolution de problèmes

### La vidéo ne se lit pas

**Problème :** La balise vidéo HTML ne fonctionne pas avec les fichiers du dépôt.

**Solution :** Utilisez la méthode de téléchargement via GitHub Issues/Releases.

### Les images ne s'affichent pas

**Problème :** Type de lien incorrect.
**Solution :** Assurez-vous d'utiliser un lien direct (`raw.githubusercontent.com`), et non un lien vers la page du fichier (`github.com/blob`).

```markdown
![Faux](https://github.com/user/repo/blob/main/image.png)

![Correct](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### Fichiers multimédias trop volumineux

**Solutions :**

  * Optimisez les images et les vidéos.
  * Utilisez **Git LFS** (Large File Storage) pour les fichiers volumineux.
  * Hébergez les médias sur un CDN ou utilisez la méthode avec les Issues.

-----

### Exemples d'utilisation

### README avec un ensemble complet de médias

```markdown
# Mon Projet

<div align="center">
  <img src="assets/logo.png" alt="Logo" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Démonstration

[![Démo vidéo](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Captures d'écran

<details>
<summary>Voir les captures d'écran</summary>

![Page d'accueil](assets/screenshots/main.png)
![Paramètres](assets/screenshots/settings.png)

</details>

## 🎯 Fonctionnalités

![Démo de fonctionnalité](assets/gifs/feature-demo.gif)

- ✅ Fonctionnalité 1
- ✅ Fonctionnalité 2
- ✅ Fonctionnalité 3

## 🏗️ Architecture

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Architecture" width="600">
</div>
```
