import PyPDF2
from PyPDF2 import PdfReader
import os

class Pdfoperacoes:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.reader = PdfReader(arquivo)
    def gettext(self):
        texto = "Analisar esse curriculo,  e criar um curriculo melhor em em latex. Responder apenas com o codigo em latex. "
        for pagina in self.reader.pages:
            texto += pagina.extract_text()
            texto=texto.replace("\n"," ")
            texto=texto+"se não tiver informaçoes sobre curriculo, responder apenas texto invalido e não analisar texto"
        return texto
