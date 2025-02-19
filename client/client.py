import requests
import streamlit as st

def get_groq_response(input_text, language="French"):
    json_body = {
        "input": {
            "language": language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }

    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Invalid response from API"}

## Streamlit app
st.title("LLM Application Using LCEL")

# User input field
input_text = st.text_input("Enter the text you want to convert")

# Language selection dropdown
language = st.selectbox("Select target language", options=["Yoruba", "French", "Igbo", "Hausa"])

# Disable button if there's no input
translate_button = st.button("Translate", disabled=not bool(input_text))

if translate_button:
    response = get_groq_response(input_text, language)
    st.write("**Translated Text:**", response)
