import os
from pathlib import Path
import re


def convert_md_to_html_content(md_content: str) -> str:
    """
    Конвертирует Markdown-контент в HTML с поддержкой RTL и правильным экранированием.
    Блоки кода остаются без изменений.
    """
    lines = md_content.splitlines()
    html_lines = []
    in_code_block = False
    code_fence = ""
    code_language = "python"

    for line in lines:
        if line.startswith("```"):
            if not in_code_block:
                # Начало блока кода
                match = re.match(r"```(\w+)", line)
                code_language = match.group(1).lower() if match else "python"
                code_fence = line[:3]
                html_lines.append(f'<pre class="line-numbers"><code class="language-{code_language}">')
                in_code_block = True
            else:
                # Конец блока кода
                html_lines.append('</code></pre>')
                in_code_block = False
                code_fence = ""
            continue

        if in_code_block:
            # Сохраняем код "как есть"
            html_lines.append(line)
            continue

        # Обработка Markdown вне кода
        stripped = line.strip()

        if stripped == "":
            continue

        # Заголовки: ## ...
        if re.match(r"^#{2,6}\s", line):
            level = len(re.match(r"^#+", line).group())
            content = line.strip("# ").strip()
            # Обрабатываем смешанный текст
            processed = process_mixed_text(content)
            html_lines.append(f"<h{level} dir=\"rtl\">{processed}</h{level}>")
            continue

        # Списки
        if re.match(r"^(\*|\d+\.)\s", line):
            content = re.sub(r"^(\*|\d+\.)\s+", "", line, count=1).strip()
            processed = process_mixed_text(content)
            html_lines.append(f"<li dir=\"rtl\">{processed}</li>")
            continue

        # Обычные параграфы
        processed = process_mixed_text(line.strip())
        html_lines.append(f"<p dir=\"rtl\">{processed}</p>")

    return "\n".join(html_lines)


def process_mixed_text(text: str) -> str:
    """
    Обрабатывает текст, смешанный из иврита и латиницы.
    Все латинские фрагменты (содержащие __, (), и т.д.) оборачиваются в <span dir="ltr">.
    """
    # Шаблоны для выделения латинских/технических фрагментов
    patterns = [
        r'`[^`]+`',  # инлайн-код
        r'\b\w*__\w*\b',  # __init__, __eq__ и т.д.
        r'dir\(\)',  # dir()
        r'dict\(\)',  # dict()
        r'\b[A-Z][a-zA-Z0-9_]*\([^)]*\)',  # вызовы функций: Point(1,2)
        r'\b[a-zA-Z][\w.()]*\b',  # переменные, методы
    ]

    def wrap_match(match):
        matched = match.group(0)
        if any(c.isascii() and c.isalpha() for c in matched):
            return f'<span dir="ltr">{matched}</span>'
        return matched

    result = text

    # Заменяем инлайн-код отдельно, чтобы не дробить
    def replace_inline_code(match):
        code = match.group(0)
        clean = code.strip("`")
        wrapped = f'<span dir="ltr"><code>{clean}</code></span>'
        return wrapped

    # Сначала обрабатываем инлайн-код
    result = re.sub(r'`[^`]+`', replace_inline_code, result)

    # Затем остальные латинские фрагменты
    for pattern in patterns:
        # Пропускаем уже обработанные
        result = re.sub(pattern, wrap_match, result)

    return result


def convert_directory(root_path: str | Path):
    """
    Рекурсивно обходит директорию и конвертирует .md → .html, если .html не существует.
    """
    root = Path(root_path)
    md_files = root.rglob("*.md")

    for md_file in md_files:
        html_file = md_file.with_suffix(".html")

        if html_file.exists():
            print(f"Пропускаю (уже существует): {html_file}")
            continue

        try:
            md_content = md_file.read_text(encoding="utf-8")
            html_content = convert_md_to_html_content(md_content)
            html_file.write_text(html_content, encoding="utf-8")
            print(f"Создан: {html_file}")
        except Exception as e:
            print(f"Ошибка при обработке {md_file}: {e}")


# =============== ЗАПУСК ===============
if __name__ == "__main__":
    # Укажите путь к вашей директории с .md файлами
    DIRECTORY_PATH = fr"C:\Users\user\Documents\repos\public_repositories\1001-python-he\1001-python-games\cheat_sheets"  # ← измените на нужный путь

    print(f"Начинаю обработку директории: {DIRECTORY_PATH}")
    convert_directory(DIRECTORY_PATH)
    print("✅ Готово.")