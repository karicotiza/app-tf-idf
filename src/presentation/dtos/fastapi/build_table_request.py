"""Build table data transfer object."""

from datetime import UTC, datetime

from fastapi import UploadFile
from pydantic import BaseModel

from src.domain.entities.text_file import TextFileEntity


class Request(BaseModel):
    """Build table request body."""

    text_file: UploadFile

    async def as_text_file_entity(self) -> TextFileEntity:
        """Get as text file entity.

        Returns:
            TextFileEntity: text file entity.

        """
        return TextFileEntity(
            name=self.text_file.filename or await self._datetime(),
            text=self.text_file.file.read().decode(),
        )

    async def _datetime(self) -> str:
        current_datetime: datetime = datetime.now(UTC)
        return f"{current_datetime!s}.txt"
