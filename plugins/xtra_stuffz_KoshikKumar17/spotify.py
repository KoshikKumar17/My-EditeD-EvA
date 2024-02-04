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
    k = await message.reply_text("**Processing...⏳**", quote=True)
    if not message.reply_to_message:
        return await k.edit_text("**Reply to some Spotify link.**", quote=True)
    if not message.reply_to_message.text:
        return await k.edit_text("**Reply to some Spotify link.**", quote=True)
    if ("album" in message.reply_to_message.text) or ("playlist" in message.reply_to_message.text):
        return await k.edit_text("**Album or Playlist links not supported.**", quote=True)
    url = requests.get(f"{message.reply_to_message.text}", allow_redirects=True).url
    API1 = f"https://api.fabdl.com/spotify/get?url={url}"
    request = requests.get(API1)
    result1 = request.json()
    track_name = result1["result"]["track"]
    
    



  
