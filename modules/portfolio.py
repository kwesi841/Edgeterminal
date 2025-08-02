import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def portfolio_component(wallet_address=None):
    if wallet_address:
        st.write(f"Portfolio for wallet: {wallet_address}")
        # Fetch ETH balance from Etherscan
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            if data['status'] == '1':
                eth_balance = int(data['result']) / 1e18
                st.success(f"ETH Balance: {eth_balance:.6f} ETH")
            else:
                st.error("Could not fetch balance. Check wallet address.")
        except Exception as e:
            st.error(f"Error fetching balance: {e}")
        st.info("ERC-20 token balances coming soon!")
    else:
        st.warning("Connect your wallet to view portfolio analytics.")
