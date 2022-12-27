# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Banco(Base):
    __tablename__ = 'banco'

    id = Column(INTEGER(11), primary_key=True)
    nome = Column(String(20), nullable=False)
    agencia = Column(String(6), nullable=False)
    conta = Column(String(12), nullable=False)


class Cartao(Base):
    __tablename__ = 'cartao'

    id = Column(INTEGER(11), primary_key=True)
    digitos = Column(INTEGER(5), nullable=False)
    obs = Column(String(50))
    id_banco = Column(ForeignKey('banco.id'), index=True)

    banco = relationship('Banco')


class Lancamento(Base):
    __tablename__ = 'lancamento'

    id = Column(INTEGER(11), primary_key=True)
    valor = Column(Float(asdecimal=True), nullable=False)
    dt_inclusao = Column(TIMESTAMP, nullable=False,
                         server_default=text("CURRENT_TIMESTAMP"))
    dt_ultater = Column(TIMESTAMP)
    parcelas = Column(INTEGER(11), nullable=False)
    id_banco = Column(ForeignKey('banco.id'), index=True)
    id_cartao = Column(ForeignKey('cartao.id'), index=True)
    obs = Column(String(20))

    banco = relationship('Banco')
    cartao = relationship('Cartao')


class Prestacao(Base):
    __tablename__ = 'prestacao'
    __table_args__ = (
        Index('parcela_lanc', 'parcela', 'id_lancamento', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    parcela = Column(INTEGER(11), nullable=False)
    id_lancamento = Column(ForeignKey('lancamento.id'),
                           nullable=False, index=True)
    dt_vencimento = Column(Date, nullable=False)

    lancamento = relationship('Lancamento')
