from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session

from model.models import Paciente
from model.db import engine, Base, get_db
from controller.repositories import  PacienteRepository
from controller.SchemasPaciente import PacienteResponse, PacienteRequest


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

# CADASTRAR PACIENTE
@router.post("/paciente/criarPaciente", response_model=PacienteResponse, status_code=status.HTTP_201_CREATED,  tags=["Paciente"]) # Cadastro de um paciente
def cadastraPaciente(paciente: PacienteRequest, db: Session = Depends(get_db)):
    paciente = PacienteRepository.create(db, Paciente(**paciente.dict()))
    return PacienteResponse.from_orm(paciente)

# ATUALIZAR PACIENTE
@router.put("/paciente/{id_paciente}", response_model=PacienteResponse, tags=["Paciente"]) # Atualização de um paciente
def atualizaPaciente(id_paciente: int, paciente: PacienteRequest, db: Session = Depends(get_db)):
    Paciente = PacienteRepository.listaPacientePorId(id_paciente, db)
    if Paciente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
    Paciente = PacienteRepository.update(db, Paciente, **paciente.dict())
    return PacienteResponse.from_orm(Paciente)


# DELETAR PACIENTE
@router.delete("/paciente/{id_paciente}", status_code=status.HTTP_204_NO_CONTENT, tags=["Paciente"]) # Deletar um paciente
def deletaPaciente(id_paciente: int, db: Session = Depends(get_db)):
    Paciente = PacienteRepository.listaPacientePorId(id_paciente, db)
    if Paciente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
    PacienteRepository.delete(db, Paciente)




