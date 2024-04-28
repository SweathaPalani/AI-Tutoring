# sentiment-analysis
# If no model is specified, distilbert-base-uncased-finetuned-sst-2-english is loaded 

from transformers import pipeline

# Create a sentiment analysis pipeline
classifier = pipeline('sentiment-analysis')

# Define the text to analyze
text = "I love using Hugging Face models for my NLP tasks!"

result = classifier(text)

print(result)
