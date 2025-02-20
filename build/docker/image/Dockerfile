FROM python:3.12.9-slim-bookworm

ENV PIP_NO_CACHE_DIR=1

WORKDIR /app/

RUN python -m pip install fastapi==0.115.8
RUN python -m pip install python_multipart==0.0.20
RUN python -m pip install sqlmodel==0.0.22
RUN python -m pip install pydantic_settings==2.7.1
RUN python -m pip install psycopg2_binary==2.9.10
RUN python -m pip install uvicorn==0.34.0
RUN python -m pip install uvloop==0.21.0

COPY ./src/ ./src/

ENTRYPOINT [ "uvicorn", "src.presentation.controllers.fastapi.controller:app", "--host", "0.0.0.0" ]
