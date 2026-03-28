from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", frozen=True
    )
    DB: PostgresDsn = PostgresDsn("postgresql+asyncpg://postgres:@localhost:5432")

    @field_validator("DB")
    @classmethod
    def validate_db_connection(cls, value):
        assert value.path and len(value.path) > 1, "database must be provided"
        return value


settings = Settings()
