from langchain import PromptTemplate
from langchain import FewShotPromptTemplate

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

# create an example template
example_template = """
User: {query}
AI: {answer}
"""

# create a prompt example from above template
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

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)
chain = LLMChain(llm=chat, prompt=few_shot_prompt_template)
chain.run("What's meaning of life in heaven")
#to print output on console
print(chain.run("What's meaning of life in heaven"))

#Sample Output: "In heaven, the meaning of life is probably just to enjoy an endless supply of fluffy clouds and angelic harp music."