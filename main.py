from fastapi import FastAPI
from api.routers import BancoRouter, CartaoRouter


app = FastAPI()

app.include_router(BancoRouter)
app.include_router(CartaoRouter)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, port=8000, host='0.0.0.0')
