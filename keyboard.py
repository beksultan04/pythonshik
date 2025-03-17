from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from core.config import settings


def create_reply_keyboard(buttons: list[list[str]], resize: bool = True) -> ReplyKeyboardMarkup:
    """
    Универсальная функция для создания обычной клавиатуры.
    Принимает список списков с текстом кнопок.
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text) for text in row]
            for row in buttons
        ],
        resize_keyboard=resize
    )


def create_inline_keyboard(buttons: list[list[tuple]]) -> InlineKeyboardMarkup:
    """
    Универсальная функция для создания Inline клавиатуры.
    Принимает список списков с кортежами (текст кнопки, callback_data).
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=data) for text, data in row]
        ]
    )


def main(user_id: int) -> ReplyKeyboardMarkup:
    buttons = [
        ['▶️ ПУСК', '⏸ СТОП'],
        ['⚙️', 'ТЦ', 'Токен']
    ]

    if user_id == settings.ADMIN_ID:
        buttons.append(['Админ панель'])

    return create_reply_keyboard(buttons)


def trade_settings() -> ReplyKeyboardMarkup:
    return create_reply_keyboard([
        ['💰', '📉', '📈', '⏳'],
        ['покупка↓', '💸', '⬅️']
    ])


def buy_subs() -> InlineKeyboardMarkup:
    return create_inline_keyboard([
        [('Оформить подписку', 'buy_subs')]
    ])


def buy_mailing_confirm(pay_url: str, pay_hash: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='💰 Оплатить', url=pay_url)],
            [InlineKeyboardButton(text='🔄 Проверить', callback_data=f'checkInvoice:{pay_hash}')]
        ]
    )


def delete() -> InlineKeyboardMarkup:
    return create_inline_keyboard([
        [('Отмена', 'delete')]
    ])
