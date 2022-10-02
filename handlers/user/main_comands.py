from aiogram import Dispatcher
from aiogram.types import Message


async def send_welcome(message: Message):
    await message.answer("Привет, я телеграм бот "
                         "прогнозов Чемпионата Мира "
                         "по футболу 2022 года. "
                         "Что бы приступить к игре нажми кнопку 'МЕНЮ'")


async def send_help(message: Message):
    await message.answer("Вывод справики.")


def register_main_comands(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"], state="*")
    dp.register_message_handler(send_help, commands=['help'], state="*")
