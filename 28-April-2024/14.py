from transformers import pipeline

# Sentiment Analysis
sentiment_analyzer = pipeline("sentiment-analysis")
sentiment_result = sentiment_analyzer("I love using the new Transformers library by Hugging Face!")
print("Sentiment Analysis:", sentiment_result)

# Text Generation
text_generator = pipeline("text-generation", model="gpt2")
generated_text = text_generator("Transformers are", max_length=30, num_return_sequences=1)
print("Generated Text:", generated_text[0]['generated_text'])

# Question Answering
question_answerer = pipeline("question-answering")
context = "Hugging Face is a company based in New York that provides tools for machine learning."
qa_result = question_answerer(question="Where is Hugging Face based?", context=context)
print("Question Answering:", qa_result['answer'])

# Named Entity Recognition
ner_recognizer = pipeline("ner", grouped_entities=True)
ner_result = ner_recognizer("Hugging Face's headquarters is in New York.")
print("Named Entity Recognition:", ner_result)

# Summarization
summarizer = pipeline("summarization")
summary = summarizer("Hugging Face has created a powerful library called Transformers, which simplifies natural language processing tasks.", max_length=45, min_length=10)
print("Summarization:", summary[0]['summary_text'])

# Translation
translator = pipeline("translation_en_to_fr")
translation = translator("Hugging Face is revolutionizing AI.")
print("Translation:", translation[0]['translation_text'])

# Text Classification
classifier = pipeline("zero-shot-classification")
classification = classifier("The company specializes in AI.", candidate_labels=["technology", "finance", "healthcare"])
print("Zero-Shot Classification:", classification['labels'][0])

# Conversational AI
conversational_model = pipeline("conversational")
from transformers import Conversation
conversation = Conversation("How can I use the library?")
response = conversational_model(conversation)
print("Conversational AI:", response)

# Feature Extraction
feature_extractor = pipeline("feature-extraction")
features = feature_extractor("Transformers library provides easy access to pre-trained models.")
print("Feature Extraction:", features[0][0][:5])  # Print first 5 features of the first token

# Zero-Shot Classification
zero_shot_classifier = pipeline("zero-shot-classification")
zero_shot_result = zero_shot_classifier("Hugging Face enables better NLP.", candidate_labels=["education", "technology", "music"])
print("Zero-Shot Classification:", zero_shot_result['labels'][0])

