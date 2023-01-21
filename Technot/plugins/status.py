import os
import urllib

from telethon.tl import functions

from Technot import techno

from ..helpers.core.managers import eod, eor
from ..helpers.sql_helper.globals import set_var, get_var

menu_category = "utils"


OFFLINE_TAG = "[OFFLINE]"


@techno.techno_cmd(
    pattern="offline$",
    command=("offline", menu_category),
    info={
        "header": "To your status as offline",
        "description": " it change your pic as offline, and add offline tag in name.",
        "usage": "{tr}offline",
    },
)
async def pussy(event):
    "make yourself offline"
    user = await event.client.get_entity("me")
    if user.first_name.startswith(OFFLINE_TAG):
        return await eod(event, "**Already in Offline Mode.**")
    await eor(event, "**Changing Profile to Offline...**")
    photo = "./temp/donottouch.jpg"
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    urllib.request.urlretrieve(
        "https://telegra.ph/file/249f27d5b52a87babcb3f.jpg", photo
    )
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
        else:
            await eor(event, "**Changed profile to OffLine.**")
    os.remove(photo)
    first_name = user.first_name
    set_var("my_first_name", first_name)
    last_name = user.last_name
    if last_name:
        set_var("my_last_name", last_name)
    tag_name = OFFLINE_TAG
    await event.client(
        functions.account.UpdateProfileRequest(
            last_name=first_name, first_name=tag_name
        )
    )
    await eod(event, f"**`{tag_name} {first_name}`\nI am Offline now.**")


@techno.techno_cmd(
    pattern="online$",
    command=("online", menu_category),
    info={
        "header": "To your status as online",
        "description": " it change your pic back normal, and remove offline tag in name.",
        "usage": "{tr}online",
    },
)
async def techno(event):
    "make yourself online"
    user = await event.client.get_entity("me")
    if user.first_name.startswith(OFFLINE_TAG):
        await eor(event, "**Changing Profile to Online...**")
    else:
        await eod(event, "**Already Online.**")
        return
    try:
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await eor(event, str(e))
    else:
        await eor(event, "**Changed profile to Online.**")
    first_name = get_var("my_first_name")
    last_name = get_var("my_last_name") or ""
    await event.client(
        functions.account.UpdateProfileRequest(
            last_name=last_name, first_name=first_name
        )
    )
    await eod(event, f"**`{first_name} {last_name}`\nI am Online !**")
