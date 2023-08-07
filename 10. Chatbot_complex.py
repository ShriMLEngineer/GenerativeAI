from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature=0)

messages = [
    SystemMessage(content="You aree a helpful assistant that translates English to French."),
    HumanMessage(content="Translate the following sentence: I love programming")
]

print(chat(messages).content)