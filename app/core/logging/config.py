from pydantic import BaseModel, Field
from typing import Dict, Optional, Tuple, Type
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent.parent

class FormatterConfig(BaseModel):
    format: str
    datefmt: Optional[str] = None

class HandlerConfig(BaseModel):
    class_: str = Field(
        alias="class",
        # serialization_alias="class3",
        # validation_alias="class",
    )
    level: str
    formatter: Optional[str] = None
    filename: Optional[str] = None
    maxBytes: Optional[int] = None
    backupCount: Optional[int] = None
    encoding: Optional[str] = None
    stream: Optional[str] = None

class LoggerConfig(BaseModel):
    level: str
    handlers: list[str]
    propagate: bool

class LoggingConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        yaml_file=[
            Path(ROOT_DIR, 'log.default.yaml'),
            Path(ROOT_DIR, 'log.yaml')
        ]
    )

    version: int
    disable_existing_loggers: bool
    formatters: Dict[str, FormatterConfig]
    handlers: Dict[str, HandlerConfig]
    loggers: Dict[str, LoggerConfig]

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        'Add yaml to sources'
        return (
            init_settings,
            env_settings,
            YamlConfigSettingsSource(settings_cls),
        )
