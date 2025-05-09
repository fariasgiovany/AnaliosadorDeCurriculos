from typing import Annotated
import pdfoperacoes as pdfop
from fastapi import FastAPI, File, UploadFile
import iapai as ia

app = FastAPI()

origins = ["*"]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/enviar/")
async def create_upload_file(file: UploadFile):
    if (file.content_type == "application/pdf"):
        
        arquivo=pdfop.Pdfoperacoes(file.file)
        texto = arquivo.gettext()
        resposta = ia.Iapai().pediriagemini(texto) #usar pediriadeepseek() e pediriagemini()
        resposta = resposta.replace("\n","<br />")
        return(resposta)
    else:
        return("File type not supported")
    
    