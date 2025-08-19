## \file /src/ai/llama/model.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

# https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF?library=llama-cpp-python

"""
.. module:: src.ai.llama 
	:platform: Windows, Unix
	:synopsis:

"""


from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
	filename="Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf",
)


output = llm(
	"Once upon a time,",
	max_tokens=512,
	echo=True
)
print(output)