from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session


# 
from model.models import Especialidade
from model.db import engine, Base, get_db
from controller.repositories import  EspecialidadeRepository
from controller.SchemasEspecialidade import EspecialidadeResponse


router = APIRouter()

# LISTAR ESPECIALIDADES
@router.get("/especialidade/", response_model=list[EspecialidadeResponse], tags=["Especialidade"]) # Listagem de todos os medicos
def listaEspecialidades(db: Session = Depends(get_db)):
    especialidade = EspecialidadeRepository.listaEspecialidades(db)
    return [EspecialidadeResponse.from_orm(especialidade) for especialidade in especialidade]


# LISTAR ESPECIALIDADES POR ID
@router.get("/especialidade/{id}", response_model=EspecialidadeResponse, tags=["Especialidade"]) # Listagem de todos os medicos
def listaEspecialidadesId(id: int, db: Session = Depends(get_db)):
    especialidade = EspecialidadeRepository.listaEspecialidadesId(db, id)
    if Especialidade is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Especialidade não encontrada")
    return EspecialidadeResponse.from_orm(especialidade)