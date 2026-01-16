import streamlit as st
import hashlib

# MD5 esperado
MD5_VALIDO = "e10adc3949ba59abbe56e057f20f883e"  # md5("123456")

st.set_page_config(page_title="API Streamlit", layout="centered")

st.title("API Streamlit com MD5")

# 📥 Entrada da chave (simula POST)
chave_md5 = st.text_input("Informe a chave MD5", type="password")

if st.button("Enviar"):
    if not chave_md5:
        st.error("Chave não informada")
    elif chave_md5 != MD5_VALIDO:
        st.error("Chave MD5 inválida")
    else:
        st.success("Acesso autorizado")
        st.json({
            "status": "ok",
            "mensagem": "Autenticado com sucesso"
        })
