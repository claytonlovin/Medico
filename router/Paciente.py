from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session

from model.models import Paciente
from model.db import  get_db
from controller.repositories import  PacienteRepository
from controller.SchemasPaciente import PacienteResponse

router = APIRouter()


# LISTAR PACIENTES
@router.get("/paciente/", response_model=list[PacienteResponse], tags=["Paciente"]) # Listagem de todos os pacientes
def listaPacientes(db: Session = Depends(get_db)):
    Paciente = PacienteRepository.listaPacientes(db)
    return [PacienteResponse.from_orm(paciente) for paciente in Paciente]

# LISTAR PACIENTE POR ID
@router.get("/paciente/{id_paciente}", response_model=PacienteResponse, tags=["Paciente"]) # Listagem de um paciente por id
def listaPacientePorId(id_paciente: int, db: Session = Depends(get_db)):
    Paciente = PacienteRepository.listaPacientePorId(id_paciente, db)
    if Paciente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
    return PacienteResponse.from_orm(Paciente)