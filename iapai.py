from openai import OpenAI
import os
from dotenv import load_dotenv

class Iapai:
    
    def __init__(self):
        self.texto = ''
    def pediria(self,texto):
        self.texto = texto
        load_dotenv()
        client = OpenAI(api_key=os.getenv("DEEPSEEKKEY"), base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": self.texto}],
        )

        
        return response.choices[0].message.content
    
