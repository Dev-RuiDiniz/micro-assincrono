# app/main.py

from fastapi import FastAPI
from datetime import datetime
import platform # Usado para obter informações do sistema

# A instância do FastAPI permanece a mesma
app = FastAPI(
    title="Micro-Assíncrono: Gestão de Microsserviços",
    description="API de alta performance para orquestração e gestão de serviços assíncronos.",
    version="0.1.0"
)

# ----------------------------------------------------
# 📌 1. Endpoint Assíncrono (Root/Teste)
# ----------------------------------------------------

@app.get("/")
async def root():
    """
    Endpoint raiz para verificar se a API está online e respondendo (Assíncrono).
    """
    return {"message": "API principal operando com sucesso!"}

# ----------------------------------------------------
# 📌 2. Endpoint Síncrono (Health Check)
# ----------------------------------------------------

@app.get("/health")
def health_check():
    """
    Endpoint síncrono para verificar a saúde e o status do sistema.
    O FastAPI executa esta função em um thread pool separado (Blocking I/O).
    """
    uptime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Retorna informações úteis sobre o status da aplicação
    return {
        "status": "UP",
        "api_version": app.version,
        "current_time": uptime,
        "os": platform.system(),
        "message": "Serviço saudável e rodando em thread síncrono."
    }