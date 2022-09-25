from src.config.config import Config
from src.dao.kafka import KafkaHandler
from src.parsers.lamoda_parser import LamodaParser
from src.app.container_controller import ContainerController


class ContainerParser:
    def __init__(self, config: Config, container_controller: ContainerController):
        self._config = config
        self._kafka = KafkaHandler(config)
        self._lamoda_parser = LamodaParser(self._kafka, config, container_controller)

    @property
    def kafka(self):
        return self._kafka

    @property
    def lamoda(self):
        return self._lamoda_parser
