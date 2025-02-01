from fastapi import APIRouter, Query
from app.services.coingecko import fetch_coins, fetch_coin_by_id

router = APIRouter()

@router.get("/", summary="List all coins", tags=["Coins"])
def get_coins(page_num: int = 1, per_page: int = 10):
    return fetch_coins(page_num, per_page)

@router.get("/{coin_id}", summary="Get specific coin", tags=["Coins"])
def get_coin(coin_id: str):
    return fetch_coin_by_id(coin_id)
