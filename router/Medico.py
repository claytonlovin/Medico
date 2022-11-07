from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session


# 
from model.models import Medico
from model.db import engine, Base, get_db
from controller.repositories import  MedicoRepository
from controller.SchemasMedico import MedicoResponse, MedicoRequest

router = APIRouter()

# LISTAR MEDICOS

@router.get("/medico/", response_model=list[MedicoResponse], tags=["Medico"]) # Listagem de todos os medicos
def listaMedicos(db: Session = Depends(get_db)):
    Medico = MedicoRepository.listaMedicos(db)
    return [MedicoResponse.from_orm(medico) for medico in Medico]
    
# GET /medico/{id} - Listagem de um medico específico
@router.get("/medico/{id}", response_model=MedicoResponse, tags=["Medico"]) # Listagem de um medico específico
def listaMedicosId(id_medico: int, db: Session = Depends(get_db)):
    medico = MedicoRepository.listaMedicosId(db, id_medico)
    if not medico:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medico não encontrado")
    return MedicoResponse.from_orm(medico)

# POST /medico - Criação de um medico
@router.post("/medico/CriarMedico", response_model=MedicoResponse, status_code=status.HTTP_201_CREATED, tags=["Medico"]) # Criação de um medico
def CriarMedico(medico: MedicoRequest, db: Session = Depends(get_db)):
    db_medico = MedicoRepository.create(db, Medico(**medico.dict()))
    return MedicoResponse.from_orm(db_medico)

# PUT /medico/{id} - Atualização de um medico
@router.put("/medico/atualizarMedico/{id}", response_model=MedicoResponse, tags=["Medico"]) # Atualização de um medico
def atualizarMedico(id_medico: int, request: MedicoRequest, db: Session = Depends(get_db)):
    if not MedicoRepository.update(db, id_medico):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Medico não encontrado"
        )
    medico = MedicoRepository.create(db,  Medico(id_medico = id_medico, **request.dict()))
    return MedicoResponse.from_orm(medico)

# DELETE /medico/{id} - Exclusão de um medico
@router.delete("/medico/deletarMedico/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Medico"]) # Deleção de um medico
def deletarMedico(id_medico: int, db: Session = Depends(get_db)):
    if not MedicoRepository.delete(db, id_medico):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Medico não encontrado"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
