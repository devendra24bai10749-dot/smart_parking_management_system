import sqlite3
import os

def connect():
    # create folder if not exists
    if not os.path.exists("data"):
        os.makedirs("data")

    conn = sqlite3.connect("data/parking.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS parking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_number TEXT,
        entry_time TEXT,
        exit_time TEXT,
        fee REAL
    )
    """)

    conn.commit()
    conn.close()