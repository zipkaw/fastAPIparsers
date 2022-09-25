from src.app.general import ContainerGeneral
from src.app.container_dao import ContainerDao
from src.app.container_controller import ContainerController
from src.app.container_parser import ContainerParser
from src.dao.twitch import TwitchDao
from src.dao.kafka import KafkaHandler

container_general = ContainerGeneral()
container_dao = ContainerDao(container_general)
container_controller = ContainerController(
    db=container_dao.db,
    twitch=TwitchDao(),
    kafka=KafkaHandler(container_general.config))
container_parser = ContainerParser(container_general.config, container_controller)
