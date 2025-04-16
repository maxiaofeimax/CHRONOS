import dashscope
from http import HTTPStatus
from openai import OpenAI
import json

DASHSCOPE_API_KEY = "API_KEY"
OPENROUTER_API_KEY = "API_KEY"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def query_model(model: str, raw_prompt: str):
    if 'qwen' in model:
        responses = query_qwen(model, raw_prompt)
    elif 'gpt' in model or 'claude' in model:  # 支持更多模型
        responses = query_openrouter(model, raw_prompt)
    return responses


def query_qwen(model: str, raw_prompt: str):
    response = dashscope.Generation.call(
        api_key=DASHSCOPE_API_KEY,
        model=model,
        prompt=raw_prompt,
        result_format='message',
        use_raw_prompt=True
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.choices[0].message.content
    else:
        err = 'Error code: %s, error message: %s' % (
            response.code,
            response.message,
        )
        return err


def query_openrouter(model: str, raw_prompt: str):
    response = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": raw_prompt
        }],
        extra_headers={
            "HTTP-Referer": "YOUR_SITE_URL",  # Optional. Site URL for rankings
            "X-Title": "YOUR_SITE_NAME",      # Optional. Site title for rankings
        }
    )
    return response.choices[0].message.content
