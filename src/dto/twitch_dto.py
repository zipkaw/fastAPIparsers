from pydantic import BaseModel
from typing import List


class GameDto(BaseModel):
    id: str
    name: str
    box_art_url: str


class StreamsDto(BaseModel):
    id: str
    user_id: str
    user_login: str
    user_name: str
    game_id: str
    game_name: str
    type: str
    title: str
    viewer_count: str
    started_at: str
    language: str
    thumbnail_url: str
    tag_ids: List[str]
    is_mature: str
