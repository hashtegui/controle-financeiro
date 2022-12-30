# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from config import Base


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

    banco = relationship('Banco', lazy='joined')
    cartao = relationship('Cartao', lazy='joined')
