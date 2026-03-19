from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()