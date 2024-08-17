from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()  ## load all environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="QA Chat Bot",page_icon="🤖")

st.header("My QA Chat Bot Application")

input = st.text_input("Write your question here:",key="input")

submit = st.button("Submit")

def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

if submit:
    response = get_gemini_response(input)
    st.write(response)