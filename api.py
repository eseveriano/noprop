from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

MD5_VALIDO = "e10adc3949ba59abbe56e057f20f883e"

class Payload(BaseModel):
    chave_md5: str
    dado: str | None = None

@app.post("/api/receber")
def receber(payload: Payload):
    if payload.chave_md5 != MD5_VALIDO:
        raise HTTPException(status_code=401, detail="MD5 inválido")

    return {"status": "ok", "dado": payload.dado}
