# (c) @KoshikKumar17
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://v2.jokeapi.dev/joke/Any?type=single"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️Father🙋‍♂️', url='https://t.me/KoshikKumar17')]])

@Client.on_message(filters.command("joke"))
async def reply_info(bot, update):
    koshik = await update.reply_text("**Getting a Joke...😂**")
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=gett_joke,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def gett_joke(type):
    try:
        r = requests.get("https://v2.jokeapi.dev/joke/Any?type=single").json()
        joke = r['joke']
        gett_joke = f"""__**😂 Jokes 😂**__

😁Here is Your Joke😁 :\n \n **{joke}**
\nWith ❤️ by @KoshikKumar17"""
        return gett_joke
    except Exception as error:
        return error
