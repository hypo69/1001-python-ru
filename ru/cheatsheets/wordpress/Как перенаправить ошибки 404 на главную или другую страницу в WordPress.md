

# 🚀 Как перенаправить ошибки 404 на главную или другую страницу в WordPress

В WordPress есть несколько способов сделать редирект для всех страниц с ошибкой **404 (Страница не найдена)**.

---

## 🔹 Способ 1. Через `.htaccess` (Apache)

Если у вас сервер Apache, можно прописать правило в `.htaccess` (расположен в корне сайта).

👉 Вариант: просто отправить все 404 на `index.php`:

```apache
ErrorDocument 404 /index.php
```

👉 Жёсткий редирект на главную страницу:

```apache
Redirect 301 /404.html /
```

---

## 🔹 Способ 2. Через `functions.php` темы

Можно добавить этот код в `functions.php` вашей темы (или в отдельный `mu-plugin`, чтобы не зависеть от темы):

```php
add_action( 'template_redirect', function() {
    if ( is_404() ) {
        wp_redirect( home_url(), 301 );
        exit;
    }
});
```

Здесь:

* `home_url()` — главная страница.
* `301` — постоянный редирект (лучше для SEO).
* Можно заменить на `302` (временный).

---

## 🔹 Способ 3. Плагины

Есть готовые плагины в каталоге WordPress:

* **Redirection** — гибкий и мощный (управление множеством редиректов).
* **404 to 301** — заточен именно под перенаправление 404-страниц.

---

## 🔹 Способ 4. Собственный плагин (гибкий и лёгкий)

Ниже — пример **собственного плагина** с настройками в админке.
Можно выбрать:

* редирект на главную / страницу по ID / любой URL,
* тип редиректа: **301** или **302**.

---

### 📂 Установка плагина

1. Создайте папку:
   `wp-content/plugins/404-redirect/`
2. Внутри создайте файл:
   `404-redirect.php`

---

### 📄 Код плагина

Плагин “404 Redirect Manager”** для WordPress с:

* Редиректами на главную/страницу/URL
* Тип редиректа 301/302
* Логированием последних 500 404
* Экспортом логов в CSV
* Уведомлениями в Telegram **только для уникальных URL**

---

### 📂 Папка плагина

`wp-content/plugins/404-redirect/`

Файл: `404-redirect.php`

---

### 📄 Полный код

```php
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
```

---

✅ **Функционал плагина:**

1. Редиректы на главную, страницу по ID или произвольный URL
2. Выбор типа редиректа: 301/302

## Пошаговая инструкция, как установить этот плагин в WordPress:


### 1️⃣ Создай папку плагина

* Перейди в папку WordPress:
  `wp-content/plugins/`
* Создай новую папку, например:
  `404-redirect`

---

### 2️⃣ Создай файл плагина

* Внутри папки `404-redirect` создай файл:
  `404-redirect.php`
* Вставь **полный код плагина**, который я прислал выше.
* Сохрани файл.

---

### 3️⃣ Активируй плагин

1. В админке WordPress перейди в **Плагины → Установленные плагины**
2. Найди **404 Redirect Manager**
3. Нажми **Активировать**

---

### 4️⃣ Настрой плагин

* Перейди в **Настройки → 404 Redirect**

* Укажи:

  1. **Redirect target** – главная страница / конкретная страница / произвольный URL
  2. **Redirect type** – 301 или 302
  3. **Telegram Bot Token** и **Chat ID** (если хочешь уведомления в Telegram)

* Сохрани настройки.

---

### 5️⃣ Проверка работы

* Попробуй открыть несуществующую страницу, например:
  `https://yourdomain.com/thispagedoesnotexist`
* Должен произойти редирект на указанный URL
* В админке появится запись в **404 Logs**
* Если Telegram настроен — придёт уведомление (только один раз для каждого уникального URL)

---

💡 **Совет:**
Если используешь кеширующие плагины (WP Rocket, W3 Total Cache и др.), очисти кеш после установки плагина, чтобы редиректы работали сразу.

