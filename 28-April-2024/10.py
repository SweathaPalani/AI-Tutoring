# Text Classification Using BERT

from transformers import pipeline

# Initialize the Text Classification model
classification_model = pipeline('text-classification', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Function to perform Text Classification using BERT
def bert_text_classification(prompt):
    classification = classification_model(prompt)
    return {"label": classification[0]['label'], "score": classification[0]['score']}

prompt = "I love my new laptop, it's fast and the screen is beautiful."
classification = bert_text_classification(prompt)
print("Classification:", classification)
