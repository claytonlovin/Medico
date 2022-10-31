from pydantic import BaseModel

class ConatoBase(BaseModel):
    telefone: str
    email: str

class ContatoResponse(ConatoBase):
    id_contato: int

    class Config:
        orm_mode = True

class ContatoRequest(ConatoBase):
    ...
