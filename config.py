import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings, SettingsConfigDict

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    BOT_TOKEN: str
    CRYPTO_PAY_API_TOKEN: str

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    ADMIN_ID: int

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )


try:
    settings = Settings()
except Exception as e:
    logging.error(f'Ошибка загрузки переменных из .env: {e}')
    exit(1)


bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Словарь для хранения активных задач (например, отслеживания)
tasks: dict[int, asyncio.Task] = {}
