from fastapi import FastAPI
from app.api.api_v1.endpoints import api_router


app = FastAPI()
app.include_router(api_router, prefix='/api/v1')
