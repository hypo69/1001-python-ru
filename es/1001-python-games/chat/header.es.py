## \file /src/endpoints/hypo69/header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.hypo69 
	:platform: Windows, Unix
	:synopsis:

"""


import sys

from pathlib import Path
def set_project_root(marker_files=('__root__','.git')) -> Path:
    """
    Encuentra el directorio raíz del proyecto a partir del directorio del archivo actual,
    buscando hacia arriba y deteniéndose en el primer directorio que contenga cualquiera de los archivos marcadores.

    Argumentos:
        marker_files (tuple): Nombres de archivos o directorios para identificar la raíz del proyecto.
    
    Devuelve:
        Path: Ruta al directorio raíz si se encuentra, de lo contrario el directorio donde se encuentra el script.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Obtener el directorio raíz del proyecto
__root__: Path = set_project_root()
"""__root__ (Path): Ruta al directorio raíz del proyecto"""

