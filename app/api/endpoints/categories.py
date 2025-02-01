from fastapi import APIRouter
from app.services.coingecko import fetch_categories

router = APIRouter()

@router.get("/", summary="List all coin categories", tags=["Categories"])
def get_categories():
    return fetch_categories()
