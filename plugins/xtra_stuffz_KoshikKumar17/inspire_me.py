# © Siriustar

import requests
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BTN = InlineKeyboardMarkup([[InlineKeyboardButton('💡 Source 💡', url='tg://openmessage?user_id=1857338892')],[InlineKeyboardButton('Inspire Me Again!!', callback_data='inspireagain')]])
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖🇮🇳✨ Made By ✨🇮🇳💖', url='https://t.me/KoshikKumar17')]])
A = """{} with user id:- {} used /git command."""

@Client.on_message(filters.command("inspire"))
async def inspireme(bot, update):
    s = await update.reply_text("Processing...⏳",quote=True)
    url = "http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    await update.reply_photo(photo=img, caption="Inspire me again! © Sirius", reply_markup=BTN, quote=True)
    await s.delete()

@Koshik.on_message(filters.command("github", "git")
async def getgithub(bot, message):
    await update.reply_chat_action("typing")
    un = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{un}'
    request = requests.get(URL)
    result = request.json()
    try:
        url = result['html_url']
        name = result['name']
        company = result['company']
        bio = result['bio']
        created_at = result['created_at']
        avatar_url = result['avatar_url']
        blog = result['blog']
        location = result['location']
        repositories = result['public_repos']
        followers = result['followers']
        following = result['following']
        caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Click Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`
**@KoshikKumar17**"""
    except Exception as e:
        print(str(e))
        pass
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=BUTTONS)
    await bot.send_message(LOG_CHANNEL, A.format(update.from_user.mention, update.from_user.id))
