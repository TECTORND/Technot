import asyncio
import io
import os
import sys
import traceback

from ..helpers.utils import _format
from . import *

menu_category = "tools"


@techno.techno_cmd(
    pattern="exec(?:\s|$)([\s\S]*)",
    command=("exec", menu_category),
    info={
        "header": "To Execute terminal commands in a subprocess.",
        "usage": "{tr}exec <command>",
        "examples": "{tr}exec techno stringsetup.py",
    },
)
async def _(event):
    "To Execute terminal commands in a subprocess."
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await eod(event, "`What should i execute?..`")
    technoevent = await eor(event, "`Executing.....`")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    TechnoUSer = await event.client.get_me()
    curruser = TechnoUSer.username or "TechnoUserBot"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"```{curruser}:~#``` ```{cmd}```\n```{result}```"
    else:
        cresult = f"```{curruser}:~$``` ```{cmd}```\n```{result}```"
    await eor(
        technoevent,
        text=cresult,
        aslink=True,
        linktext=f"**•  Exec : **\n```{cmd}``` \n\n**•  Result : **\n",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"Terminal command\n\n `{cmd}`\n\n was executed sucessfully.",
        )


@techno.techno_cmd(
    pattern="eval(?:\s|$)([\s\S]*)",
    command=("eval", menu_category),
    info={
        "header": "To Execute python script/statements in a subprocess.",
        "usage": "{tr}eval <command>",
        "examples": "{tr}eval print('TechnoUserBot')",
    },
)
async def _(event):
    "To Execute python script/statements in a subprocess."
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await eod(event, "`What should i run ?..`")
    if "session" in cmd:
        return await eor(
            event, "`This Is A Sensitive Data.So Its Protected By Technot.`"
        )
    if "SESSION" in cmd:
        return await eor(
            event, "`This Is A Sensitive Data.So Its Protected By Technot.`"
        )
    cmd = (
        cmd.replace("sendmessage", "send_message")
        .replace("sendfile", "send_file")
        .replace("editmessage", "edit_message")
    )
    technoevent = await eor(event, "`Running ...`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = (
        f"**•  Eval : **\n```{cmd}``` \n\n**•  Result : **\n```{evaluation}``` \n"
    )
    await eor(
        technoevent,
        text=final_output,
        aslink=True,
        linktext=f"**•  Eval : **\n```{cmd}``` \n\n**•  Result : **\n",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"eval command\n\n`{cmd}` \n\nwas executed sucessfully.",
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        (
            "async def __aexec(message, event , reply, client, p, chat): "
            + "".join(f"\n {l}" for l in code.split("\n"))
        )
    )

    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )
