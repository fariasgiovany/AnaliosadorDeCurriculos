import pytest
from fastapi.testclient import TestClient
import io



# test_test.py


from main import app  # Importa o app FastAPI do main.py

client = TestClient(app)

def test_read_root():
    
    response = client.get("/")
    assert response.status_code == 200
    # Ajuste conforme a resposta esperada da sua API
    assert "Hello world" in response.json() or response.json() != {}

def test_enviar_pdf():

    # Usando um PDF real
    pdf_file= open("teste.pdf", "rb")
    files = {"file": ("teste.pdf", pdf_file, "application/pdf")}
    response = client.post("/enviar/", files=files)
    assert response.status_code == 200

def test_erroesperado():
    response =client.post("/erro/")
    assert response.status_code == 404
        