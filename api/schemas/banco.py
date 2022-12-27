from pydantic import BaseModel, Field, constr
from typing import Optional


class BaseConfig(BaseModel):
    class Config:
        orm_mode = True


class Banco(BaseConfig):
    id: Optional[int]
    nome: str = Field(constr(max_length=20))
    agencia: str
    conta: str
