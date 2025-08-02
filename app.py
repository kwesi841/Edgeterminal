import streamlit as st
from modules.wallet import wallet_connect_component
from modules.chatbot import chatbot_component
from modules.portfolio import portfolio_component
from modules.analytics import analytics_component

st.set_page_config(page_title="Edge Terminal Dashboard", layout="wide")
st.title("🚀 Edge Terminal AI Dashboard")

# Sidebar: Wallet Connect
wallet_address = wallet_connect_component()

st.divider()

# Main tabs for modular navigation
tabs = st.tabs(["Portfolio", "AI Copilot", "Analytics"])

with tabs[0]:
    st.header("📊 Portfolio Overview")
    portfolio_component(wallet_address)

with tabs[1]:
    st.header("💬 AI Copilot")
    chatbot_component(wallet_address)

with tabs[2]:
    st.header("📈 Analytics & Insights")
    analytics_component(wallet_address)

st.divider()
st.markdown("Made with ❤️ for next-gen finance.")
