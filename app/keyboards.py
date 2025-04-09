from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

main_menu = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Цены', callback_data = 'cash')],
    [InlineKeyboardButton(text = 'Отзывы', callback_data = 'feedback')],
    [InlineKeyboardButton(text = 'О нас', callback_data = 'about_us')]
])


back = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
])