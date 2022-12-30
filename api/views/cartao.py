from config import get_db
from api.schemas import CartaoSchema
from api.models import Cartao, Banco
from typing import List


def create(cartao: CartaoSchema):
    with get_db() as db:
        try:
            banco: Banco = db.get(Banco, cartao.id_banco)
            db_cartao = Cartao(digitos=cartao.digitos,
                               obs=cartao.obs,
                               banco=banco)
            db.add(db_cartao)
            db.commit()
            db.refresh(db_cartao)
            return db_cartao
        except Exception as err:
            db.rollback()
            print(err)


def get_all() -> List[Cartao]:
    with get_db() as db:
        result = db.query(Cartao).all()
        return result
