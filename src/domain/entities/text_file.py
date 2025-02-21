"""Text file entity."""

from collections import Counter
from string import punctuation


class TextFileEntity:
    """Text file entity."""

    def __init__(
        self,
        name: str,
        text: str,
        *,
        word_occurrences: dict[str, int] | None = None,
        words_total: int | None = 0,
    ) -> None:
        """Make new instance.

        Args:
            name (str): text file name.
            text (str): text file text.
            word_occurrences: dict[str, int] | None: word as key, occurrences
                as value. Defaults to None
            words_total: dict[str, int] | None: words total.

        """
        self._name: str = name
        self._text: str = text

        if word_occurrences:
            self._word_occurrences: dict[str, int] = word_occurrences
        else:
            self._word_occurrences = {}

        if words_total:
            self._words_total: int = words_total
        else:
            self._words_total = 0

    @property
    def name(self) -> str:
        """Get name.

        Returns:
            str: name

        """
        return self._name

    @property
    def text(self) -> str:
        """Get text.

        Returns:
            str: text

        """
        return self._text

    @property
    def words_occurrences(self) -> dict[str, int]:
        """Get word occurrences.

        Returns:
            dict[str, int]: word as key, occurrences as value.

        """
        if not self._word_occurrences:
            self._word_occurrences = self._count_words()

        return self._word_occurrences

    @property
    def words_total(self) -> int:
        """Get total amount of words.

        Returns:
            int: total amount of words.

        """
        if not self._word_occurrences:
            self._word_occurrences = self._count_words()

        if not self._words_total:
            self._words_total = sum(
                occurrence for occurrence in self._word_occurrences.values()
            )

        return self._words_total

    def _count_words(self) -> dict[str, int]:
        return dict(Counter(
            word.strip(punctuation).lower() for word in self._text.split()
        ))
