from dynaconf import Dynaconf
from pydantic_settings import SettingsConfigDict

from core.conf import Settings as BaseSettings
from settings.authentication import AuthenticationSettings
from settings.database import DatabaseSettings
from settings.logging import LoggingSettings
from settings.queue import QueueSettings
from settings.server import ServerSettings

dynaconf = Dynaconf(
    settings_files=["config.toml"],
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(dynaconf=dynaconf)

    server: ServerSettings
    database: DatabaseSettings
    queue: QueueSettings
    logging: LoggingSettings
    authentication: AuthenticationSettings
