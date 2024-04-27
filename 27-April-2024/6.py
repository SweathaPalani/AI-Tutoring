# one shot prompt
# https://www.baseball-reference.com/

from langchain.llms import OpenAI  
from langchain.chains import LLMChain
from langchain import PromptTemplate, FewShotPromptTemplate
import os

api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI(api_key=api_key, temperature=0.7)

# Setup examples correctly
examples = [
    {
        "input": "Babe Ruth",
        "output": "player: Babe Ruth\nhome runs: 714\ninnings pitched: 107.1",
    }
]

# Define how individual examples are structured
example_prompt = PromptTemplate(
    input_variables=["input"],  # These should match the keys used in examples
    template="{output}"
)

# Set up the FewShotPromptTemplate with formatted examples
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="player: {input}.",
    input_variables=["input"],
    example_separator="\n",
)

# Format the few-shot prompt for 'Nolan Ryan'
print(few_shot_prompt.format(input='Nolan Ryan'))

chain=LLMChain(llm=llm,prompt=few_shot_prompt)
result= chain({'input':"Nolan Ryan"})

print(result)
