#few-shot prompt
from langchain import PromptTemplate
from langchain.llms import OpenAI  
from langchain.chains import LLMChain
from langchain import PromptTemplate, FewShotPromptTemplate
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI(api_key=api_key, temperature=0.7)

# First, create the list of few shot examples.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
]

# Next, we specify the template to format the examples we have provided.
# We use the `PromptTemplate` class for this.
example_formatter_template = """Word: {word}
Antonym: {antonym}
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)

# Finally, we create the `FewShotPromptTemplate` object.
few_shot_prompt = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=examples,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix="Give the antonym of every input\n",
    # The suffix is some text that goes after the examples in the prompt.
    # Usually, this is where the user input will go
    suffix="Word: {input}\nAntonym: ",
    # The input variables are the variables that the overall prompt expects.
    input_variables=["input"],
    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
    example_separator="\n",
)

print(few_shot_prompt.format(input='big'))

chain=LLMChain(llm=llm,prompt=few_shot_prompt)
result= chain({'input':"big"})

print(result)