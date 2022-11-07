"""Точка входа"""
import sys

from loguru import logger

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import load_config
from handlers.user.main_comands import register_main_comands
from handlers.user.main_menu import register_main_menu
from handlers.echo import register_echo


@logger.catch
def main():
    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()

    dp = Dispatcher(bot, storage=storage)

    register_main_comands(dp)
    register_main_menu(dp)
    register_echo(dp)

    executor.start_polling(dp)


if __name__ == '__main__':
    log = logger.add(sys.stderr, format="{time} - {level}: {message}", level="DEBUG")
    main()
