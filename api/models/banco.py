from config import Base
# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER


class Banco(Base):
    __tablename__ = 'banco'

    id = Column(INTEGER(11), primary_key=True)
    nome = Column(String(20), nullable=False)
    agencia = Column(String(6), nullable=False)
    conta = Column(String(12), nullable=False)
