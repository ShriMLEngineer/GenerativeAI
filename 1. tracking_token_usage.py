#Tracking Token Usage

#The callback will track the tokens used, successful requests, and total cost.

from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os

OpenAI.api_key = os.getenv('OPENAI_API_KEY')
print("a", OpenAI.api_key)
llm = OpenAI(model_name = "text-davinci-003", n=2, best_of=2)

with get_openai_callback() as cb:
    result=llm("tell me a joke")
    print(result)
    print(cb)

"""
Result of cb:
Tokens Used: 47
        Prompt Tokens: 4
        Completion Tokens: 43
Successful Requests: 1
Total Cost (USD): $0.00094
"""
