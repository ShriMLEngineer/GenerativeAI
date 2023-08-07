from langchain.chains import LLMChain
from langchain import OpenAI
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(template="Question:{question}\nAnswer:", input_variables=['question'])

llm = OpenAI(model_name = 'text-davinci-003', temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("What is life?")
print (response)