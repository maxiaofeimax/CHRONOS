import dashscope
import requests
import json
import os

def query_model(model: str, raw_prompt: str):
    if 'qwen' in model:
        responses = query_qwen(model, raw_prompt)
    elif 'gpt' in model:
        responses = query_gpt(model, raw_prompt)
    elif 'Llama' in model:
        responses = query_llama(model, raw_prompt)
    return responses


def query_llama(model, prompt_str):
    """
    Replace with your LLAMA model's query function.
    """
    pass


def query_qwen(model: str, raw_prompt: str):
    """
    Replace with your Qwen model's query function.
    """
    pass


def query_gpt(model: str, raw_prompt: str):
    """
    Replace with your GPT model's query function.
    """
    pass