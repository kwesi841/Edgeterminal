import streamlit as st

def chatbot_component(wallet_address=None):
    st.write("Type your question about tokens, risk, or strategies below.")
    user_input = st.text_input("Your question:", key="chat_input")
    if user_input:
        # Mock AI response, personalize if wallet connected
        if wallet_address:
            st.write(f"👤 {wallet_address} asked: {user_input}")
            st.success(f"AI Copilot (Personalized):\nHere's a mock analysis of your question: '{user_input}'.\n[In production, this will query the AI modules with your wallet context!]")
        else:
            st.write(f"You asked: {user_input}")
            st.success(f"AI Copilot:\nHere's a mock analysis of your question: '{user_input}'.\n[Connect your wallet for personalized insights!]")
