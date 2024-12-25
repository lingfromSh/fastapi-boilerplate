from dynaconf import Dynaconf
from pydantic_settings import SettingsConfigDict

from core.conf import Settings as BaseSettings
from settings.database import DatabaseSettings
from settings.server import ServerSettings

dynaconf = Dynaconf(
    settings_files=["config.toml"],
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(dynaconf=dynaconf)

    server: ServerSettings
    database: DatabaseSettings
