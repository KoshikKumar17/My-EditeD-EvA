# Thanks to api.fabdl.com
import os
import requests
import pyrogram
import json
from pyrogram import Client
from pyrogram import filters

@Client.on_message(filters.command("spotify"))
async def spotifydl(bot, message):
    if message.reply_to_message:
        m = message.reply_to_message
        k = await message.reply_text("**Processing...⏳**", quote=True)
        url = requests.get(m, allow_redirects=True).url
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
        await message.reply_photo(
            photo=image,
            caption=caption,
            quote=True
        )
        API2 = f"https://api.fabdl.com/spotify/mp3-convert-task/{gid}/{id}"
        request1 = requests.get(API2)
        result2 = request1.json()
        predlurl = result2["result"]["download_url"]
        dlurl = predlurl.replace("\\", "")
        audio = f"https://api.fabdl.com{dlurl}"
        await message.reply_audio(
            audio=audio,
            caption=caption1,
            quote=True
        )
    else:
        await message.reply_text("**Reply to some Spotify link.**", quote=True)
#Thanks
