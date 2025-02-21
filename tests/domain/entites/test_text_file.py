"""Test text file entity."""

import pytest

from src.domain.entities.text_file import TextFileEntity

pytest_plugins: tuple[str, ...] = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_text_file_entity() -> None:
    """Test text file entity."""
    text_file: TextFileEntity = TextFileEntity(
        name="test.txt",
        text="One. Two, Two. Three, Three, Three.",
    )

    expected_words: dict[str, int] = {"one": 1, "three": 3, "two": 2}
    expected_total_words: int = 6

    assert text_file.words_occurrences == expected_words
    assert text_file.words_total == expected_total_words
