from src.app.general import ContainerGeneral
from src.dao.mongo import Mongo


class ContainerDao:
    def __init__(self, container_general: ContainerGeneral):
        self._config = container_general.config
        self._db = Mongo(self._config).db

    @property
    def db(self):
        return self._db
