# © Siriustar

import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("inspire"))
def inspireme(update,context):
    bot = context.bot
    url = r"http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    bot.sendPhoto(chat_id=update.effective_chat.id, photo=img, caption="Inspire me again!")
