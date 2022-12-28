from fastapi import APIRouter, HTTPException, status
from api.schemas import CartaoSchema
from api.views import cartao

router = APIRouter(prefix='/cartoes')


@router.get('/')
def get():
    return {'message': 'Cartao route'}


@router.post('/', response_model=CartaoSchema)
def post(model: CartaoSchema):
    db_cartao = cartao.create(model)
    if db_cartao is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Não foi possivel criar o cartão')
    return db_cartao
