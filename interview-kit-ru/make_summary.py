## \file /src/endpoints/hypo69/code_assistant/make_summary.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
module: src.endpoints.hypo69.code_assistant.make_summary
    :platform: Windows, Unix
    :synopsis: Модуль собирает файл `summary.md` для компиляции средствами `mdbook`
    Подробнее: https://chatgpt.com/share/6742f054-aaa0-800d-9f84-0ab035a2a2c2
"""

from pathlib import Path
from typing import Optional
import argparse



def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    Args:
        docs_dir (Path): Путь к исходной директории 'src'.
        lang (str): Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    summary_file = Path.cwd() / '500' / 'SUMMARY.md'
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    _make_summary(docs_dir, summary_file, lang)


def _make_summary(src_dir: Optional[Path] = Path.cwd() , summary_file_path: Optional[Path] = Path.cwd() / 'SUMMARY.MD', lang: str = 'en') -> bool:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.

    Args:
        src_dir (Path): Путь к папке с исходниками .md.
        summary_file (Path): Путь для сохранения файла SUMMARY.md.
        lang (str): Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    """
    try:
        if summary_file_path.exists():
            print(f"Файл {summary_file_path} уже существует. Его содержимое будет перезаписано.")

        with summary_file_path.open('w', encoding='utf-8') as summary:
            summary.write('# Summary\n\n')

            for path in sorted(src_dir.rglob('*.md')):
                if path.name == 'SUMMARY.md':
                    continue

                # Фильтрация файлов по языку
                if lang == 'ru' and not path.name.endswith('.ru.md'):
                    continue  # Пропускаем файлы без суффикса .ru.md

                elif lang == 'en' and path.name.endswith('.ru.md'):
                    continue  # Пропускаем файлы с суффиксом .ru.md

                relative_path = path.relative_to(src_dir.parent)
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        print(f"Ошибка создания файла `summary.md`: {ex}")
        return False


if __name__ == '__main__':
    # Парсинг аргументов командной строки
    # parser = argparse.ArgumentParser(description="Создание файла SUMMARY.md с фильтрацией по языку.")
    # parser.add_argument('-lang', type=str, choices=['ru', 'en'], default='en', help="Язык фильтрации файлов (ru или en). По умолчанию 'en'.")
    # parser.add_argument('src_dir', type=str, help="Путь к исходной директории 'src'.")
    # args = parser.parse_args()

    # Преобразование пути в объект Path
    src_dir = input(f"Старовая директория (по умолчанию {Path.cwd()/ '500'})") or Path.cwd() / '500'
    ...
    # Вызов функции make_summary с переданными аргументами
    make_summary(src_dir,'en')