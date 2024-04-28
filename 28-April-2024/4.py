# question-answering
from transformers import pipeline

# BERT model that has been fine-tuned on the SQuAD dataset
# Create a question answering pipeline
qa = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')

# Define the context and the question
context = """
The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation.
"""

question = "What is the oldest university in the English-speaking world?"

# Use the QA model to find the answer
answer = qa(question=question, context=context)

# Print the answer
print(f"Answer: {answer['answer']}")
print(f"Score: {answer['score']:.2f}")
