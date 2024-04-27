# Text Embedding Model usecase
#pip install scikit-learn

import os
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

api_key = os.environ['OPENAI_API_KEY']
embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)

documents = [
    "Exploring the beaches of Florida",
    "The best sunscreen for summer 2024",
    "Top 10 travel destinations in the US",
    "Guide to marine life while scuba diving",
    "Hi! It's time for the beach"
]

# Embed all documents
doc_embeddings = [embeddings_model.embed_query(doc) for doc in documents]

# Embed the text of current user's reading
current_text = "Hi! It's time for the beach"
current_embedding = embeddings_model.embed_query(current_text)

# Calculate similarity scores
similarities = cosine_similarity([current_embedding], doc_embeddings)

# Recommend content based on similarity
# Ignore the first one as it is the current text
recommended_indices = similarities.argsort()[0][::-1][1:]  

# Top 3 recommendations
recommended_texts = [documents[i] for i in recommended_indices[:3]]  

print("Recommended articles based on your current reading:")
for text in recommended_texts:
    print(text)
