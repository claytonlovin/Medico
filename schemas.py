from pydantic import BaseModel

class ConatoBase(BaseModel):
    telefone: str
    email: str
    
class ContatoRequest(ConatoBase):
    pass

    class Config:
        orm_mode = True

class ContatoResponse(ConatoBase):
    id_contato: int

    class Config:
        orm_mode = True
