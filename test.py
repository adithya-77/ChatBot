# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv # type: ignore

load_dotenv()  # take environment variables from .env.

import streamlit as st # type: ignore
import os
import pathlib
import textwrap

import google.generativeai as genai # type: ignore

from IPython.display import display # type: ignore
from IPython.display import Markdown # type: ignore


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Chat Bot")

st.header("I'm ChatBot")
#st.image("https://media.licdn.com/dms/image/D5603AQGRvuyBNzcBkA/profile-displayphoto-shrink_800_800/0/1711598312512?e=2147483647&v=beta&t=8spohchaHsFrh_Sr_UZzYyZobRIGJKflKGFzT3sUmrk", width=100)
input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
