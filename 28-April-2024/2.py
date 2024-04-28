# text-generation

from transformers import pipeline

# Create a text generation pipeline using GPT-2
generator = pipeline('text-generation', model='gpt2')

# Prompt for the model
prompt = "In a distant future, humanity has colonized Mars and"

generated_text = generator(prompt, max_length=100, num_return_sequences=1)

print("---------")
for text in generated_text:
    print(text['generated_text'])
print("---------")