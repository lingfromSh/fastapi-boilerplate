from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

from settings import Settings

TORTOISE_ORM = {
    "connections": {
        "default": Settings().database.dsn,
    },
    "apps": {
        "models": {
            "models": ["aerich.models"],
            "default_connection": "default",
        },
    },
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    yield
    await Tortoise.close_connections()
