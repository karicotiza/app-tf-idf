"""FastAPI controller."""

from fastapi import FastAPI

from src.presentation.views.fastapi.build_table import build_table_router

app: FastAPI = FastAPI()

app.include_router(build_table_router)
