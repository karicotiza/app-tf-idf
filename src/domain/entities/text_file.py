"""Text file entity."""

from collections import Counter
from string import punctuation


class TextFileEntity:
    """Text file entity."""

    def __init__(self, name: str, text: str) -> None:
        """Make new instance.

        Args:
            name (str): text file name.
            text (str): text file text.

        """
        self._name = name
        self._text = text

        self._counter: dict[str, int] | None = None

    async def get_words(self) -> dict[str, int]:
        """Get words.

        Returns:
            dict[str, int]: word as a key, amount as a value.

        """
        if self._counter is None:
            await self._count_words()

        return self._counter

    async def get_total_words(self) -> int:
        """Get total amount of words.

        Returns:
            int: total amount of words.

        """
        if self._counter is None:
            await self._count_words()

        return self._counter.total()

    async def _count_words(self) -> None:
        self._counter = Counter(
            word.strip(punctuation).lower() for word in self._text.split()
        )
