import PyPDF2
from PyPDF2 import PdfReader
import os

class Pdfoperacoes:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.reader = PdfReader(arquivo)
    def gettext(self):
        texto = "Analisar esse curriculo,  de forma suscinta ver o que pode ser melhorado e ignorando fragmentação"
        for pagina in self.reader.pages:
            texto += pagina.extract_text()
            texto=texto.replace("\n"," ")
            texto=texto+"se não tiver informaçoes sobre curriculo, responder texto invalido e não analisar texto"
        return texto
