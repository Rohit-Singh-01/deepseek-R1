import openai
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-r1:faree",
  messages=[
    {
      "role": "user",
      "content": "how a non techinical learn get placed in IT firm ?"
    }
  ]
)
print(completion.choices[0].message.content)