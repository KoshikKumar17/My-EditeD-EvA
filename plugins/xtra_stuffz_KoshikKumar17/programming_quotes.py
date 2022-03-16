# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PX = "https://programming-quotes-api.herokuapp.com/quotes/"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️ Made by 🙋‍♂️', url='https://t.me/KoshikKumar17')]])

@Koshik.on_message(filters.command("programmingqt"))
async def get_prgrmng_qt(bot, update):
    k = await update.reply_text("**I Am Processing...😇**")
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await k.edit_text(
        text=gett_qt(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def gett_qt(type):
    try:
        r = requests.get(PX + requote_uri(type.lower()))
        info = r.json()
        qqt = info['en']
        athrr = info['author']
        gett_tht = f"""__{qqt}__\n               >> **{athrr}**
\n **@KoshikKumar17 ❤️**"""
        return gett_qt
    except Exception as error:
        return error
