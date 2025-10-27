import langchain_chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")


model = ChatGoogleGenerativeAI(
    model = "models/gemini-2.5-flash",
    api_key = GEMINI_KEY
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = model.invoke(messages)
print(ai_msg)