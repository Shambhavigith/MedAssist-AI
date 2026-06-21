from helper import get_embeddings
from langchain_community.vectorstores import FAISS


print("Starting retrieval.py")

def load_vector_store():
    print("Loading embeddings...")
    embedding_model=get_embeddings()
    print("Loading FAISS...")
    db=FAISS.load_local("faiss_index",embedding_model,allow_dangerous_deserialization=True)
    print("FAISS loaded!")
    return db

db = load_vector_store()

print("Searching...")


def retrieve_context(db,query,k=3):
    retrieved_docs = db.similarity_search(
    query,
    k=k)
    return retrieved_docs


retrieved_docs = retrieve_context(
    db,
    "What are symptoms of dengue?")
print("Retrieved:", len(retrieved_docs))

for doc in retrieved_docs:
    print(doc.page_content)
    print(doc.metadata)
