# (c) @KoshikKumar17
import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖🇮🇳✨ Made By ✨🇮🇳💖', url='https://t.me/KoshikKumar17')]])
A = """{} with user id:- {} used /git command."""

async def json_prettify(data):
    output = ""
    try:
        for key, value in data.items():
            output += f"**{key}:** `{value}`\n"
    except Exception:
        for datas in data:
            for key, value in datas.items():
                output += f"**{key}:** `{value}`\n"
            output += "------------------------\n"
    return output

@Koshik.on_message(filters.command(["isro"]))
async def getgithub(bot, message):
    if len(message.command) != 2:
        await message.reply_text("**Use proper syntax to get proper results. :)**\n------\n• Spacecrafts: `/isro spacecrafts`\n\n• Launchers: `/isro launchers`\n\n• Customer Satellites: `/isro customer_satellites`\n\n• Centres: `/isro centres`", quote=True)
        return
    await message.reply_chat_action("typing")
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    query = message.text.split(None, 1)[1]
    URL = f'https://isro.vercel.app/api/{query}'
    request = requests.get(URL)
    result = request.json()
    data = await json_prettify(result)
