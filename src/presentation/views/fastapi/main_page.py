"""Main page FastAPI view."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

main_page_router: APIRouter = APIRouter()
templates = Jinja2Templates(directory="./static/templates/")


@main_page_router.get("/")
async def process_build_table(request: Request) -> HTMLResponse:
    """Process main page.

    Returns:
        HTMLResponse: main page.

    """
    return templates.TemplateResponse(request=request, name="index.html")
