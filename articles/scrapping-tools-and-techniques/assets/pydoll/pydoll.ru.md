# Pydoll: асинхронная веб-автоматизация на Python

Pydoll — это мощная библиотека Python для автоматизации браузеров на базе Chromium. Она предлагает современный, асинхронный подход к веб-скрапингу и автоматизации, устраняя необходимость в традиционных веб-драйверах.

## Ключевые особенности

*   **Архитектура без WebDriver:** Pydoll напрямую взаимодействует с браузерами, такими как Chrome и Edge, используя протокол DevTools. Это означает, что вам не нужно управлять исполняемыми файлами WebDriver (например, `chromedriver.exe`), что упрощает настройку и позволяет избежать проблем с совместимостью версий.
*   **Асинхронность по своей природе:** Pydoll, созданный на основе библиотеки `asyncio` в Python, может выполнять несколько операций одновременно. Это обеспечивает значительный прирост производительности, особенно при работе с несколькими вкладками или сборе данных с многочисленных страниц одновременно.
*   **Человекоподобные взаимодействия:** Чтобы избежать обнаружения в качестве бота, Pydoll имитирует реалистичное поведение пользователя. Он может имитировать человекоподобные движения мыши, скорость набора текста и вводить случайные задержки.
*   **Встроенный обход Cloudflare:** Pydoll включает функции для автоматической обработки и обхода защиты от ботов Cloudflare, включая Turnstile и reCAPTCHA v3.
*   **Расширенный выбор элементов:** Вы можете находить элементы на странице, используя различные стратегии, в том числе:
    *   Простые атрибуты (ID, имя класса, имя тега)
    *   CSS-селекторы
    *   Запросы XPath
*   **Интеграция с прокси:** Легко настройте Pydoll для использования прокси для ротации IP-адресов, что необходимо для крупномасштабного скрапинга и предотвращения блокировки по IP.
*   **Всесторонний контроль:** Pydoll предоставляет богатый API для детального управления браузером, включая:
    *   Создание скриншотов и экспорт страниц в PDF
    *   Перехват и изменение сетевых запросов
    *   Автоматизация загрузки файлов
    *   Выполнение пользовательского кода JavaScript

## Установка

Чтобы начать использовать Pydoll, установите его через pip:

```bash
pip install pydoll-python
```

## Начало работы: простой пример

Вот базовый скрипт, который открывает Google, ищет «pydoll python» и ждет загрузки результатов:

```python
import asyncio
from pydoll.browser.chrome import Chrome
from pydoll.constants import Key

async def main():
    async with Chrome() as browser:
        # Запустите браузер и получите новую вкладку
        tab = await browser.start()

        # Перейдите в Google
        await tab.go_to('https://www.google.com')

        # Найдите поле поиска по его атрибутам
        search_box = await tab.find(tag_name='textarea', name='q')

        # Введите поисковый запрос и нажмите Enter
        await search_box.insert_text('pydoll python')
        await search_box.press_keyboard_key(Key.ENTER)

        # Дождитесь появления результатов поиска
        await tab.wait_element(id='search')

        print("Результаты поиска загружены!")

# Запустите асинхронную основную функцию
asyncio.run(main())
```

## Взаимодействие с веб-элементами

Объект `tab` — ваш основной инструмент для взаимодействия с веб-страницей. Он работает аналогично `WebDriver` в Selenium, но с асинхронными методами.

### Поиск элементов

*   **`tab.find(...)`:** Находит первый элемент, соответствующий заданным критериям.
*   **`tab.find_elements(...)`:** Находит все элементы, соответствующие критериям.
*   **`tab.query(...)`:** Находит элементы с помощью селекторов CSS или запросов XPath.
*   **`tab.wait_element(...)`:** Ожидает, пока элемент станет доступен на странице, прежде чем вернуть его.

### Действия с элементами

Получив элемент, вы можете с ним взаимодействовать:

*   **`element.click()`:** Нажимает на элемент.
*   **`element.insert_text('...')`:** Вводит текст в поле ввода.
*   **`element.text`:** Получает текстовое содержимое элемента.
*   **`element.press_keyboard_key(...)`:** Имитирует нажатие клавиши на клавиатуре.

## Обработка Cloudflare

Pydoll предоставляет два основных подхода для работы с мерами защиты от ботов Cloudflare:

### 1. Менеджер контекста (синхронная обработка)

Этот подход приостановит выполнение вашего скрипта до тех пор, пока не будет решена задача Cloudflare.

```python
async with tab.expect_and_bypass_cloudflare_captcha():
    await tab.go_to('https://www.example.com')
```

### 2. Фоновая обработка (асинхронная обработка)

Этот метод позволяет вашему скрипту продолжать выполнять другие задачи, пока Pydoll обрабатывает задачу Cloudflare в фоновом режиме.

```python
# Включить автоматическое решение Cloudflare
await tab.enable_auto_solve_cloudflare_captcha()

# Перейдите на страницу
await tab.go_to('https://www.example.com')

# Продолжайте выполнять другие задачи...

# Отключите эту функцию, когда она больше не нужна
await tab.disable_auto_solve_cloudflare_captcha()
```

## Ограничения, которые следует учитывать

*   **Ограничение скорости:** Хотя Pydoll может помочь вам избежать обнаружения, отправка слишком большого количества запросов за короткий период все равно может привести к блокировке вашего IP-адреса. Важно реализовывать задержки и использовать прокси для крупномасштабного скрапинга.
*   **Сложность CAPTCHA:** Автоматический обход Pydoll работает для многих, но не для всех типов CAPTCHA. Более сложные задачи могут потребовать ручного вмешательства или сторонних сервисов для их решения.
*   **Совместимость с браузерами:** Pydoll специально разработан для браузеров на базе Chromium (таких как Chrome и Edge). Он не будет работать с другими браузерами, такими как Firefox или Safari.