"""Модуль определения таблиц ДБ"""
from enum import Enum
from dataclasses import dataclass


class State(Enum):
    ADMIN: 1
    REGULAR: 2


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    state: State


class Country(Enum):
    pass


@dataclass
class Team:
    id: int
    name: Country
    logo: str
