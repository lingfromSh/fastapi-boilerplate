from fastapi import FastAPI
from fastapi_health import health
from fastapi_pagination import add_pagination

from apps.blog.handlers import router as blog_router
from core.authx import security
from core.health import failure_handler
from core.health import is_database_ready
from core.health import success_handler
from core.logger import logger
from core.socketio import app as socketio_app
from lifespan import lifespan
from settings import Settings

settings = Settings()
app = FastAPI(title=settings.server.name, lifespan=lifespan)


def configure_app(app: FastAPI):
    logger.info("Configuring app")
    add_pagination(app)
    app.add_api_route(
        "/health", health([is_database_ready], success_handler=success_handler, failure_handler=failure_handler)
    )
    app.include_router(blog_router)
    app.mount("/socket.io", socketio_app)
    security.handle_errors(app)


configure_app(app)
