import sqlite3
from app.core.config import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    time TEXT,
    guests INTEGER
)
""")
conn.commit()


def add_reservation(name, date, time, guests):
    cursor.execute(
        "INSERT INTO reservations VALUES (NULL, ?, ?, ?, ?)",
        (name, date, time, guests),
    )
    conn.commit()
