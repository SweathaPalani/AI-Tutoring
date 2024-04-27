#zero shot prompt
import os
from langchain_openai import ChatOpenAI

# print(os.environ['OPENAI_API_KEY'])
api_key = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(openai_api_key=api_key,temperature=0.6)

response = llm.invoke("Nolan Ryan")

print(response)