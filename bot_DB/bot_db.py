import sqlite3
import random
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors "
        "(id INTEGER PRIMARY KEY, fullname TEXT, "
        "direction TEXT, age INTEGER, "
        "gruppa TEXT)"
    )
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors ").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id,
                           f"id - {random_user[0]}, \nИмя - {random_user[1]}, \nНаправление - {random_user[2]}, \n"
                           f"Возраст - {random_user[3]}, \nГруппа - {random_user[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(mentor_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (int(mentor_id),))
    db.commit()


async def sql_commands_get_all_id():
    return cursor.execute('SELECT id FROM mentors').fetchall()
