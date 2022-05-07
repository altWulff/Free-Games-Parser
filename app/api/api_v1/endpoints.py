from fastapi import APIRouter
import requests
from app.config import URL


api_router = APIRouter()


@api_router.get('/')
async def games():
    request = requests.get(URL)
    data = request.json()
    return data['data']['Catalog']['searchStore']['elements']
