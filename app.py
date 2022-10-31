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

# POST /contato - Criação de um contato
@app.post("/contato/CriarContato", response_model=ContatoResponse, status_code=status.HTTP_201_CREATED) # Criação de um contato
def CriarContato(contato: ContatoRequest, db: Session = Depends(get_db)):
    db_contato = ContatoRepository.create(db, Contato(**contato.dict()))
    return ContatoResponse.from_orm(db_contato)
    

# PUT /contato/{id} - Atualização de um contato
@app.put("/contato/atualizarContato/{id}", response_model=ContatoResponse) # Atualização de um contato
def atualizarContato(id_contato: int, request: ContatoRequest, db: Session = Depends(get_db)):
    if not ContatoRepository.update(db, id_contato):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado"
        )
    contato = ContatoRepository.create(db,  Contato(id_contato = id_contato, **request.dict()))
    return ContatoResponse.from_orm(contato)

# DELETE /contato/{id} - Exclusão de um contato
@app.delete("/contato/deletarContato/{id}", status_code=status.HTTP_204_NO_CONTENT) # Deleção de um contato
def deletarContato(id_contato: int, db: Session = Depends(get_db)):
    if not ContatoRepository.delete(db, id_contato):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# EXECUÇÃO DO SERVIDOR
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)