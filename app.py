
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI 
import uvicorn

# 
from model.db import engine, Base
from router import Especialidade, Convenio, Contato, Medico, Paciente, Medicamento, Consulta, Receita

Base.metadata.create_all(bind=engine) # Criação do banco de dados

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API Prontuário Médico",
        version="1.0.0",
        description="Desenvolvido por: Clayton Silva",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cdn-icons-png.flaticon.com/512/4140/4140047.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# IMPORTAR ROTAS
app.include_router(Especialidade.router)
app.include_router(Convenio.router)
app.include_router(Contato.router)
app.include_router(Medico.router)
app.include_router(Paciente.router)
app.include_router(Medicamento.router)
app.include_router(Consulta.router)
app.include_router(Receita.router)

# EXECUÇÃO DO SERVIDOR
app.openapi = custom_openapi
