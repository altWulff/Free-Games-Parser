"""
Main file to start
"""


from fastapi import FastAPI
from app.api.api_v1.endpoints import api_router
import uvicorn


app = FastAPI()
app.include_router(api_router, prefix='/api/v1')


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
