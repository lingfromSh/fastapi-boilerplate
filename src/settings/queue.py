from pydantic import BaseModel
from pydantic import computed_field


class QueueSettings(BaseModel):
    host: str
    port: int
    username: str
    password: str
    vhost: str

    @computed_field
    def url(self) -> str:
        return f"amqp://{self.username}:{self.password}@{self.host}:{self.port}/{self.vhost}"
