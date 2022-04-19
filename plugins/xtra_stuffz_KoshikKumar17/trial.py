import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["rkrishnaa"]))
async def getgithub(bot, message):
    await message.reply_chat_action("typing")
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    px = message.text.split(None, 1)[1]
    if "radhakrishn" in px:
        await message.reply_text("**@RadhaKrishna_SB**")
    else "jklk" in px:
        await message.reply_text("**@JayKanhaiyaLaalKi**")
