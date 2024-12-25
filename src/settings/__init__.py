from dynaconf import Dynaconf
from core.conf import Settings as BaseSettings
from settings.server import ServerSettings
from pydantic_settings import SettingsConfigDict


dynaconf = Dynaconf(
    settings_files=["config.toml"],
)


class Settings(BaseSettings):

    model_config = SettingsConfigDict(dynaconf=dynaconf)

    server: ServerSettings