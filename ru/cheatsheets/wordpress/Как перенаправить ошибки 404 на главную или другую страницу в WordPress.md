
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
<?php
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
    if ( isset( $_POST['export_logs'] ) && ! empty( $logs ) ) {
        header( 'Content-Type: text/csv; charset=utf-8' );
        header( 'Content-Disposition: attachment; filename=404-logs-' . date('Y-m-d') . '.csv' );
        $output = fopen( 'php://output', 'w' );
        fputcsv( $output, ['Time', 'Requested URL', 'Redirected To', 'IP'] );
        foreach ( $logs as $log ) fputcsv( $output, $log );
        fclose( $output );
        exit;
    }

    ?>
    <div class="wrap">
        <h1>404 Redirect Manager</h1>
        <form method="post" action="options.php">
            <?php settings_fields( 'redirect_404_options' ); ?>
            <?php do_settings_sections( 'redirect_404_options' ); ?>
            <table class="form-table">
                <tr>
                    <th scope="row">Redirect target</th>
                    <td>
                        <select name="redirect_404_target[mode]">
                            <option value="home" <?php selected( get_option('redirect_404_target')['mode'] ?? '', 'home' ); ?>>Homepage</option>
                            <option value="page" <?php selected( get_option('redirect_404_target')['mode'] ?? '', 'page' ); ?>>Specific Page</option>
                            <option value="url" <?php selected( get_option('redirect_404_target')['mode'] ?? '', 'url' ); ?>>Custom URL</option>
                        </select>
                        <br><br>
                        <label>
                            Page ID / URL:
                            <input type="text" name="redirect_404_target[value]" value="<?php echo esc_attr( get_option('redirect_404_target')['value'] ?? '' ); ?>" style="width:300px;">
                        </label>
                        <p class="description">If mode = "page", enter page ID. If "url", enter full URL.</p>
                    </td>
                </tr>
                <tr>
                    <th scope="row">Redirect type</th>
                    <td>
                        <select name="redirect_404_type">
                            <option value="301" <?php selected( get_option('redirect_404_type'), '301' ); ?>>301 Permanent</option>
                            <option value="302" <?php selected( get_option('redirect_404_type'), '302' ); ?>>302 Temporary</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <th scope="row">Telegram Bot Token</th>
                    <td>
                        <input type="text" name="redirect_404_telegram_token" value="<?php echo esc_attr( get_option('redirect_404_telegram_token') ); ?>" style="width:300px;">
                    </td>
                </tr>
                <tr>
                    <th scope="row">Telegram Chat ID</th>
                    <td>
                        <input type="text" name="redirect_404_telegram_chat_id" value="<?php echo esc_attr( get_option('redirect_404_telegram_chat_id') ); ?>" style="width:300px;">
                        <p class="description">Where to send notifications (user or group chat ID)</p>
                    </td>
                </tr>
            </table>
            <?php submit_button(); ?>
        </form>

        <h2>404 Logs</h2>
        <?php if ( ! empty( $logs ) ): ?>
            <table class="widefat striped" style="max-width:900px;">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Requested URL</th>
                        <th>Redirected To</th>
                        <th>IP</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ( array_reverse( $logs ) as $log ): ?>
                        <tr>
                            <td><?php echo esc_html( $log['time'] ); ?></td>
                            <td><?php echo esc_html( $log['requested'] ); ?></td>
                            <td><?php echo esc_html( $log['redirected'] ); ?></td>
                            <td><?php echo esc_html( $log['ip'] ); ?></td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
            <form method="post" style="margin-top:15px;">
                <?php submit_button( 'Export Logs (CSV)', 'secondary', 'export_logs', false ); ?>
                <?php submit_button( 'Clear Logs', 'delete', 'clear_logs', false ); ?>
            </form>
            <?php
            if ( isset($_POST['clear_logs']) ) {
                update_option( 'redirect_404_logs', [] );
                update_option( 'redirect_404_seen', [] );
                wp_safe_redirect( admin_url('options-general.php?page=redirect-404') );
                exit;
            }
            ?>
        <?php else: ?>
            <p>No 404 logs yet.</p>
        <?php endif; ?>
    </div>
    <?php
}

// --- Telegram function ---
function redirect_404_send_telegram($message) {
    $token = get_option('redirect_404_telegram_token');
    $chat_id = get_option('redirect_404_telegram_chat_id');
    if ( empty($token) || empty($chat_id) ) return;

    $url = "https://api.telegram.org/bot{$token}/sendMessage";
    $data = ['chat_id'=>$chat_id, 'text'=>$message, 'parse_mode'=>'HTML'];
    $options = [
        'http'=>[
            'header'=>"Content-type: application/x-www-form-urlencoded\r\n",
            'method'=>'POST',
            'content'=>http_build_query($data),
            'timeout'=>5,
        ]
    ];
    $context = stream_context_create($options);
    @file_get_contents($url, false, $context);
}

// --- Redirect + Logging + Telegram (unique URLs) ---
add_action( 'template_redirect', function() {
    if ( is_404() ) {
        $target = get_option( 'redirect_404_target', ['mode' => 'home', 'value' => ''] );
        $type   = get_option( 'redirect_404_type', '301' );
        $redirect_url = home_url();

        if ( $target['mode'] === 'page' && ! empty( $target['value'] ) ) {
            $redirect_url = get_permalink( intval( $target['value'] ) );
        }
        if ( $target['mode'] === 'url' && ! empty( $target['value'] ) ) {
            $redirect_url = esc_url( $target['value'] );
        }

        // --- Logging ---
        $logs   = get_option( 'redirect_404_logs', [] );
        $logs[] = [
            'time'      => current_time( 'mysql' ),
            'requested' => esc_url_raw( $_SERVER['REQUEST_URI'] ?? '' ),
            'redirected'=> $redirect_url,
            'ip'        => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
        ];
        if ( count( $logs ) > 500 ) $logs = array_slice($logs, -500);
        update_option( 'redirect_404_logs', $logs );

        // --- Unique Telegram notifications ---
        $seen_urls = get_option('redirect_404_seen', []);
        if ( ! in_array($_SERVER['REQUEST_URI'], $seen_urls) ) {
            $message = "⚠️ <b>404 Detected</b>\nURL: " . esc_html($_SERVER['REQUEST_URI'] ?? '') .
                       "\nRedirected to: " . esc_html($redirect_url) .
                       "\nIP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown');
            redirect_404_send_telegram($message);
            $seen_urls[] = $_SERVER['REQUEST_URI'];
            if ( count($seen_urls) > 1000 ) $seen_urls = array_slice($seen_urls, -1000);
            update_option('redirect_404_seen', $seen_urls);
        }

        // --- Redirect ---
        if ( $redirect_url ) {
            wp_redirect( $redirect_url, intval( $type ) );
            exit;
        }
    }
});

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


