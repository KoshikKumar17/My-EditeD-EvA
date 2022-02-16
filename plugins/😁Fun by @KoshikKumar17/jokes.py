import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://v2.jokeapi.dev/joke/Any?type="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️Father🙋‍♂️', url='https://t.me/KoshikKumar17')]])

@Client.on_message(filters.command("joke"))
async def reply_info(bot, update):
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await update.reply_text(
        text=gett_joke(query),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )

def gett_joke(type):
    try:
        r = requests.get(API + requote_uri(type.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--
Country : `{country}`
Actived : `{active}`
Confirmed : `{confirmed}`
Deaths : `{deaths}`
ID : `{info_id}`
Last Update : `{last_update}`
Latitude : `{latitude}`
Longitude : `{longitude}`
Recovered : `{recovered}`
Made by @SakuraBotUpdates ❤️"""
        return covid_info
    except Exception as error:
        return error
