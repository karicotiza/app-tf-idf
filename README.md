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
2. Wait until `server-# | INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`
line appears (about 20 seconds).
3. Open [http://localhost](http://localhost) in your browser.

## Notes

* The IDF accumulates in such a way that refreshing the page does not reset it;
* IDF will be specified only for words that are present in the current
document, not for all words in general;
* The data is first sorted by IDF, then by TF;
* If you run it via Docker Compose, PostgreSQL will be used, otherwise
(e.g. in tests), SQLite will be used;
* I used Tailwind with CDN, not with compiled CSS.
