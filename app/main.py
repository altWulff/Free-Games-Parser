"""
Main file to start
"""


import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.api_v1.endpoints import api_router
from app.view import routes

app = FastAPI()
app.include_router(routes)
app.include_router(api_router, prefix="/api/v1")

#app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
