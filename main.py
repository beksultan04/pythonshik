import asyncio
import asyncpg

from user.handlers import router
from admin.handlers import router as admin_router
from my_classes import database
from core.config import settings, dp, bot

# Хранение настроек пользователей в ОЗУ
user_settings = {}

async def load_user_settings():
    global user_settings
    conn = await asyncpg.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS
    )
    rows = await conn.fetch("SELECT user_id, settings FROM user_settings")
    user_settings = {row['user_id']: row['settings'] for row in rows}
    await conn.close()

async def save_user_settings():
    conn = await asyncpg.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS
    )
    for user_id, settings in user_settings.items():
        await conn.execute("""
            INSERT INTO user_settings (user_id, settings)
            VALUES ($1, $2)
            ON CONFLICT (user_id) DO UPDATE SET settings = EXCLUDED.settings
        """, user_id, settings)
    await conn.close()

async def periodic_settings_update():
    while True:
        await asyncio.sleep(settings.UPDATE_INTERVAL)  # Настраиваемый интервал обновления
        await save_user_settings()

async def main():
    try:
        conn = await asyncpg.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASS
        )
        await conn.close()
    except asyncpg.exceptions.ConnectionDoesNotExistError:
        print(f'Не удалось подключиться к Базе Данных (Не существует БД с названием {settings.DB_NAME})')

    await database.create_tables()
    await load_user_settings()
    dp.include_routers(router, admin_router)
    
    asyncio.create_task(periodic_settings_update())  # Запуск обновления настроек в БД
    await dp.start_polling(bot)
    print("Все проверки завершены. База данных готова. Бот запущен")

if __name__ == "__main__":
    asyncio.run(main())
