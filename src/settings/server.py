from pydantic import BaseModel


class ServerSettings(BaseModel):
    """
    Server settings
    """

    name: str
    host: str
    port: int
    debug: bool
