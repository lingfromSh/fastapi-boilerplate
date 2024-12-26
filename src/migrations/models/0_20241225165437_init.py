from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "authors" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" BIGINT NOT NULL  DEFAULT 0,
    "name" VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_authors_deleted_869c34" ON "authors" ("deleted_at");
CREATE TABLE IF NOT EXISTS "blogs" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" BIGINT NOT NULL  DEFAULT 0,
    "title" VARCHAR(255) NOT NULL,
    "content" TEXT NOT NULL,
    "views" INT NOT NULL  DEFAULT 0,
    "likes" INT NOT NULL  DEFAULT 0,
    "published" BOOL NOT NULL  DEFAULT False,
    "published_at" TIMESTAMPTZ,
    "author_id" BIGINT NOT NULL REFERENCES "authors" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_blogs_deleted_d47e64" ON "blogs" ("deleted_at");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
