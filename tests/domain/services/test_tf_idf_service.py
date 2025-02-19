"""Test TF IDF service."""

import pytest

from src.domain.services.tf_idf import TFIDFDomainService

pytest_plugins: tuple[str, ...] = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_tf_idf_service() -> None:
    """Test TF IDF service."""
    service: TFIDFDomainService = TFIDFDomainService()

    amount_of_text_files_with_word: int = 1000
    amount_of_text_files: int = 10000000

    expected_tf: float = 0.03
    expected_idf: float = 4

    assert (
        await service.calculate_tf(
            word_occurrences=3,
            amount_of_words_in_document=100,
        )
        == expected_tf
    )

    assert (
        await service.calculate_idf(
            amount_of_text_files_with_word=amount_of_text_files_with_word,
            amount_of_text_files=amount_of_text_files,
        )
        == expected_idf
    )
