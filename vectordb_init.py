from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from langchain_community.embeddings import SentenceTransformerEmbeddings


def init():
    load_dotenv()

    GEMINI_KEY = os.getenv("GEMINI_KEY")


    model = ChatGoogleGenerativeAI(
        model = "models/gemini-2.5-flash",
        api_key = GEMINI_KEY
    )


    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = Chroma(
        persist_directory= "DataPreparation/db/chroma_db",
        embedding_function=embeddings
    )

