from xmlrpc.client import DateTime
from pydantic import BaseModel

class MedicoBase(BaseModel):
    nome: str
    cpf: str
    id_contato: int
    crm: str
    

class MedicoResponse(MedicoBase):
    id_medico: int

    class Config:
        orm_mode = True

class MedicoRequest(MedicoBase):
    ...
