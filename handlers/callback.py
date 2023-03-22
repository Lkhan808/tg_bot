from config import bot, dp
from aiogram import types, Dispatcher


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС", callback_data="button_2")
    markup.add(button_1)
    question = 'кто ответственный за лопату?'
    answer = [
        'я',
        'не знаю',
        'Зубенко Михаил Петрович']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Я-футбольный мячик',
        reply_markup=markup)


@dp.callback_query_handler(text="button_2")
async def quiz_3(call: types.CallbackQuery):
    question = 'сколько на планете материков?'
    answer = [
        '2',
        '96',
        'Я футбол не смотрю',
        '6']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Ну ты тупой конечно')


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
