"""Модуль для подуключения к БД"""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base
from data.config import load_config

config = load_config('.env')

engine = create_engine(
    url=f"postgresql+psycopg2:"
        f"//{config.db.user}"
        f":{config.db.password}"
        f"@{config.db.host}"
        f":{config.db.port}"
        f"/{config.db.database}",
    echo=True)
Base = declarative_base(bind=engine)
