# © SpEcHiDe @anydlbot
import asyncio
import json
import math
import os
import time
from PIL import Image

import pyrogram

from plugins.ytdl.a import humanbytes
from plugins.ytdl.b import DownLoadFile
from plugins.ytdl.c import random_char

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserBannedInChannel


@Client.on_message(filters.command(["ytdl"]))
async def echo(bot, message):
    await message.reply_chat_action("typing")
    if len(message.command) != 2:
        await message.reply_text("/ytdl [YTDL supported link] \n\n Like:- `/ytdl https://abc.xyz/123pqr`", quote=True)
        return
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    url = message.text.split(None, 1)[1]
