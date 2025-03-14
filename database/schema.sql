DROP TABLE IF EXISTS cheapest_flights;

CREATE TABLE cheapest_flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_now TEXT NOT NULL,
    cityCodeFrom TEXT NOT NULL,
    cityCodeTo TEXT NOT NULL,
    cityFrom TEXT NOT NULL,
    cityTo TEXT NOT NULL,
    deep_link TEXT NOT NULL,
    price INTEGER NOT NULL,
    nightsInDest INTEGER NOT NULL
)