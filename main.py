from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="dummy",  # vLLM側で認証してなければ何でもOK
)

res = client.chat.completions.create(
    model="nvidia/Qwen3.6-27B-NVFP4",
    messages=[
        {"role": "user", "content": "日本語で自己紹介して"}
    ],
    max_tokens=1000,
)

print(res.choices[0].message.content)