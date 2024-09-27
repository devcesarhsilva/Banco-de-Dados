import sqlite3

conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS filmes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        ano INTEGER,
        nota REAL
        )
    """
)
conn.commit()
conn.close()
