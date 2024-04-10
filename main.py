from fastapi import FastAPI

appTuto = FastAPI()


@appTuto.get("/items/{item_id}")
async def root():
    return {"message": "Hello World"}