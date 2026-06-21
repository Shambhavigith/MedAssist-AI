from langchain_community.vectorstores import FAISS
from helper import load_pdf, split_text, get_embeddings
from csv_to_documents import load_clinical_documents


pdf_documents = load_pdf("Data/guidelines/")
pdf_chunks = split_text(pdf_documents)

clinical_documents = load_clinical_documents()


all_documents = pdf_chunks + clinical_documents

embedding_model = get_embeddings()

faiss_index = FAISS.from_documents(
    all_documents,
    embedding_model
)

faiss_index.save_local("faiss_index")

print(f"PDF Chunks: {len(pdf_chunks)}")
print(f"Clinical Documents: {len(clinical_documents)}")
print(f"Total Documents: {len(all_documents)}")