from functools import wraps
from datetime import datetime, UTC

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

import crud
from user import keyboards
from states import UserForm
from core.config import settings


class PrivateChatFilterAdmin(BaseFilter):
    async def __call__(self, message_callback: Message | CallbackQuery) -> bool:
        chat_type = message_callback.chat.type if isinstance(message_callback, Message) else message_callback.message.chat.type

        if chat_type != 'private':
            if isinstance(message_callback, CallbackQuery):
                await message_callback.delete()
            return False

        return message_callback.from_user.id == settings.ADMIN_ID


async def has_keys(user_id: int) -> bool:
    keys = await crud.get_keys(user_id)
    return bool(keys.get('api_key') and keys.get('api_secret'))


async def check_params(user_id: int) -> str:
    params = await crud.get_user(user_id)
    missing_params = {
        'symbol': 'Вы не выбрали торговую пару.',
        'trade_amount': 'Вы не ввели количество токенов.\n\nВведите 💰 чтобы назначить',
        'stop_buy_limit': 'Вы не назначили нижний предел покупки.\n\nВведите 📉 чтобы назначить',
        'stop_sell_limit': 'Вы не назначили верхний предел продажи.\n\nВведите 📈 чтобы назначить',
        'buy_percentage': 'Вы не ввели значение покупки при снижении цены в %.\n\nВведите <b><u>покупка↓</u></b> чтобы назначить',
        'trade_frequency': 'Вы не ввели значение интенсивности опроса биржи в секундах.\n\nВведите ⏳ чтобы назначить'
    }

    for param, message in missing_params.items():
        if not params.get(param):
            return message

    return 'ok'


async def is_access(user_id: int) -> bool:
    subs_end = await crud.get_subs_end(user_id)
    return subs_end and datetime.now(UTC) < subs_end


def check_keys(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user_id = args[0].from_user.id
        state = kwargs.get('state')

        if not await is_access(user_id):
            text = 'У вас закончился доступ к боту. Для продолжения использования бота оплатите подписку'
            kb = keyboards.buy_subs()
        elif not await has_keys(user_id):
            text = 'Для продолжения использования бота, отправьте <b>access_key</b>'
            kb = None
            await state.set_state(UserForm.wait_access_key)
        else:
            return await func(*args, **kwargs)

        # Отправляем сообщение в зависимости от типа (Message или Callback)
        message = args[0].message if isinstance(args[0], CallbackQuery) else args[0]
        await message.answer(text, reply_markup=kb)

    return wrapper


def get_month_text(month: int) -> str:
    endings = {1: 'месяц', 2: 'месяца', 3: 'месяца', 4: 'месяца'}
    return f'{month} {endings.get(month, "месяцев")}'
