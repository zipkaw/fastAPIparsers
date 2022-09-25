from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from json import dumps, loads

from src.config.config import Config


class KafkaHandler:
    def __init__(self, config: Config):
        self._producer = KafkaProducer(
            bootstrap_servers=[f'{config.kafka.host}:{config.kafka.port}'],
            value_serializer=lambda x: dumps(x).encode('utf-8'),
        )
        self._consumer = KafkaConsumer(
            bootstrap_servers=[f'{config.kafka.host}:{config.kafka.port}'],
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            group_id='my-group-id',
            # value_deserializer=lambda x: loads(x.decode('utf-8')),
            consumer_timeout_ms=2000
        )
        self._topic_list = []

    @property
    def topic_list(self):
        return self._topic_list

    # def __create_topic(self, topic_name):
    #     self.topic_list.append(NewTopic(
    #         name=topic_name,
    #         num_partitions=1,
    #         replication_factor=1
    #     ))
    #     self.admin_client.create_topics(new_topics=self.topic_list, validate_only=False)

    @property
    def admin_client(self):
        return self._admin_client

    @property
    def producer(self):
        return self._producer

    @property
    def consumer(self):
        return self._consumer

    def send_message(self, topic, key, instance):
        return self.producer.send(topic, instance, key=key.encode('ascii'))

    def get_message(self, topic, key):
        topic_partition = TopicPartition(topic, 0)
        data = []
        assigned_topic = [topic_partition]
        self.consumer.assign(assigned_topic)
        self.consumer.seek_to_beginning(topic_partition)
        for message in self.consumer:
            if message.key and message.key.decode('ascii') == key:
                data.append(loads(message.value.decode()))
        self.consumer.commit()
        return data
