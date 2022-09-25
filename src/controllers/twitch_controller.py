from src.dao.twitch import TwitchDao
from src.dao.kafka import KafkaHandler


class TwitchController:
    def __init__(self, twitch, kafka):
        self._twitch: TwitchDao = twitch
        self._kafka: KafkaHandler = kafka

    @property
    def twitch(self):
        return self._twitch.twitch

    @property
    def kafka(self):
        return self._kafka

    def get_name(self):
        return self.twitch.get_user()

    def get_top_games(self):
        return self.twitch.get_top_games()

    def get_streams(self):
        return self.twitch.get_streams()

    def put_data_to_kafka(self, data_set, topic, key):
        for data in data_set:
            self.kafka.send_message(topic=topic, instance=data, key=key)
        return data_set

    def get_data_from_kafka(self, topic, key):
        return self.kafka.get_message(topic, key)
