"""
Config Proxy class for the application.
"""
import json
from dynaconf import Dynaconf
from pathlib import Path
from typing import Any, Dict, Tuple, Type
from pydantic.fields import FieldInfo

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


class DynaconfSettingsSource(PydanticBaseSettingsSource):

    def get_field_value(
        self, field: FieldInfo, field_name: str
    ) -> Tuple[Any, str, bool]:
        dynaconf = self.config.get("dynaconf")
        if not dynaconf:
            raise ValueError("dynaconf is not set")
        if field_name not in dynaconf:
            return field.get_default(), field_name, False
        return dynaconf[field_name], field_name, False

    def prepare_field_value(
        self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
    ) -> Any:
        return value

    def __call__(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(
                field, field_name
            )
            field_value = self.prepare_field_value(
                field_name, field, field_value, value_is_complex
            )
            if field_value is not None:
                d[field_key] = field_value

        return d


class Settings(BaseSettings):
    
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, DynaconfSettingsSource(settings_cls)
