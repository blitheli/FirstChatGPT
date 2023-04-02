import os
import openai

print('----openai------')
openai.organization = "org-DaDfB9xHQ5ySB3qRdJC8G0zD"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "北京有多大？"}]
)

print(completion)
