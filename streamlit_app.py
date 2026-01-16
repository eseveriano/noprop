from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

MD5_VALIDO = "e10adc3949ba59abbe56e057f20f883e"  # md5("123456")

# -------- POST --------
class Payload(BaseModel):
    chave_md5: str
    dado: Optional[str] = None

@app.post("/api/receber")
def receber_post(payload: Payload):
    if payload.chave_md5 != MD5_VALIDO:
        raise HTTPException(status_code=401, detail="MD5 inválido")

    return {
        "status": "ok",
        "metodo": "POST",
        "mensagem": "POST recebido com sucesso",
        "dado": payload.dado
    }

# -------- GET --------
@app.get("/api")
def receber_get(
    chave_md5: str = Query(...),
    dado: Optional[str] = Query(None)
):
    if chave_md5 != MD5_VALIDO:
        raise HTTPException(status_code=401, detail="MD5 inválido")

    return {
        "status": "ok",
        "metodo": "GET",
        "mensagem": "GET recebido com sucesso",
        "dado": dado
    }
