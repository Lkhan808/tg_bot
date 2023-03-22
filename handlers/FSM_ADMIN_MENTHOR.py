from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_DB.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.id.set()
        await message.answer('введи id ментора, лох')
    else:
        await message.answer('пиши в личку боту')


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if not message.text.isdigit():
            await message.answer('id это только цифры!')
        else:
            data['id'] = message.text
            await FSMAdmin.next()
            await message.answer('как зовут')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isdigit():
            await message.answer('в имени не должно быть чисел!')
        else:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.answer('какое направление?')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isdigit():
            await message.answer('без цифр!')
        else:
            data['direction'] = message.text
            await FSMAdmin.next()
            await message.answer('сколько лет?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if not message.text.isdigit():
            await message.answer(' только цифры!')
        elif int(message.text) > 50:
            print('таких старых нет')
        elif int(message.text) < 16:
            print('таких мелких нет')
        else:
            data['age'] = message.text
            await FSMAdmin.next()
            await message.answer('какая группа?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"id - {data['id']},\n"
                             f"имя - {data['name']},\nнаправление - {data['direction']},\nвозраст - {data['age']}, \n"
                             f"группа - {data['group']}")
        await FSMAdmin.next()
        await message.answer('все правильно?\n да/нет')


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('регистрация завершена')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('отмена!')
    else:
        await message.answer('не понимаю тебя ')


def register_handlers_FSM(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'], commands_prefix='!/')
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
