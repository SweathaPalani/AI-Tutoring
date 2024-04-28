
# Named Entity Recognition (NER)

from transformers import pipeline

ner = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')

# text = "Apple Inc. announced its Q1 earnings with a revenue surpassing $100 billion, led by Tim Cook."
# text = "President Joe Biden met with Canadian Prime Minister Justin Trudeau to discuss climate change and trade agreements. The meeting was held on March 15, 2023, in Washington, D.C."
text = "Jessica's birthday party will be at her house in Chicago this Saturday."

entities = ner(text)

print("---------")
for entity in entities:
    print(f"Entity: {entity['word']}, Type: {entity['entity']}, Score: {entity['score']:.2f}")
print("---------")