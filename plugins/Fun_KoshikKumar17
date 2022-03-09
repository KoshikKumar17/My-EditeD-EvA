# (c) @KoshikKumar17
import os 
import json
import string 
import random
import asyncio
import aiofiles
from random import choice
import pyrogram
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.text & filters.private & filters.reply & filters.regex(r'https?://[^\s]+'))
async def attach(bot, update):
    shit = await update.reply_text("**Processing...UR Request 🙂**")
    await shit.edit_text(
	    text=f"[\u2063]({update.text}){update.reply_to_message.text}",
	    reply_markup=update.reply_to_message.reply_markup
    )
