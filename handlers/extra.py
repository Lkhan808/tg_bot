from random import choice

from config import dp, bot, ADMIN
from aiogram import types, Dispatcher


@dp.message_handler()
async def echo(message: types.Message):
    if not message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=message.text)
    else:
        await message.answer(text=int(message.text) ** 2)
    if message.text.lower() == 'game':
        dices = ['🎲', '🎯', '🏀', '⚽', '🎰']
        if message.from_user.id not in ADMIN:
            await message.answer('you are not an admin')
        else:
            a = choice(dices)
            await message.answer_dice(a)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)