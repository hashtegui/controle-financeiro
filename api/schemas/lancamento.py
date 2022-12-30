from config import BaseConfig
from datetime import date, datetime
from . import BancoSchema, CartaoSchema


class LancamentoSchema(BaseConfig):
    id: int | None
    valor: float
    dt_inclusao: datetime | None
    dt_ultater: datetime | None
    parcelas: int
    id_banco: int | None
    id_cartao: int | None
    obs: str

    banco: BancoSchema | None
    cartao: CartaoSchema | None


class CreateLancamento(BaseConfig):
    valor: float
    parcelas: float
    id_banco: int | None
    id_cartao: int | None
    obs: str
