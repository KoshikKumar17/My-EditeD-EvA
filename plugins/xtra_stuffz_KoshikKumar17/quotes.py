# ✋ Hand Written by Koshik Kumar
import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

A = """{} with user id:- {} used /quote command."""
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖✨🇮🇳  Made By 🇮🇳✨💖', url='https://t.me/KoshikKumar17')],[InlineKeyboardButton('List All Types of Quote Categories', callback_data='qtstags')]])

@Client.on_message(filters.command("quote"))
async def get_quote(bot, message):
    await message.reply_chat_action("typing")
    if len(message.command) != 2:
        await message.reply_text("/quote [quote category] \n\n Like:- `/quote love`", quote=True, reply_markup=BUTTONS)
        return
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    nu = message.text.split(None, 1)[1]
    URL = f'https://api.quotable.io/random?tags={nu}'
    request = requests.get(URL)
    result = request.json()
    qt = result['content']
    athr = result['author']
    tgs = result['tags']
    gett_qt = f"""**{qt}**\n                  - __{athr}__\n\nCategory:- {tgs}
\n **@KoshikKumar17** 💖 🇮🇳"""
    await k.edit_text(
        text=gett_qt,
        disable_web_page_preview=True,
        reply_markup = BUTTONS
    )
    await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id))
