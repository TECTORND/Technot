import math
import os
import re
import time

import heroku3
import lottie
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from ..helpers.Config import Config
from ..helpers.core.logger import logging
from ..helpers.core.managers import eod, eor
from ..helpers.core.session import techno
from ..helpers import *
from ..helpers.utils import _format, _technotools, _technoutils, install_pip, reply_id
from ..helpers.sql_helper.globals import get_var

# =================== CONSTANT ===================
bot = techno
LOGS = logging.getLogger(__name__)
USERID = techno.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Techname()
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO


Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"
APP_NAME = Config.APP_NAME
API_KEY = Config.API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


# mention user
mention = f"[{ALIVE_NAME}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{Config.ALIVE_NAME}</a>"


TECHNO_USER = techno.me.first_name
Techno_Boy = techno.uid
techno_mention = f"[{TECHNO_USER}](tg://user?id={Techno_Boy})"


# pic
gban_pic = "./Technot/helpers/resources/pics/gban.mp4"
main_pic = "./Technot/helpers/resources/pics/main.jpg"
core_pic = "./Technot/helpers/resources/pics/core.jpg"
chup_pic = "./Technot/helpers/resources/pics/chup.mp4"
bsdk_pic = "./Technot/helpers/resources/pics/bsdk.jpg"
bsdkwale_pic = "./Technot/helpers/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./Technot/helpers/resources/pics/chutiya.jpg"
promote_pic = "./Technot/helpers/resources/pics/promote.jpg"
demote_pic = "./Technot/helpers/resources/pics/demote.jpg"
mute_pic = "./Technot/helpers/resources/pics/mute.jpg"
ban_pic = "./Technot/helpers/resources/pics/ban.jpg"


# channel
my_channel = Config.YOUR_CHANNEL or "Technot_Support"
my_group = Config.YOUR_GROUP or "Technot_Updates"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

# My Channel
chnl_link = "https://t.me/Technot_Updates"
Techno_channel = f"[†ê¢hñðßð†]({chnl_link})"
grp_link = "https://t.me/Technot_Support"
Techno_grp = f"[†ê¢hñð†]({grp_link})"


PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD


TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    check = url(Config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]

async def Techname():
  a = Config.ALIVE_NAME
  if a:
    return a
  else:
    techn=await bot.get_me()
    a = get_display_name(techn)
    return a

async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _technoutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
