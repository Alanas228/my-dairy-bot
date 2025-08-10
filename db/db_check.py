import aiosqlite
import asyncio

async def check_records_table():
    async with aiosqlite.connect("database.db") as db:
        async with db.execute("SELECT * FROM entries") as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                print(row)

async def check_read_position_table():
    async with aiosqlite.connect("database.db") as db:
        async with db.execute("SELECT * FROM reading_position") as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                print(row)

asyncio.run(check_records_table())
asyncio.run(check_read_position_table())
