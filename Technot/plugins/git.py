import os
from datetime import datetime

import aiohttp
import requests
from github import Github
from pySmartDL import SmartDL
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from Technot import techno

from ..helpers.Config import Config
from ..helpers.core.logger import logging
from ..helpers.core.managers import eod, eor
from ..helpers.utils import reply_id
from . import reply_id

LOGS = logging.getLogger(os.path.basename(__name__))
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
menu_category = "misc"
from . import Techno_channel

GIT_TEMP_DIR = "./temp/"

msg = f"""
**â đģđđđđđđđđĸ đ°đ đđđđđđđ â**
  âĸ        [âĨī¸ đđđđ âĨī¸](https://github.com/TeamTechnot/Technot)
  âĸ        [âĻī¸ Deploy âĻī¸](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamTechnot%2FTechnot&template=https%3A%2F%2Fgithub.com%2FTeamTechnot%2FTechnot)
  âĸ  ÂŠī¸ {Techno_channel} âĸ
"""


@techno.techno_cmd(
    pattern="repo$",
    command=("repo", menu_category),
    info={
        "header": "Source code link of Technot",
        "usage": [
            "{tr}repo",
        ],
    },
)
async def source(e):
    "Source code link of Technot"
    reply_to_id = await reply_id(e)
    try:
        techno = await e.client.inline_query(Config.BOT_USERNAME, "repo")
        await techno[0].click(e.chat_id, reply_to=reply_to_id, hide_via=True)
        await e.delete()
    except (noin, dedbot):
        await eor(e, msg)


@techno.techno_cmd(
    pattern="github( -l(\d+))? ([\s\S]*)",
    command=("github", menu_category),
    info={
        "header": "Shows the information about an user on GitHub of given username",
        "flags": {"-l": "repo limit : default to 5"},
        "usage": "{tr}github [type] [username]",
        "examples": ["{tr}github TeamTechnot", "{tr}github -l5 TeamTechnot"],
    },
)
async def _(event):
    "Get info about an GitHub User"
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await eod(event, f"`{username} not found`")
            technoevent = await eor(event, "`fetching github info ...`")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = 5 if not limit else int(limit)
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**GitHub Info for** `{username}`\
                \nđ¤ **Name:** [{name}]({html_url})\
                \nđ§ **Type:** `{type}`\
                \nđĸ **Company:** `{company}`\
                \nđ­ **Blog** : {blog}\
                \nđ **Location** : `{location}`\
                \nđ **Bio** : __{bio}__\
                \nâ¤ī¸ **Followers** : `{followers}`\
                \nđ **Following** : `{following}`\
                \nđ **Public Repos** : `{public_repos}`\
                \nđ **Public Gists** : `{public_gists}`\
                \nđ **Profile Created** : `{created_at}`\
                \nâī¸ **Profile Updated** : `{updated_at}`".format(
                username=username, **result
            )

            if repos:
                REPLY += "\nđ **Some Repos** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(
                event.chat_id,
                ppath,
                caption=REPLY,
                reply_to=reply_to,
            )
            os.remove(ppath)
            await technoevent.delete()


@techno.techno_cmd(
    pattern="commit$",
    command=("commit", menu_category),
    info={
        "header": "To commit the replied plugin to github.",
        "description": "It uploads the given file to your github repo in **Technot/plugins** folder\
        \nTo work commit plugin set `GITHUB_ACCESS_TOKEN` and `GIT_REPO_NAME` Variables in Heroku vars First",
        "note": "As of now not needed i will sure develop it ",
        "usage": "{tr}commit",
    },
)
async def download(event):
    "To commit the replied plugin to github."
    if Config.GITHUB_ACCESS_TOKEN is None:
        return await eod(event, "`Please ADD Proper Access Token from github.com`", 5)
    if Config.GIT_REPO_NAME is None:
        return await eod(
            event, "`Please ADD Proper Github Repo Name of your Technot`", 5
        )
    mone = await eor(event, "`Processing ...`")
    if not os.path.isdir(GIT_TEMP_DIR):
        os.makedirs(GIT_TEMP_DIR)
    start = datetime.now()
    reply_message = await event.get_reply_message()
    if not reply_message or not reply_message.media:
        return await eod(
            event, "__Reply to a file which you want to commit in your github.__"
        )
    try:
        downloaded_file_name = await event.client.download_media(reply_message.media)
    except Exception as e:
        await mone.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(
            "Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms)
        )
        await mone.edit("Committing to Github....")
        await git_commit(downloaded_file_name, mone)


async def git_commit(file_name, mone):
    content_list = []
    access_token = Config.GITHUB_ACCESS_TOKEN
    g = Github(access_token)
    file = open(file_name, "r", encoding="utf-8")
    commit_data = file.read()
    repo = g.get_repo(Config.GIT_REPO_NAME)
    LOGS.info(repo.name)
    create_file = True
    contents = repo.get_contents("")
    for content_file in contents:
        content_list.append(str(content_file))
        LOGS.info(content_file)
    for i in content_list:
        create_file = True
        if i == 'ContentFile(path="' + file_name + '")':
            return await mone.edit("`File Already Exists`")
    if create_file:
        file_name = f"Technot/plugins/{file_name}"
        LOGS.info(file_name)
        try:
            repo.create_file(
                file_name, "Uploaded New Plugin", commit_data, branch="master"
            )
            LOGS.info("Committed File")
            ccess = Config.GIT_REPO_NAME
            ccess = ccess.strip()
            await mone.edit(
                f"`Commited On Your Github Repo`\n\n[Your PLUGINS](https://github.com/{ccess}/tree/master/Technot/plugins/)"
            )
        except BaseException:
            LOGS.info("Cannot Create Plugin")
            await mone.edit("Cannot Upload Plugin")
    else:
        return await mone.edit("`Committed Suicide`")
