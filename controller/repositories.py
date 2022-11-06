
from sqlalchemy.orm import Session
from model.models import Medico, Paciente, Contato, Medicamento, Receita, Consulta


class ContatoRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaContatos(db: Session) -> list[Contato]:
        return db.query(Contato).all()
    # 
    @staticmethod
    def listaContatosId(db: Session, id: int) -> Contato:
        return db.query(Contato).filter(Contato.id_contato == id).first()
    # Criação de um contato
    @staticmethod
    def create(db: Session, contato: Contato) -> Contato:
        if contato.id_contato:
            db.merge(Contato)
        else:
            db.add(contato)
        db.commit()
        return contato
    
    @staticmethod
    def update(db: Session, id_contato: int) -> bool:
        return db.query(Contato).filter(Contato.id_contato == id_contato).first() is not None

    @staticmethod
    def delete(db: Session, id_contato: int) -> bool:
        contato = db.query(Contato).filter(Contato.id_contato == id_contato).first()
        if contato:
            db.delete(contato)
            db.commit()
            return True
        return False
