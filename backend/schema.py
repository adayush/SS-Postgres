from pydantic import BaseModel
from pydantic_settings import BaseSettings

class CreateOrderRequest(BaseModel):
    p_id: int
    price: int

class PostgresSettings(BaseSettings):
    postgres_user: str
    postgres_pass: str
    postgres_host: str
    postgres_port: str
    postgres_dbname: str

    class Config:
        env_file = "../.env"

def get_settings():
    return PostgresSettings()
