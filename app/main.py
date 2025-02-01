from fastapi import FastAPI
from app.api.routers import router

app = FastAPI(
    title="Crypto Market API",
    description="Fetch cryptocurrency market updates from CoinGecko",
    version="1.0.0"
)

app.include_router(router)

@app.get("/", summary="Welcome")
def root():
    return {"message": "Welcome to the Crypto Market API!"}
