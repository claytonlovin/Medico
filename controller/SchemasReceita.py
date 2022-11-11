from pydantic import BaseModel


class ReceitaBase(BaseModel):
    id_medicamento: int
    id_paciente: int
    id_medico: int
    id_consulta: int
    modo_de_uso: str

class ReceitaResponse(ReceitaBase):
    id_receita: int

    class Config:
        orm_mode = True

class ReceitaRequest (ReceitaBase):
    pass