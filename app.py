import streamlit as st

from src.chatbot import generate_answer

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Support Chatbot")

st.markdown(
    """
Ask questions about:

✅ Returns

✅ Refunds

✅ Deliveries

✅ Tracking

✅ Customer Support
"""
)

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


user_question = st.chat_input(
    "Ask your question..."
)

if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.spinner("Searching Knowledge Base..."):

        answer, sources = generate_answer(
            user_question
        )

    source_text = "\n".join(
        [f"- {source}" for source in sources]
    )

    final_answer = f"""
{answer}

### Sources

{source_text}
"""

    with st.chat_message("assistant"):
        st.markdown(final_answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )