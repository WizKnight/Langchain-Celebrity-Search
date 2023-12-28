## Integrating coe with openai API
import os
from constants import openai_key
from langchain.chains import LLMChain
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Search the topic")

## OPENAI LLM Models
# This shows how much control an agent should have while providing you the response.
llm = OpenAI(temperature=0.8)


if input_text:
        st.write(llm(input_text))