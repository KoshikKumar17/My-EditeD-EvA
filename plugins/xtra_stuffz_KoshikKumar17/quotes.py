# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PX = "https://api.quotable.io/random?tags="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️ Made by 🙋‍♂️', url='https://t.me/KoshikKumar17')],[InlineKeyboardButton('List All Types of Quote Tags', callback_data='qtstags')]])

@Client.on_message(filters.command("quote"))
async def get_quote(bot, update):
    koshik = await update.reply_text("**I Am Processing...😇**",quote=True,reply_markup=BUTTONS)
    query = update.text.split(None, 1)[1]
    await koshik.edit_text(
        text=gett_qt(query),
        disable_web_page_preview=True,
        reply_markup = BUTTONS
    )

def gett_qt(type):
    try:
        r = requests.get(PX + requote_uri(type.lower()))
        info = r.json()
        qt = info['content']
        athr = info['author']
        tgs = info['tags']
        gett_qt = f"""**{qt}**\n                  - __{athr}__\n\nCategory:- {tgs}
\n **@KoshikKumar17** ❤️"""
        return gett_qt
    except Exception as error:
        await koshik.edit_text(str(e))
        return error
