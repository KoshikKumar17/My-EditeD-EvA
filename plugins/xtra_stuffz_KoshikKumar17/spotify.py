# ✋ Hand Written by Koshik Kumar
# Thanks to api.fabdl.com
import os
import requests
import pyrogram
import json
from pyrogram import Client
from pyrogram import filters

@Client.on_message(filters.command("spotify"))
async def spotifydl(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("**Reply to some Spotify link.**", quote=True)
    if not message.reply_to_message.text:
        return await message.reply_text("**Reply to some Spotify link.**", quote=True)



  
