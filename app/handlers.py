from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

import app.keyboards as kb

router = Router()

 # роутер для старта
@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(
        photo = 'AgACAgIAAxkBAAMGZ_W9HvQRnVGYwJ_1jFto_W2JsS8AAoz3MRv7bahLrqQEdRvoU1IBAAMCAANtAAM2BA',
        caption = '',
    reply_markup = kb.main_menu
        )

# кнопка прайс
@router.callback_query(F.data == 'price')
async def contacts(callback: CallbackQuery):
    await callback.answer('Вы перешли в раздел прайс.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='Прайс наших картингов:',
            reply_markup = kb.catalog
        )
    else:
        await callback.message.edit_text(
            text='Прайс наших картингов:',
            reply_markup = kb.catalog
        )
# кнопка назад из прайса
@router.callback_query(F.data == 'back_price')
async def cart(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.main_menu
    )

# кнопка инфо
@router.callback_query(F.data == 'info')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку информация.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='Текст по информации...',
            reply_markup=kb.info
        )
    else:
        await callback.message.edit_text(
            text='Текст по информации...',
            reply_markup=kb.info
        )
# кнопка назад из инфо
@router.callback_query(F.data == 'back_info')
async def cart(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.main_menu
    )

# кнопка отзывы
@router.callback_query(F.data == 'feedback')
async def contacts(callback: CallbackQuery):
    await callback.answer('Вы перешли в раздел отзывы.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='Телеграм канал с отзывами:',
            reply_markup = kb.feedback
        )
    else:
        await callback.message.edit_text(
            text='Телеграм канал с отзывами:',
            reply_markup = kb.feedback
        )
# кнопка назад из отзывов
@router.callback_query(F.data == 'back_feedback')
async def cart(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.main_menu
    )

# кнопка связь с менеджером
@router.callback_query(F.data == 'communication')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку связь с менеджером.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption=' Связаться с нами: \n Номер телефона: +7 800 555 35 35',
            reply_markup=kb.communication
        )
    else:
        await callback.message.edit_text(
            text=' Связаться с нами: \n Номер телефона: +7 800 555 35 35',
            reply_markup=kb.communication
        )
# назад из связи
@router.callback_query(F.data == 'back_communication')
async def cart(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.main_menu
    )

# кнопка карт1
@router.callback_query(F.data == 'cart1')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку карт1.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='карт1',
            reply_markup=kb.cart_order
        )
    else:
        await callback.message.edit_text(
            text='карт1',
            reply_markup=kb.cart_order
        )
# назад из карт1
@router.callback_query(F.data == 'back_cart_order')
async def cart(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.catalog
    )


# связь с менеджером для вкладки карт1
@router.callback_query(F.data == 'communication_order')
async def info_order(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку связь с менеджером.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption=' Связаться с нами: \n Номер телефона: +7 800 555 35 35',
            reply_markup=kb.communication_order
        )
    else:
        await callback.message.edit_text(
            text=' Связаться с нами: \n Номер телефона: +7 800 555 35 35',
            reply_markup=kb.communication_order
        )
# назад из связи с менеджером карт1
@router.callback_query(F.data == 'back_communication_order')
async def cart(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.cart_order
    )

'''
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото:  {message.photo[-1].file_id}')
'''