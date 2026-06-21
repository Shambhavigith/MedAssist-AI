import os
from dotenv import load_dotenv
import google.generativeai as genai

from retrieval import load_vector_store, retrieve_context
from prompt import build_context, build_prompt

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


db = load_vector_store()

query = "What is the cure for alien fever?"

retrieved_docs = retrieve_context(
    db,
    query
)

context = build_context(
    retrieved_docs
)

prompt = build_prompt(
    context,
    query
)

print("\nRetrieved Documents:", len(retrieved_docs))
print("\nContext Preview:\n")
print(context[:1000])

response = model.generate_content(
    prompt
)

print(response.text)