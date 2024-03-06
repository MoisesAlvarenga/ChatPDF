from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
load_dotenv()

# ---------------------------------------- OpenAi Exxample ----------------------------------
def create_vectorstore(chunks):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vectorstore




def create_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain


# -------------------- Ollama Example ---------------------------------------


# def create_vectorstore(chunks):
#     embeddings = OllamaEmbeddings()
#     vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

#     return vectorstore

# def create_conversation_chain(vectorstore):
#     llm = Ollama(model="llama2")

#     memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

#     conversation_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectorstore.as_retriever(),
#         memory=memory
#     )

#     return conversation_chain