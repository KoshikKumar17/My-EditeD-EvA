# (c) @KoshikKumar17
# Thanks to https://github.com/FayasNoushad/Youtube-Video-Thumbnail

import os
import time
import ytthumb
from pyrogram import Client, filters

@Client.on_message(filters.command(["ytthumb"]))
async def send_thumbnail(bot, message):
    if len(message.command) == 2:
        link = message.text.split(None, 1)[1]
        thumbnail = ytthumb.thumbnail(
            video=link,
            quality=maxres
        )
        await message.reply_photo(
            photo=thumbnail,
            quote=True
        )
    elif message.reply_to_message:
        link = message.reply_to_message
        thumbnail = ytthumb.thumbnail(
            video=link,
            quality=maxres
        )
        await message.reply_photo(
            photo=thumbnail,
            quote=True
        )
    else:
        await message.reply_text("**Either reply to a YouTube link or use /ytthumb YouTube_link.**", quote=True)
