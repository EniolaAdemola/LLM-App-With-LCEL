from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()
from langserve import add_routes
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

groq_api_key = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="mixtral-8x7b-32768",groq_api_key=groq_api_key)

prompt_template = " Translate the following from English into {language}"

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [("system", prompt_template), ("user","{text}")]
)

# Output parser
parser = StrOutputParser()

chain = prompt | model | parser

# app 
app = FastAPI(
    title="Langchain API",
    description="API for langchain Expression Language",
    version="1.0"
)

# Add routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)