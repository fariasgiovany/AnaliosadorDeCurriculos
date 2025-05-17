import pymupdf4llm
import time
class Pdfoperacoesii:
    def __init__(self, arquivo):
        self.arquivo = arquivo
    
    def gettext(self):
        
        
        texto = pymupdf4llm.to_markdown(self.arquivo)
        print(texto)
       
        resposta = texto + "verificar se texto acima é um currículo, se não for um curriculo responder apenas ""texto invalido"".Adcionar melhorias ao curriculo. Criar uma introdução no curriculo. Formatar texto em html com foco em impressão. Não adicionar sugestões no arquivo html, mostrar links inteiros.Resposta apenas com o texto em html com algum design gráfico e com cabeçalho centralizado"
        
        return resposta


  