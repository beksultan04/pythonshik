from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_media_group import media_group_handler

from user import keyboards
from states import UserForm
from core.config import settings, bot

router = Router()


@router.message(Command('help'))
async def send_help(message: Message, state: FSMContext):
    """Команда /help. Очищает state и запрашивает у пользователя описание проблемы."""
    await state.clear()
    await state.set_state(UserForm.wait_help_message)

    msg = await message.answer(
        'Опишите свою проблему или вопрос администратору',
        reply_markup=keyboards.delete()
    )
    # Сохраняем ID сообщения для последующего удаления
    await state.update_data(info_msg_id=msg.message_id)


@router.message(F.media_group_id, F.photo | F.video, UserForm.wait_help_message)
@media_group_handler
async def handle_media_group(messages: list[Message], state: FSMContext):
    """Обработка медиа-группы (фото/видео) в состоянии отправки запроса."""
    await bot.forward_messages(
        chat_id=settings.ADMIN_ID,
        from_chat_id=messages[0].chat.id,
        message_ids=[msg.message_id for msg in messages]
    )

    await _send_admin_notification(messages[0].from_user.id)
    await _clear_user_state(state, messages[0].chat.id)


@router.message(UserForm.wait_help_message)
async def handle_text_message(message: Message, state: FSMContext):
    """Обработка текстового сообщения в состоянии отправки запроса."""
    await bot.forward_message(
        chat_id=settings.ADMIN_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

    await _send_admin_notification(message.from_user.id)
    await _clear_user_state(state, message.chat.id)


async def _send_admin_notification(user_id: int):
    """Уведомление админа о новом обращении."""
    await bot.send_message(
        settings.ADMIN_ID,
        f'📩 Новое обращение от пользователя <code>{user_id}</code>\n\n<i>Чтобы ответить, отправьте сообщение ответом</i>'
    )


async def _clear_user_state(state: FSMContext, chat_id: int):
    """Очищаем состояние и удаляем сообщение с текстом 'Опишите проблему'."""
    data = await state.get_data()
    await state.clear()

    info_msg_id = data.get('info_msg_id')
    if info_msg_id:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=info_msg_id)
        except:
            pass

    await bot.send_message(chat_id, '✅ Ваше сообщение успешно отправлено. Ожидайте ответа от администратора.')
