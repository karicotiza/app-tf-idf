"""Test FastAPI build table view."""

import json

from fastapi.testclient import TestClient

from src.infrastructure.repositories.sqlite_text_files import (
    SQLTextFilesRepository,
)
from src.presentation.controllers.fastapi.controller import app


def test_build_table() -> None:
    """Test FastAPI build table view."""
    repository: SQLTextFilesRepository = SQLTextFilesRepository()
    repository.drop()

    texts: list[str] = [
        "hare hare hare placeholder placeholder\n"
        "placeholder placeholder placeholder placeholder placeholder ",
        "placeholder placeholder placeholder placeholder placeholder\n"
        "placeholder placeholder placeholder placeholder placeholder",
        "hare hare hare placeholder placeholder\n"
        "placeholder placeholder placeholder placeholder placeholder",
    ]

    expected_result: dict = {
        "rows": {
            "0": ["hare", 0.3, 0.17609125905568124],
            "1": ["placeholder", 0.7, 0.],
        },
    }

    for text in texts:
        response = TestClient(app).post(
            "/build_table/",
            files={"text_file": ("text_file.txt", text.encode())},
        )

    assert json.loads(response.content) == expected_result
