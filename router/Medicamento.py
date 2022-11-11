from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session


# 
from model.models import Medicamento
from model.db import engine, Base, get_db
from controller.repositories import  MedicamentoRepository
from controller.SchemasMedicamento import MedicamentoResponse, MedicamentoRequest


router = APIRouter()

# LISTAR MEDICAMENTOS
@router.get("/medicamento/", response_model=list[MedicamentoResponse], tags=["Medicamento"]) # Listagem de todos os medicos
def listaMedicamentos(db: Session = Depends(get_db)):
    medicamento = MedicamentoRepository.listaMedicamentos(db)
    return [MedicamentoResponse.from_orm(medicamento) for medicamento in medicamento]


# LISTAR MEDICAMENTOS POR ID
@router.get("/medicamento/{id}", response_model=MedicamentoResponse, tags=["Medicamento"]) # Listagem de todos os medicos
def listaMedicamentosId(id: int, db: Session = Depends(get_db)):
    medicamento = MedicamentoRepository.listaMedicamentosId(db, id)
    if Medicamento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento não encontrado")
    return MedicamentoResponse.from_orm(medicamento)


# CRIAR MEDICAMENTO
@router.post("/medicamento/", response_model=MedicamentoResponse, tags=["Medicamento"])
async def createMedicamento(medicamento: MedicamentoRequest, db: Session = Depends(get_db)):
    medicamento = MedicamentoRepository.create(db, Medicamento(**medicamento.dict()))
    return MedicamentoResponse.from_orm(medicamento)

# ATUALIZAR MEDICAMENTO
@router.put("/medicamento/{id}", response_model=MedicamentoResponse, tags=["Medicamento"])
async def updateMedicamento(id: int, medicamento: MedicamentoRequest, db: Session = Depends(get_db)):
    medicamento = MedicamentoRepository.update(db, id, Medicamento(**medicamento.dict()))
    if medicamento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento não encontrado")
    return MedicamentoResponse.from_orm(medicamento)


# DELETAR MEDICAMENTO
@router.delete("/medicamento/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Medicamento"])
def deleteMedicamento(id: int, db: Session = Depends(get_db)):
    if not MedicamentoRepository.delete(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento não encontrado")
    return Response(status_code=status.HTTP_204_NO_CONTENT)