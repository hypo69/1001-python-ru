
# 🔹 Как перенаправить 404 ошибки на главную страницу в WordPress

В WordPress ошибки 404 — это страницы, которых не существует на сайте. Если их не обрабатывать, это может негативно влиять на SEO и пользовательский опыт.

Существует несколько способов, как перенаправлять такие страницы на главную, на определённую страницу или произвольный URL.

---

## 1️⃣ Способы редиректа 404

### **1. Через `.htaccess`**

Если ваш сервер использует Apache, можно добавить правило в файл `.htaccess`:

```apache
# Redirect all 404s to homepage
ErrorDocument 404 /index.php
```

Или через модуль `mod_rewrite`:

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule .* / [L,R=301]
```

**Минусы:**

* Нет логирования конкретных URL
* Нет уведомлений, если много битых ссылок

---

### **2. Через functions.php темы**

Можно добавить обработку в файл `functions.php` вашей темы:

```php
add_action('template_redirect', function() {
    if (is_404()) {
        wp_redirect(home_url(), 301);
        exit;
    }
});
```

**Минусы:**

* Трудно менять настройки без редактирования кода
* Нет логирования и уведомлений

---

### **3. Через плагин**

Плагин даёт больше гибкости:

* Редирект на главную, страницу по ID или произвольный URL
* Выбор типа редиректа 301/302
* Логирование последних 404
* Уведомления в Telegram (только уникальные URL)

---

## 2️⃣ Полный плагин “404 Redirect Manager”

Ниже полный код плагина для WordPress с экранированием HTML для вставки на страницу:

```html
<pre><code>&lt;?php
/**
 * Plugin Name: 404 Redirect Manager
 * Plugin URI:  https://github.com/hypo69
 * Description: Redirect all 404 pages to homepage, custom page, or custom URL with 301/302 option. Logs all 404 requests, supports CSV export and Telegram notifications (unique URLs only).
 * Version:     1.5.0
 * Author:      hypo69
 * License:     GPL2
 */

if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

// --- Admin menu ---
add_action( 'admin_menu', function() {
    add_options_page(
        '404 Redirect Manager',
        '404 Redirect',
        'manage_options',
        'redirect-404',
        'redirect_404_settings_page'
    );
});

// --- Register settings ---
add_action( 'admin_init', function() {
    register_setting( 'redirect_404_options', 'redirect_404_target' );
    register_setting( 'redirect_404_options', 'redirect_404_type' );
    register_setting( 'redirect_404_options', 'redirect_404_logs' );
    register_setting( 'redirect_404_options', 'redirect_404_telegram_token' );
    register_setting( 'redirect_404_options', 'redirect_404_telegram_chat_id' );
    register_setting( 'redirect_404_options', 'redirect_404_seen' );
});

// --- Settings page ---
function redirect_404_settings_page() {
    $logs = get_option( 'redirect_404_logs', [] );

    // CSV export
    if ( isset( $_POST['export_logs'] ) &amp;&amp; ! empty( $logs ) ) {
        header( 'Content-Type: text/csv; charset=utf-8' );
        header( 'Content-Disposition: attachment; filename=404-logs-' . date('Y-m-d') . '.csv' );
        $output = fopen( 'php://output', 'w' );
        fputcsv( $output, ['Time', 'Requested URL', 'Redirected To', 'IP'] );
        foreach ( $logs as $log ) fputcsv( $output, $log );
        fclose( $output );
        exit;
    }

    ?&gt;
    &lt;div class=&quot;wrap&quot;&gt;
        &lt;h1&gt;404 Redirect Manager&lt;/h1&gt;
        &lt;form method=&quot;post&quot; action=&quot;options.php&quot;&gt;
            &lt;?php settings_fields( 'redirect_404_options' ); ?&gt;
            &lt;?php do_settings_sections( 'redirect_404_options' ); ?&gt;
            &lt;table class=&quot;form-table&quot;&gt;
                &lt;tr&gt;
                    &lt;th scope=&quot;row&quot;&gt;Redirect target&lt;/th&gt;
                    &lt;td&gt;
                        &lt;select name=&quot;redirect_404_target[mode]&quot;&gt;
                            &lt;option value=&quot;home&quot; &lt;?php selected( get_option('redirect_404_target')['mode'] ?? '', 'home' ); ?&gt;&gt;Homepage&lt;/option&gt;
                            &lt;option value=&quot;page&quot; &lt;?php selected( get_option('redirect_404_target')['mode'] ?? '', 'page' ); ?&gt;&gt;Specific Page&lt;/option&gt;
                            &lt;option value=&quot;url&quot; &lt;?php selected( get_option('redirect_404_target')['mode'] ?? '', 'url' ); ?&gt;&gt;Custom URL&lt;/option&gt;
                        &lt;/select&gt;
                        &lt;br&gt;&lt;br&gt;
                        &lt;label&gt;
                            Page ID / URL:
                            &lt;input type=&quot;text&quot; name=&quot;redirect_404_target[value]&quot; value=&quot;&lt;?php echo esc_attr( get_option('redirect_404_target')['value'] ?? '' ); ?&gt;&quot; style=&quot;width:300px;&quot;&gt;
                        &lt;/label&gt;
                        &lt;p class=&quot;description&quot;&gt;If mode = &quot;page&quot;, enter page ID. If &quot;url&quot;, enter full URL.&lt;/p&gt;
                    &lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;th scope=&quot;row&quot;&gt;Redirect type&lt;/th&gt;
                    &lt;td&gt;
                        &lt;select name=&quot;redirect_404_type&quot;&gt;
                            &lt;option value=&quot;301&quot; &lt;?php selected( get_option('redirect_404_type'), '301' ); ?&gt;&gt;301 Permanent&lt;/option&gt;
                            &lt;option value=&quot;302&quot; &lt;?php selected( get_option('redirect_404_type'), '302' ); ?&gt;&gt;302 Temporary&lt;/option&gt;
                        &lt;/select&gt;
                    &lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;th scope=&quot;row&quot;&gt;Telegram Bot Token&lt;/th&gt;
                    &lt;td&gt;
                        &lt;input type=&quot;text&quot; name=&quot;redirect_404_telegram_token&quot; value=&quot;&lt;?php echo esc_attr( get_option('redirect_404_telegram_token') ); ?&gt;&quot; style=&quot;width:300px;&quot;&gt;
                    &lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;th scope=&quot;row&quot;&gt;Telegram Chat ID&lt;/th&gt;
                    &lt;td&gt;
                        &lt;input type=&quot;text&quot; name=&quot;redirect_404_telegram_chat_id&quot; value=&quot;&lt;?php echo esc_attr( get_option('redirect_404_telegram_chat_id') ); ?&gt;&quot; style=&quot;width:300px;&quot;&gt;
                        &lt;p class=&quot;description&quot;&gt;Where to send notifications (user or group chat ID)&lt;/p&gt;
                    &lt;/td&gt;
                &lt;/tr&gt;
            &lt;/table&gt;
            &lt;?php submit_button(); ?&gt;
        &lt;/form&gt;
        ...
</code></pre>
```

---

## 3️⃣ Установка плагина

1. Создаём папку `404-redirect` и файл `404-redirect.php` с кодом плагина
2. Сжимаем в ZIP (`404-redirect.zip`)
3. В админке WordPress → **Плагины → Добавить новый → Загрузить плагин**
4. Выбираем ZIP → Установить → Активировать
5. Настраиваем редирект, тип, Telegram уведомления

---

## 4️⃣ Проверка работы

* Откройте несуществующую страницу (`example.com/404test`)
* Плагин должен:

  * Редиректить на выбранный URL
  * Логировать событие в админке
  * Отправить уведомление в Telegram (если уникальный URL)


