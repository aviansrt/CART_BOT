from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(
        photo = 'AgACAgIAAxkBAAMGZ_W9HvQRnVGYwJ_1jFto_W2JsS8AAoz3MRv7bahLrqQEdRvoU1IBAAMCAANtAAM2BA',
        caption = 'текст про компанию и тп...',
    reply_markup = kb.main_menu
        )

'''
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото:  {message.photo[-1].file_id}')
'''