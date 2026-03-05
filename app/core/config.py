from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Incident Tracker API"
    database_url: str = "sqlite:///./local.db"

    class Config:
        env_file = ".env"


settings = Settings()