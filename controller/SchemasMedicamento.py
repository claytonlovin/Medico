from pydantic import BaseModel

class MedicamentoBase(BaseModel):
    nome: str
    fabricante: str
    modo_de_uso: str

class MedicamentoResponse(MedicamentoBase):
    id_medicamento: int

    class Config:
        orm_mode = True

class MedicamentoRequest(MedicamentoBase):
    pass