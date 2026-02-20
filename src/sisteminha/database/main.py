import sqlite3
from pathlib import Path


class DatabaseService:
    connection: sqlite3.Connection = None
    db_url: str = None

    def __init__(self, db_url: str):
        self.db_url = db_url
        if self.connection:
            self.disconnect()
        path = Path(db_url)
        if path.parent != Path(".") and not path.parent.exists():
            raise FileNotFoundError(
                f"O diretório '{path.parent}' não existe. "
                "Crie o diretório antes de iniciar o banco de dados."
            )

    def connect(self):
        if not self.db_url or self.db_url.strip() == "":
            raise ValueError("Database URL is not set. Cannot connect to the database.")
        self.connection = sqlite3.connect(self.db_url)

    def disconnect(self):
        if self.connection:
            self.connection = None

    def inicializar(self):
        if not self.connection:
            raise RuntimeError("Cannot initialize database: No active database connection.")
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id         INTEGER  PRIMARY KEY AUTOINCREMENT,
                nome       TEXT     NOT NULL,
                email      TEXT     NOT NULL UNIQUE,
                senha      TEXT     NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()

