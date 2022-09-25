from fastapi import FastAPI

from src.config.config import Config


class ContainerGeneral:
    def __init__(self):
        self._app = FastAPI(
            title="FastAPIparsers"
        )
        self._config = Config()

    @property
    def app(self):
        return self._app

    @property
    def config(self):
        return self._config
