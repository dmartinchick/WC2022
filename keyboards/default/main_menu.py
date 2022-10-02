from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = KeyboardButton('Главное меню')
main_menu_button = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu)
