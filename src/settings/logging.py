from pydantic import BaseModel


class LoggingConfig(BaseModel):
    sink: str
    level: str


class LoggingSettings(BaseModel):
    configs: list[LoggingConfig]
