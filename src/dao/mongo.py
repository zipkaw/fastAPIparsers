from pymongo import MongoClient

from src.config.config import Config


class Mongo:
    def __init__(self, config: Config):
        self._client = MongoClient(
            host=config.mongo.host,
            port=config.mongo.port,
            username=config.mongo.username,
            password=config.mongo.password
        )
        self._db = None

    @property
    def db(self):
        return self._client.db
