"""
REST API
v1
"""

from datetime import date

import requests
from fastapi import APIRouter

from app.config import URL
from app.schemas import GameCard

api_router = APIRouter()


def request_data() -> list[dict]:
    """
    Request from epic store
    :return: list[dict]
    """
    request = requests.get(URL)
    data = request.json()
    data = data["data"]["Catalog"]["searchStore"]["elements"]
    filtered_data = []
    for i in data:
        current_date = date.today()
        effective_date = date(*map(int, i["effectiveDate"].split("T")[0].split("-")))
        is_correct_year = current_date.year == effective_date.year
        if is_correct_year:
            filtered_data.append(i)
    return filtered_data


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
