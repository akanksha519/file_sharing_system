from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your_secret_key"
    DATABASE_URL: str = "sqlite:///./test.db"
    EMAIL_API_KEY: str = "your_email_api_key"
    UPLOAD_FOLDER: str = "./uploads"

    class Config:
        env_file = ".env"

settings = Settings()
