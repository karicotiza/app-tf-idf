"""FastAPI controller."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.presentation.views.fastapi.build_table import build_table_router
from src.presentation.views.fastapi.main_page import main_page_router

app: FastAPI = FastAPI()

app.mount(
    path="/static",
    app=StaticFiles(directory="./static/templates/"),
    name="static",
)

app.include_router(build_table_router)
app.include_router(main_page_router)
