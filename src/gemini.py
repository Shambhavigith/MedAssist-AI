import os
from dotenv import load_dotenv
import google.generativeai as genai

from src.retrieval import load_vector_store, retrieve_context
from src.prompt import build_context, build_prompt

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


db = None


def ask_medassist(query):
    global db
    
    if db is None:
        db = load_vector_store()

    retrieved_docs = retrieve_context(
        db,
        query
    )
    context = build_context(
        retrieved_docs)

    prompt = build_prompt(
        context,
        query
    )

    response = model.generate_content(
        prompt
    )
        
    return response.text
    
if __name__ == "__main__":  
    query = input("Ask MedAssist: ")
    answer = ask_medassist(query)
    print(answer)