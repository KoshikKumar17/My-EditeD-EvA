# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://short-link-api.vercel.app/?query="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ ❤️ 😁 Made By 😁 ❤️ ✨', url='https://t.me/KoshikKumar17')]])

@Koshik.on_message(filters.command("short"))
async def linkshortener(bot, update):
    koshik = await update.reply_text("**Shorting your link....👤\n\nPlease wait a bit..🙃**",quote=True)
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=shortlink(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def shortlink(type):
    try:
        r = requests.get(API + requote_uri(type.lower()))
        info = r.json()
        clickru = info['click.ru']
        dagd = info['da.gd']
        isgd = info['is.gd']
        osdb = info['osdb.link']
        ttm = info['ttm.sh']
        shortlink = f"""
**🔗Your link has been shortened 🔗** :\n \n
**CLICK.RU:-** {clickru}
**DA.GD:-** {dagd}
**IS.GD:-** {isgd}
**OSDB.LINK:-** {osdb}
**TTM.SH:-** {ttm}
\nWith ❤️ by @KoshikKumar17"""
        return gett_joke
    except Exception as error:
        return error
