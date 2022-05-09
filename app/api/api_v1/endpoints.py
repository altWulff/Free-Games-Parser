"""
REST API
v1
"""

import requests
from fastapi import APIRouter

from app.config import URL

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
