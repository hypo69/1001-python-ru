## \file /src/ai/gradio/gradio.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.ai.gradio 
    :platform: Windows, Unix
    :synopsis:

"""

#https://www.gradio.app/guides/quickstart
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()   