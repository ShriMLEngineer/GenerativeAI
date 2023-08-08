# Few-shot learning is an impressive skill that enables LLMs (large language models) to learn and make generalizations
# from a small number of examples. In this context, prompts play a vital role as they provide input to these models, 
# facilitating this capability.

#This strategy employs the FewShotPromptTemplate class, which requires a PromptTemplate and a collection of a few 
# example shots. The class arranges the prompt template using these examples, which enhances the language model's 
# ability to create a more accurate response. To simplify this procedure, we can utilize LangChain's 
# FewShotPromptTemplate to organize this method effectively.

from langchain import PromptTemplate
from langchain import FewShotPromptTemplate

OpenAI_api_key = 'sk-'
# OpenAI_api_key = os.getenv('OPENAI_API_KEY')

# create our examples
examples = [
    {
        "query": "What's the weather like",
        "answer": "It's raining cats and dogs, better bring an embrella"
    },
    {
        "query": "How old are you?",
        "answer": "Age is just a number, but I'm timeless"
    }
]

# Let's create an example template
example_template = """
User: {query}
AI: {answer}
"""

# create a prompt example from above template. We are making use of 2 parametere input_variable and template
# to pass values 
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)

# now break our previous prompt into a prefix and suffix
# the prefix is our instructions
prefix = """The following are excerpts from conversation with an AI assistant. The assistant is known for its humor
and wit, providing entertaining responses to user's questions. Here are some examples:
"""

# and the suffix our user input and output indicator
suffix = """
User = {query},
AI:
"""

# now create the few-shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator = "\n\n"
)


#After creating a template, we pass the example and user query, and we get the results
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2, openai_api_key=OpenAI_api_key)
chain = LLMChain(llm=chat, prompt=few_shot_prompt_template)
output = chain.run("What's meaning of Large Language Models in heaven")
#to print output on console
print(output)

#Sample Output: "Well, in heaven, Large Language Models are probably busy solving the mysteries of the universe or having deep philosophical discussions with the angels. But hey, that's just my imagination running wild!"