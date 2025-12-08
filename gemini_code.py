import streamlit as st

from google import genai

st.title("CharmyGPT")

def answer(question):
    client = genai.Client(api_key = "...........")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f''' You're a summarising expert , so now summarise the given content in clear, simple, and concise way, 
        give a highlighting headline ,
        start with a catchy line,
        highlight the key points,mainn idea , and important conclusions {question} '''
        )
    return response

content = st.file_uploader("Please upload the document so i can generate a concise summary for you.")

if st.button("Summarise"):
    if content:
        with st.spinner("Processing your file....almost there."):
            question = content.read()
            result = answer(question)
            st.write(result.text)
    else:
        st.warning("⚠️File Error: Unable to retrive the file. Re-upload needed.")
