from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter

from load_documents import load_documents

ROOT_DIR = Path(__file__).resolve().parent.parent

VECTOR_STORE_PATH = ROOT_DIR / "vectorstore"

EMBEDDING_MODEL = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store():

    documents = load_documents()

    print(f"Loaded Documents: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Generated Chunks: {len(chunks)}")

    vector_store = FAISS.from_documents(
        chunks,
        EMBEDDING_MODEL
    )

    vector_store.save_local(
        str(VECTOR_STORE_PATH)
    )

    print("FAISS Vector Store Created Successfully")


if __name__ == "__main__":
    create_vector_store()
