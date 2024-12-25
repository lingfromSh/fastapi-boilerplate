from fastapi import FastAPI
from fastapi_pagination import add_pagination

from core.logger import logger
from lifespan import lifespan
from settings import Settings

settings = Settings()
app = FastAPI(title=settings.server.name, lifespan=lifespan)


def configure_app(app: FastAPI):
    logger.info("Configuring app")
    add_pagination(app)


configure_app(app)
