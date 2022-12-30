from fastapi import APIRouter, HTTPException, status
from api.views import lancamento
from api.schemas.lancamento import CreateLancamento, LancamentoSchema
from typing import List

router = APIRouter(prefix='/lancamentos')


@router.get('/', response_model=List[LancamentoSchema])
async def get():
    return lancamento.get_all()


@router.post('/')
async def create(model: CreateLancamento):
    db_lanc = lancamento.create(model)

    if db_lanc is not None:
        return db_lanc

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Não foi possivel cadastrar o lancamento')
