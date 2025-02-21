"""In memory text files repository."""

from typing import ClassVar

from src.domain.entities.text_file import TextFileEntity
from src.domain.repository_interfaces.text_files import ITextFilesRepository


class InMemoryTextFilesRepository(ITextFilesRepository):
    """In memory words repository."""

    _db: ClassVar[list[TextFileEntity]] = []

    async def add_text_file(self, text_file: TextFileEntity) -> None:
        """Add text file to repository.

        Args:
            text_file (TextFileEntity): text file entity.

        """
        self._db.append(text_file)

    async def get_total_text_files(self) -> int:
        """Get total amount of text files.

        Returns:
            int: Get total amount of text files.

        """
        return len(self._db)

    async def get_total_text_files_with_word(self, word: str) -> int:
        """Get total amount of text files that include the word.

        Returns:
            int: total amount of text files that include the word.

        """
        counter: int = 0

        for text_file in self._db:
            words: dict[str, int] = text_file.words_occurrences
            if word in words:
                counter += 1

        return counter

    async def get_all_words(self) -> list[str]:
        """Get all words from all documents.

        Returns:
            list[str]: all words from all documents.

        """
        memory: set[str] = set()

        for text_file in self._db:
            for word in text_file.words_occurrences:
                memory.add(word)

        return list(memory)

    async def drop(self) -> None:
        """Drop all data."""
        self._db.clear()
