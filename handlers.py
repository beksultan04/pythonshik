import logging
import traceback

import aiogram.exceptions
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import crud
from core.config import bot
from admin import keyboards
from states import AdminForm
from utils import PrivateChatFilterAdmin

router = Router()


@router.message(F.text == 'Админ панель', PrivateChatFilterAdmin())
async def admin_panel(message: Message):
    """Открываем админ-панель по тексту 'Админ панель'."""
    await message.answer(
        'Добро пожаловать в <b>Админ панель</b>',
        reply_markup=keyboards.admin_panel()
    )


@router.callback_query(F.data == 'admin_panel', PrivateChatFilterAdmin())
async def admin_panel_callback(callback: CallbackQuery, state: FSMContext):
    """Открываем админ-панель по кнопке."""
    await state.clear()
    await callback.message.edit_text(
        'Добро пожаловать в <b>Админ панель</b>',
        reply_markup=keyboards.admin_panel()
    )


@router.callback_query(F.data == 'find_user', PrivateChatFilterAdmin())
async def find_user(callback: CallbackQuery, state: FSMContext):
    """Запрашиваем ID пользователя."""
    await state.set_state(AdminForm.find_user)
    msg = await callback.message.edit_text('Введите <b>Telegram ID</b> пользователя', reply_markup=keyboards.back())
    await state.update_data(info_msg_id=msg.message_id)


@router.message(F.text, AdminForm.find_user, PrivateChatFilterAdmin())
async def find_user_valid(message: Message, state: FSMContext):
    """Обработка введенного ID."""
    user_id = message.text
    if not user_id.isdigit():
        await message.answer('❗️ Введите число!')
        return

    user_info = await crud.get_user(int(user_id))
    if not user_info:
        await message.answer('❌ Такого пользователя нет в базе данных.')
        return

    # Получаем сохранённый ID сообщения для удаления
    data = await state.get_data()
    info_msg_id = data.get('info_msg_id')

    # Очищаем состояние
    await state.clear()

    # Удаляем сообщение с вводом ID
    if info_msg_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=info_msg_id)
        except:
            pass

    # Формируем информацию о пользователе
    username = f"@{user_info['username']}" if user_info.get('username') else 'Отсутствует'
    
    await message.answer(
        text=(
            f'👤 <b>ID:</b> {user_info["id"]}\n'
            f'👤 <b>Username:</b> {username}\n'
        ),
        reply_markup=keyboards.back()
    )


@router.message(F.text, F.reply_to_message, PrivateChatFilterAdmin())
async def reply_help_message(message: Message):
    """Ответ админа пользователю."""
    reply_msg = message.reply_to_message
    if not reply_msg.forward_from:
        await message.answer('❌ Невозможно отправить ответ. Пользователь не найден.')
        return

    text = f'<b>Ответ от Администратора:</b>\n\n<blockquote>{message.text}</blockquote>'

    try:
        # Отправляем сообщение пользователю
        await bot.send_message(chat_id=reply_msg.forward_from.id, text=text)
    except aiogram.exceptions.TelegramBadRequest:
        logging.error(traceback.format_exc())
