"""Модуль Эхо бота"""
from aiogram import types
from aiogram import Dispatcher


async def echo(message: types.Message):
    await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)
