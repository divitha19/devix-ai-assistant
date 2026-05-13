from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from agents.pdf_tool import search_pdf
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

prompt = ChatPromptTemplate.from_template(
    '''
    You are Jarvex AI assistant.

    User Question:
    {question}

    PDF Context:
    {context}

    Give a helpful response.
    '''
)

chain = prompt | llm

def ask_agent(question):
    context = search_pdf(question)

    response = chain.invoke({
        "question": question,
        "context": context
    })

    return response.content
