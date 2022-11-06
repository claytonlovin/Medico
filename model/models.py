from datetime import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime
from sqlalchemy.orm import mapper
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from model.db import Base
    
    


class Contato(Base):
    __tablename__ = "contatos"

    id_contato = Column(Integer, primary_key=True, index=True, autoincrement=True)
    telefone = Column(String(11))
    email = Column(String(50))


class Medico(Base):
    __tablename__ = "medicos"

    id_medico = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    data_nascimento = Column(DateTime)
    cpf = Column(String(20))
    id_contato = Column(Integer, ForeignKey(Contato.id_contato))
    crm = Column(String(200))
    
class Paciente(Base):
    __tablename__ = "pacientes"

    id_paciente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    data_nascimento = Column(DateTime)
    cpf = Column(String(20))
    id_contato = Column(Integer, ForeignKey(Contato.id_contato))
    plano_saude = Column(String(200))

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id_medicamento = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    fabricante = Column(String(255))
    modo_de_uso = Column(String(255))

class Receita(Base):
    __tablename__ = "receitas"

    id_receita = Column(Integer, primary_key=True, index=True)
    id_medicamento = Column(Integer, ForeignKey(Medicamento.id_medicamento))
    id_paciente = Column(Integer, ForeignKey(Paciente.id_paciente))
    id_medico = Column(Integer, ForeignKey(Medico.id_medico))
    modo_de_uso = Column(String, nullable=False)

class Consulta(Base):
    __tablename__ = "consultas"

    id_consulta = Column(Integer, primary_key=True, index=True)
    id_medico = Column(Integer, ForeignKey(Medico.id_medico))
    id_paciente = Column(Integer, ForeignKey(Paciente.id_paciente))
    data_consulta = Column(String, nullable=False)
    data_retorno = Column(String, nullable=True)
    id_receita = Column(Integer, ForeignKey(Receita.id_receita))
