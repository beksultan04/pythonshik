import hmac
import hashlib
import asyncio
import logging
import traceback
from functools import wraps
from urllib.parse import urlencode

import aiohttp
import asyncpg.exceptions
from aiohttp import client_exceptions
from asyncpg import create_pool, Pool

from core.config import settings


def database_error_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            except (
                    asyncpg.exceptions.ConnectionDoesNotExistError,
                    ConnectionError,
                    OSError
            ) as error:
                print(error)
                await asyncio.sleep(2)

    return wrapper


def request_error_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            except (
                    client_exceptions.ClientConnectorDNSError
            ):
                logging.error(traceback.format_exc())
                await asyncio.sleep(1)

    return wrapper


class Database:
    def __init__(self, database_url=str):
        self.database_url = database_url
        self._pool: Pool = None

    async def create_tables(self):
        tables = {
            'users': """
                CREATE TABLE IF NOT EXISTS users (
                    id              BIGINT not null
                                       constraint users_pk
                                           primary key,
                    username        VARCHAR(30),
                    api_key         VARCHAR(50),
                    api_secret      VARCHAR(100),
                    symbol          VARCHAR(25),
                    trade_amount    FLOAT,
                    stop_buy_limit  FLOAT,
                    stop_sell_limit FLOAT,
                    buy_percentage  FLOAT,
                    sell_percentage FLOAT,
                    trade_frequency INTEGER,
                    subs_end        TIMESTAMPTZ
                );
            """
        }

        for sql in tables.values():
            await self.execute(sql)

    @database_error_decorator
    async def get_pool(self) -> Pool:
        if self._pool is None:
            self._pool = await create_pool(self.database_url, max_size=2, min_size=1)
            return self._pool
        else:
            return self._pool

    @database_error_decorator
    async def fetch(self, query: str, values: list = None, one: bool = False) -> list[dict] | dict:
        if values is None:
            values = []

        pool = await self.get_pool()
        async with pool.acquire() as conn:
            data = [dict(i) for i in await conn.fetch(query, *values)]
            if one:
                return data[0] if data else {}
            else:
                return data

    @database_error_decorator
    async def fetchval(self, query: str, values: list = None):
        if values is None:
            values = []

        pool = await self.get_pool()
        async with pool.acquire() as conn:
            return await conn.fetchval(query, *values)

    @database_error_decorator
    async def execute(self, query: str, values: list = None) -> None:
        if values is None:
            values = []

        pool = await self.get_pool()
        async with pool.acquire() as conn:
            await conn.execute(query, *values)


class MexcAPI:
    def __init__(self, base_url: str):
        """
        Инициализация клиента API.

        :param base_url: Базовый URL API.
        """
        self.base_url = base_url.rstrip('/')

    async def get_keys(self, user_id: int):
        return await database.fetch('SELECT api_key, api_secret FROM users WHERE id = $1', [user_id], one=True)

    async def _get_server_time(self):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get('https://api.mexc.com/api/v3/time') as response:
                data = await response.json()
        return data['serverTime']

    def _generate_signature(self, api_secret: str, req_time: int, params: dict) -> str:
        """
        Генерация подписи для запроса.

        :req_time: Время в timestamp
        :param params: Параметры запроса.
        :return: Подпись для заголовка.
        """

        if params == {}:
            to_sign = 'timestamp={}'.format(req_time)
        else:
            to_sign = '{}&timestamp={}'.format(urlencode(params), req_time)

        return hmac.new(api_secret.encode('utf-8'), to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

    @request_error_decorator
    async def _send_request(self, method: str, endpoint: str, params: dict = None, keys: dict = None, auth_required: bool = False):

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        params = params or {}
        headers = {}

        if auth_required:

            headers.update({
                'X-MEXC-APIKEY': keys.get('api_key', ''),
                'Content-Type': 'application/json',
            })

            req_time = await self._get_server_time()
            signature = self._generate_signature(keys.get('api_secret'), req_time, params)
            params.update({
                'timestamp': req_time,
                'signature': signature,
            })

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.request(
                    method,
                    url,
                    params=params,
                    headers=headers
            ) as response:
                return {'status': response.status, 'data': await response.json()}

    async def public_request(self, endpoint: str, params: dict = None):

        return await self._send_request('GET', endpoint, params)

    async def private_request(self, endpoint: str, keys: dict, params: dict = None, method: str = 'GET'):

        return await self._send_request(method, endpoint, params, keys, auth_required=True)

class CryptoBot:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    @staticmethod
    async def get_invoices(offset: int = 0):
        invoices = await crypto.request(
            'getInvoices',
            {
                'status': 'paid',
                'offset': offset,
                'count': 1000
            }
        )
        return invoices

    @request_error_decorator
    async def _send_request(self, method: str, endpoint: str, params: dict):
        url = f'{self.base_url}/{endpoint.lstrip('/')}'

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                url,
                headers={
                    'Crypto-Pay-API-Token': settings.CRYPTO_PAY_API_TOKEN,
                    'Host': 'pay.crypt.bot',
                },
                params=params,
            ) as response:
                return {'status': response.status, 'data': await response.json()}

    async def request(self, endpoint: str, params: dict):
        return await self._send_request('GET', endpoint, params)


database = Database(f'postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}')
crypto = CryptoBot('https://pay.crypt.bot/api/')
mexc = MexcAPI('https://api.mexc.com/api/v3')