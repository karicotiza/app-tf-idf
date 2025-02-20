"""SQLite text files repository."""

from sqlmodel import Field, Session, SQLModel, create_engine, select

from src.domain.entities.text_file import TextFileEntity
from src.domain.repository_interfaces.text_files import ITextFilesRepository


class _TextFileModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    text: str


_engine = create_engine("sqlite:///data/sqlite/database.db")
SQLModel.metadata.create_all(_engine)


class SQLiteTextFilesRepository(ITextFilesRepository):
    """SQLite text file repository."""

    _session = Session(_engine)

    async def add_text_file(self, text_file: TextFileEntity) -> None:
        """Add text file to repository.

        Args:
            text_file (TextFileEntity): text file entity.

        """
        with Session(_engine) as session:
            session.add(
                _TextFileModel(name=text_file.name, text=text_file.text)
            )
            session.commit()

    async def get_total_text_files(self) -> int:
        """Get total amount of text files.

        Returns:
            int: Get total amount of text files.

        """
        with Session(_engine) as session:
            return len(session.exec(select(_TextFileModel)).all())

    async def get_total_text_files_with_word(self, word: str) -> int:
        """Get total amount of text files that include the word.

        Returns:
            int: total amount of text files that include the word.

        """
        counter: int = 0

        with Session(_engine) as session:
            for row in session.exec(select(_TextFileModel)):
                text_file: TextFileEntity = TextFileEntity(
                    name=row.name,
                    text=row.text,
                )

                words: dict[str, int] = await text_file.get_words()

                if word in words:
                    counter += 1

            session.commit()

        return counter

    async def get_all_words(self) -> list[str]:
        """Get all words from all documents.

        Returns:
            list[str]: all words from all documents.

        """
        memory: set[str] = set()

        with Session(_engine) as session:
            for row in session.exec(select(_TextFileModel)):
                text_file: TextFileEntity = TextFileEntity(
                    name=row.name,
                    text=row.text,
                )

                for word in await text_file.get_words():
                    memory.add(word)

            session.commit()

        return list(memory)

    def drop(self) -> None:
        """Drop all data."""
        with Session(_engine) as session:
            for row in session.exec(select(_TextFileModel)):
                session.delete(row)

            session.commit()


_db: SQLiteTextFilesRepository = SQLiteTextFilesRepository()
_db.drop()
