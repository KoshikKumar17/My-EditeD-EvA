# ✋Hand Written by @KoshikKumar17
import os
from os import error
import pyrogram
from info import LOG_CHANNEL, ADMINS
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

A = """Hi Friend 👋,
My Admin has a message for you:- 

<b>{}</b>

Thanks ❤️."""

@Koshik.on_message(filters.command(["sendmsg"]) & filters.user(ADMINS))
async def report_me(bot, message):
    if len(message.command) != 3:
        await message.reply_text("/sendmsg [user id] [your message] \n\n Like:- `/sendmsg 1234567890 Hi..!!`", quote=True)
        return
    await message.reply_chat_action("typing")
    try:
        k = await message.reply_text("**Processing...⏳**", quote=True)
        id = message.text.split(None, 1)[1]
        FD = id
        msg = message.text.split(None, None, 1)[1]
        await bot.send_message(FD, A.format(msg))
        await k.edit_text("**Sent Successfully**")
    except Exception as error:
        await message.reply_text(str(error))
