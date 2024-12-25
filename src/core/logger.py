from loguru import logger


class Logger:
    def __init__(self):
        self.logger = logger

        self._setup_logger()

    def _setup_logger(self):
        from settings import Settings

        settings = Settings()

        for config in settings.logging.configs:
            self.logger.add(
                config.sink,
                level=config.level,
            )

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def fatal(self, message: str):
        self.logger.fatal(message)

    def exception(self, message: str):
        self.logger.exception(message)


logger = Logger()  # noqa: F811
