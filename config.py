from pydantic import BaseSettings


class Settings(BaseSettings):
    raw_data_base_path: str = "./raw_data"
    input_file: str

    class Config:
        env_file = ".env"


settings = Settings()
