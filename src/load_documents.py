import os
from pathlib import Path

from langchain_core.documents import Document 

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"


def load_txt_file(file_path):
    """
    Load a text file and convert it into LangChain Document
    """

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    document = Document(
        page_content=content,
        metadata={
            "source": os.path.basename(file_path)
        }
    )

    return [document]


def load_documents():

    documents = []

    for file_name in os.listdir(DATA_DIR):

        file_path = DATA_DIR / file_name

        if file_name.endswith(".txt"):

            docs = load_txt_file(file_path)

            documents.extend(docs)

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(f"Total Documents Loaded: {len(docs)}")

    for doc in docs:
        print(doc.metadata)