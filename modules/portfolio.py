import streamlit as st
import os
import requests

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

@st.cache_data(ttl=60, show_spinner=False)
def _fetch_eth_balance(wallet_address: str, api_key: str):
    """Return ETH balance (float) for wallet, or raise on error."""
    url = (
        "https://api.etherscan.io/api?module=account&action=balance"
        f"&address={wallet_address}&tag=latest&apikey={api_key}"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("status") == "1":
        return int(data["result"]) / 1e18
    raise ValueError(data.get("message", "Unknown Etherscan error"))

def portfolio_component(wallet_address=None):
    if not wallet_address:
        st.warning("Connect your wallet to view portfolio analytics.")
        return

    st.write(f"Portfolio for wallet: {wallet_address}")

    if not ETHERSCAN_API_KEY:
        st.error("Missing ETHERSCAN_API_KEY. Set it in environment to fetch balances.")
        return

    try:
        eth_balance = _fetch_eth_balance(wallet_address, ETHERSCAN_API_KEY)
        st.success(f"ETH Balance: {eth_balance:.6f} ETH")
    except requests.Timeout:
        st.error("Etherscan request timed out. Please try again.")
    except Exception as e:
        st.error(f"Error fetching balance: {e}")

    st.info("ERC-20 token balances coming soon!")
