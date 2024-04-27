# A model that does text in -> text out!
# pip install -U langchain-openai
# model list : https://platform.openai.com/docs/models/overview

import os
from langchain_openai import ChatOpenAI

# print(os.environ['OPENAI_API_KEY'])
api_key = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(openai_api_key=api_key)
# llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=api_key)

response = llm.invoke("Hi, what model are you using to generate the text?")

print(response)