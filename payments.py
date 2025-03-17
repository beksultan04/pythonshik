import logging
from datetime import datetime, UTC, timedelta

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import crud
import utils
from user import keyboards
from states import UserForm
from my_classes import crypto

router = Router()


@router.callback_query(F.data == 'buy_subs')
async def buy_mailing(callback: CallbackQuery, state: FSMContext):
    msg = await callback.message.edit_text(
        'Напишите на какое кол-во месяцев хотите купить подписку'
    )
    await state.set_state(UserForm.wait_month)
    await state.update_data(info_msg=msg)


@router.message(F.text, UserForm.wait_month)
async def month_valid(message: Message, state: FSMContext):
    month = message.text

    if not month.isdigit():
        return await message.answer('Введите число')

    month = int(month)
    if month <= 0:
        return await message.answer('Введите число от 1')

    if month > 120:
        return await message.answer('Слишком большое число')

    data = await state.get_data()
    await data['info_msg'].delete()

    try:
        create_payment = await crypto.request(
            'createInvoice',
            {
                'amount': 10 * month,
                'asset': 'USDT',
                'allow_anonymous': 'false',
                'expires_in': 60 * 60,  # 1 час
                'payload': month
            }
        )
    except Exception as e:
        logging.error(f"Ошибка при создании инвойса: {e}")
        return await message.answer('Техническая ошибка, повторите попытку позже')

    if create_payment.get('status') == 200:
        await message.answer(
            f'<b>Оформление подписки на {utils.get_month_text(month)}</b>\n\n<i>После оплаты нажмите кнопку <u><b>Проверить</b></u></i>',
            reply_markup=keyboards.buy_mailing_confirm(
                create_payment['data']['result']['pay_url'],
                create_payment['data']['result']['hash']
            )
        )
    else:
        logging.warning(create_payment['data'])
        logging.warning(create_payment['status'])
        await message.answer('Техническая ошибка, повторите попытку позже')


@router.callback_query(F.data.startswith('checkInvoice:'))
async def check_invoice(callback: CallbackQuery):
    _, pay_hash = callback.data.split(':')
    offset = 0
    attempts = 0

    while attempts < 5:  # Ограничиваем количество попыток, чтобы избежать бесконечного цикла
        try:
            invoices = await crypto.get_invoices(offset)
        except Exception as e:
            logging.error(f"Ошибка при получении инвойсов: {e}")
            return await callback.answer('Ошибка при проверке платежа. Попробуйте позже.')

        if invoices.get('status') != 200:
            return await callback.answer('Ошибка при проверке платежа. Повторите позже.')

        for item in invoices['data']['result']['items']:
            if item['hash'] == pay_hash:
                month = int(item['payload'])
                await callback.message.delete()
                await crud.update_subs_end(callback.from_user.id, datetime.now(UTC) + timedelta(days=month * 31))
                return await callback.message.answer(f'<b>Покупка подтверждена! Вам продлена подписка на {utils.get_month_text(month)}</b>')
        
        # Если инвойс не найден, проверяем дальше
        if len(invoices['data']['result']['items']) == 1000:
            offset += 1000
        else:
            return await callback.answer('Вы не оплатили счёт')

        attempts += 1
        await asyncio.sleep(2)  # Небольшая пауза между запросами
