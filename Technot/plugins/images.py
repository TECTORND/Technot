# image search for TechnoUserBot
import os
import shutil

from telethon.errors.rpcerrorlist import MediaEmptyError

from Technot import techno

from ..core.managers import eor
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.utils import reply_id

menu_category = "misc"


@techno.techno_cmd(
    pattern="img(?: |$)(\d*)? ?([\s\S]*)",
    command=("img", menu_category),
    info={
        "header": "Google image search.",
        "description": "To search images in google. By default will send 3 images.you can get more images(upto 10 only by changing limit value as shown in usage and examples.",
        "usage": ["{tr}img <1-10> <query>", "{tr}img <query>"],
        "examples": [
            "{tr}img 10 TechnoUserBot",
            "{tr}img TechnoUserBot",
            "{tr}img 7 TechnoUserBot",
        ],
    },
)
async def img_sampler(event):
    "Google image search."
    reply_to_id = await reply_id(event)
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await eor(event, "Reply to a message or pass a query to search!")
    techno = await eor(event, "`Processing...`")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        if lim > 10:
            lim = int(10)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(3)
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query.replace(",", " "),
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await techno.edit(f"Error: \n`{e}`")
    lst = paths[0][query.replace(",", " ")]
    try:
        await event.client.send_file(event.chat_id, lst, reply_to=reply_to_id)
    except MediaEmptyError:
        for i in lst:
            try:
                await event.client.send_file(event.chat_id, i, reply_to=reply_to_id)
            except MediaEmptyError:
                pass
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await techno.delete()
