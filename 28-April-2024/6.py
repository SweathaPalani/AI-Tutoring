# We'll use BERT for NER and GPT-2 for generating responses:
# Model Integration

from transformers import pipeline

ner = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')
generator = pipeline('text-generation', model='gpt2')

def generate_response(user_input):
    # Extract entities
    entities = ner(user_input)
    names = [entity['word'] for entity in entities if entity['entity'] == 'I-PER']
    names = list(set(names))  # Remove duplicates

    # Create a context-based prompt for the text generation
    if names:
        name_list = ', '.join(names[:-1]) + ' and ' + names[-1] if len(names) > 1 else names[0]
        prompt = f"I just met {name_list}. What should I say?"
    else:
        prompt = "I didn't catch any names. Let's talk about something else!"

    # Generate a response
    print("prompt: ", prompt)
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

# Example user input
user_input = "I met Angela and Tom at the conference in New York last week."

# Generate and print the response
response=generate_response(user_input)
print("==========")
print (response)
