import requests
from app.core.config import settings

COINGECKO_API = settings.COINGECKO_API

def fetch_coins(page_num: int = 1, per_page: int = 10):
    """Fetches a paginated list of coins."""
    url = f"{COINGECKO_API}/coins/markets"
    params = {"vs_currency": "cad", "page": page_num, "per_page": per_page}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def fetch_categories():
    """Fetches cryptocurrency categories."""
    url = f"{COINGECKO_API}/coins/categories/list"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_coin_by_id(coin_id: str):
    """Fetches details of a specific coin."""
    url = f"{COINGECKO_API}/coins/{coin_id}"
    params = {"localization": "false", "tickers": "false", "market_data": "true"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
