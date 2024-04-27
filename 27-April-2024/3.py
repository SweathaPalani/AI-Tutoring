# Text Embedding Model

import os
from langchain_openai import OpenAIEmbeddings

api_key = os.environ['OPENAI_API_KEY']
embeddings = OpenAIEmbeddings(openai_api_key=api_key)

text = "Hi! It's time for the beach"

text_embedding = embeddings.embed_query(text)
print (f"Here's a sample: {text_embedding[:5]}...")

# how many dimensions the embedding has.
print (f"Your embedding is length {len(text_embedding)}")