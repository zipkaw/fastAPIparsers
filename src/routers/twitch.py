from fastapi import APIRouter
from typing import List

from src.dto.twitch_dto import GameDto, StreamsDto
from src.app import container_controller

router = APIRouter(
    tags=['Twitch router'],
    prefix='/twitch'
)


@router.get('/top_games', response_model=List[GameDto])
def get_top_games() -> GameDto:
    return container_controller.twitch.get_top_games()['data']


@router.get('/streams', response_model=List[StreamsDto])
def get_streams() -> StreamsDto:
    return container_controller.twitch.get_streams()['data']


@router.get('/streams-kafka')
def put_streams_to_kafka():
    data_set = container_controller.twitch.get_streams()['data']
    container_controller.twitch.put_data_to_kafka(
        data_set=data_set,
        topic='twitch',
        key='streams'
    )
    return "Streams was added to kafka"


@router.get('/get-streams-kafka', response_model=List[StreamsDto])
def get_streams_from_kafka() -> StreamsDto:
    return container_controller.twitch.get_data_from_kafka(topic='twitch', key='stream')


@router.get('/games-kafka')
def put_games_to_kafka():
    data_set = container_controller.twitch.get_top_games()['data']
    container_controller.twitch.put_data_to_kafka(
        data_set=data_set,
        topic='twitch',
        key='games'
    )
    return "Games was added to kafka"


@router.get('/get-games-kafka')
def get_games_from_kafka():
    return container_controller.twitch.get_data_from_kafka(topic='twitch', key='games')
