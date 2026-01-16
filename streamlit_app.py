import streamlit as st

params = st.query_params
chave = params.get("chave_md5")

if chave:
    resposta = {
        "status": "ok",
        "chave_md5": chave,
        "mensagem": "Parâmetro recebido com sucesso"
    }
else:
    resposta = {
        "status": "erro",
        "mensagem": "Parâmetro chave_md5 não informado"
    }

st.json(resposta)
