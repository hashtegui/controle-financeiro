from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/lancamentos')


@router.get('/')
async def get():
    return {'message': 'routes'}
