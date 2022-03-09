# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PX = "https://game-of-thrones-quotes.herokuapp.com/v1/"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️ Made by 🙋‍♂️', url='https://t.me/KoshikKumar17')]])

@Client.on_message(filters.command("thought"))
async def get_thought(bot, update):
    koshik = await update.reply_text("**I Am Processing...😇**")
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=gett_tht(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def gett_tht(type):
    try:
        r = requests.get(PX + requote_uri(type.lower()))
        info = r.json()
        thought = info['sentence']
        gett_tht = f"""**{thought}**
\n **@KoshikKumar17**"""
        return gett_tht
    except Exception as error:
        return error
