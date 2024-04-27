#one-shot prompt
from langchain import PromptTemplate  # Import the necessary module
import os  # Import os module for accessing environment variables
import warnings  # Import warnings module to suppress warnings

# Suppress specific warnings
warnings.filterwarnings("ignore")

# Retrieve API key from environment
api_key = os.getenv('OPENAI_API_KEY')  # It's safer to use getenv to avoid errors if the variable isn't set

# Define a prompt template
demo_template = '''I want you to act as a financial advisor for people.
In an easy way, explain the basics of {financial_concept}.'''

# Create a PromptTemplate instance
prompt = PromptTemplate(
    input_variables=['financial_concept'],
    template=demo_template
)

# Format the prompt with a specific financial concept
formatted_prompt = prompt.format(financial_concept='tax in Canada')
print(formatted_prompt)  # Optional: print the formatted prompt to verify

from langchain.llms import OpenAI  # Import necessary classes
from langchain.chains import LLMChain

# Initialize the LLM using the OpenAI model with a specific temperature setting
llm = OpenAI(api_key=api_key, temperature=0.7)

# Create a chain instance
chain1 = LLMChain(llm=llm, prompt=prompt)

# Run the chain with the input 'GDP'
result = chain1.run('GDP')
print(result)  # Print the result
