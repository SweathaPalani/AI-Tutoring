#one shot prompt
from langchain import PromptTemplate
from langchain.llms import OpenAI  
from langchain.chains import LLMChain
import os
import warnings

warnings.filterwarnings("ignore")

api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI(api_key=api_key, temperature=0.7)

template='''In an easy way translate the following sentence '{sentence}' into {target_language}'''
language_prompt = PromptTemplate(
    input_variables=["sentence",'target_language'],
    template=template,
)
language_prompt.format(sentence="How are you",target_language='french')

chain2=LLMChain(llm=llm,prompt=language_prompt)

result=chain2({'sentence':"Hello How are you",'target_language':'hindi'})

print(result)