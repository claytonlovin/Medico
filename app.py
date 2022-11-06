from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI as MedicoAPI
from sqlalchemy.orm import Session
import uvicorn

# 
from model.models import Contato, Medico
from model.db import engine, Base, get_db
from controller.repositories import ContatoRepository, MedicoRepository
from controller.SchemasContato import ContatoResponse, ContatoRequest

from controller.SchemasMedico import MedicoResponse, MedicoRequest
from router import Contato, Medico


Base.metadata.create_all(bind=engine) # Criação do banco de dados

app = MedicoAPI()

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
app.include_router(Contato.router)
app.include_router(Medico.router)

# EXECUÇÃO DO SERVIDOR
app.openapi = custom_openapi

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)