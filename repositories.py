
from sqlalchemy.orm import Session
from models import Medico, Paciente, Contato, Medicamento, Receita, Consulta


class ContatoRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaContatos(db: Session) -> list[Contato]:
        return db.query(Contato).all()

    @staticmethod
    def listaContatosId(db: Session, id: int) -> Contato:
        return db.query(Contato).filter(Contato.id_contato == id).first()

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

class MedicoRepository:

    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def get_medico(db: Session, id_medico: int):
        return db.query(Medico).filter(Medico.id_medico == id_medico).first()

    @staticmethod
    def create_medico(db: Session, medico: Medico):
        db_medico = Medico(**medico.dict())
        db.add(db_medico)
        db.commit()
        db.refresh(db_medico)
        return db_medico

    @staticmethod
    def update_medico(db: Session, medico: Medico):
        db_medico = Medico(**medico.dict())
        db.add(db_medico)
        db.commit()
        db.refresh(db_medico)
        return db_medico

    @staticmethod
    def delete_medico(db: Session, id_medico: int):
        db.query(Medico).filter(Medico.id_medico == id_medico).delete()
        db.commit()