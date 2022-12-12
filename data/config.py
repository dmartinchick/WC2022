"""Модуль настроек"""
from dataclasses import dataclass
from environs import Env


@dataclass
class DbMySQLConfig:
    host: str
    password: str
    port: int
    user: str
    database: str


@dataclass
class DbPgConfig:
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
    db: DbPgConfig  # can use MySQLConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        db=DbPgConfig(
            host=env.str("PG_DB_HOST"),
            password=env.str("PG_DB_PASSWORD"),
            port=env.int("PG_DB_PORT"),
            user=env.str("PG_DB_USER"),
            database=env.str("PG_DB_NAME")
        )
    )
