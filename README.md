AI Customer Support Chatbot

## A RAG (Retrieval Augmented Generation) chatbot built using:

LangChain
FAISS
Sentence Transformers
Ollama
Llama 3.2
Streamlit

## Features
FAQ Search
Delivery Information
Return Policy Search
Refund Queries
Semantic Search
Local AI Model
No API Key Required

## Installation
pip install -r requirements.txt
Pull Ollama Model:

ollama pull llama3.2
Create Embeddings:

python src/create_embeddings.py
Run Application:

streamlit run app.py

## Sample Questions
What is your refund policy?
How can I track my order?
What is standard delivery time?
Can I return a product after 10 days?