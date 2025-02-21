"""Table builder application service."""

from src.domain.entities.text_file import TextFileEntity
from src.domain.repository_interfaces.text_files import ITextFilesRepository
from src.domain.services.tf_idf import TFIDFDomainService


class TableBuilderApplicationService:
    """Table builder application service."""

    async def get_table(
        self,
        text_file: TextFileEntity,
        repository: ITextFilesRepository,
        service: TFIDFDomainService,
        limit: int = 50,
    ) -> dict[int, tuple[str, float, float]]:
        """Get table.

        Args:
            text_file (TextFileEntity): text file entity.
            repository (ITextFilesRepository): text file repository interface.
            service (TFIDFDomainService): TF IDF domain service.
            limit (int): rows in table. Defaults to 50.

        Returns:
            list[tuple[str, float, float]]: word, TF, IDF.

        """
        await repository.add_text_file(text_file)

        total: int = await repository.get_total_text_files()
        words: dict[str, int] = text_file.words_occurrences

        top_words_by_idf: list[tuple[str, float, float]] = sorted(
            [
                (
                    word,
                    await self._get_tf(word, service, words, text_file),
                    await self._get_idf(word, service, repository, total),
                ) for word in words
            ],
            key=lambda element: (element[2], element[1]),
            reverse=True,
        )

        return dict(enumerate(top_words_by_idf[:limit]))

    async def _get_tf(
        self,
        word: str,
        service: TFIDFDomainService,
        words_if_text_file: dict[str, int],
        text_file: TextFileEntity,
    ) -> float:
        return await service.calculate_tf(
            word_occurrences=words_if_text_file.get(word, 0),
            amount_of_words_in_document=text_file.words_total,
        )

    async def _get_idf(
        self,
        word: str,
        service: TFIDFDomainService,
        repository: ITextFilesRepository,
        total_files: int,
    ) -> float:
        return await service.calculate_idf(
            amount_of_text_files=total_files,
            amount_of_text_files_with_word=(
                await repository.get_total_text_files_with_word(word)
            ),
        )
