from datetime import datetime
from typing import Optional, Dict, Union

from my_classes import database


async def check_user_db(user_id: int) -> Optional[int]:
    return await database.fetchval('SELECT COUNT(*) FROM users WHERE id = $1', (user_id,))


async def save_user(user_id: int, username: Optional[str]) -> None:
    await database.execute('INSERT INTO users (id, username) VALUES ($1, $2)', (user_id, username))


async def get_subs_end(user_id: int) -> Optional[datetime]:
    return await database.fetchval('SELECT subs_end FROM users WHERE id = $1', (user_id,))


async def get_keys(user_id: int) -> Optional[Dict[str, str]]:
    return await database.fetch('SELECT api_key, api_secret FROM users WHERE id = $1', (user_id,), one=True)


async def update_keys(user_id: int, api_key: str, api_secret: str) -> None:
    await database.execute('UPDATE users SET api_key = $1, api_secret = $2 WHERE id = $3', 
                           (api_key, api_secret, user_id))


async def get_param(user_id: int, param: str) -> Optional[Union[int, float, str]]:
    return await database.fetchval(f'SELECT {param} FROM users WHERE id = $1', (user_id,))


async def update_param(user_id: int, param: str, value: Union[int, float, str]) -> None:
    await database.execute(f'UPDATE users SET {param} = $1 WHERE id = $2', (value, user_id))


async def get_user(user_id: int) -> Optional[Dict]:
    return await database.fetch('SELECT * FROM users WHERE id = $1', (user_id,), one=True)


async def update_subs_end(user_id: int, new_subs_end: int) -> None:
    await update_param(user_id, 'subs_end', new_subs_end)
