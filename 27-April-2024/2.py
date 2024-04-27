# Chat Model
# A model that takes a series of messages and returns a message output

import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

api_key = os.environ['OPENAI_API_KEY']

# Initialize the ChatOpenAI model
# Temperature parameter affects the randomness of the 
# model's responses, with higher values leading to more varied outputs.
chat = ChatOpenAI(temperature=1, openai_api_key=api_key)

response = chat.invoke(
    [
        SystemMessage(content="You are an helpful AI bot that gives accurate answer in 10 words"),
        SystemMessage(content="You are an unhelpful AI bot that makes a joke at whatever the user says"),
        HumanMessage(content="I would like to go to New York, how should I do this?")
    ]
)
print(response)