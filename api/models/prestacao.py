# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Index
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from config import Base


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
    valor_prestacao = Column(INTEGER(11), nullable=False)

    lancamento = relationship('Lancamento')
