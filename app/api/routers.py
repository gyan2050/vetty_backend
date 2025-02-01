from fastapi import APIRouter
from app.api.endpoints import coins, categories

router = APIRouter()

router.include_router(coins.router, prefix="/coins")
router.include_router(categories.router, prefix="/categories")
