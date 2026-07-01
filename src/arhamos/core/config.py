from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    OLLAMA_BASE_URL: str
    OLLAMA_MODEL: str
    OLLAMA_API_KEY: str


settings = Settings()