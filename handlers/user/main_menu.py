from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from keyboards.inline_keyboard import MainMenuKeyboard


async def start_main_menu(message: Message | CallbackQuery):

    markup = await MainMenuKeyboard(1).make_keyboard()

    if isinstance(message, Message):
        await message.answer(
            text='Главное меню',
            reply_markup=markup
        )
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.answer(
            text='Главное меню',
            reply_markup=markup
        )


def register_main_menu(dp: Dispatcher):
    dp.register_message_handler(start_main_menu, commands=['menu'], state="*")
