# importing
import aiosqlite

async def get_max_position(user_id):
    async with aiosqlite.connect("db/database.db") as db:
        async with db.execute(
            "SELECT MAX(position) FROM entries WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            temp = await cursor.fetchone()
            return temp[0] if temp[0] is not None else 0

async def add_entry(user_id, text):
    position = await get_max_position(user_id) + 1
    async with aiosqlite.connect("db/database.db") as db:
        await db.execute(
            "INSERT INTO entries (position, user_id, text) VALUES (?, ?, ?)",
            (position, user_id, text)
        )
        await db.commit()

async def del_entry(user_id, position):
    async with aiosqlite.connect("db/database.db") as db:
        await db.execute(
            "DELETE FROM entries WHERE user_id = ? AND position = ?",
            (user_id, position)
        )
        await db.execute(
            "UPDATE entries SET position = position - 1 WHERE user_id = ? AND position > ?",
            (user_id, position)
        )
        await db.commit()

async def get_entry(user_id, position):
    async with aiosqlite.connect("db/database.db") as db:
        async with db.execute(
            "SELECT * FROM entries WHERE user_id = ? AND position = ?",
            (user_id, position)
        ) as cursor:
            temp = await cursor.fetchone()
            return temp[2] if temp else None
        
async def save_edited_entry(user_id, text, position):
    async with aiosqlite.connect("db/database.db") as db:
        await db.execute(
            "UPDATE entries SET text = ? WHERE position = ? AND user_id = ?",
            (text, position, user_id)
        )
        await db.commit()

async def get_reading_position(user_id):
    async with aiosqlite.connect("db/database.db") as db:
        async with db.execute(
            "SELECT position FROM reading_position WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            temp = await cursor.fetchone()
            return temp[0] if temp else None

async def update_reading_position(user_id, position):
    async with aiosqlite.connect("db/database.db") as db:
        await db.execute(
            "REPLACE INTO reading_position (user_id, position) VALUES (?, ?)",
            (user_id, position)
        )
        await db.commit()

async def update_reading_positions_after_del_first_entry(user_id):
    async with aiosqlite.connect("db/database.db") as db:
            await db.execute(
                "UPDATE reading_position SET position = position - 1 WHERE user_id = ?",
                (user_id,)
            )
            await db.commit()