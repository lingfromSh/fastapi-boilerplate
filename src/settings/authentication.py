import typing as t

from pydantic import BaseModel


class AuthenticationSettings(BaseModel):
    # time in seconds
    jwt_access_token_expires: t.Optional[int] = None
    jwt_algorithm: str = "HS256"
    jwt_secret_key: t.Optional[str] = None
