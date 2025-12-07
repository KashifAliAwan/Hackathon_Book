"""
Database module for the RAG system.
Handles Neon Serverless Postgres connection and schema management.
"""
from typing import Optional
import asyncpg
import uuid
from datetime import datetime


class DatabaseManager:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool = None

    async def connect(self):
        """Create a connection pool to the database."""
        self.pool = await asyncpg.create_pool(
            self.database_url,
            min_size=1,
            max_size=10,
            command_timeout=60
        )

    async def close(self):
        """Close the database connection pool."""
        if self.pool:
            await self.pool.close()

    async def create_tables(self):
        """Create the initial tables for textbooks and chapters."""
        async with self.pool.acquire() as conn:
            # Create textbooks table
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS textbooks (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    title VARCHAR(255) NOT NULL,
                    language VARCHAR(50) NOT NULL DEFAULT 'english',
                    version VARCHAR(50) NOT NULL,
                    qdrant_collection_name VARCHAR(255) UNIQUE NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Create chapters table
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS chapters (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    textbook_id UUID NOT NULL REFERENCES textbooks(id) ON DELETE CASCADE,
                    chapter_number INT NOT NULL,
                    title VARCHAR(255) NOT NULL,
                    slug VARCHAR(255) NOT NULL,
                    file_path VARCHAR(500) UNIQUE NOT NULL,
                    content_hash VARCHAR(64) NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(textbook_id, chapter_number),
                    UNIQUE(textbook_id, slug)
                );
            """)

            # Create an index on textbook_id for faster queries
            await conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_chapters_textbook_id ON chapters(textbook_id);
            """)

    async def create_textbook(self, title: str, version: str, qdrant_collection_name: str, language: str = "english") -> dict:
        """Create a new textbook entry in the database."""
        async with self.pool.acquire() as conn:
            textbook_id = str(uuid.uuid4())
            query = """
                INSERT INTO textbooks (id, title, language, version, qdrant_collection_name)
                VALUES ($1, $2, $3, $4, $5)
                RETURNING id, title, language, version, qdrant_collection_name, created_at, updated_at
            """
            row = await conn.fetchrow(query, textbook_id, title, language, version, qdrant_collection_name)
            return dict(row)

    async def get_textbook_by_collection(self, collection_name: str) -> Optional[dict]:
        """Get a textbook by its Qdrant collection name."""
        async with self.pool.acquire() as conn:
            query = """
                SELECT id, title, language, version, qdrant_collection_name, created_at, updated_at
                FROM textbooks
                WHERE qdrant_collection_name = $1
            """
            row = await conn.fetchrow(query, collection_name)
            return dict(row) if row else None

    async def create_chapter(self, textbook_id: str, chapter_number: int, title: str,
                           slug: str, file_path: str, content_hash: str) -> dict:
        """Create a new chapter entry in the database."""
        async with self.pool.acquire() as conn:
            chapter_id = str(uuid.uuid4())
            query = """
                INSERT INTO chapters (id, textbook_id, chapter_number, title, slug, file_path, content_hash)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                RETURNING id, textbook_id, chapter_number, title, slug, file_path, content_hash, created_at, updated_at
            """
            row = await conn.fetchrow(query, chapter_id, textbook_id, chapter_number, title, slug, file_path, content_hash)
            return dict(row)

    async def get_chapters_by_textbook(self, textbook_id: str) -> list:
        """Get all chapters for a specific textbook."""
        async with self.pool.acquire() as conn:
            query = """
                SELECT id, textbook_id, chapter_number, title, slug, file_path, content_hash, created_at, updated_at
                FROM chapters
                WHERE textbook_id = $1
                ORDER BY chapter_number
            """
            rows = await conn.fetch(query, textbook_id)
            return [dict(row) for row in rows]

    async def get_chapter_by_slug(self, textbook_id: str, slug: str) -> Optional[dict]:
        """Get a specific chapter by textbook ID and slug."""
        async with self.pool.acquire() as conn:
            query = """
                SELECT id, textbook_id, chapter_number, title, slug, file_path, content_hash, created_at, updated_at
                FROM chapters
                WHERE textbook_id = $1 AND slug = $2
            """
            row = await conn.fetchrow(query, textbook_id, slug)
            return dict(row) if row else None


# Helper function to create textbook content hash
def generate_content_hash(content: str) -> str:
    """Generate a hash of the content for change detection."""
    import hashlib
    return hashlib.sha256(content.encode()).hexdigest()