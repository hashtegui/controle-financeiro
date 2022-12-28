from api.models import Banco
from api.schemas import banco
from fastapi import HTTPException
from config import get_db


def get_many():
    with get_db() as db:
        return db.query(Banco).all()


def create(banco: banco.BancoSchema):
    with get_db() as db:
        try:
            db_banco = Banco(**banco.dict())
            db.add(db_banco)
            db.commit()
            db.refresh(db_banco)
            return db_banco
        except Exception as err:
            raise HTTPException(status_code=400, detail=err)
