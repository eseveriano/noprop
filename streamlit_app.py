import streamlit as st
import requests

st.title("Monitor da API")

if st.button("Testar POST"):
    r = requests.post(
        "http://127.0.0.1:8000/api/receber",
        json={
            "chave_md5": "e10adc3949ba59abbe56e057f20f883e",
            "dado": "teste streamlit"
        }
    )
    st.json(r.json())
