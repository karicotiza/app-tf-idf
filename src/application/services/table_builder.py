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

        return await self._get_top_words_by_idf(
            repository=repository,
            service=service,
            text_file=text_file,
            limit=limit,
        )

    async def _get_top_words_by_idf(
        self,
        repository: ITextFilesRepository,
        service: TFIDFDomainService,
        text_file: TextFileEntity,
        limit: int = 50,
    ) -> dict[int, tuple[str, float, float]]:
        memory: list[tuple[str, float, float]] = []
        total: int = await repository.get_total_text_files()

        for word in await text_file.get_words():
            words: dict[str, int] = await text_file.get_words()
            memory.append(
                (
                    word,
                    await self._get_tf(word, service, words, text_file),
                    await self._get_idf(word, service, repository, total),
                )
            )

        sorted_list: list[tuple[str, float, float]] = sorted(
            memory,
            key=lambda element: (element[2], element[1]),
            reverse=True,
        )[:limit]

        return dict(enumerate(sorted_list))

    async def _get_tf(
        self,
        word: str,
        service: TFIDFDomainService,
        words_if_text_file: dict[str, int],
        text_file: TextFileEntity,
    ) -> float:
        return await service.calculate_tf(
            word_occurrences=words_if_text_file.get(word, 0),
            amount_of_words_in_document=await text_file.get_total_words(),
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
