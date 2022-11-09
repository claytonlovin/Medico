from pydantic import BaseModel


class EspcialidadeBase(BaseModel):
    nome: str

class EspecialidadeResponse(EspcialidadeBase):
    id_especialidade: int

    class Config:
        orm_mode = True

class EspecialidadeRequest(EspcialidadeBase):
    pass