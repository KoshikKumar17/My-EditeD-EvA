# ✋ Hand Written by Koshik Kumar
import os
import requests
import pyrogram
import json
from bing_image_urls import bing_image_urls
from info import LOG_CHANNEL
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

A = """{} with user id:- {} used /quote command."""
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖✨🇮🇳  Made By 🇮🇳✨💖', url='https://t.me/KoshikKumar17')],[InlineKeyboardButton('List All Types of Quote Categories', callback_data='qtstags')]])

@Client.on_message(filters.command("quote"))
async def get_quote(bot, message):
    if len(message.command) != 2:
        k = await message.reply_text("**Processing...⏳**", quote=True)
        await asyncio.sleep(2)
        await k.delete()
        URL = f'https://api.quotable.io/random'
        request = requests.get(URL)
        result = request.json()
        qt = result['content']
        athr = result['author']
        tgs = result['tags']
        gett_qt = f"""**“{qt}”**\n                        ~ {athr}\n\n**Category**:- {tgs}"""
        link = bing_image_urls(f'{qt}', limit=1)
        await message.reply_photo(
            photo=link,
            caption=gett_qt,
            disable_web_page_preview=True,
            reply_markup = BUTTONS
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
        link = bing_image_urls(f'{qt}', limit=1)
        await message.reply_photo(
            photo=link,
            caption=gett_qt,
            disable_web_page_preview=True,
            reply_markup = BUTTONS
        )
        await k.delete()
