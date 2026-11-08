import sqlite3


def get_connection():
    conn = sqlite3.connect("shelter.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS species (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)

    cursor.execute("PRAGMA table_info(animals)")
    columns = [column[1] for column in cursor.fetchall()]

    if "owner_id" not in columns:
        cursor.execute("""
            ALTER TABLE animals
            ADD COLUMN owner_id INTEGER REFERENCES owners(id)
        """)

    conn.commit()
    conn.close()