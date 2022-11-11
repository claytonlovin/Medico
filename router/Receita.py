from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session


# 
from model.models import Receita
from model.db import engine, Base, get_db
from controller.repositories import  ReceitaRepository
from controller.SchemasReceita import ReceitaResponse, ReceitaRequest


router = APIRouter()

# LISTAR RECEITAS
@router.get("/receita/", response_model=list[ReceitaResponse], tags=["Receita"]) # Listagem de todos os medicos
def listaReceitas(db: Session = Depends(get_db)):
    receita = ReceitaRepository.listaReceitas(db)
    return [ReceitaResponse.from_orm(receita) for receita in receita]


# LISTAR RECEITAS POR ID
@router.get("/receita/{id}", response_model=ReceitaResponse, tags=["Receita"]) # Listagem de todos os medicos
def listaReceitasId(id: int, db: Session = Depends(get_db)):
    receita = ReceitaRepository.listaReceitasId(db, id)
    if receita is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    return ReceitaResponse.from_orm(receita)


# CRIAR RECEITA
@router.post("/receita/", response_model=ReceitaResponse, tags=["Receita"])
def createReceita(receita: ReceitaRequest, db: Session = Depends(get_db)):
    receita = ReceitaRepository.create(db, Receita(**receita.dict()))
    return ReceitaResponse.from_orm(receita)


# ATUALIZAR RECEITA
@router.put("/receita/{id}", response_model=ReceitaResponse, tags=["Receita"])
def updateReceita(id: int, receita: ReceitaRequest, db: Session = Depends(get_db)):
    if not ReceitaRepository.update(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    receita = ReceitaRepository.create(db, Receita(id_receita=id, **receita.dict()))
    return ReceitaResponse.from_orm(receita)


# DELETAR RECEITA
@router.delete("/receita/{id}", response_model=ReceitaResponse, tags=["Receita"])
def deleteReceita(id: int, db: Session = Depends(get_db)):
    if not ReceitaRepository.delete(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    