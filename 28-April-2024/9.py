# Named Entity Recognition (NER) Using BERT

from transformers import pipeline

ner_model = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')

# Function to perform NER using BERT
def bert_named_entity_recognition(prompt):
    entities = ner_model(prompt)
    return [{"entity": entity['entity'], "word": entity['word']} for entity in entities]

prompt = "Alice lives in Zurich and works for the United Nations."
entities = bert_named_entity_recognition(prompt)
print("Named Entities:", entities)
