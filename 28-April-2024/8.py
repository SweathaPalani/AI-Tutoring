# BERT Sentiment Analysis Model:
from transformers import pipeline

# Initialize BERT sentiment analysis model
bert_sentiment = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Function to perform sentiment analysis using BERT
def bert_sentiment_analysis(prompt):
    sentiment = bert_sentiment(prompt)
    return f"Sentiment Analysis: {sentiment}"

# Example usage of the function
prompt = "I love this new phone because it has a great camera."
result = bert_sentiment_analysis(prompt)
print(result)
