#Это основной код бота.
import asyncio
import logging
import traceback

import utils
from user import keyboards
from my_classes import mexc
from core.config import bot, tasks

### Глобальные переменные
- **`repeat_error`** — счетчик ошибок для контроля количества повторных попыток при возникновении сбоев.
- **`last_buy_price`** — хранит последнюю цену покупки актива.
- **`order_id`** — идентификатор активного лимитного ордера на продажу.
- **`lower_limit_reached`** — флаг, показывающий, была ли достигнута нижняя граница цены (stop_buy_limit).
- **`upper_limit_reached`** — флаг, показывающий, была ли достигнута верхняя граница цены (stop_sell_limit).
- **`keys`** — словарь с API-ключами (`api_key`, `api_secret`).

### Параметры в `params` (передаются в функцию)
- **`api_key` / `api_secret`** — ключи для аутентификации на бирже.
- **`symbol`** — торговая пара (например, 'KASUSDT').


5. **Обработка успешной продажи:**
   - Если статус ордера становится `FILLED`, рассчитывается прибыль.
   - Выводится сообщение о полученной прибыли.

6. **Обработка ошибок:**
   - При неудачных операциях бот делает до трех повторных попыток.
   - При превышении лимита попыток бот останавливает работу.

7. **Контроль подписки:**
   - Бот проверяет доступ пользователя через `utils.is_access()`.
   - Если доступ закончен — задача (`tasks[params['id']]`) отменяется.

Этот бот работает в многопользовательском режиме, постоянно отслеживает цену актива на бирже и автоматически совершает сделки на основе указанных параметров. 
При необходимости уведомляет о статусе операций в Telegram и обрабатывает различные ошибки.


