import streamlit as st

MD5_VALIDO = "e10adc3949ba59abbe56e057f20f883e"

params = st.query_params
chave = params.get("chave_md5")
dado = params.get("dado")

if chave == MD5_VALIDO:
    resposta = {
        "status": "ok",
        "mensagem": "GET recebido com sucesso",
        "dado": dado
    }
else:
    resposta = {
        "status": "erro",
        "mensagem": "MD5 inválido ou não informado"
    }

st.json(resposta)
