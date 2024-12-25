from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

from core.logger import logger
from core.taskiq import broker
from settings import Settings

TORTOISE_ORM = {
    "connections": {
        "default": Settings().database.dsn,
    },
    "apps": {
        "models": {
            "models": ["apps.blog.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting lifespan")
    await Tortoise.init(config=TORTOISE_ORM)
    logger.info("Tortoise initialized")
    await broker.startup()
    logger.info("Broker started")
    yield
    await broker.shutdown()
    logger.info("Broker shutdown")
    await Tortoise.close_connections()
    logger.info("Tortoise connections closed")
