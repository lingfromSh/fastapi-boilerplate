from fastapi import FastAPI
from lifespan import lifespan
from settings import Settings

from fastapi_pagination import add_pagination

settings = Settings()
app = FastAPI(title=settings.server.name, lifespan=lifespan)


def configure_app(app: FastAPI):
    add_pagination(app)


configure_app(app)
