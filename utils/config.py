from pydantic import BaseSettings


class Settings(BaseSettings):
    USER_EMAIL: str
    USER_PASSWORD: str
    APPIUM_SERVER_URL: str
    ANDROID_VERSION: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()  # type: ignore
