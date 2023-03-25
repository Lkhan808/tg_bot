from aiogram import types, Dispatcher
from config import ADMIN, bot, dp
from bot_DB.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMIN:
            await message.answer("ТЫ НЕ МОЙ БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")


async def pin(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer('вы не можете закреплять сообщения так как вы не админ')
    elif message.from_user.id in ADMIN:
        if not message.reply_to_message:
            pass
        else:
            await message.pin(message.reply_to_message.from_user.id)
            await message.answer(
                f'{message.from_user.first_name} pinned {message.reply_to_message.from_user.first_name}s message')


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer('вы не админ')
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(f"id - {user[0]},\n"
            f"имя - {user[1]},\nнаправление - {user[2]},\nвозраст - {user[3]}, \n"
            f"группа - {user[4]}",
            reply_markup = InlineKeyboardMarkup.add(InlineKeyboardButton(f"Delete {user[1]}",callback_data=f"Delete{user[0]}")))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(id=call.data.replace("Delete ", ""))
    await call.answer(text="deleted", show_alert=True)
    await call.message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("Delete"))