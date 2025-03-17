from aiogram.fsm.state import StatesGroup, State


class AdminForm(StatesGroup):
    find_user = State()


class UserForm(StatesGroup):
    # Настройка API ключей
    wait_access_key = State()
    wait_secret_key = State()

    # Сброс параметров
    reset_symbol = State()
    reset_trade_amount = State()
    reset_stop_buy_limit = State()
    reset_stop_sell_limit = State()
    reset_trade_frequency = State()
    reset_buy_percentage = State()
    reset_sell_percentage = State()

    # Покупка подписки
    wait_month = State()

    # Обработка сообщений
    wait_help_message = State()
