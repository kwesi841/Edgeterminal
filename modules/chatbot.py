import streamlit as st
import os

def _get_openai_module():
    """Lazily import and configure OpenAI; cache across reruns."""
    # Avoid importing heavy libs at app start
    try:
        import openai  # type: ignore
    except Exception as import_error:
        raise RuntimeError(
            "OpenAI package is not installed. Please install 'openai'."
        ) from import_error

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

    openai.api_key = api_key
    return openai

def chatbot_component(wallet_address=None):
    st.write("Type your question about tokens, risk, or strategies below.")
    user_input = st.text_input("Your question:", key="chat_input")
    if user_input:
        with st.spinner("Thinking..."):
            try:
                openai = _get_openai_module()
                # Use OpenAI's GPT model to answer
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert crypto and finance advisor."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=256,
                    temperature=0.7,
                    request_timeout=30,
                )
                answer = completion['choices'][0]['message']['content']
                st.success(answer)
            except Exception as e:
                st.error(f"Error with OpenAI API: {e}")
