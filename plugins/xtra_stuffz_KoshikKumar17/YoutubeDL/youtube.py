# By Koshik 🇮🇳
# Thanks to TgExplore

from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.xtra_stuffz_KoshikKumar17.YoutubeDL.utils import extractYt, create_buttons, user_time
import wget
import os
from PIL import Image



@Client.on_message(filters.command(["ytdl", "youtubedl", "youtube"]))
async def ytdl(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/ytdl [youtube link] \n\n Like:- `/ytdl https://youtu.be/dgght5hbg`", quote=True)
        return

    userLastDownloadTime = user_time.get(message.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await message.reply_text(f"`Wait {wait_time} Minutes before next Request`. **You can use YTDL command every 5 minutes.**", quote=True)
            return
    except:
        pass
