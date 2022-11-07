from pydantic import BaseModel

class PacienteBase(BaseModel):
    nome: str
    data_nascimento: str
    cpf: str
    id_contato: int
    plano_saude: str

class PacienteResponse(PacienteBase):
    id_paciente: int

    class Config:
        orm_mode = True

class PacienteRequest(PacienteBase):
    pass

# Path: controller\SchemasPaciente.py