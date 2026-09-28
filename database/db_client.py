from sqlalchemy import create_engine, text

class DatabaseClient:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url, pool_pre_ping=True)

    def fetch_one(self, query: str, params: dict | None = None):
        with self.engine.connect() as connection:
            row = connection.execute(text(query), params or {}).mappings().first()
            return dict(row) if row else None

    def fetch_all(self, query: str, params: dict | None = None):
        with self.engine.connect() as connection:
            rows = connection.execute(text(query), params or {}).mappings().all()
            return [dict(row) for row in rows]

    def execute(self, query: str, params: dict | None = None):
        with self.engine.begin() as connection:
            connection.execute(text(query), params or {})
