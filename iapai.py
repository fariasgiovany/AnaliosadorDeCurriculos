from openai import OpenAI
import os
from dotenv import load_dotenv

class Iapai:
    
    def __init__(self):
        self.texto = ''
    def pediriagemini(self,texto):
        self.texto = texto
        
        load_dotenv()
        client = OpenAI(api_key=os.getenv("GOOGLE_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": self.texto}],
        )

        
        return response.choices[0].message.content


    def pediriadeepseek(self,texto):
        self.texto = texto
        load_dotenv()
        client = OpenAI(api_key=os.getenv("DEEPSEEKKEY"), base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": self.texto}],
        )

        
        return response.choices[0].message.content
    
