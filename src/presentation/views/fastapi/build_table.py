"""Build table FastAPI view."""

from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, Form

from src.application.services.table_builder import (
    TableBuilderApplicationService,
)
from src.domain.services.tf_idf import TFIDFDomainService
from src.infrastructure_.repositories.sqlite_text_files import (
    SQLTextFilesRepository,
)
from src.presentation.dtos.fastapi.build_table_request import Request
from src.presentation.dtos.fastapi.build_table_response import Response

if TYPE_CHECKING:
    from src.domain.entities.text_file import TextFileEntity

build_table_router: APIRouter = APIRouter()


@build_table_router.post("/build_table/")
async def process_build_table(request: Annotated[Request, Form()]) -> Response:
    """Process build table.

    Args:
        request (Request): build table request body.

    Returns:
        Response: build table response body.

    """
    service: TableBuilderApplicationService = TableBuilderApplicationService()
    text_file: TextFileEntity = await request.as_text_file_entity()

    return Response(
        rows=await service.get_table(
            text_file=text_file,
            repository=SQLTextFilesRepository(),
            service=TFIDFDomainService(),
        ),
    )
