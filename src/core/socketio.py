import ujson
from socketio.asgi import ASGIApp
from socketio.async_aiopika_manager import AsyncAioPikaManager
from socketio.async_server import AsyncServer

from settings import Settings

settings = Settings()


client_mgr = AsyncAioPikaManager(url=settings.queue.url)
sio = AsyncServer(client_manager=client_mgr, json=ujson, cors_allowed_origins="*", async_mode="asgi")
app = ASGIApp(sio)
