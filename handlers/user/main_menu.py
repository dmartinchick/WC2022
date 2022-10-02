from aiogram import Dispatcher
from aiogram.types import Message

from keyboards.default.main_menu import main_menu_button


async def start_main_menu(message: Message):
    await message.answer(
        text="Главное меню",
        reply_markup=main_menu_button
    )


def register_main_menu(dp: Dispatcher):
    dp.register_message_handler(start_main_menu, commands=['menu'], state="*")
