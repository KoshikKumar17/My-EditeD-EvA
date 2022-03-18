# © Siriustar

import requests
import pyrogram
from pyrogram import Client, filters
from pyrogram import InlineKeyboardButton InlineKeyboardMarkup

BTN = InlineKeyboardMarkup([[InlineKeyboardButton('💡 Source 💡', url='tg://openmessage?user_id=1857338892')],[InlineKeyboardButton('Inspire Me Again!!', callback_data='inspireagain')]])

@Client.on_message(filters.command("inspire"))
async def inspireme(bot, update):
    s = await update.reply_text("Processing...⏳",quote=True)
    url = "http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    await update.reply_photo(photo=img, caption="Inspire me again! © Sirius")
    await s.delete()

@Client.on_callback_query(filters.regex(r'^inspireagain'))
async def inspiremecallbak(bot, update):
    p = await update.reply_text("Processing...⏳",quote=True)
    await update.answer('Generating.....⏳')
    url = "http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    await update.reply_photo(photo=img, caption="Inspire me again! © Sirius")
    await p.delete()
    
