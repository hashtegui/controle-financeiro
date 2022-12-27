from fastapi import APIRouter
from typing import List
from api import schemas

router = APIRouter(prefix='/bancos')


@router.get('/bancos', response_model=List[schemas.Banco])
def get_bancos():
    bancos = banco.get_many()
    return bancos


@router.post('/bancos', response_model=schemas.Banco, status_code=201)
def post_banco(model: schemas.Banco):
    return banco.create(model)
