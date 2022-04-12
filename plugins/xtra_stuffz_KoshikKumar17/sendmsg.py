# ✋Hand Written by @KoshikKumar17
import os
from os import error
import pyrogram
from info import LOG_CHANNEL, ADMINS
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Koshik.on_message(filters.command(["sendmsg"]) & filters.user(ADMINS))
async def report_me(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/sendmsg [user id] \n\n Like:- `/sendmsg 1234567890`", quote=True)
        return
    if message.reply_to_message:
        k = await message.reply_text("**Processing...⏳**", quote=True)
        await message.reply_chat_action("typing")
        msgg = message.reply_to_message
        id = message.text.split(None, 1)[1]
        PX = id
        await msgg.copy(chat_id=PX)
        await message.reply_to_message.forward(chat_id=LOG_CHANNEL)
        await k.edit_text("**Successfully forwarded....💥✨**")
    else:
        await message.reply_text("Please Reply to a Message")
