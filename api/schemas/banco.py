from pydantic import Field, constr
from typing import Optional
from config import BaseConfig


class BancoSchema(BaseConfig):
    id: Optional[int]
    nome: str = Field(constr(max_length=20))
    agencia: str
    conta: str
