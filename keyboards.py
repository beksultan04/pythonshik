from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_keyboard(buttons: list[list[tuple]]) -> InlineKeyboardMarkup:
    """
    Универсальная функция для создания Inline клавиатуры.
    Принимает список списков с кортежами (текст кнопки, callback_data).
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=data) for text, data in row]
            for row in buttons
        ]
    )


def admin_panel():
    return create_keyboard([
        [('Найти пользователя по ID', 'find_user')]
    ])


def back():
    return create_keyboard([
        [('Отмена', 'admin_panel')]
    ])
