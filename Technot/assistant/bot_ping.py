from datetime import datetime

from telethon import Button

from Technot import Config, techno

from ..helpers.core.logger import logging
from ..helpers import reply_id
from ..plugins import mention
from ..helpers.sql_helper.bot_blacklists import check_is_black_list
from ..helpers.sql_helper.globals import get_var
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


@techno.bot_cmd(
    pattern=f"^/ping({botusername})?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    chat = await event.get_chat()
    await techno.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    buttons = [(Button.url("⚜ †ê¢hñðßð† ⚜", "https://t.me/Technot_Official"))]
    PM_IMG = (
        get_var("BOT_PING_PIC")
        or "https://telegra.ph/file/d01a2163ad90a87a99c8c.jpg"
    )
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    pm_caption = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{mention}』"
    try:
        await event.client.send_file(
            chat.id,
            PM_IMG,
            caption=pm_caption,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Error**\nThere was a error while using **alive**. `{e}`",
            )
