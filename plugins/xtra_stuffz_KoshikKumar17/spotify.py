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
        return await k.edit_text("**Reply to some Spotify link.**")
    if not message.reply_to_message.text:
        return await k.edit_text("**Reply to some Spotify link.**")
    if ("album" in message.reply_to_message.text) or ("playlist" in message.reply_to_message.text):
        return await k.edit_text("**Album or Playlist links not supported.**")
    url = requests.get(f"{message.reply_to_message.text}", allow_redirects=True).url
    API1 = f"https://api.fabdl.com/spotify/get?url={url}"
    request = requests.get(API1)
    result1 = request.json()
    track_name = result1["result"]["name"]
    id = result1["result"]["id"]
    gid = result1["result"]["gid"]
    artists = result1["result"]["artists"]
    preimage = result1["result"]["image"]
    image = preimage.replace("\\", "")
    caption = f"""**{track_name}**\n\n__{artists}__"""
    caption1 = f"""**Title:** {track_name}\n\n**Artists:** {artists}"""
    await k.delete()
    z = await message.reply_photo(
        photo=image,
        caption=caption,
        quote=True
    )
    API2 = f"https://api.fabdl.com/spotify/mp3-convert-task/{gid}/{id}"
    request1 = requests.get(API2)
    result2 = request1.json()
    predlurl = result1["result"]["download_url"]
    dlurl = predlurl.replace("\\", "")
    API = f"https://api.fabdl.com{dlurl}"
    await message.reply_audio(
        audio=API,
        caption=caption1,
        quote=True)
#Thanks
