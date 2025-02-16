'''Secret keys for authentication (JWT tokens, API keys, etc.).
Debug mode settings.
Third-party service credentials (e.g., Google Maps API keys).'''

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:123456789@postgres_db:5432/mydb"
    #DATABASE_URL: str = "postgresql://postgres:123456789@localhost:5433/mydb"
    #DATABASE_URL: str = "postgresql://myuser:mypassword@localhost:5432/mydb"
    DEBUG_MODE: bool = True  # Enable debugging mode

    class Config:
        env_file = ".env"  # Load from .env file if available

# Create a settings instance that can be used in the app
settings = Settings()