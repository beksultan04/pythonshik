import asyncio
import logging

from aiogram.types import Message

import crud
from user import keyboards
from bot_bs_cal import tracking
from core.config import tasks, bot


async def start_tracking(message: Message):
    user_id = message.from_user.id

    if user_id in tasks:
        await message.answer('⛔️ Отслеживание уже активировано!')
    else:
        params = await crud.get_user(user_id)
        if not params:
            await message.answer('❌ Не удалось получить данные пользователя.')
            return
        
        task = asyncio.create_task(tracking(params))
        tasks[user_id] = task
        await message.answer('✅ Отслеживание активировано')


async def stop_tracking_(user_id: int):
    if user_id in tasks:
        tasks[user_id].cancel()
        try:
            await tasks[user_id]
        except asyncio.CancelledError:
            logging.info(f'Задача для пользователя {user_id} была успешно отменена.')
            await bot.send_message(user_id, '⛔️ Отслеживание остановлено', reply_markup=keyboards.main(user_id))

        del tasks[user_id]
    else:
        await bot.send_message(user_id, '⚠️ Отслеживание неактивно', reply_markup=keyboards.main(user_id))
