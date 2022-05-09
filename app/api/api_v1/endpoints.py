"""
REST API
v1
"""

import requests
from fastapi import APIRouter

from app.config import URL
from app.schemas import GameCard
api_router = APIRouter()


@api_router.get("/")
async def games() -> list[dict]:
    """
    Request json from epic store
    :return: json response
    """
    request = requests.get(URL)
    data = request.json()
    return data["data"]["Catalog"]["searchStore"]["elements"]


@api_router.get('/{game_id}')
async def game_by_id(game_id: int) -> GameCard:
    """
    Id game request
    :param game_id: int
    :return: GameCard
    """
    request = requests.get(URL)
    data = request.json()
    data = data["data"]["Catalog"]["searchStore"]["elements"][game_id]
    return GameCard(**data)
