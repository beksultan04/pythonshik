# Доработанный код бота с учетом требований

from datetime import datetime, UTC, timedelta

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import crud
import utils
from my_classes import mexc
from states import UserForm
from user import functions, keyboards

router = Router()

# TODO: Добавить хранение настроек пользователя в ОЗУ с обновлением в БД
user_settings_cache = {}

def update_user_settings(user_id, key, value):
    if user_id not in user_settings_cache:
        user_settings_cache[user_id] = {}
    user_settings_cache[user_id][key] = value
    # Обновление в БД с периодичностью

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = await crud.get_user_language(user_id) or 'RU'
    
    if user_id not in user_settings_cache:
        user_settings_cache[user_id] = await crud.load_user_settings(user_id)
    
    welcome_text = utils.get_localized_text(lang, 'welcome_message')
    
    if not await crud.check_user_db(user_id):
        await crud.save_user(user_id, message.from_user.username)
    
    subs_end = await crud.get_subs_end(user_id)
    if subs_end:
        keys = await crud.get_keys(user_id)
        if keys.get('api_key') and keys.get('api_secret'):
            if await utils.is_access(user_id):
                check = await utils.check_params(user_id)
                if check == 'ok':
                    await functions.start_tracking(message)
                else:
                    await message.answer(check)
            else:
                await message.answer(
                    utils.get_localized_text(lang, 'subscription_expired'),
                    reply_markup=keyboards.buy_subs(lang)
                )
        else:
            await state.set_state(UserForm.wait_access_key)
            await message.answer(utils.get_localized_text(lang, 'send_access_key'))
    else:
        await message.answer(utils.get_localized_text(lang, 'demo_mode'))
        await state.set_state(UserForm.wait_access_key)

# TODO: Добавить мультиязычность и выбор языка при старте
@router.message(F.text.in_(['RU', 'EN']))
async def set_language(message: Message):
    user_id = message.from_user.id
    lang = message.text.upper()
    await crud.set_user_language(user_id, lang)
    update_user_settings(user_id, 'language', lang)
    await message.answer(utils.get_localized_text(lang, 'language_set'))

# TODO: Добавить отслеживание ордеров и уведомления
# TODO: Добавить систему ограничений, логику блокировок пользователей
# TODO: Реализовать поддержку админского чата с разными темами
# TODO: Обновить команды вызова помощи с учетом языков
# TODO: Ограничение пользователей в демо/платном режиме

# Остальной код обновлю по мере выполнения ТЗ