
# Мульти-язычные тексты в WordPress: подробное руководство для начинающих

**Author:** hypo69  
**Copyright:** hypo69, 2025  
**License:** MIT (https://opensource.org/licenses/MIT)

---

WordPress сам по себе не умеет хранить один текст на нескольких языках в одном поле. Чтобы создать мультиязычную систему, мы можем использовать разметку типа `[:en]…[:]` и небольшой хелпер, который автоматически будет показывать **только текст на текущем языке**.  

Эта статья подойдёт для новичков, которые хотят:

- Использовать ACF (Advanced Custom Fields) или обычные поля WordPress.  
- Работать с WPML, Polylang или стандартным WordPress.  
- Автоматически выводить нужный язык на фронтенде.  

---

## 1️⃣ Подготовка

### 1.1 Что нам понадобится

1. WordPress последней версии  
2. Плагин **ACF (Advanced Custom Fields)** для удобного создания полей  
3. Плагин **WPML** или **Polylang**, если нужен мультиязычный сайт  
4. Доступ к файлам темы (лучше дочерней)  

---

### 1.2 Принцип работы

Мы будем использовать формат строки:

```

\[:en]Text in English\[:es]Texto en Español\[:fr]Texte en Français\[:]

```

- `[:en]…[:]` – английский  
- `[:es]…[:]` – испанский  
- `[:fr]…[:]` – французский  
- И так далее для других языков  

На фронтенде функция хелпера будет **определять текущий язык** и показывать только нужный текст.

---

## 2️⃣ Создание хелпера

### 2.1 Создаём файл

В папке темы создаём, например:

```

/wp-content/themes/your-child-theme/inc/lang\_string\_helper.php

````

### 2.2 Вставляем код хелпера

```php
<?php
/**
 * Lang String Helper
 *
 * Универсальный хелпер для работы с мульти-язычной разметкой [:en]…[:]
 *
 * Author: hypo69
 * Copyright: hypo69, 2025
 * License: MIT (https://opensource.org/licenses/MIT)
 */

if ( ! function_exists('get_lang_string') ) :
function get_lang_string(string $str, ?string $default = null): string {
    if (defined('ICL_LANGUAGE_CODE') && ICL_LANGUAGE_CODE) {
        $lang = ICL_LANGUAGE_CODE;
    } elseif (function_exists('pll_current_language')) {
        $lang = pll_current_language();
    } else {
        $lang = substr(get_locale(), 0, 2);
    }

    preg_match_all('/\[:([a-z]{2})\](.*?)(?=\[:|$)/s', $str, $matches, PREG_SET_ORDER);

    foreach ($matches as $match) {
        if ($match[1] === $lang) {
            return $match[2];
        }
    }

    if (!empty($matches)) {
        return $matches[0][2];
    }

    return $default ?? $str;
}
endif;

// Дополнительно: ACF, посты, опции, таксономии хелперы
// (код аналогичный ранее предоставленному)
````

### 2.3 Подключаем хелпер в `functions.php`

```php
require_once get_stylesheet_directory() . '/inc/lang_string_helper.php';
```

---

## 3️⃣ Использование

### 3.1 ACF-поля

```php
the_acf_lang('subtitle');
$subtitle = get_acf_lang('subtitle');
echo "<h2>$subtitle</h2>";
```

### 3.2 Заголовки и контент постов

```php
the_post_lang($post); // title
the_post_lang($post, 'post_content'); // content
```

### 3.3 Опции сайта

```php
echo get_option_lang('footer_text');
```

### 3.4 Таксономии

```php
the_term_lang($term, 'name');
the_term_lang($term, 'description');
```

### 3.5 Любая строка

```php
the_lang_string('[:en]Hello[:es]Hola[:fr]Bonjour[:]');
```

---

## 4️⃣ Автоматическая интеграция

Чтобы не менять шаблоны, используем фильтры WordPress:

```php
<?php
/**
 * Multilang Auto Integration
 *
 * Author: hypo69
 * Copyright: hypo69, 2025
 * License: MIT (https://opensource.org/licenses/MIT)
 */

add_filter('the_title', fn($title, $id=null) => get_lang_string($title), 10, 2);
add_filter('the_content', fn($content) => get_lang_string($content));
add_filter('get_the_excerpt', fn($excerpt, $post) => get_lang_string($excerpt), 10, 2);
add_filter('acf/format_value', fn($value, $post_id, $field) => get_lang_string($value), 10, 3);
add_filter('pre_option', fn($value, $option_name) => get_lang_string($value), 10, 2);
add_filter('single_cat_title', fn($title) => get_lang_string($title), 10, 1);
add_filter('single_tag_title', fn($title) => get_lang_string($title), 10, 1);
add_filter('term_name', fn($name) => get_lang_string($name));
add_filter('term_description', fn($desc) => get_lang_string($desc));
add_filter('widget_text', fn($text) => get_lang_string($text));
add_filter('gettext', fn($translated_text, $text, $domain) => get_lang_string($translated_text), 10, 3);
```

---

## 5️⃣ Преимущества

* Полностью автоматическая мультиязычность
* Работает с WPML, Polylang и стандартной локалью WordPress
* Не требует правки шаблонов
* Поддержка ACF, таксономий, виджетов, опций
* Фоллбэк при отсутствии нужного языка

---

## 6️⃣ Рекомендации

1. Используйте **дочернюю тему**
2. Проверяйте корректность разметки `[:en]…[:]`
3. Тестируйте сайт на всех языках

---

Теперь ты можешь просто скопировать этот файл и использовать готовый мультиязычный хелпер вместе с автоматической интеграцией через фильтры.
