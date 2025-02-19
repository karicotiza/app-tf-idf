"""TF IDF domain service."""

from math import log10


class TFIDFDomainService:
    """TF IDF domain service."""

    async def calculate_tf(
        self,
        word_occurrences: int,
        amount_of_words_in_document: int,
    ) -> float:
        """Calculate term frequency.

        Args:
            word_occurrences (int): term occurrences in text file.
            amount_of_words_in_document (int): amount of words in text file.

        Returns:
            int: term frequency.

        """
        return word_occurrences / amount_of_words_in_document

    async def calculate_idf(
        self,
        amount_of_text_files_with_word: int,
        amount_of_text_files: int,
    ) -> float:
        """Calculate inverse document frequency.

        Returns:
            float: inverse document frequency.

        """
        return log10(amount_of_text_files / amount_of_text_files_with_word)
