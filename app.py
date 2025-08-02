import streamlit as st
from modules.wallet import wallet_connect_component
from modules.chatbot import chatbot_component
from modules.portfolio import portfolio_component
from modules.analytics import analytics_component
from modules.signal_discovery import signal_discovery_component
from modules.forecasting import forecasting_component
from modules.narrative import narrative_component
from modules.news_impact import news_impact_component
from modules.research_reports import research_reports_component
from modules.learning import learning_component
from modules.onchain_forensics import onchain_forensics_component
from modules.alpha_marketplace import alpha_marketplace_component
from modules.smart_alerts import smart_alerts_component
from modules.visualizations import visualizations_component
from modules.compliance import compliance_component

st.set_page_config(page_title="Edge Terminal Dashboard", layout="wide")
st.title("🚀 Edge Terminal AI Dashboard")

# Sidebar: Wallet Connect
wallet_address = wallet_connect_component()

st.divider()

tabs = st.tabs([
    "Portfolio",
    "AI Copilot",
    "Analytics",
    "Signal Discovery",
    "Forecasting",
    "Narrative Evolution",
    "News Impact",
    "Research Reports",
    "Learning/Adaptation",
    "On-Chain Forensics",
    "Alpha Marketplace",
    "Smart Alerts",
    "Visualizations",
    "Compliance"
])

with tabs[0]:
    st.header("📊 Portfolio Overview")
    portfolio_component(wallet_address)

with tabs[1]:
    st.header("💬 AI Copilot")
    chatbot_component(wallet_address)

with tabs[2]:
    st.header("📈 Analytics & Insights")
    analytics_component(wallet_address)

with tabs[3]:
    st.header("🧠 AI-Driven Signal Discovery")
    signal_discovery_component(wallet_address)

with tabs[4]:
    st.header("🔮 Predictive & Generative Models")
    forecasting_component(wallet_address)

with tabs[5]:
    st.header("📰 Narrative Evolution Prediction")
    narrative_component(wallet_address)

with tabs[6]:
    st.header("🌐 News/Event Impact Prediction")
    news_impact_component(wallet_address)

with tabs[7]:
    st.header("📄 Automated Research Reports")
    research_reports_component(wallet_address)

with tabs[8]:
    st.header("♻️ Continuous Learning & Adaptation")
    learning_component(wallet_address)

with tabs[9]:
    st.header("🔎 Advanced On-Chain Forensics")
    onchain_forensics_component(wallet_address)

with tabs[10]:
    st.header("🚀 Alpha Discovery Marketplace")
    alpha_marketplace_component(wallet_address)

with tabs[11]:
    st.header("⚡ Smart Alerting & Proactive Guidance")
    smart_alerts_component(wallet_address)

with tabs[12]:
    st.header("📊 AI-Augmented Visualizations")
    visualizations_component(wallet_address)

with tabs[13]:
    st.header("🛡️ Security & Compliance")
    compliance_component(wallet_address)

st.divider()
st.markdown("Made with ❤️ for next-gen finance.")
