# app/api/v1/endpoints/ping.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def ping():
    return {"status": "ok"}
