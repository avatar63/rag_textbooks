from langchain_text_splitters import RecursiveCharacterTextSplitter
from glob import glob
import pdf_data
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
import os
from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
load_dotenv()
GEMINI_KEY=os.getenv("GEMINI_KEY")

text=""
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

pdf_paths = [k for k in glob("../textbooks/*/*.pdf")]

for path in pdf_paths:
    text+=pdf_data.convert_to_text(path)
print(len(text))



splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_text(text)



db = Chroma.from_texts(texts = docs,embedding = embeddings,persist_directory="db/chroma_db")
db.persist()



print("ChromaDB created.")
