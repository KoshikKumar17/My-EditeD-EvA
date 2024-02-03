# ✋ Hand Written by Koshik Kumar
import os
import requests
import pyrogram
import json
# first install pip install bing-image-urls
from bing_image_urls import bing_image_urls
from pyrogram import Client
from pyrogram import filters

@Client.on_message(filters.command("imgqt"))
async def get_imgqt(bot, message):
    if len(message.command) != 2:
        k = await message.reply_text("**Processing...⏳**", quote=True)
        URL = f'https://api.quotable.io/random'
        request = requests.get(URL)
        result = request.json()
        qt = result['content']
        athr = result['author']
        tgs = result['tags']
        gett_qt = f"""**“{qt}”**\n                        ~ {athr}\n\n**Category**:- {tgs}"""
        apple = bing_image_urls(f'{qt}', limit=1)
        ball = apple[0]
        await k.delete()
        await message.reply_photo(
            photo=ball,
            caption=gett_qt,
            quote=True,
            disable_web_page_preview=True
        )
    else:
        k = await message.reply_text("**Processing...⏳**", quote=True)
        nu = message.text.split(None, 1)[1]
        URL = f'https://api.quotable.io/random?tags={nu}'
        request = requests.get(URL)
        result = request.json()
        qt = result['content']
        athr = result['author']
        tgs = result['tags']
        gett_qt = f"""**“{qt}”**\n                      ~ {athr}\n\n**Category**:- {tgs}"""
        apple = bing_image_urls(f'{qt}', limit=1)
        ball = apple[0]
        await message.reply_photo(
            photo=ball,
            quote=True,
            caption=gett_qt,
            disable_web_page_preview=True
        )
