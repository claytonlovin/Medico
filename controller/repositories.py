
from sqlalchemy.orm import Session
from model.models import Medico, Paciente, Contato, Medicamento, Receita, Consulta, Especialidade, Convenio


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

class EspecialidadeRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaEspecialidades(db: Session) -> list[Especialidade]:
        return db.query(Especialidade).all()
    # 
    @staticmethod
    def listaEspecialidadesId(db: Session, id: int) -> Especialidade:
        return db.query(Especialidade).filter(Especialidade.id_especialidade == id).first()

class ConvenioRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaConvenios(db: Session) -> list[Convenio]:
        return db.query(Convenio).all()
    # 
    @staticmethod
    def listaConveniosId(db: Session, id: int) -> Convenio:
        return db.query(Convenio).filter(Convenio.id_convenio == id).first()

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



# Medicamento
class MedicamentoRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaMedicamentos(db: Session) -> list[Medicamento]:
        return db.query(Medicamento).all()
    # 
    @staticmethod
    def listaMedicamentosId(db: Session, id: int) -> Medicamento:
        return db.query(Medicamento).filter(Medicamento.id_medicamento == id).first()
    # Criação de um medicamento
    @staticmethod
    def create(db: Session, medicamento: Medicamento) -> Medicamento:
        if medicamento.id_medicamento:
            db.merge(Medicamento)
        else:
            db.add(medicamento)
        db.commit()
        return medicamento
    
    @staticmethod
    def update(db: Session, id_medicamento: int) -> bool:
        return db.query(Medicamento).filter(Medicamento.id_medicamento == id_medicamento).first() is not None

    @staticmethod
    def delete(db: Session, id_medicamento: int) -> bool:
        medicamento = db.query(Medicamento).filter(Medicamento.id_medicamento == id_medicamento).first()
        if medicamento:
            db.delete(medicamento)
            db.commit()
            return True
        return False


# consulta

class ConsultaRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaConsultas(db: Session) -> list[Consulta]:
        return db.query(Consulta).all()
    # 
    @staticmethod
    def listaConsultasId(db: Session, id: int) -> Consulta:
        return db.query(Consulta).filter(Consulta.id_consulta == id).first()
    # Criação de um consulta
    @staticmethod
    def create(db: Session, consulta: Consulta) -> Consulta:
        if consulta.id_consulta:
            db.merge(Consulta)
        else:
            db.add(consulta)
        db.commit()
        return consulta
    
    @staticmethod
    def update(db: Session, id_consulta: int) -> bool:
        return db.query(Consulta).filter(Consulta.id_consulta == id_consulta).first() is not None

    @staticmethod
    def delete(db: Session, id_consulta: int) -> bool:
        consulta = db.query(Consulta).filter(Consulta.id_consulta == id_consulta).first()
        if consulta:
            db.delete(consulta)
            db.commit()
            return True
        return False


# Receita
class ReceitaRepository:
    @staticmethod
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def listaReceitas(db: Session) -> list[Receita]:
        return db.query(Receita).all()
    # 
    @staticmethod
    def listaReceitasId(db: Session, id: int) -> Receita:
        return db.query(Receita).filter(Receita.id_receita == id).first()
    # Criação de um receita
    @staticmethod
    def create(db: Session, receita: Receita) -> Receita:
        if receita.id_receita:
            db.merge(Receita)
        else:
            db.add(receita)
        db.commit()
        return receita
    
    @staticmethod
    def update(db: Session, id_receita: int) -> bool:
        return db.query(Receita).filter(Receita.id_receita == id_receita).first() is not None

    @staticmethod
    def delete(db: Session, id_receita: int) -> bool:
        receita = db.query(Receita).filter(Receita.id_receita == id_receita).first()
        if receita:
            db.delete(receita)
            db.commit()
            return True
        return False