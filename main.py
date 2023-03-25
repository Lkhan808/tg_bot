from aiogram.utils import executor
from aiogram import types

from bot_DB.bot_db import sql_create
from handlers import client
from config import dp, bot, storage
from handlers import callback, admin, FSM_ADMIN_MENTHOR, scheduler


# from configurations import extra

async def on_startup(_):
    await scheduler.set_scheduler()
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
FSM_ADMIN_MENTHOR.register_handlers_FSM(dp=dp)

# extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
