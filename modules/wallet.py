import streamlit as st

def wallet_connect_component():
    st.sidebar.subheader("🔑 Wallet Login")
    wallet_address = st.sidebar.text_input("Paste your Ethereum wallet address here:")
    if wallet_address and wallet_address.startswith("0x") and len(wallet_address) == 42:
        st.sidebar.success(f"Wallet connected: {wallet_address}")
        return wallet_address
    elif wallet_address:
        st.sidebar.error("Invalid Ethereum address. Should start with 0x and be 42 characters.")
    else:
        st.sidebar.info("Connect your wallet to personalize analytics.")
    return None
