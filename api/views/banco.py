from api.models import Banco
from api import schemas
from fastapi import HTTPException, APIRouter
from config import get_db


router = APIRouter(prefix='/bancos')


def get_many():
    with get_db() as db:
        return db.query(Banco).all()


def create(banco: schemas.Banco):
    with get_db() as db:
        try:
            db_banco = Banco(**banco.dict())
            db.add(db_banco)
            db.commit()
            db.refresh(db_banco)
            return db_banco
        except HTTPException as err:
            raise HTTPException(status_code=400, detail=err)
