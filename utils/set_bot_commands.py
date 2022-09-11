"""Установка команд бота"""
from aiogram.types import BotCommand


async def set_default_commands(dp):
    """
    Установка команд бота
    Args:
        dp: Диспетчер
    """
    await dp.bot.set_my_commands(
        [
            BotCommand('menu', 'Показать главное меню'),
            BotCommand('start', 'Запустить бота'),
            BotCommand('help', 'Вызов справки')
        ]
    )
