#Combine different pipelines
import openai
from transformers import pipeline
import os

api_key = os.getenv('OPENAI_API_KEY')

# Setup OpenAI and Hugging Face pipelines
gpt3 = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt="Write a short review about the latest sci-fi movie.", max_tokens=50)
bert_sentiment = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Generate text with GPT-3
generated_text = gpt3['choices'][0]['text'].strip()
print("Generated Text:", generated_text)

# Analyze sentiment with BERT
sentiment_result = bert_sentiment(generated_text)
print("Sentiment Analysis Result:", sentiment_result)
