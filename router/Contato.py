from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
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

router = APIRouter()


@router.get("/contato/", response_model=list[ContatoResponse], tags=["Contato"]) # Listagem de todos os contatos
def listaContatos(db: Session = Depends(get_db)):
    Contato = ContatoRepository.listaContatos(db)
    return [ContatoResponse.from_orm(contato) for contato in Contato]


@router.get("/contato/", response_model=list[ContatoResponse], tags=["Contato"]) # Listagem de todos os contatos
def listaContatos(db: Session = Depends(get_db)):
    Contato = ContatoRepository.listaContatos(db)
    return [ContatoResponse.from_orm(contato) for contato in Contato]
    
# GET /contato/{id} - Listagem de um contato específico
@router.get("/contato/{id}", response_model=ContatoResponse, tags=["Contato"]) # Listagem de um contato específico
def listaContatosId(id_contato: int, db: Session = Depends(get_db)):
    contato = ContatoRepository.listaContatosId(db, id_contato)
    if not contato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado")
    return ContatoResponse.from_orm(contato)

# POST /contato - Criação de um contato
@router.post("/contato/CriarContato", response_model=ContatoResponse, status_code=status.HTTP_201_CREATED, tags=["Contato"]) # Criação de um contato
def CriarContato(contato: ContatoRequest, db: Session = Depends(get_db)):
    db_contato = ContatoRepository.create(db, Contato(**contato.dict()))
    return ContatoResponse.from_orm(db_contato)
    

# PUT /contato/{id} - Atualização de um contato
@router.put("/contato/atualizarContato/{id}", response_model=ContatoResponse, tags=["Contato"]) # Atualização de um contato
def atualizarContato(id_contato: int, request: ContatoRequest, db: Session = Depends(get_db)):
    if not ContatoRepository.update(db, id_contato):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado"
        )
    contato = ContatoRepository.create(db,  Contato(id_contato = id_contato, **request.dict()))
    return ContatoResponse.from_orm(contato)

# DELETE /contato/{id} - Exclusão de um contato
@router.delete("/contato/deletarContato/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Contato"]) # Deleção de um contato
def deletarContato(id_contato: int, db: Session = Depends(get_db)):
    if not ContatoRepository.delete(db, id_contato):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
