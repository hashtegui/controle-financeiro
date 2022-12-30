from fastapi import APIRouter, HTTPException, status
from api import schemas
from api.views import cartao
from typing import List

router = APIRouter(prefix='/cartoes')


@router.get('/', response_model=List[schemas.CartaoSchema])
async def get():
    return cartao.get_all()


@router.post('/', response_model=schemas.CartaoSchema)
async def post(model: schemas.CartaoSchema):
    db_cartao = cartao.create(model)
    if db_cartao is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Não foi possivel criar o cartão')
    return db_cartao
