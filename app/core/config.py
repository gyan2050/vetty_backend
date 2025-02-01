from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your_secret_key"
    COINGECKO_API: str = "https://api.coingecko.com/api/v3"

    class Config:
        env_file = ".env"

settings = Settings()

