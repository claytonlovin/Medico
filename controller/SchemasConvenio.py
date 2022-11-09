from pydantic import BaseModel


class ConvenioBase(BaseModel):
    nome: str

class ConvenioResponse(ConvenioBase):
    id_convenio: int

    class Config:
        orm_mode = True