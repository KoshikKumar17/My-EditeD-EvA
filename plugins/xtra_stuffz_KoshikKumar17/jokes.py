# (c) @KoshikKumar17
import os
import requests
import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://v2.jokeapi.dev/joke/Any?type="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️Father🙋‍♂️', url='https://t.me/KoshikKumar17')]])

@Client.on_message(filters.command("joke"))
async def jokeapibot(bot, update):
    koshik = await update.reply_text("Getting a Joke...😂")
    px = "https://v2.jokeapi.dev/joke/Any?type=single"
        request = requests.get(px)
        result = request.json()
        joke = result['joke']
        gett_joke = f"""
😁Here is Your Joke😁 :\n \n **{joke}**
\nWith ❤️ by @KoshikKumar17"""
    await koshik.edit_text(
        text=gett_joke,
        reply_markup=BUTTONS,
        disable_web_page_preview=True
   )
    
