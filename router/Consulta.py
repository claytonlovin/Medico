from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session


# 
from model.models import Consulta, Medicamento
from model.db import engine, Base, get_db
from controller.repositories import  ConsultaRepository
from controller.SchemasConsulta import ConsultaResponse, ConsultaRequest



router = APIRouter()

# LISTAR CONSULTAS
@router.get("/consulta/", response_model=list[ConsultaResponse], tags=["Consulta"]) # Listagem de todos os medicos
def listaConsultas(db: Session = Depends(get_db)):
    consulta = ConsultaRepository.listaConsultas(db)
    return [ConsultaResponse.from_orm(consulta) for consulta in consulta]

# LISTAR CONSULTAS POR ID
@router.get("/consulta/{id}", response_model=ConsultaResponse, tags=["Consulta"]) # Listagem de todos os medicos
def listaConsultasId(id: int, db: Session = Depends(get_db)):
    consulta = ConsultaRepository.listaConsultasId(db, id)
    if consulta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta não encontrada")
    return ConsultaResponse.from_orm(consulta)

# CADASTRAR CONSULTAS
@router.post("/consulta/", response_model=ConsultaResponse, tags=["Consulta"])
def cadastrarConsulta(consulta: ConsultaRequest, db: Session = Depends(get_db)):
    consulta = ConsultaRepository.create(db, Consulta(**consulta.dict()))
    return ConsultaResponse.from_orm(consulta)

# ATUALIZAR CONSULTAS
@router.put("/consulta/{id}", response_model=ConsultaResponse, tags=["Consulta"])
def atualizarConsulta(id: int, consulta: ConsultaRequest, db: Session = Depends(get_db)):
    consulta = ConsultaRepository.update(db, id)
    if consulta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta não encontrada")
    return ConsultaResponse.from_orm(consulta)


# DELETAR CONSULTAS
@router.delete("/consulta/{id}", response_model=ConsultaResponse, tags=["Consulta"])
def deletarConsulta(id: int, db: Session = Depends(get_db)):
    consulta = ConsultaRepository.delete(db, id)
    if consulta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta não encontrada")
    return ConsultaResponse.from_orm(consulta)
    