# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PU = "https://zenquotes.io/api/"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ ❤️ 😇 OWNER 😇 ❤️ ✨', url='https://t.me/KoshikKumar17')]])

@Client.on_message(filters.command("quote"))
async def get_quote(bot, update):
    koshik = await update.reply_text("**I Am Processing...**")
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=getquote(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def getquote(type):
    try:
        r = requests.get(PU + requote_uri(type.lower()))
        info = r.json()
        qt = info['q']
        athr = info['a']
        getquote = f"""
✨ Here is Your Quote ✨ :\n \n **{qt}**\n           --**{athr}**\n
@KoshikKumar17"""
        return getquote
    except Exception as error:
        return error
