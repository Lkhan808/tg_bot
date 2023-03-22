from aiogram import types, Dispatcher

from config import bot, dp
from bot_DB.bot_db import sql_command_random


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("LessGoooo!!!")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС", callback_data="button_1")
    markup.add(button_1)
    question = 'сколько океанов в мире?'
    answer = [
        '5',
        '8',
        '4',
        '12']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Их 4: Атлантический, Индийский, Тихий, Северный Ледовитый',
        reply_markup=markup)


@dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    p = open("cat.png", "rb")
    await bot.send_photo(chat_id=message.from_user.id, photo=p)


async def get_random_user(message: types.Message):
    random_user = sql_command_random()
    await message.answer(f"id - {random_user[0]},\n"
                         f"имя - {random_user[1]},\nнаправление - {random_user[2]},\nвозраст - {random_user[3]}, \n"
                         f"группа - {random_user[4]}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_meme, commands=['meme'])
    dp.register_message_handler(get_random_user, commands=['get'])
