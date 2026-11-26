from pathlib import Path

import ollama

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

ROOT_DIR = Path(__file__).resolve().parent.parent

VECTOR_STORE_PATH = ROOT_DIR / "vectorstore"

EMBEDDING_MODEL = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    str(VECTOR_STORE_PATH),
    EMBEDDING_MODEL,
    allow_dangerous_deserialization=True
)


def retrieve_documents(question):

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    return docs


def generate_answer(question):

    documents = retrieve_documents(question)

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
You are a customer support assistant.

Answer ONLY from the provided context.

If answer is not available in context then say:

"I do not have enough information to answer this question."

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    sources = []

    for doc in documents:

        source_name = doc.metadata.get(
            "source",
            "Unknown"
        )

        if source_name not in sources:
            sources.append(source_name)

    return answer, sources