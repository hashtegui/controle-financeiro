from config import get_db
from api.schemas import CartaoSchema
from api.models import Cartao


def create(cartao: CartaoSchema):
    with get_db() as db:
        try:
            db_cartao = Cartao(**cartao.dict())
            db.add(db_cartao)
            db.commit()
            db.refresh(db_cartao)
            return db_cartao
        except Exception as err:
            db.rollback()
            print(err)
