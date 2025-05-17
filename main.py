from typing import Annotated
import pdfoperacoesii as pdfop
from fastapi import FastAPI, File, UploadFile
import codecs
import iapai as ia
import random
import os
import pdfkit
from fastapi.responses import FileResponse

app = FastAPI()

origins = ["*"]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/enviar/")
async def create_upload_file(file: UploadFile):
    if (file.content_type == "application/pdf"):
       
        # Cria a pasta 'cvs' se não existir
        os.makedirs("cvs", exist_ok=True)
        os.makedirs("respostas", exist_ok=True)

        # Gera um nome de arquivo aleatório
        const=str(random.randint(1, 100000))
        filename = f"cv"+const+".pdf"
        filepath = os.path.join("cvs", filename)
        # Salva o arquivo no diretório 'cvs'
        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())
        file.file.seek(0)

        # Processa o arquivo PDF
        arquivo=pdfop.Pdfoperacoesii(os.path.join("cvs", filename))
        texto = arquivo.gettext()
       
        # processa a resposta da ia
        resposta = ia.Iapai().pediriagemini(texto) #usar pediriadeepseek(texto) e pediriagemini(texto)
        resposta = resposta.replace("html\n", "")
        resposta = resposta.replace("```", "")
        
        #compila o arquivo html
        filename = f"resposta"+const+".html"
        with codecs.open(os.path.join("respostas", filename), "w", encoding="utf-8") as f:
            f.write(resposta)
        
        

        # Compila o arquivo html para PDF
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        out=filename.replace(".html", ".pdf")
        pdf = pdfkit.from_file(os.path.join("respostas", filename), os.path.join("pdfentrega", out), options={"page-size": "A4", "encoding": "UTF-8"},configuration=config)
        
        
        return (FileResponse(os.path.join("pdfentrega", out), media_type="application/pdf", filename=out))
    else:
        return("File type not supported")
    
    