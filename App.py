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

# Abrir planilha Excel
st.markdown("### 📊 Abrir Planilha Excel (rede interna)")
excel_path = r"\\10.50.90.18\Radioterapia\PORTAL-RADIOTERAPIA.xlsb"

if st.button("Abrir Planilha Excel"):
    try:
        os.startfile(excel_path)  # Isso só funciona no Windows local
        st.success("Arquivo aberto com sucesso!")
    except Exception as e:
        st.error(f"Erro ao abrir o arquivo: {e}")
