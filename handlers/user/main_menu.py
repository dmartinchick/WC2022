from loguru import logger
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from keyboards.inline_keyboard import MainMenuKeyboard


async def start_main_menu(message: Message | CallbackQuery):

    markup = await MainMenuKeyboard(1).make_keyboard()

    if isinstance(message, Message):
        await message.answer(
            text='Главное меню',
            reply_markup=markup
        )
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.answer(
            text='Главное меню',
            reply_markup=markup
        )


async def test(call: CallbackQuery):
    logger.info(call)


async def show_bettors_rating(call: CallbackQuery, *args):

    logger.info(f'callback_data: {call.data}; args: {args}')
    await call.message.answer(
        text="рейтинг прогнозистов"
    )


async def show_matches_of_the_day(call: CallbackQuery, *args):

    logger.info(f'callback_data: {call.data}; args: {args}')
    await call.message.answer(
        text="Матчи игрового дня"
    )


async def show_all_matches(call: CallbackQuery, *args):

    logger.info(f'callback_data: {call.data}; args: {args}')
    await call.message.answer(
        text="Все матчи"
    )


async def show_my_bets(call: CallbackQuery, *args):

    logger.info(f'callback_data: {call.data}; args: {args}')
    await call.message.answer(
        text="Мои прогнозы"
    )


async def navigate(call: CallbackQuery):

    chapter, category, item_id = call.data.split(sep=':')
    await navigate_to_category(call, category=category, item_id=int(item_id))


async def navigate_to_category(call: CallbackQuery, category: str, item_id: int):

    categories = {
        'betteros_rating': show_bettors_rating,
        'matches_of_the_day': show_matches_of_the_day,
        'all_matches': show_all_matches,
        'my_bets': show_my_bets
    }
    curent_category_function = categories[category]
    await curent_category_function(call, category, item_id)


def register_main_menu(dp: Dispatcher):
    dp.register_message_handler(start_main_menu, commands=['menu'], state="*")
    dp.register_callback_query_handler(navigate, text_contains='main_menu')
