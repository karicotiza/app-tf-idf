"""Test table builder application service."""

import pytest

from src.application.services.table_builder import (
    TableBuilderApplicationService,
)
from src.domain.entities.text_file import TextFileEntity
from src.domain.services.tf_idf import TFIDFDomainService
from src.infrastructure.repositories.in_memory_text_files import (
    InMemoryTextFilesRepository,
)

pytest_plugins: tuple[str, ...] = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_table_builder_application_service() -> None:
    """Test table builder application service."""
    text_files_text: list[str] = [
        "One. Two. Three.",
        "Two. Three. Four.",
        "Three. Four. Five.",
    ]

    for index, text in enumerate(text_files_text[:-1]):
        await InMemoryTextFilesRepository().add_text_file(
            text_file=TextFileEntity(
                name=f"test_{index}.txt",
                text=text,
            )
        )

    table: dict[
        int, tuple[str, float, float]
    ] = await TableBuilderApplicationService().get_table(
        text_file=TextFileEntity(
            name="test_3.txt",
            text=text_files_text[-1],
        ),
        repository=InMemoryTextFilesRepository(),
        service=TFIDFDomainService(),
    )

    assert table == {
        0: ("five", 0.3333333333333333, 0.47712125471966244),
        1: ("four", 0.3333333333333333, 0.17609125905568124),
        2: ("three", 0.3333333333333333, 0.),
    }
