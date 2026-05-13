import streamlit as st
from agents.main_agent import ask_agent
from voice.speech_to_text import listen
from rag.vector_store import create_vector_store

st.set_page_config(page_title="Jarvex AI")

st.title("🤖 Jarvex AI Voice Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    create_vector_store("temp.pdf")

    st.success("PDF Processed Successfully")

query = st.text_input("Ask Something")

if st.button("Ask AI"):
    answer = ask_agent(query)

    st.write("### AI Response")
    st.write(answer)


if st.button("🎤 Voice Command"):
    voice_query = listen()

    st.write("You Said:", voice_query)

    answer = ask_agent(voice_query)

    st.write(answer)
