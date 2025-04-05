from typing import Annotated
import pdfoperacoes as pdfop
from fastapi import FastAPI, File, UploadFile

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
        print (texto)
        return("PDF file detected")
    else:
        return("File type not supported")
    
    