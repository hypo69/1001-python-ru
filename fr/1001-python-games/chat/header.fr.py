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
    Trouve le répertoire racine du projet à partir du répertoire du fichier actuel,
    en cherchant vers le haut et en s'arrêtant au premier répertoire contenant l'un des fichiers marqueurs.

    Arguments:
        marker_files (tuple): Noms de fichiers ou de répertoires pour identifier la racine du projet.
    
    Renvoie:
        Path: Chemin vers le répertoire racine si trouvé, sinon le répertoire où se trouve le script.
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


# Obtenir le répertoire racine du projet
__root__: Path = set_project_root()
"""__root__ (Path): Chemin vers le répertoire racine du projet"""

