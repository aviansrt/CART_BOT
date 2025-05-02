import pytz
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State


from datetime import datetime
import app.keyboards as kb
from config import TARGET_CHAT, MAX_LENGTH

router = Router()

# группировка полей для формы регистрации
class Form(StatesGroup):
    name = State()
    phone_num = State()
    age = State()
    crowd = State()
    time_order = State()


class Feed_back(StatesGroup):
    feed_back = State()


 # роутер для старта
@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(
        photo = 'AgACAgIAAxkBAAMDaBKF8fkYawznPGHO27duzvwtrPgAAiDwMRscuplIKpKVJ_tBxBgBAAMCAAN5AAM2BA',
    reply_markup = kb.main_menu
        )

'''
# ограничитель на количество символов
@router.message(F.text) # фильтр для всех текстовых сообщений
async def limiter(mess: Message):
    overstate = len(mess.text) - MAX_LENGTH
    if len(mess.text) > MAX_LENGTH:
        await mess.answer(f"лимит символов превышен на {overstate} !")
        return
'''

# проверка на количество символов
@router.message(lambda messange: len(messange.text or "") > MAX_LENGTH) # лямбда - условие. Если длинна вводимого текста больше константы, а-та-та
async def max_len(mess: Message):
    await mess.answer(f'Сообщение слишком длинное! максимум {MAX_LENGTH}')

# проверка на ссылки
@router.message(F.text.contains("http://") | F.text.contains("https://")) # если в тексте есть такая дичь, то а-та-та сразу
async def linc_guard(mess: Message):
    await mess.answer('Ссылки запрещены!')



######################################################## К ОТЗЫВАМ ДОБАВИЛ КЛАВИАТУРУ
# тут реагирование на кнопку отзывы
@router.callback_query(F.data == 'feedback')
async def feedback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Ваш отзыв, пожалуйста!')
    await state.set_state(Feed_back.feed_back)
    await callback.answer()


@router.message(Feed_back.feed_back)
async def output(mess: Message, state: FSMContext, bot: router):
    # Получаем текст сообщения
    feedback_text = mess.text

    # Сохраняем в состояние
    await state.update_data(feedback=feedback_text)

    try:
        # Получаем данные из состояния
        user_feedback = await state.get_data()

        # Проверяем наличие данных
        if 'feedback' not in user_feedback:
            await mess.answer("Произошла ошибка при обработке отзыва. Попробуйте еще раз.")
            return

        # Формируем сообщение
        response = f"#ОТЗЫВЫ\n{user_feedback['feedback']}"

        # Отправляем в целевой чат
        await bot.send_message(chat_id=TARGET_CHAT, text=response)
        await mess.answer('Спасибо за отзыв!')

        # Очищаем состояние
        await state.clear()

    except TelegramBadRequest as e:
        await mess.answer(f"Проверьте наличие бота в приемном канале и наличие у него прав администратора. Ошибка: {e}")
    except Exception as e:
        await mess.answer(f"Произошла непредвиденная ошибка: {e}")


# тут реагирование на кнопку записаться
@router.callback_query(F.data == 'order')
async def form_context(callback: CallbackQuery, state: FSMContext):
    """ вместо message - callback, потому что при нажатии на кнопку
не высвечивалось сообщение с просьбой ввести имя, потому что реакция и на то и на другое не возможна. Пришлось так """
    await callback.message.answer('Введите имя')
    await state.set_state(Form.name)
    await callback.answer() # закрыть callback для того, чтобы оно в себя приняло только имя

# тут имя сохраняется и идет запрос для возраста
@router.message(Form.name)
async def reg_name(mess: Message, state: FSMContext):
    await state.update_data(name = mess.text)
    await state.set_state(Form.age)
    await mess.answer('Введите свой возраст')

# сохранение и запрос на время
@router.message(Form.age)
async def reg_age(mess: Message, state: FSMContext):
    await state.update_data(age = mess.text)

    if not 5 < int(mess.text) < 100:
        await mess.answer('Введите корректный возраст.')
        return

    await state.set_state(Form.time_order)
    await mess.answer('Введите день и время, в которые хотели бы посетить наш клуб(xx.yy.20nn и время)')

# сохранение и запрос на количество человек
@router.message(Form.time_order)
async def reg_time(mess: Message, state: FSMContext):
    await state.update_data(time_order = mess.text)
    await state.set_state(Form.crowd)
    await mess.answer('Введите количество человек, которое посетит нас')

# сохранение и запрос на номер телефона
@router.message(Form.crowd)
async def reg_crowd(mess: Message, state: FSMContext):
    await state.update_data(crowd = mess.text)
    await state.set_state(Form.phone_num)
    await mess.answer('Введите свой номер телефона(По виду 7 *** *** ** **)')

# сохранение всех данных и их вывод.
@router.message(Form.phone_num)
async def reg_num_and_close_form(mess: Message, state: FSMContext, bot: router):

    # валидация номера телефона, она простейшая, вероятность маленькая, но быть может, попросят переписать
    if (len(mess.text) != 11) or not any(char.isdigit() for char in mess.text): # Методы для строк. Isdigit - проверка на цифры.
        await mess.answer("Пожалуйста, введите корректный номер телефона")
        return # обрывание функции, для повторного использования функции

####################### ТУТ ВИДОИЗМЕНИЛ ТЕКСТ ПОСЛЕ РЕГИСТРАЦИИ
    # сохранение номера и создание объекта, который отдает все данные
    await mess.answer('''Спасибо, регистрация завершена. \nС вами скоро свяжется наш менеджер.
    Помните также, что услугу оплатить может только лицо, достигшее 18 лет. Учитывайте, что персонал может запросить документ, для удостоверения возраста''')

########################### ТУТ ДОБАВИЛ ВЫВОД ДОКУМЕНТА С ТЕХНИКОЙ БЕЗОПАСНОСТИ
    await bot.send_document(
        chat_id=mess.chat.id,
        document="BQACAgIAAxkBAAMeaBKLEFbG2RqKPIdg9MzDgjnkY5gAAppoAAL-fJhInsj5ZsOasn02BA",
        caption="Техника Безопасности(!Обязательно к ознакомлению!)"
    )
    await state.update_data(number=mess.text)
    user_data = await state.get_data()

    # хрень для вывода всей полученной информации
    response = (
        "✅ #Заявка от нового пользователя!\n"
        f" Имя: {user_data['name']}\n"
        f" Возраст: {user_data['age']}\n"
        f" Время: {user_data['time_order']}\n"
        f" Количество человек: {user_data['crowd']}\n"
        f" Телефон: {user_data['number']}\n"
        f"---------------------------------------\n"
        f" Заявка отправлена: {datetime.now(pytz.timezone('Europe/Moscow')).strftime("%H:%M, %d.%m.%Y")}"
    )

    # проверка на наличие ошибок и несоответствий
    try:
        await bot.send_message(chat_id=TARGET_CHAT, text=response)
    except TelegramBadRequest as e:
        await mess.answer(f"Проверьте наличие бота в приемном канале и наличие у него прав администратора. Ошибка: {e}")
    except Exception as e:
        await mess.answer(f"Неизвестная Ошибка: {e}")

    await state.clear()  # очистка состояния (ВАЖНО!!!!)

########################### НА ОКНЕ ПРАЙСА ТЕПЕРЬ ИЗОБРАЖЕНИЕ САМОГО ПРАЙСА, КОТОРЫЙ КИДАЛ АРУТ
# кнопка прайс
@router.callback_query(F.data == 'price')
async def show_price(callback: CallbackQuery, bot: router):
    await callback.answer('Вы перешли в раздел прайс.')

    await bot.send_photo(photo = 'AgACAgIAAxkBAAMFaBKGGg3y2aA6MXw3X3LkiBZBDLQAAirwMRscuplIVQyNlnZWJDgBAAMCAAN5AAM2BA',
                         chat_id= callback.from_user.id,
                         reply_markup=kb.catalog)
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.catalog
    )
    await callback.message.delete()


############################## ЭТА ХРЕНЬ ОТПРАВЛЯЕТ НОВОЕ СООБЩЕНИЕ С ГЛАВНЫМ МЕНЮ, НЕ УДАЛЯЯ СТАРОЕ. (ТОЛЬКО ПРИ ВЫХОДЕ ИЗ ПРАЙСА)
# кнопка назад из прайса
@router.callback_query(F.data == 'back_price')
async def cart(callback: CallbackQuery, bot: router):
    await callback.answer('Вы вернулись назад.')
    await bot.send_photo(photo = 'AgACAgIAAxkBAAMDaBKF8fkYawznPGHO27duzvwtrPgAAiDwMRscuplIKpKVJ_tBxBgBAAMCAAN5AAM2BA',
                         chat_id= callback.from_user.id,
                         reply_markup=kb.main_menu)
    await callback.message.edit_caption(
        caption='',
        reply_markup=kb.main_menu
    )
    await callback.message.delete()

# кнопка инфо
@router.callback_query(F.data == 'info')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку информация.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='''Мы Даем вам возможность почувствовать эмоции, которые вы до этого не испытывали никогда
                    Мы - ДрайвКарт. Мы - скорость и адреналин.
                    t.me/drivekart_adler''',
            reply_markup=kb.info
        )
    else:
        await callback.message.edit_text(
            text='''Мы Даем вам возможность почувствовать эмоции, которые вы до этого не испытывали никогда
                    Мы - ДрайвКарт. Мы - скорость и адреналин.
                    t.me/drivekart_adler''',
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

@router.callback_query(F.data == 'back_feedback')
async def back_from_feedback(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад.')
    await callback.message.edit_text(  # Используем edit_text вместо edit_caption
        text='Вы вернулись в главное меню!',  # Можно оставить пустым или добавить текст
        reply_markup=kb.main_menu
    )


############################################# ЗАМЕНИЛ КОНТАКТНЫЕ ДАННЫЕ
# кнопка связь с менеджером
@router.callback_query(F.data == 'communication')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку связь с менеджером.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption=' Связаться с нами: \n Номер телефона: +7 918 201 8008',
            reply_markup=kb.communication
        )
    else:
        await callback.message.edit_text(
            text=' Связаться с нами: \n Номер телефона: +7 918 201 8008',
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
    await callback.answer('Вы перешли во вкладку "Взрослый 9Л.С".')
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
# кнопка карт2
@router.callback_query(F.data == 'cart2')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку "Взрослый 11Л.С".')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='карт2',
            reply_markup=kb.cart_order
        )
    else:
        await callback.message.edit_text(
            text='карт2',
            reply_markup=kb.cart_order
        )

# кнопка карт3
@router.callback_query(F.data == 'cart3')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку "Дуо".')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='карт3',
            reply_markup=kb.cart_order
        )
    else:
        await callback.message.edit_text(
            text='карт3',
            reply_markup=kb.cart_order
        )

# кнопка карт4
@router.callback_query(F.data == 'cart4')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку "Турнир".')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='карт4',
            reply_markup=kb.cart_order
        )
    else:
        await callback.message.edit_text(
            text='карт4',
            reply_markup=kb.cart_order
        )


# кнопка карт4
@router.callback_query(F.data == 'cart5')
async def info(callback: CallbackQuery):
    await callback.answer('Вы перешли в "Аренда трека".')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption='карт4',
            reply_markup=kb.cart_order
        )
    else:
        await callback.message.edit_text(
            text='карт4',
            reply_markup=kb.cart_order
        )


################################################## КНОПКА НАЗАД ИЗ ЛЮБОГО КАРТА, С УДАЛЕНИЕМ УЖЕ ПРЕДЫДУЩЕГО СООБЩЕНИЯ
# назад из любого карта
@router.callback_query(F.data == 'back_cart_order')
async def back_to_main_menu(callback: CallbackQuery, bot: router):
    await callback.answer("Возвращаемся в главное меню")
    await callback.message.delete()
    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo='AgACAgIAAxkBAAIBRmgSglAiyZvceTdFigb_acUZ63aIAAIg8DEbHLqZSCKYMKsqye3_AQADAgADeQADNgQ',
        caption="Добро пожаловать в главное меню",
        reply_markup=kb.main_menu
    )


# связь с менеджером для любого карта
@router.callback_query(F.data == 'communication_order')
async def info_order(callback: CallbackQuery):
    await callback.answer('Вы перешли во вкладку связь с менеджером.')
    if callback.message.photo:
        await callback.message.edit_caption(
            caption=' Связаться с нами: \n Номер телефона: +7 918 201 8008',
            reply_markup=kb.communication_order
        )
    else:
        await callback.message.edit_text(
            text=' Связаться с нами: \n Номер телефона: +7 918 201 8008',
            reply_markup=kb.communication_order
        )


# назад из связи с менеджером для любого карта
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


################################## ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ АЙДИШНИКА ДЛЯ ДОКУМЕНТОВ.
'''
@router.message(F.document)  # Ловим все документы
async def handle_document(message: Message):
    file_id = message.document.file_id
    print(f"File ID документа: {file_id}")
    await message.answer(f"File ID: `{file_id}`", parse_mode="Markdown")
'''