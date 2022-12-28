from api.schemas.banco import BancoSchema
from config import BaseConfig


class CartaoSchema(BaseConfig):
    id: int | None
    digitos: int
    obs: str | None
    id_banco: int | None
    banco: BancoSchema | None
