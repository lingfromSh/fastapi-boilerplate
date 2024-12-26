from authx import AuthX
from authx import AuthXConfig
from pendulum import duration

from settings import Settings

settings = Settings()

config = AuthXConfig(
    JWT_ALGORITHM=settings.authentication.jwt_algorithm,
    JWT_SECRET_KEY=settings.authentication.jwt_secret_key,
    JWT_ACCESS_TOKEN_EXPIRES=duration(seconds=settings.authentication.jwt_access_token_expires).as_timedelta(),
)
security = AuthX(config=config)
