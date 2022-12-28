from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from config import Base


class Cartao(Base):
    __tablename__ = 'cartao'

    id = Column(INTEGER(11), primary_key=True)
    digitos = Column(INTEGER(5), nullable=False)
    obs = Column(String(50))
    id_banco = Column(ForeignKey('banco.id'), index=True)

    banco = relationship('Banco', lazy='joined')

    def __repr__(self) -> str:
        return f'Cartao<{self.id} + {self.__class__}>'
