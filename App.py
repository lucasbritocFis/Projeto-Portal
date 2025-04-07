import streamlit as st
import os

st.set_page_config(page_title="Portal Interno", layout="centered")
st.title("🖥️ Acesso Rápido - Portal Interno")

# Citrix
st.markdown("### 💻 Abrir Citrix StoreWeb")
citrix_url = "http://bronbsv004app.adhosp.com.br/Citrix/StoreWeb/"
st.markdown(f"[Abrir Citrix]({citrix_url})", unsafe_allow_html=True)

# Tasy
st.markdown("### 💻 Abrir Tasy")
tasy_url = "https://tasyprd.adhosp.com.br/#/login"
st.markdown(f"[Abrir Tasy]({tasy_url})", unsafe_allow_html=True)

st.markdown("### 📊 Abrir Planilha Excel (rede interna)")

# Caminho da planilha (use \\ para Windows ou / para Linux se necessário)
planilha_path = r"file://10.50.90.18/Radioterapia/PORTAL-RADIOTERAPIA.xlsb"

# Link clicável para abrir a planilha
st.markdown(f"""
    <a href="{planilha_path}" target="_blank" style='text-decoration:none;'>
        <button style='padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:8px; cursor:pointer;'>
            Abrir Planilha Excel
        </button>
    </a>
""", unsafe_allow_html=True)
