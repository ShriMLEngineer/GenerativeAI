from langchain import PromptTemplate

template = """Question: {question}
Answer: """
prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

# user question
question = "What is capital city of France?"

from langchain import HuggingFaceHub, LLMChain

hub_llm = HuggingFaceHub(
    repo_id='google/flan-t5-large',huggingfacehub_api_token='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',
    model_kwargs={'temperature': 0}
)

#create prompt template > LLM chain
llm_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm
)

# ask the user the question about the capital of France
print(llm_chain(question))

# Asking Multiple Questions


multi_template = """Answer the following questions one at a time.

Questions:
{questions}

Answers:
"""

long_prompt = PromptTemplate(
    template=multi_template,
    input_variables=["questions"]
)
llm_chain = LLMChain(
    prompt=long_prompt,
    llm=hub_llm
    )

qs_str = (
    "What is the capital city of France?\n" +
    "What is the largest mammal on Earth?\n" +
    "Which gas is most abundant in Earth's atmosphere?\n" +
	"What color is a ripe banana?\n"
)
print(llm_chain.run(qs_str))
