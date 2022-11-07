from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Button:
    @staticmethod
    def make_main_menu_button(button_text: str) -> ReplyKeyboardMarkup:
        """
        create default button
        Returns:

        """
        main_menu = KeyboardButton(button_text)
        return ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu)


# main_menu = KeyboardButton('Главное меню')
# main_menu_button = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu)
