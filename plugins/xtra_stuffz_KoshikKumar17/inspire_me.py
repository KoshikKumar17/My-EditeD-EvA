# © Siriustar

import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("inspire"))
async def inspireme(bot, update):
    s = await update.reply_text("Processing...⏳",quote=True)
    url = "http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    await update.reply_photo(photo=img, caption="Inspire me again! © Sirius")
    await s.delete()
