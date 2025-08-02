# Edge Terminal

**Edge Terminal** is a next-generation AI-powered dashboard for digital asset professionals and sophisticated crypto users.  
It provides a unified workspace for portfolio analytics, AI research, risk management, Web3 wallet integration, and customizable insights—all in your browser.

---

## 🚀 Features

- **Web3 Wallet Integration:**  
  Connect your wallet (MetaMask, WalletConnect, or manual entry) for real-time, personalized analytics on your actual holdings and on-chain activity.

- **AI Copilot Chat:**  
  Natural language copilot to answer your questions, surface insights, explain token risks, and suggest strategies—using both general AI models and proprietary analytics.

- **Portfolio Dashboard:**  
  Visualize your token holdings, allocations, historical P&L, and risk metrics. Drill down into assets, protocols, and DeFi positions.

- **Market Intelligence:**  
  Aggregated news, token analytics, and sentiment—curated by AI and tailored to your wallet’s exposure.

- **Risk & Compliance:**  
  Automated risk scoring, position health monitoring, and alerts for volatility, liquidation risk, or wallet events.

- **Modular App Architecture:**  
  Plug in additional modules: trading, alerts, custom analytics, web3 dapps, and more.

- **Enterprise-Grade Security:**  
  Client-side wallet integration—your keys/seed never leave your browser. No custody, no trust required.

---

## 🛠️ Quick Start

### 1. **Install Python 3.9+**

[Download Python](https://www.python.org/downloads/) and install it.

---

### 2. **Clone the Repository**

```sh
git clone https://github.com/your-username/edge-terminal.git
cd edge-terminal
```

---

### 3. **Install Dependencies**

```sh
pip install -r requirements.txt
```

---

### 4. **Run the Dashboard**

```sh
streamlit run app.py
```

Visit the local URL shown in the terminal (usually http://localhost:8501).

---

## 🧑‍💻 How to Use

- **Connect Wallet:** Use the sidebar to connect your Web3 wallet (MetaMask, WalletConnect, or paste your address for read-only mode).
- **Explore Dashboard:** View your portfolio, analytics, and real-time risk insights.
- **AI Copilot:** Chat with the Edge Copilot to ask about tokens, risks, strategies, or any crypto topic.
- **Customize:** Add or remove modules as needed.

---

## 🌍 Deployment

### Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
1. Push your code to GitHub.
2. Go to Streamlit Cloud.
3. Click "New app", select your repo, and set main file path (`app.py`).
4. Click "Deploy" for a public URL.

### Advanced: Deploy on your own server (Docker, cloud, etc.)
- See `DEPLOY.md` (coming soon).

---

## 📦 Project Structure

```
edge-terminal/
│
├─ app.py               # Main Streamlit entrypoint
├─ modules/             # All feature modules (wallet, portfolio, chat, analytics, etc.)
│   ├─ wallet.py
│   ├─ portfolio.py
│   ├─ chatbot.py
│   ├─ analytics.py
│   └─ ...
├─ requirements.txt     # Python dependencies
├─ README.md
└─ ... (more files)
```

---

## ✨ Contributing

PRs welcome! Open an issue or discuss your module idea.

---

## 🛡️ Security & Disclaimer

Edge Terminal is non-custodial and does NOT store or transmit your wallet private keys.  
It is for informational and research purposes only—no investment advice.  
Use at your own risk.

---

**Edge Terminal**  
Built for digital asset professionals by digital asset professionals.
