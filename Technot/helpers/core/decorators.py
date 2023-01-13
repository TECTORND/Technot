import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from ..helpers.Config import Config
from ..sql_helper.globals import get_var


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            HELP_TEXT = (
                get_var("HELP_TEXT")
                or "Only My Master can Access This Button !!\n\nDeploy your own @Technot_Official."
            )
            await c_q.answer(
                HELP_TEXT,
                alert=True,
            )

    return wrapper