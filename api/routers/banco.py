from fastapi import APIRouter
from typing import List
from api.schemas.banco import BancoSchema
from api.views import banco

router = APIRouter(prefix='/bancos')


@router.get('/', response_model=List[BancoSchema])
async def get_bancos():
    bancos = banco.get_many()
    return bancos


@router.post('/', response_model=BancoSchema, status_code=201)
async def post_banco(model: BancoSchema):
    return banco.create(model)
