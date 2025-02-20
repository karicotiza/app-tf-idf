# app-tf-idf

Web application for calculating TF-IDF metric.

## How to reproduce

Prerequisites:

1. Python `==3.12.3`
2. Docker Engine `==27.4.0`
3. Docker Compose `==2.31.0`

Steps:

1. Launch using Docker Compose -
`docker compose -f .\build\docker\compose\docker-compose.yml up --build`
2. Open [http://localhost:8000](http://localhost:8000/) in your browser.

## Notes

* If you run it via Docker Compose, PostgreSQL will be used;
otherwise (e.g. in tests), SQLite will be used.
* I used Tailwind with CDN, not with compiled CSS.
