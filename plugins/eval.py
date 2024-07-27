import io
import os
from re import sub
import sys
import traceback
from pyrogram.errors import RPCError
import subprocess
from datetime import datetime
from config import ADMINS
from levi import Bot as app
import asyncio
from pyrogram import filters

async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

@app.on_message(filters.command(["eval", "ex", "ev"]))
async def eval(client, message):
    try:
        user_id = message.from_user.id
    except:
        return
    if user_id not in ADMINS:
        return
    if len(message.text.split()) < 2:
        return await message.reply_text("**ɪɴᴘᴜᴛ ɴᴏᴛ ғᴏᴜɴᴅ!**")

    cmd = message.text.split(maxsplit=1)[1]     
    status_message = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ...**")    
    start = datetime.now()
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
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
        evaluation = "**sᴜᴄᴄᴇss**"
    end = datetime.now()
    ping = (end-start).microseconds / 1000
    final_output = "**ɪɴᴘᴜᴛ**:\n"
    final_output += f"``` python\n{cmd}```\n\n"
    final_output += "<b>ᴏᴜᴛᴘᴜᴛ</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code>\n"
    final_output += f"<b>ᴛᴀᴋᴇɴ ᴛɪᴍᴇ</b>: {ping}ms"
    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await status_message.edit_text(final_output)