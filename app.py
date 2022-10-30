from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session


from models import Contato
from db import engine, Base, get_db
from repositories import ContatoRepository
from schemas import ContatoResponse, ContatoRequest
import uvicorn

Base.metadata.create_all(bind=engine) # Criação do banco de dados


app = FastAPI()

@app.get("/contato/", response_model=list[ContatoResponse]) # Listagem de todos os contatos
def listaContatos(db: Session = Depends(get_db)):
    Contato = ContatoRepository.listaContatos(db)
    return [ContatoResponse.from_orm(contato) for contato in Contato]
    
# GET /contato/{id} - Listagem de um contato específico
@app.get("/contato/{id}", response_model=ContatoResponse) # Listagem de um contato específico
def listaContatosId(id_contato: int, db: Session = Depends(get_db)):
    contato = ContatoRepository.listaContatosId(db, id_contato)
    if not contato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado")
    return ContatoResponse.from_orm(contato)


# EXECUÇÃO DO SERVIDOR
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, workers=True, debug=True)