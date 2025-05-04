from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

# клавиатура основного меню
main_menu = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Прайс 💰📋', callback_data = 'price')],
    [InlineKeyboardButton(text = 'Инфо ℹ️📢', callback_data = 'info')],
    [InlineKeyboardButton(text = 'Написать отзыв ✍️⭐', callback_data = 'feedback')],
    [InlineKeyboardButton(text = 'Связь с менеджером 👨💼📞', callback_data = 'communication')]
])


# клавиатура каталог
catalog = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Карт 9Л.С 🚗💨', callback_data = 'cart1')],
    [InlineKeyboardButton(text = ' Карт 11Л.С 🏁⚡', callback_data = 'cart2')],
    [InlineKeyboardButton(text = 'Детский 9Л.С 👶🚦', callback_data = 'cart_child')],
    [InlineKeyboardButton(text = ' Дуэт 👫🏎️', callback_data = 'cart3')],
    [InlineKeyboardButton(text = ' Турнир 🏆🎯', callback_data = 'cart4')],
    [InlineKeyboardButton(text = ' Аренда трека 🛣️🔧', callback_data = 'cart5')],
    [InlineKeyboardButton(text = '🔄 Назад ↩️', callback_data = 'back_price')]
])

# инфо
info = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '🔄 Назад ↩️', callback_data = 'back_info')]
])

# клавиатура отзывы
feedback = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '🔄 Назад ↩️', callback_data = 'back_feedback')]
])

# обычная клавиатура для связи с менеджером
communication = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'WhatsApp 💚📱', url = f"https://wa.me/{+79182018008}")],
    [InlineKeyboardButton(text = ' Telegram 📨✈️', url = 'https://web.telegram.org/k/#8198872775')],
    [InlineKeyboardButton(text = '🔄 Назад ↩️', callback_data = 'back_communication')]
])

# клавиатура 'связь с менеджером' для заказа
communication_order = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'WhatsApp 💚📱', url = f"https://wa.me/{+79182018008}")],
    [InlineKeyboardButton(text = 'Telegram 📨✈️', url = 'https://web.telegram.org/k/#8198872775')],
    [InlineKeyboardButton(text = '🔄 Назад ↩️', callback_data = 'back_communication_order')]
])

# клавиатура для всех картингов
cart_order = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '✅ Записаться 📅🏁', callback_data = 'order')],
    [InlineKeyboardButton(text = 'Связь с менеджером 👨💼📞', callback_data = 'communication_order')],
    [InlineKeyboardButton(text = '🔄 Назад / Главное меню ↩️🏠', callback_data = 'back_cart_order')]
])