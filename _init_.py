from aiogram import Router

from . import main, payments, help

router = Router()

router.include_routers(
    main.router,
    payments.router,
    help.router
)
