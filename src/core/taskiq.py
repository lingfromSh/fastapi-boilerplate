from taskiq_aio_pika.broker import AioPikaBroker

from settings import Settings

settings = Settings()

broker = AioPikaBroker(
    url=settings.queue.url,
)
