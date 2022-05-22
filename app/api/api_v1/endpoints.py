"""
REST API
v1
"""

from fastapi import APIRouter

from app.celery_worker import request_data
from app.schemas import GameCard

api_router = APIRouter()


@api_router.get("/")
async def games() -> list[dict]:
    """
    Return requested json
    :return: json response
    """
    return request_data()


@api_router.get("/{game_id}")
async def game_by_id(game_id: int) -> GameCard:
    """
    Id game request
    :param game_id: int
    :return: GameCard
    """
    data = request_data()[game_id]
    return GameCard(**data)
