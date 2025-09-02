# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

""" .. module: header
        sysnposys: установка переменной __root__ (корневой директории проекта)

"""
import sys
from pathlib import Path

def set_project_root(marker_files:tuple=('__root__','pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    и поднимаясь вверх, пока не найдет один из маркерных файлов.

    Аргументы:
        marker_files (tuple): Имена файлов или директорий для идентификации корневой директории.
    
    Возвращает:
        Path: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root(('__root__'))
"""__root__ (Path): Путь к корневой директории проекта"""