import PyPDF2
from PyPDF2 import PdfReader
import os

class Pdfoperacoes:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.reader = PdfReader(arquivo)
    def gettext(self):
        texto = ''
        for pagina in self.reader.pages:
            texto += pagina.extract_text()
        return texto
