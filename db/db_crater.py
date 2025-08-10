import aiosqlite
import asyncio

# records db

async def create_table():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                position INTEGER,
                user_id INTEGER,
                text TEXT
            )
        """)
        await db.commit()

asyncio.run(create_table())


# db for reading entry

async def create_table():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS reading_position (
                user_id INTEGER PRIMARY KEY,
                position INTEGER 
            )
        """)
        await db.commit()

asyncio.run(create_table())

