import asyncio
import contextlib
import os
import sys
from asyncio.exceptions import CancelledError

import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from Technot import HEROKU_APP, UPSTREAM_REPO_URL, techno

from ..helpers.Config import Config
from ..helpers.core.logger import logging
from ..helpers.core.managers import eod, eor
from ..helpers.sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)

lb_info = "https://raw.githubusercontent.com/TeamTechnot/Technot/master/Technot/version.py"


async def ld_info(lb_info):
    infos = requests.get(lb_info).py()
    _version = infos["__version__"]
    _release = infos["release-date"]
    _branch = """[Repo().active_branch]((Repo().remotes[0].config_reader.get("url")).replace(".git", f"/tree/Repo().active_branch"))"""
    _author = "TechnoMembers"
    _auturl = "https://github.com/TeamTechno"
    return _version, _release, _branch, _author, _auturl


menu_category = "tools"
cmdhd = Config.HANDLER
DYNO = bool(os.getenv("DYNO",False))

LOGS = logging.getLogger(__name__)
# -- Constants -- #

APP_NAME = Config.APP_NAME or None
API_KEY = Config.API_KEY or None
Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"

UPSTREAM_REPO_BRANCH = Config.UPSTREAM_REPO_BRANCH

REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)


# -- Constants End -- #

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"  • {c.summary} ({c.committed_datetime.strftime(d_form)}) <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"**🤖 New Update available for [{ac_br}]:\n\nChangeLogs:**\n`{changelog}`"
    )
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
        )
        os.remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id,
            changelog_str,
            reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def update_techno(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    TECHNO = await event.edit(
        "`✅ Successfully Updated Technot!\n"
        "Bot is restarting... Wait for a minute!`"
    )
    await event.client.reload(TECHNO)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if API_KEY is None:
        return await event.edit("`Please set up`  **API_KEY**  ` Var...`")
    heroku = heroku3.from_key(API_KEY)
    heroku_applications = heroku.apps()
    if APP_NAME is None:
        await event.edit(
            "`Please set up the` **APP_NAME** `Var`"
            " to be able to deploy your Lêɠêɳ̃dẞο†...`"
        )
        repo.__del__()
        return
    heroku_app = next(
        (app for app in heroku_applications if app.name == APP_NAME),
        None,
    )
    if heroku_app is None:
        await event.edit(
            f"{txt}\n" "`Invalid Heroku credentials for deploying Technot dyno.`"
        )
        return repo.__del__()
    TECHNO = await event.edit(
        "`Userbot dyno build in progress, please wait until the process finishes it usually takes 4 to 5 minutes .`"
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [TECHNO.chat_id, TECHNO.id])
    except Exception as e:
        LOGS.error(e)
    ups_rem.fetch(ac_br)
    repo.git.reset("--hard", "FETCH_HEAD")
    heroku_git_url = heroku_app.git_url.replace("https://", f"https://api:{API_KEY}@")
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(heroku_git_url)
    else:
        remote = repo.create_remote("heroku", heroku_git_url)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**Error log:**\n`{error}`")
        return repo.__del__()
    build_status = heroku_app.builds(order_by="created_at", sort="desc")[0]
    if build_status.status == "failed":
        return await eod(
            event, "`Build failed ⚠️!\n" "Cancelled or there were some errors...`"
        )
    try:
        remote.push("master:main", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**Here is the error log:**\n`{error}`")
        return repo.__del__()
    await event.edit("`Deploy was failed. So restarting to update`")
    with contextlib.suppress(CancelledError):
        await event.client.disconnect()
        if HEROKU_APP is not None:
            HEROKU_APP.restart()


@techno.techno_cmd(
    pattern="update(| now)?$",
    command=("update", menu_category),
    info={
        "header": "To update Technot.",
        "description": "I recommend you to do update deploy atlest once a week.",
        "options": {
            "now": "Will update bot but requirements doesnt update.",
            "deploy": "Bot will update completly with requirements also.",
        },
        "usage": [
            "{tr}update",
            "{tr}update now",
            "{tr}update deploy",
        ],
    },
)
async def upstream(event):
    "To check if the bot is up to date and update if specified"
    conf = event.pattern_match.group(1).strip()
    event = await eor(event, "`Checking for updates, please wait....`")
    off_repo = UPSTREAM_REPO_URL
    _version, _release, _branch, _author, _auturl = await ld_info(lb_info)
    force_update = False
    if DYNO and (API_KEY is None or APP_NAME is None):
        return await eor(
            event,
            "`👨‍💻 Set the required vars first to Update the [†ê¢hñðßð†](https://t.me/Technot_Updates/292)`",
        )
    try:
        txt = (
            "`Oops.. Updater cannot continue due to "
            + "some problems occured`\n\n**LOGTRACE:**\n"
        )
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`Unfortunately, the directory {error} does not seem to be a git repository.\nBut we can fix that by force updating the Technot using .update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Looks like you are using your own custom branch ({ac_br}). "
            "in that case, Updater is unable to identify "
            "which branch is to be merged. "
            "please checkout to any official branch`"
        )
        return repo.__del__()
    with contextlib.suppress(BaseException):
        repo.create_remote("upstream", off_repo)
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    # Special case for deploy
    if changelog == "" and not force_update:
        await event.edit(
            f"<b><i>†ê¢hñðßð† Is UP-TO-DATE !!</b></i> \n\n<b><i><u>Update Information :</b></i></u> \n<b>• Branch :</b> {_branch} \n<b>• Release Date :</b> {_release} \n<b>• Version :</b> {_version} \n<b>• Author :</b> <a href='{_auturl}'>{_author}</a>",
            link_preview=False,
            parse_mode="HTML",
        )
        """await event.edit(
            "\n`TechnoUserBot is`  **up-to-date**  `with`  "
            f"**{UPSTREAM_REPO_BRANCH}**\n"
        )"""
        return repo.__del__()
    if conf == "" and not force_update:
        await print_changelogs(event, ac_br, changelog)
        await event.delete()
        return await event.respond(
            f"👨‍💻 To __UP-TO-DATE__ †ê¢hñðßð† do `{cmdhd}update deploy` "
        )
    if force_update:
        await event.edit(
            "`Force-Syncing to latest stable Technot code, please wait...`"
        )
    if conf == "now":
        await event.edit("`Updating Technot, please wait....`")
        await update_techno(event, repo, ups_rem, ac_br)
    return


@techno.techno_cmd(
    pattern="update deploy$",
)
async def upstream(event):
    event = await eor(event, "`Pulling the Technot repo wait a sec ....`")
    off_repo = "https://github.com/TeamTechnot/Technot"
    os.chdir("/app")
    try:
        txt = (
            "`Oops.. Updater cannot continue due to "
            + "some problems occured`\n\n**LOGTRACE:**\n"
        )

        repo = Repo()

    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ac_br = repo.active_branch.name
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    await event.edit("`Deploying Technot, please wait....`")
    await deploy(event, repo, ups_rem, ac_br, txt)


@techno.techno_cmd(
    pattern="MULTI$",
    command=("MULTI", menu_category),
    info={
        "header": "To update to Multi Its Features Currently Not Available Soon Add.Ok ",
        "usage": "{tr}MULTI",
    },
)
async def variable(var):
    "To update to gootechno."
    if Config.API_KEY is None:
        return await eod(
            var,
            "Set the required var in heroku to function this normally `API_KEY`.",
        )
    if Config.APP_NAME is not None:
        app = Heroku.app(Config.APP_NAME)
    else:
        return await eod(
            var,
            "Set the required var in heroku to function this normally `APP_NAME`.",
        )
    heroku_var = app.config()
    await eor(var, "`Changing PRO to MULTI wait for 2-3 minutes.`")
    heroku_var["UPSTREAM_REPO"] = "https://github.com/TeamTechnot/Technot"
