# Pet name generator

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType
import os
import warnings

warnings.filterwarnings("ignore")

api_key = os.environ['OPENAI_API_KEY']
def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)

    prompt_template = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a pet {animal_type} and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="pet_name")
    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})
    return response


def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run("What is the average age of a dog? Multiply the age by 3")

    print(result)


if __name__ == "__main__":
    print(generate_pet_name("dog", "gold"))