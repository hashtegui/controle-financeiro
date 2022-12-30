from fastapi import APIRouter
from typing import List
from api import schemas
from api.views import banco

router = APIRouter(prefix='/bancos')


@router.get('/', response_model=List[schemas.BancoSchema])
async def get_bancos():
    bancos = banco.get_many()
    return bancos


@router.post('/', response_model=schemas.BancoSchema, status_code=201)
async def post_banco(model: schemas.BancoSchema):
    return banco.create(model)
