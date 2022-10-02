"""Точка входа"""
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import load_config
from handlers.user.main_comands import register_main_comands
from handlers.user.main_menu import register_main_menu
from handlers.echo import register_echo


def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-4s [%(asctime)s] - %(name)s - %(message)s',
        )

    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    register_main_comands(dp)
    register_main_menu(dp)
    register_echo(dp)

    executor.start_polling(dp)


if __name__ == '__main__':
    main()
