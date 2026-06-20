from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

def load_pdf(folder):
    loader=DirectoryLoader(
            folder,
            glob="*.pdf",
            loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents
    
def split_text(documents):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=30)
    chunks=text_splitter.split_documents(documents)
    return chunks

def get_embeddings():
    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings
