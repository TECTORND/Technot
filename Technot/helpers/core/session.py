import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config, get_var
from .client import TechnoClient
from Technot.version import __version__

loop = None

if Config.SESSION:
    session = StringSession(str(Config.SESSION))
else:
    session = "TechnoUserBot"

try:
    techno = TechnoClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        device_model="Technot",
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"SESSION - {e}")
    sys.exit()

techno.tgbot = tgbot = TechnoClient(
    session="TechnoTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=get_var("BOT_TOKEN"))
