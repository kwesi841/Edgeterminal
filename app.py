import streamlit as st
from importlib import import_module
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # dotenv is optional; environment variables may already be set
    pass

st.set_page_config(page_title="Edge Terminal Dashboard", layout="wide")
st.title("🚀 Edge Terminal AI Dashboard")

# Sidebar: Wallet Connect
wallet_module = import_module("modules.wallet")
wallet_address = wallet_module.wallet_connect_component()

st.divider()

# Lazy-render a single section to reduce imports and execution on load
sections = [
    ("Portfolio", "portfolio", "📊 Portfolio Overview", "portfolio_component"),
    ("AI Copilot", "chatbot", "💬 AI Copilot", "chatbot_component"),
    ("Analytics", "analytics", "📈 Analytics & Insights", "analytics_component"),
    ("Signal Discovery", "signal_discovery", "🧠 AI-Driven Signal Discovery", "signal_discovery_component"),
    ("Forecasting", "forecasting", "🔮 Predictive & Generative Models", "forecasting_component"),
    ("Narrative Evolution", "narrative", "📰 Narrative Evolution", "narrative_component"),
    ("News Impact", "news_impact", "🌐 News/Event Impact Prediction", "news_impact_component"),
    ("Research Reports", "research_reports", "📄 Automated Research Reports", "research_reports_component"),
    ("Learning/Adaptation", "learning", "♻️ Continuous Learning & Adaptation", "learning_component"),
    ("On-Chain Forensics", "onchain_forensics", "🔎 Advanced On-Chain Forensics", "onchain_forensics_component"),
    ("Alpha Marketplace", "alpha_marketplace", "🚀 Alpha Discovery Marketplace", "alpha_marketplace_component"),
    ("Smart Alerts", "smart_alerts", "⚡ Smart Alerting & Proactive Guidance", "smart_alerts_component"),
    ("Visualizations", "visualizations", "📊 AI-Augmented Visualizations", "visualizations_component"),
    ("Compliance", "compliance", "🛡️ Security & Compliance", "compliance_component"),
]

labels = [label for (label, _, _, _) in sections]
selected_label = st.sidebar.selectbox("Navigate", labels, index=0)

label_to_section = {label: (module_name, header, func_name) for (label, module_name, header, func_name) in sections}
module_name, header, func_name = label_to_section[selected_label]

st.header(header)
module = import_module(f"modules.{module_name}")
getattr(module, func_name)(wallet_address)

st.divider()
st.markdown("Made with ❤️ for next-gen finance.")
