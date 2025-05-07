from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/v1")

@app.get("/")
def read_root():    
    return {"message": "FastAPI funcionando como un cohete 🚀"}
