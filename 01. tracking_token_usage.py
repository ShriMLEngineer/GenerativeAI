# If you want to check how many tokens are being used during a LLM request, how many are request tokens and how many of them are response (completion) tokens, then
# use below code. It will also give you the cost of the request

#Import required libraries
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os

#specify OpenAI API key or store it as an environmental variable and fetch the same
OpenAI_api_key = 'sk-'
# OpenAI_api_key = os.getenv('OPENAI_API_KEY')

# LLM model call
llm = OpenAI(model_name = "text-davinci-003", openai_api_key=OpenAI_api_key)   

with get_openai_callback() as cb:
    result=llm("tell me a technical joke")
    print(result)
    print(cb)


"""
Response example
Q: What did the computer do at lunchtime?
A: He had a byte!
Tokens Used: 26
        Prompt Tokens: 5
        Completion Tokens: 21
Successful Requests: 1
Total Cost (USD): $0.00052
"""
