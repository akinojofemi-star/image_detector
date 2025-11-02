import sqlite3

DB_PATH = "predictions.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            prediction TEXT,
            confidence REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_prediction(filename, prediction, confidence):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO predictions (filename, prediction, confidence) VALUES (?, ?, ?)",
        (filename, prediction, confidence)
    )
    conn.commit()
    conn.close()

def fetch_predictions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT filename, prediction, confidence FROM predictions ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data
