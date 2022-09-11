"""Точка входа"""
from loader import dp
from aiogram import executor

import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    """
    Запуск стартовых функции бота
    Args:
        dispatcher:Диспетчер

    Returns:
    """
    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
