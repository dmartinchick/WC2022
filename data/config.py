"""Модуль настроек"""
from environs import Env

env = Env()
env.read_env()

# Данные для подключения к Телеграммботу
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
# IP = env.str("ip")
