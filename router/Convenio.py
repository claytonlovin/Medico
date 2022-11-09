from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session



# 
from model.models import Convenio
from model.db import engine, Base, get_db
from controller.repositories import  ConvenioRepository
from controller.SchemasConvenio import ConvenioResponse

router = APIRouter()

# LISTAR CONVENIOS
@router.get("/convenio/", response_model=list[ConvenioResponse], tags=["Convenio"]) # Listagem de todos os medicos
def listaConvenios(db: Session = Depends(get_db)):
    convenio = ConvenioRepository.listaConvenios(db)
    return [ConvenioResponse.from_orm(convenio) for convenio in convenio]


# LISTAR CONVENIOS POR ID
@router.get("/convenio/{id}", response_model=ConvenioResponse, tags=["Convenio"]) # Listagem de todos os medicos
def listaConveniosId(id: int, db: Session = Depends(get_db)):
    convenio = ConvenioRepository.listaConveniosId(db, id)
    if Convenio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convenio não encontrado")
    return ConvenioResponse.from_orm(convenio)