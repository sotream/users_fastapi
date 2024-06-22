from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://sotream:dS0zr52uB2f2@localhost:5433/sotream"

settings = Settings()
