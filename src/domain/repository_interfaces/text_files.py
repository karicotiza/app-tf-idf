"""Text file repository interface."""

from typing import Protocol

from src.domain.entities.text_file import TextFileEntity


class ITextFilesRepository(Protocol):
    """Text file repository interface."""

    async def add_text_file(self, text_file: TextFileEntity) -> None:
        """Add text file to repository.

        Args:
            text_file (TextFileEntity): text file entity.

        """
        ...

    async def get_total_text_files(self) -> int:
        """Get total amount of text files.

        Returns:
            int: Get total amount of text files.

        """
        ...

    async def get_total_text_files_with_word(self, word: str) -> int:
        """Get total amount of text files that include the word.

        Returns:
            int: total amount of text files that include the word.

        """
        ...

    async def get_all_words(self) -> list[str]:
        """Get all words from all documents.

        Returns:
            list[str]: all words from all documents.

        """
        ...
