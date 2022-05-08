"""
Base renders games
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.api_v1.endpoints import games as request_games
from app.config import BASE_URL

routes = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@routes.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Request json and return html
    """
    api_request = await request_games()
    return templates.TemplateResponse(
        "index.html", {"request": request, "data": api_request, "base_url": BASE_URL}
    )
