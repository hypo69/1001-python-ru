## Как подружить редактор Gutenberg с подсветкой синтаксиса Prism в WordPress

Стандартный блок "Код" в редакторе Gutenberg — это спартанский инструмент. Он отображает код моноширинным шрифтом, но не дает ни подсветки синтаксиса, ни нумерации строк, ни удобной кнопки для копирования. Это делает чтение кода на странице утомительным, а сайт выглядит менее профессионально.

К счастью, эту проблему легко решает Prism.js — легкая, быстрая и расширяемая библиотека для подсветки синтаксиса.

В этом руководстве мы по шагам интегрируем Prism.js в вашу WordPress-тему так, чтобы любой блок кода, который вы добавляете в Gutenberg, автоматически получал красивую подсветку, номера строк и кнопку "Копировать".

### Дочерняя тема (важно)

Все изменения мы будем вносить в **дочернюю тему**. Это критически важный шаг в любой кастомизации WordPress. Почему? Если вы внесете изменения напрямую в файлы родительской темы, все ваши труды будут стерты при ее следующем обновлении. Дочерняя тема наследует все от родителя, но позволяет безопасно добавлять свои стили и функции.

(В этой статье мы не будем углубляться в процесс создания дочерней темы. Мы предполагаем, что у вас уже есть активная дочерняя тема. Если нет, вы можете прочитать об этом в статье: **«Как создать и настроить дочернюю тему в WordPress»**.)

### Шаг 1: Готовим структуру файлов

В папке вашей активной дочерней темы нам понадобятся следующие файлы. Какие-то из них у вас уже есть, какие-то мы создадим.

1.  `prism.js` — Сама библиотека Prism, которую мы скачаем.
2.  `prism.css` — Стандартная тема оформления для Prism.
3.  `prism-init.js` — Наш небольшой скрипт-помощник, который будет все "оживлять".
4.  `functions.php` — Главный файл для добавления функционала в WordPress.
5.  `style.css` — Основной файл стилей вашей дочерней темы, куда мы добавим правки.

### Шаг 2: Скачиваем правильную сборку Prism.js

Это ключевой момент. Prism — модульная библиотека, и нам нужно скачать версию, которая включает все необходимые нам функции.

1.  Перейдите на официальную страницу загрузки: [**Prism.js Download**](https://prismjs.com/download.html).
2.  На странице выберите:
    *   **Compression level:** Minified (для быстрой загрузки на сайте).
    *   В разделе **Languages** отметьте галочками те языки, которые вам нужны. Для примера, обязательно выберите **Python**.
    *   Прокрутите ниже до раздела **Plugins** и отметьте галочками **три** плагина:
        *   **Line Numbers** (для нумерации строк).
        *   **Copy to Clipboard Button** (для кнопки "Копировать").
        *   **Normalize Whitespace** (полезный плагин для корректного отображения отступов).
3.  Нажмите синюю кнопку **DOWNLOAD JS** и **DOWNLOAD CSS**.
4.  Поместите скачанные файлы `prism.js` и `prism.css` в корневую папку вашей дочерней темы.

### Шаг 3: Создаем скрипт-инициализатор

Библиотека Prism не начинает работать сама по себе. Ей нужно сказать, когда и как это сделать. Также, плагин кнопки "Копировать" требует, чтобы мы сами создали эту кнопку. Наш скрипт-помощник сделает и то, и другое.

Создайте в папке темы файл `prism-init.js` и вставьте в него следующий код:

```javascript
/**
 * Файл: prism-init.js
 * Назначение: Инициализация подсветки Prism.js и добавление кнопок "Копировать".
 */
document.addEventListener("DOMContentLoaded", function () {
    // Проверяем, была ли загружена основная библиотека Prism
    if (typeof Prism === 'undefined') {
        console.error("Критическая ошибка: Библиотека Prism.js не загружена.");
        return;
    }

    // Запускаем подсветку для всех блоков кода на странице.
    Prism.highlightAll();

    // Добавляем кнопку "Копировать" к каждому блоку
    const codeBlocks = document.querySelectorAll('pre[class*="language-"]');
    codeBlocks.forEach(preElement => {
        if (preElement.querySelector('.code-copy-btn')) { return; }
        const codeElement = preElement.querySelector('code');
        if (!codeElement) { return; }

        const button = document.createElement('button');
        button.className = 'code-copy-btn';
        button.type = 'button';
        button.innerText = 'Copy';
        button.setAttribute('aria-label', 'Copy code to clipboard');

        button.addEventListener('click', () => {
            navigator.clipboard.writeText(codeElement.innerText).then(() => {
                button.innerText = 'Copied!';
                button.disabled = true;
                setTimeout(() => {
                    button.innerText = 'Copy';
                    button.disabled = false;
                }, 2000);
            }).catch(err => {
                console.error('Ошибка при копировании: ', err);
                button.innerText = 'Error';
            });
        });
        preElement.appendChild(button);
    });
});
```

### Шаг 4: Подключаем все в `functions.php`

Теперь нам нужно сказать WordPress, чтобы он загружал наши новые CSS и JS файлы. А также — добавить "магию", которая будет автоматически подготавливать блоки кода из Gutenberg для обработки Prism.

Откройте ваш файл `functions.php` и **добавьте в него** следующий код (или замените существующие блоки, если они есть):

```php
<?php

// ========================================================================
// 1. Подключение стилей и скриптов для подсветки кода
// ========================================================================

add_action('wp_enqueue_scripts', 'my_theme_enqueue_assets');
function my_theme_enqueue_assets() {

    // Подключаем стили родительской темы (если еще не подключены)
    wp_enqueue_style('parent-style', get_template_directory_uri() . '/style.css');
    
    // Подключаем основные стили дочерней темы
    wp_enqueue_style('child-style', get_stylesheet_directory_uri() . '/style.css', array('parent-style'), wp_get_theme()->get('Version'));
    
    // Подключаем стили Prism
    wp_enqueue_style('prism-css', get_stylesheet_directory_uri() . '/prism.css', array('child-style'));

    // Подключаем скрипты Prism
    wp_enqueue_script('prism-core-js', get_stylesheet_directory_uri() . '/prism.js', array(), null, true);
    wp_enqueue_script('prism-init-js', get_stylesheet_directory_uri() . '/prism-init.js', array('prism-core-js'), null, true);
}

// ========================================================================
// 2. Автоматическая обработка блоков кода из Gutenberg
// ========================================================================

add_filter('the_content', 'prepare_code_blocks_for_prism', 20);
function prepare_code_blocks_for_prism($content) {
    $pattern = '/<pre(.*?)>(.*?)<\/pre>/is';

    $content = preg_replace_callback($pattern, function($matches) {
        $pre_attributes = $matches[1];
        $pre_content = $matches[2];

        // --- Шаг 1: Гарантированно добавляем класс 'line-numbers' в тег &lt;pre> ---
        if (strpos($pre_attributes, 'line-numbers') === false) {
            if (preg_match('/class="([^"]*)"/i', $pre_attributes, $class_matches)) {
                $pre_attributes = str_replace($class_matches[0], sprintf('class="%s line-numbers"', $class_matches[1]), $pre_attributes);
            } else {
                $pre_attributes .= ' class="line-numbers"';
            }
        }
        
        // --- Шаг 2: Гарантированно добавляем 'language-python' (по умолчанию) в тег <code> ---
        $pre_content = preg_replace_callback('/<code(.*?)>/is', function($code_matches) {
            $code_attributes = $code_matches[1];
            if (strpos($code_attributes, 'language-') === false) {
                 if (preg_match('/class="([^"]*)"/i', $code_attributes, $class_matches_code)) {
                    $code_attributes = str_replace($class_matches_code[0], sprintf('class="%s language-python"', $class_matches_code[1]), $code_attributes);
                } else {
                    $code_attributes .= ' class="language-python"';
                }
            }
            return '<code' . $code_attributes . '>';
        }, $pre_content, 1); // `1` - чтобы обработать только первый <code> внутри <pre>
        
        return '<pre' . $pre_attributes . '>' . $pre_content . '</pre>';
    }, $content);

    return $content;
}

```

### Шаг 5: Финальные штрихи в `style.css`

Стандартные стили Prism и вашей темы могут конфликтовать, приводя к появлению нежелательных скроллеров. Давайте это исправим.

Добавьте в **конец** вашего файла `style.css` следующий код:

```css
/* ========================================================================
   Prism.js: Фиксы и улучшения
   ========================================================================= */

/* 1. Убираем все скроллеры и разрешаем перенос строк */
pre[class*="language-"] {
    white-space: pre-wrap !important;   /* Разрешает перенос строк */
    word-break: break-word;           /* Разрывает длинные слова */
    max-height: none !important;      /* Убирает ограничение по высоте от родительской темы */
    overflow: hidden !important;        /* Скрывает любые скроллеры */
}

/* 2. Стили для кнопки "Копировать" */
.code-copy-btn {
    position: absolute;
    right: 12px;
    top: 12px;
    background: #e7e7e7;
    border: none;
    border-radius: 4px;
    padding: 4px 8px;
    font-size: 13px;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.3s ease;
}

pre:hover .code-copy-btn {
    opacity: 1;
}
```

### Заключение

Мы получили полностью автоматический инструмент для подсветки синтаксиса кода. Просто добавляйте код через стандартный интерфейс WordPress.