from openai import OpenAI
import os
from dotenv import load_dotenv
from google import genai

class Iapai:
    
    def __init__(self):
        self.texto = ''
    def pediria(self,texto):
        self.texto = texto
        load_dotenv()
        client = genai.Client(api_key="os.getenv('DEEPSEEK_API_KEY')")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": self.texto}],
        )

        
        return response.choices[0].message.content
    
