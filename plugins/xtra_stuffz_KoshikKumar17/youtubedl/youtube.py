# By Koshik 🇮🇳
# Thanks to TgExplore

from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.xtra_stuffz_KoshikKumar17.youtubedl.utils import extractYt, create_buttons, user_time
import wget
import os
from os import error
from PIL import Image



@Client.on_message(filters.command(["ytdl", "youtubedl", "youtube"]))
async def ytdl(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/ytdl [youtube link] \n\n Like:- `/ytdl https://youtu.be/dgght5hbg`", quote=True)
        return
    un = message.text.split(None, 1)[1]
    url = un
    await message.reply_chat_action("typing")
    try:
        title, thumbnail_url, formats = extractYt(url)
    except Exception:
        await message.reply_text("`Failed To Fetch Youtube Data... 😔 \nPossible Youtube Blocked server ip \n#error`")
        return

    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    k = await message.reply_text("**Processing Youtube Url... 🔎**", quote=True)
    try:
        img = wget.download(thumbnail_url)
        im = Image.open(img).convert("RGB")
        output_directory = os.path.join(os.getcwd(), "downloads", str(message.chat.id))
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)
        thumb_image_path = f"{output_directory}.jpg"
        im.save(thumb_image_path,"jpeg")
        await message.reply_photo(thumb_image_path, caption=title, reply_markup=buttons)
        await k.delete()
    except Exception as e:
        print(e)
        try:
            thumbnail_url = "https://telegra.ph/file/ce37f8203e1903feed544.png"
            await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await k.edit(
            f"<code>{e}</code> #Error")   #Ended
