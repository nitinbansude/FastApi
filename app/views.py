from fastapi import FastAPI
from app.controllers.add_controller import add_endpoint


app = FastAPI()

app.include_router(add_endpoint, prefix="/api")