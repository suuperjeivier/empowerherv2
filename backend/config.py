from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator, ValidationError
from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    model_config = SettingsConfigDict(env_file=".env")
    
    @field_validator('SECRET_KEY')
    @classmethod
    def validate_secret_key(cls, v: str) -> str:
        if len(v) < 32:
            raise ValueError('SECRET_KEY must be at least 32 characters long for security')
        return v
    
    @field_validator('DATABASE_URL')
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        if not v.startswith(('postgresql://', 'postgresql+psycopg2://', 'sqlite://')):
            raise ValueError('DATABASE_URL must start with a valid database scheme (postgresql://, postgresql+psycopg2://, or sqlite://)')
        return v


settings = Settings()  # type: ignore[call-arg]

# Made with Bob
