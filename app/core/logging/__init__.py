from app.core.logging.config import LoggingConfig
import logging.config

loggingConfig = LoggingConfig()

def init_logs():
    logging.config.dictConfig(
        loggingConfig.model_dump(
            exclude_unset=True,
            by_alias=True,
        )
    )
