
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


class MedicoRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaMedicos(db: Session) -> list[Medico]:
        return db.query(Medico).all()
    # 
    @staticmethod
    def listaMedicosId(db: Session, id: int) -> Medico:
        return db.query(Medico).filter(Medico.id_medico == id).first()
    # Criação de um médico
    @staticmethod
    def create(db: Session, medico: Medico) -> Medico:
        if medico.id_medico:
            db.merge(Medico)
        else:
            db.add(medico)
        db.commit()
        return medico
    
    @staticmethod
    def update(db: Session, id_medico: int) -> bool:
        return db.query(Medico).filter(Medico.id_medico == id_medico).first() is not None

    @staticmethod
    def delete(db: Session, id_medico: int) -> bool:
        medico = db.query(Medico).filter(Medico.id_medico == id_medico).first()
        if medico:
            db.delete(medico)
            db.commit()
            return True
        return False


# Paciente
class PacienteRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaPacientes(db: Session) -> list[Paciente]:
        return db.query(Paciente).all()
    # 
    @staticmethod
    def listaPacientesId(db: Session, id: int) -> Paciente:
        return db.query(Paciente).filter(Paciente.id_paciente == id).first()
    # Criação de um paciente
    @staticmethod
    def create(db: Session, paciente: Paciente) -> Paciente:
        if paciente.id_paciente:
            db.merge(Paciente)
        else:
            db.add(paciente)
        db.commit()
        return paciente
    
    @staticmethod
    def update(db: Session, id_paciente: int) -> bool:
        return db.query(Paciente).filter(Paciente.id_paciente == id_paciente).first() is not None

    @staticmethod
    def delete(db: Session, id_paciente: int) -> bool:
        paciente = db.query(Paciente).filter(Paciente.id_paciente == id_paciente).first()
        if paciente:
            db.delete(paciente)
            db.commit()
            return True
        return False