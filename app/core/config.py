from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Simple social network API'
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/test_db"
    SECRET_KEY: str = "d635c4b82e1224f87fb3d07698be50e1cc966336d9f8cfa429d27a9fec4d36ec"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
