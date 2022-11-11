from pydantic import BaseModel

class ConsultaBase(BaseModel):
    id_medico: int
    id_paciente: int
    data_consulta: str
    data_retorno: str
    id_especialidade: int

class ConsultaResponse(ConsultaBase):
    id_consulta: int

    class Config:
        orm_mode = True

class ConsultaRequest(ConsultaBase):
    pass