"""Build table data transfer object."""

from pydantic import BaseModel


class Response(BaseModel):
    """Build table response body."""

    rows: dict[int, tuple[str, float, float]]
