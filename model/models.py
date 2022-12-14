from datetime import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime
from sqlalchemy.orm import mapper
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from model.db import Base
    

class Contato(Base):
    __tablename__ = "contatos"

    id_contato = Column(Integer, primary_key=True, index=True, autoincrement=True)
    telefone = Column(String(11), nullable=False, unique=True)
    email = Column(String(50), unique=True)


class Medico(Base):
    __tablename__ = "medicos"

    id_medico = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    data_nascimento = Column(DateTime)
    cpf = Column(String(20), nullable=False, unique=True)
    id_contato = Column(Integer, ForeignKey(Contato.id_contato), nullable=False)
    crm = Column(String(200))

class Especialidade(Base):
    __tablename__ = "especialidades"

    id_especialidade = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))

class Convenio(Base):
    __tablename__ = "convenios"

    id_convenio = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))

class Paciente(Base):
    __tablename__ = "pacientes"

    id_paciente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    data_nascimento = Column(DateTime)
    cpf = Column(String(20), nullable=False, unique=True)
    id_contato = Column(Integer, ForeignKey(Contato.id_contato), nullable=False)
    plano_saude = Column(String(200))
 
class Medicamento(Base):
    __tablename__ = "medicamentos"

    id_medicamento = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False, unique=True)
    fabricante = Column(String(255))
    modo_de_uso = Column(String(255))

class Consulta(Base):
    __tablename__ = "consultas"

    id_consulta = Column(Integer, primary_key=True, index=True)
    id_medico = Column(Integer, ForeignKey(Medico.id_medico), nullable=False)
    id_paciente = Column(Integer, ForeignKey(Paciente.id_paciente), nullable=False)
    data_consulta = Column(String, nullable=False)
    data_retorno = Column(String, nullable=True)
#    id_covenio = Column(Integer, ForeignKey(Convenio.id_convenio), nullable=True)
    id_especialidade = Column(Integer, ForeignKey(Especialidade.id_especialidade), nullable=False)

class Receita(Base):
    __tablename__ = "receitas"
 
    id_receita = Column(Integer, primary_key=True, index=True)
    id_medicamento = Column(Integer, ForeignKey(Medicamento.id_medicamento), nullable=False)
    id_paciente = Column(Integer, ForeignKey(Paciente.id_paciente), nullable=False)
    id_medico = Column(Integer, ForeignKey(Medico.id_medico), nullable=False)
    id_consulta = Column(Integer, ForeignKey(Consulta.id_consulta), nullable=False)
    modo_de_uso = Column(String, nullable=False)

