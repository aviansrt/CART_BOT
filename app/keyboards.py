from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

# клавиатура основного меню
main_menu = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Прайс', callback_data = 'price')],
    [InlineKeyboardButton(text = 'Инфо', callback_data = 'info')],
    [InlineKeyboardButton(text = 'Отзывы', callback_data = 'feedback')],
    [InlineKeyboardButton(text = 'Связь с менеджером', callback_data = 'communication')]
])

# клавиатура каталог
catalog = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Карт1', callback_data = 'cart1')],
    [InlineKeyboardButton(text = 'Карт2', callback_data = 'cart2')],
    [InlineKeyboardButton(text = 'Карт3', callback_data = 'cart3')],
    [InlineKeyboardButton(text = 'Карт4', callback_data = 'cart4')],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back_price')]
])

# инфо
info = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back_info')]
])

# клавиатура отзывы
feedback = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Перейти в канал', url = "https://t.me/foma_test")],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back_feedback')]
])

# обычная клавиатура для связи с менеджером
communication = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'WhatsApp', url = f"https://wa.me/{88005553535}")],
    [InlineKeyboardButton(text = 'Telegram', url = 'https://t.me/username')],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back_communication')]
])

# клавиатура 'связь с менеджером' для заказа
communication_order = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'WhatsApp', url = f"https://wa.me/{88005553535}")],
    [InlineKeyboardButton(text = 'Telegram', url = 'https://t.me/username')],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back_communication_order')]
])

# клавиатура карт1
cart_order = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Записаться', callback_data = 'order')],
    [InlineKeyboardButton(text = 'Связь с менеджером', callback_data = 'communication_order')],
    [InlineKeyboardButton(text = 'Выбрать другой картинг', callback_data = 'back_cart_order')]
])