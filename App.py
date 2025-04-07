import streamlit as st

st.set_page_config(page_title="Portal Interno", layout="centered")
st.title("🖥️ Acesso Rápido - Portal Interno")

st.markdown("### 💻 Abrir Citrix StoreWeb")

# URL do Citrix
citrix_url = "http://bronbsv004app.adhosp.com.br/Citrix/StoreWeb/"

# Botão com link
st.markdown(f"""
    <a href="{citrix_url}" target="_blank">
        <button style='padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:8px; cursor:pointer;'>
            Abrir Citrix
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("### 💻 Abrir Tasy")

# URL do Citrix
citrix_url = "https://tasyprd.adhosp.com.br/#/login"

# Botão com link
st.markdown(f"""
    <a href="{citrix_url}" target="_blank">
        <button style='padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:8px; cursor:pointer;'>
            Abrir Citrix
        </button>
    </a>
""", unsafe_allow_html=True)
