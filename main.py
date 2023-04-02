import os
import openai

print('---------start connect openai---------')
openai.organization = "org-DaDfB9xHQ5ySB3qRdJC8G0zD"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "北京有多大？"}]
)

print("---------openAi message:----------------")
print(completion.choices[0].message.content)
