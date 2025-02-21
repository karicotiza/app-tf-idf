"""SQLite text files repository."""

from sqlmodel import Field, Session, SQLModel, create_engine, select

from src.domain.entities.text_file import TextFileEntity
from src.domain.repository_interfaces.text_files import ITextFilesRepository
from src.infrastructure.settings import settings


class _TextFileModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    text: str
    words_total: int


class _WordOccurrencesModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    word: str
    occurrences: int
    text_file_id: int | None = Field(
        default=None, foreign_key="_textfilemodel.id"
    )


class SQLTextFilesRepository(ITextFilesRepository):
    """SQL text file repository."""

    def __init__(self) -> None:
        """Make new instance."""
        self._engine = create_engine(settings.database_url)
        SQLModel.metadata.create_all(self._engine)

    async def add_text_file(self, text_file: TextFileEntity) -> None:
        """Add text file to repository.

        Args:
            text_file (TextFileEntity): text file entity.

        """
        with Session(self._engine) as session:
            text_file_model: _TextFileModel = _TextFileModel(
                name=text_file.name,
                text=text_file.text,
                words_total=text_file.words_total,
            )

            session.add(text_file_model)

            for word, occurrences in text_file.words_occurrences.items():
                word_occurrences_model: _WordOccurrencesModel = (
                    _WordOccurrencesModel(
                        word=word,
                        occurrences=occurrences,
                        text_file_id=text_file_model.id,
                    )
                )

                session.add(word_occurrences_model)

            session.commit()

    async def get_total_text_files(self) -> int:
        """Get total amount of text files.

        Returns:
            int: Get total amount of text files.

        """
        with Session(self._engine) as session:
            return len(session.exec(select(_TextFileModel)).all())

    async def get_total_text_files_with_word(self, word: str) -> int:
        """Get total amount of text files that include the word.

        Returns:
            int: total amount of text files that include the word.

        """
        counter: int = 0

        with Session(self._engine) as session:
            for row in session.exec(select(_TextFileModel)):
                text_file: TextFileEntity = TextFileEntity(
                    name=row.name,
                    text=row.text,
                )

                words: dict[str, int] = text_file.words_occurrences

                if word in words:
                    counter += 1

        return counter

    async def get_all_words(self) -> list[str]:
        """Get all words from all documents.

        Returns:
            list[str]: all words from all documents.

        """
        with Session(self._engine) as session:
            unique_words: list[str] = list(session.exec(
                select(_WordOccurrencesModel.word).distinct()
            ).all())

            return unique_words

    def drop(self) -> None:
        """Drop all data."""
        SQLModel.metadata.drop_all(self._engine)
        SQLModel.metadata.create_all(self._engine)


_db: SQLTextFilesRepository = SQLTextFilesRepository()
_db.drop()
