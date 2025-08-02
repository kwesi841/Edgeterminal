import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def chatbot_component(wallet_address=None):
    st.write("Type your question about tokens, risk, or strategies below.")
    user_input = st.text_input("Your question:", key="chat_input")
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # Use OpenAI's GPT model to answer
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert crypto and finance advisor."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=256,
                    temperature=0.7,
                )
                answer = completion['choices'][0]['message']['content']
                st.success(answer)
            except Exception as e:
                st.error(f"Error with OpenAI API: {e}")
