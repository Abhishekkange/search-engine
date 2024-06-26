import pymongo
from pymongo import MongoClient
# from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os

# load_dotenv()

# mongo_url = os.environ.get('MONGO_URL')
# gemini_api_key = os.environ.get('GEMINI_API_KEY')

def dbconnect():
    conn = MongoClient(mongo_url)
    print("Connected to database")
    return conn

def embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="AIzaSyANqyvxOpFeKyVjDI_fbkTGp2aaKYu_MS4")
    return embeddings

def generate_embeddings(text):
    embeddings_instance = embeddings()
    embeded_data = embeddings_instance.embed_documents(text)
    return embeded_data