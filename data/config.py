"""Модуль настроек"""
from dataclasses import dataclass
from environs import Env


@dataclass
class DbConfig:
    """
    Класс настроек ДБ
    """
    host: str
    password: str
    port: int
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    # db: DbConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        )
    )
