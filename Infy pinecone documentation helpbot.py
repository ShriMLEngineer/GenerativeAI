import pinecone
import os
from typing import Any, Dict, List
from tqdm.autonotebook import tqdm
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

PINECONE_API_KEY = 'badb1d6f-7029-42d4-945c-5fad98b497a6'
PINECONE_ENVIRONMENT_REGION = 'us-west4-gcp-free'

OPENAI_API_KEY = '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'

pinecone.init(
    api_key = PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT_REGION,
)

INDEX_NAME = 'chatbot-index'

loader = ReadTheDocsLoader(path="langchain_documentation_data\en\latest",
                           encoding="ISO-8859-1",
                           features="lxml"
                           )

raw_documents = loader.load()

print(f"loaded {len(raw_documents)} documents")
print(f"The variable 'raw_documents' holds a {type(raw_documents[0].page_content)} having 1868 documents")

print(f"Data in 1st document exists as: {type(raw_documents[0].page_content)} having length {len(raw_documents[0].page_content)}", '\n')

print(f"The first fw characters in the 1st doc: ", '\n')
raw_documents[0].page_content[:200]

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overloop=200, separators=["\n\n","\n"," ",""])

documents = text_splitter.split_documents(raw_documents)

print(f"Splitted into {len(documents)} chunks")



