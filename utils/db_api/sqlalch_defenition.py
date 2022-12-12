"""Модуль определения таблиц ДБ"""
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class Country(Enum):
    pass


class State(Enum):
    ADMIN: 1
    REGULAR: 2


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    state: State


@dataclass
class Team:
    id: int
    name: str
    country: Country
    logo: str


@dataclass
class Result:
    home_team_goals: int
    guest_team_goals: int


@dataclass
class MatchInfo:
    id: int
    datetime_start: datetime
    stadium: str
    league: str


@dataclass
class Match:
    id: int
    home_team: Team
    guest_team: Team
    match_info: MatchInfo


@dataclass
class MatchResult:
    id: int
    match: Match
    result: Result


@dataclass
class Bet:
    id: int
    user: User
    match: Match
    bet: Result
