# SQLite Database for Preventing Duplicate News

import sqlite3

def initialize_database():
    """Initialize the database to store news titles and prevent duplicates."""
    conn = sqlite3.connect("news_cache.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, title TEXT UNIQUE, link TEXT)")
    conn.commit()
    conn.close()

initialize_database()
