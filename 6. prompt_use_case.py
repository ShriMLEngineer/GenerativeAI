from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0)
sys_template = "You are an assistant who helps user to provide movie information"
system_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
human_template = "find the information of the {movie_title}."
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
response = chat(chat_prompt.format_prompt(movie_title="Sairat").to_messages())
print(response.content)