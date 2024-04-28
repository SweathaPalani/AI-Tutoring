#Sentiment Analysis

from transformers import RobertaTokenizer, RobertaForSequenceClassification, pipeline

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')

# Initialize the pipeline
sentiment_analysis = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Analyze sentiment
text = "I hate using Transformers. It's so easy and powerful!"
result = sentiment_analysis(text)
print(result)
