# app/main.py

from fastapi import FastAPI

# 💡 A função 'FastAPI()' cria a instância principal da aplicação.
# O parâmetro 'title' é uma boa prática que aparece na documentação interativa (Swagger UI).
app = FastAPI(
    title="Micro-Assíncrono: Gestão de Microsserviços",
    description="API de alta performance para orquestração e gestão de serviços assíncronos.",
    version="0.1.0"
)

# ----------------------------------------------------
# 📌 Endpoint de Teste Simples (Health Check)
# ----------------------------------------------------

@app.get("/")
async def root():
    """
    Endpoint raiz para verificar se a API está online e respondendo.
    """
    return {"message": "API principal operando com sucesso!"}