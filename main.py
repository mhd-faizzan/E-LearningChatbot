import streamlit as st
from langchain_helper import get_qa_chain

st.title("Udemy Q&A 🧑‍🏫")

# Access the API key securely using Streamlit secrets
api_key = st.secrets["google_palm"]["api_key"]

question = st.text_input("Question:")

if question:
    chain = get_qa_chain(api_key)  # Pass API key to helper function
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
