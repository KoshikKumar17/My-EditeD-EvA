# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://short-link-api.vercel.app/?query="
IPA = "https://unshorten.me/json/"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('â¨ â¤ï¸ ð Made By ð â¤ï¸ â¨', url='https://t.me/KoshikKumar17')]])

@Koshik.on_message(filters.command("short"))
async def linkshortener(bot, update):
    koshik = await update.reply_text("**Shorting your link....ð¤\n\nPlease wait a bit..ð**",quote=True)
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
        return f"""
**ðYour link has been shortened ð** :\n \n
**CLICKRU:-** {clickru}\n
**DAGD:-** {dagd}\n
**ISGD:-** {isgd}\n
**OSDBLINK:-** {osdb}\n
**TTMSH:-** {ttm}\n
\n**â¢| @KoshikKumar17 |â¢**"""

    except Exception as error:
        return error

@Koshik.on_message(filters.command("unshort"))
async def linkextender(bot, update):
    koshik = await update.reply_text("**Un-Shorting your link....ð¤\n\nPlease wait a bit..ð**",quote=True)
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=longlink(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def longlink(type):
    try:
        r = requests.get(IPA + requote_uri(type.lower()))
        info = r.json()
        rqrl = info['requested_url']
        rerl = info['resolved_url']
        return f"""**Your Link Un-ShorTeNed **

**Short Url **:- {rqrl}\n
**Long ** {rerl}

\n**â¢| @KoshikKumar17 |â¢**"""

    except Exception as error:
        return error
