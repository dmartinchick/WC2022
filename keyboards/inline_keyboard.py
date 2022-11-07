from abc import ABC, abstractmethod
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from dataclasses import dataclass

from loguru import logger
import sys


@dataclass
class Category:
    item_text: str
    item_name: str


class Callback(ABC):

    @abstractmethod
    def make_callback(self):
        pass


class MainMenuCallback(Callback):

    def __init__(self):
        self.__callback_data = CallbackData(
            'mm',
            'category',
            'item_id'
        )

    def make_callback(self, category: str = '0', item_id: int = 0):
        return self.__callback_data.new(category, item_id)


class Keyboard(ABC):

    def __init__(self, row_width: int):
        self.row_width = row_width
        self.markup = InlineKeyboardMarkup(row_width=self.row_width)

    @property
    def row_width(self):
        return self.__row_width

    @row_width.setter
    def row_width(self, value):
        if not isinstance(value, int):
            raise TypeError('Значение row_width должно быть int')
        elif value < 0:
            raise ValueError('Значение row_width должно быть больше 0')
        else:
            self.__row_width = value

    @property
    def markup(self):
        return self.__markup

    @markup.setter
    def markup(self, ikbm: InlineKeyboardMarkup):
        self.__markup = ikbm

    async def add_button_back(self):
        self.markup.row(
            InlineKeyboardButton(
                text='В главное меню',
                callback_data=MainMenuCallback().make_callback()
            )
        )

    @abstractmethod
    async def make_keyboard(self) -> InlineKeyboardMarkup:
        pass


class MainMenuKeyboard(Keyboard):

    def __init__(self, row_width: int = 3):
        Keyboard.__init__(self, row_width)
        self.callback = MainMenuCallback()
        self.categories = [
            Category('Рейтингн прогнозистов', 'betteros_rating'),
            Category('Матчи игрового дня', 'matches_of_the_day'),
            Category('Все матчи и результаты ЧМ', 'all_matches'),
            Category('Мои прогнозы', 'my_bets')
        ]

    async def make_keyboard(self) -> InlineKeyboardMarkup:
        for category in self.categories:
            self.markup.insert(
                InlineKeyboardButton(
                    text=category.item_text,
                    callback_data=self.callback.make_callback(category.item_name)
                )
            )
        await self.add_button_back()
        return self.markup


@logger.catch
def main():
    kb = MainMenuKeyboard(4).make_keyboard()
    print(kb)


if __name__ == '__main__':
    logger.add(sys.stderr, format="{time} - {level}: {message}", level="DEBUG")
    main()

"""
    # Главное меню
    "{mm}:{category}:{item_id}"
        [Таблица прогнозистов]
        [Матчи игрового дня]
           >>> # Список матчей игрового дня
           - Карточка матча 1 -
           [Сделать/Изменить прогноз] [Удалить прогноз:опционально]
           [<< В главное меню]
           ...
           - Карточка матча 
        -
           [Сделать/Изменить прогноз] [Удалить прогноз:опционально]
           [<< В главное меню]
        [Все матчи и результаты ЧМ]
            >>> # Список групп
            - Карточка группы А -
            [Перейти к матчам группы]
            [<< В главное меню]
            ...
            - Карточка группы n -
            [Перейти к матчам группы]
            [<< В главное меню]
        [Мои прогнозы]
            >>> # История прогнозов 
            - карточка со списком прогнозов и их результатами -
            - карточка с прогнозом по матчу, который еще не начался -
            [Изменить прогноз]  [Удалить прогноз]
            [<< В главное меню]
        --    

    -Карточка группы-
    [Перейти к матчам группы]
    [<< В главное меню]
    
    -Картинка с логотипами матча и информацией о матче-
    [Сделать/изменить прогноз]  [Удалить прогноз]
    [<< В главное меню]
"""
