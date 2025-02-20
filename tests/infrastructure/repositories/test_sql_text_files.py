"""Test in memory words repository."""

import pytest

from src.domain.entities.text_file import TextFileEntity
from src.infrastructure.repositories.sql_text_files import (
    SQLTextFilesRepository,
)

pytest_plugins: tuple[str, ...] = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_in_memory_words_repository() -> None:
    """Test in memory words repository."""
    repository: SQLTextFilesRepository = SQLTextFilesRepository()
    repository.drop()

    text_files_text: list[str] = [
        "One. Two. Three.",
        "Two. Three. Four.",
        "Three. Four. Five.",
    ]

    expected_total_text_files_with_word_three: int = 3

    for index, text in enumerate(text_files_text):
        await repository.add_text_file(
            text_file=TextFileEntity(
                name=f"test_{index}.txt",
                text=text,
            )
        )

    assert await repository.get_total_text_files() == len(text_files_text)
    assert sorted(await repository.get_all_words()) == [
        "five",
        "four",
        "one",
        "three",
        "two",
    ]
    assert (
        await repository.get_total_text_files_with_word("three")
        == expected_total_text_files_with_word_three
    )
