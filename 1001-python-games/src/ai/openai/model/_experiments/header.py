## \file /src/ai/openai/model/_experiments/header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.ai.openai.model._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.ai.openai.model._experiments """


""" Модуль управления моделью OpenAI 
"""


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
ffmpeg: Path = Path( __root__ , 'bin' , 'ffmpeg' , 'bin' , 'ffmpeg.exe') 
sys.path.append (__root__)   
sys.path.append (ffmpeg)