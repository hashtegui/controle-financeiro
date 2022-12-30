from config import get_db
from api.schemas.lancamento import LancamentoSchema, CreateLancamento
from api.models.lancamento import Lancamento
from api.models.banco import Banco
from api.models.cartao import Cartao


def create(lanc: CreateLancamento) -> LancamentoSchema | None:
    with get_db() as db:
        try:
            db_lanc = Lancamento(**lanc.dict())

            if lanc.id_banco:
                db_lanc.banco = db.get(Banco, lanc.id_banco)

            elif lanc.id_cartao:
                db_lanc.cartao = db.get(Cartao, lanc.id_cartao)

            db.add(db_lanc)

            db.commit()
            db.refresh(db_lanc)

            return db_lanc
        except Exception as err:
            db.rollback()
            print(err)
            return None


def get_all():
    with get_db() as db:
        return db.query(Lancamento).order_by(Lancamento.id).all()
