from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    dsn: str
