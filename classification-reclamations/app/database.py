
import os
import psycopg

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/reclamations"
)


def save_complaint(text, category):

    with psycopg.connect(DATABASE_URL) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS reclamations (
                id SERIAL PRIMARY KEY,
                text TEXT NOT NULL,
                category VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.execute(
            "INSERT INTO reclamations (text, category) VALUES (%s, %s)",
            (text, category)
        )
