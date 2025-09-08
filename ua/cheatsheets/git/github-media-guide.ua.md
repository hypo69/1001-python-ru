# Повний посібник з роботи з медіафайлами в GitHub

## Вступ

GitHub підтримує різні типи медіафайлів у `README.md` та інших Markdown-документах. Розуміння того, як правильно працювати з медіа, допоможе створити більш привабливу та інформативну документацію для ваших проєктів.

-----

## Зображення

### Базовий синтаксис

Для вставки зображень використовується стандартний Markdown-синтаксис.

```markdown
![Альтернативний текст](шлях/до/зображення.png)
![Логотип проєкту](assets/logo.png)
```

### Зображення з посиланнями

Щоб зробити зображення клікабельним, оберніть його в посилання Markdown.

```markdown
[![Опис](image.png)](https://example.com)
```

### Зображення з репозиторію

  * **Відносний шлях:**
    Це найнадійніший спосіб, якщо файл знаходиться у вашому репозиторії. Посилання працюватиме навіть при перенесенні проєкту.
    ```markdown
    ![Схема](docs/images/architecture.png)
    ```
  * **Пряме посилання:**
    Для вставки зображення за прямим посиланням на файл у репозиторії використовуйте домен `raw.githubusercontent.com`. Це найбільш рекомендований метод, оскільки він забезпечує пряму віддачу файлу без інтерфейсу GitHub.
    ```markdown
    # Через raw.githubusercontent.com (рекомендується)
    ![Схема](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    Також можна використовувати параметр `?raw=true` в URL-адреси файлу.
    ```markdown
    # Пряме посилання на файл у репозиторії
    ![Схема](https://github.com/username/repo/blob/main/assets/images/architecture.png?raw=true)
    ```

### HTML для зображень з додатковими параметрами

Якщо вам потрібно налаштувати розмір, центрування або додати підпис до зображення, використовуйте HTML-тег `<img>`.

```html
<img src="image.png" alt="Опис" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="Логотип" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="Знімок екрана" width="600">
  <figcaption>Рис. 1: Головний інтерфейс програми</figcaption>
</figure>
```

-----

## Відео

GitHub не підтримує пряме вбудовування відео в Markdown-файли. Однак існують перевірені методи для їх відображення.

### Метод 1: Завантаження через GitHub Issues/Releases (Рекомендується)

Цей спосіб є найнадійнішим, особливо для великих файлів та файлів з іменами кирилицею, оскільки GitHub автоматично генерує для них коректні посилання.

**Кроки:**

1.  Відкрийте новий Issue у вашому репозиторії.
2.  Перетягніть відеофайл (.mp4, .mov, .webm, .avi) у поле коментаря.
3.  GitHub завантажить файл і створить пряме посилання, яке виглядатиме приблизно так: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  Скопіюйте це посилання для використання в HTML-тезі `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  Ваш браузер не підтримує відтворення відео.
</video>
```

### Метод 2: Попередній перегляд з посиланням на відео

Ви можете використовувати зображення як попередній перегляд, яке вестиме на завантаження або перегляд відео.

```markdown
[![Демонстрація роботи](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)
*Натисніть на зображення для перегляду відео*

**[⬇️ Завантажити відео](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 Дивитися в браузері](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### Метод 3: Інтеграція YouTube

Цей метод ідеальний, якщо ваше відео вже розміщено на YouTube.

```markdown
[![Назва відео](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![Моє відео](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### Метод 4: Відео через GitHub Pages

Створіть HTML-сторінку з відео у гілці `gh-pages` і посилайтеся на неї з вашого `README.md`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Відео демонстрація</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

Потім у `README.md`:

```markdown
[📺 Дивитися відео](https://username.github.io/repo-name/video.html)
```

-----

## Аудіофайли

GitHub не підтримує пряме вбудовування аудіо, але ви можете надати посилання на завантаження або використовувати зовнішні сервіси.

### Посилання для завантаження

```markdown
🎵 [Завантажити аудіофайл](assets/audio/soundtrack.mp3)
```

### HTML5 audio (працює обмежено)

Використання `<audio>` в Markdown може працювати не у всіх браузерах і на всіх платформах.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  Ваш браузер не підтримує відтворення аудіо.
</audio>
```

### Зовнішні сервіси

Використовуйте бейджі або посилання на зовнішні сервіси на кшталт SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## GIF-анімація

GIF-файли працюють так само, як і звичайні зображення.

### Створення GIF з відео

Ви можете використовувати інструменти командного рядка, такі як **FFmpeg**, або онлайн-конвертери.

#### За допомогою FFmpeg:

```bash
# Конвертація відео в GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### Онлайн-конвертери:

  - [EZGIF](https://ezgif.com/)
  - [CloudConvert](https://cloudconvert.com/)
  - [Convertio](https://convertio.co/)

### Використання GIF у README

```markdown
![Демонстрація](demo.gif)

<div align="center">
  <img src="demo.gif" alt="Демонстрація роботи" width="600">
  <p><em>Демонстрація основного функціоналу</em></p>
</div>
```

-----

## Найкращі практики

### Організація файлів

Створюйте окремі папки для медіа, щоб підтримувати порядок у репозиторії.

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

### Оптимізація розмірів

  * **Зображення:** Використовуйте формати з хорошим стисненням (PNG, JPEG, WebP) та інструменти для оптимізації (наприклад, TinyPNG).
  * **Відео:** Рекомендований розмір — до **100 MB**. Використовуйте роздільну здатність 720p або 1080p.
  * **GIF:** Оптимальний розмір — до **5 MB**.

### Доступність

  * Завжди вказуйте `alt-текст` для зображень.
  * Надавайте альтернативи для медіафайлів. Наприклад, посилання на відео для тих, хто не може переглянути GIF.

-----

## Просунуті техніки

### Адаптивні зображення

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="Адаптивне зображення">
</picture>
```

### Лениве завантаження

```html
<img src="image.png" alt="Опис" loading="lazy" width="600">
```

### Галерея зображень

```markdown
## Знімки екрана

<div align="center">
  <img src="screenshot1.png" width="250" alt="Головна сторінка">
  <img src="screenshot2.png" width="250" alt="Налаштування">
  <img src="screenshot3.png" width="250" alt="Профіль">
</div>
```

### Бейджі та іконки

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### Інтерактивні елементи

Використовуйте тег `<details>` для створення згортаних блоків.

```markdown
<details>
<summary>📸 Переглянути знімки екрана</summary>

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

</details>
```

-----

## Вирішення проблем

### Відео не відтворюється

**Проблема:** HTML video тег не працює з файлами з репозиторію.

**Рішення:** Використовуйте метод завантаження через GitHub Issues/Releases.

### Зображення не відображаються

**Проблема:** Неправильний тип посилання.
**Рішення:** Переконайтеся, що ви використовуєте пряме посилання (`raw.githubusercontent.com`), а не посилання на сторінку файлу (`github.com/blob`).

```markdown
![Wrong](https://github.com/user/repo/blob/main/image.png)

![Correct](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### Медіафайли занадто великі

**Рішення:**

  * Оптимізуйте зображення та відео.
  * Використовуйте **Git LFS** (Large File Storage) для великих файлів.
  * Розміщуйте медіа на CDN або скористайтеся методом з Issues.

-----

### Приклади використання

### README з повним набором медіа

```markdown
# Мій Проєкт

<div align="center">
  <img src="assets/logo.png" alt="Логотип" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 Демонстрація

[![Демо відео](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 Знімки екрана

<details>
<summary>Переглянути знімки екрана</summary>

![Головна сторінка](assets/screenshots/main.png)
![Налаштування](assets/screenshots/settings.png)

</details>

## 🎯 Можливості

![Feature Demo](assets/gifs/feature-demo.gif)

- ✅ Функція 1
- ✅ Функція 2
- ✅ Функція 3

## 🏗️ Архітектура

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="Архітектура" width="600">
</div>
```
