from langchain_community.vectorstores import FAISS
from helper import load_pdf,split_text,get_embeddings

documents=load_pdf("Data/")
chunks=split_text(documents)
embedding_model=get_embeddings()
faiss_index=FAISS.from_documents(chunks,embedding_model) 
faiss_index.save_local("faiss_index")