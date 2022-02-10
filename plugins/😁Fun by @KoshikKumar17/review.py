# (c) @KoshikKumar17
import os
from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from jokeapi import Jokes # Import the Jokes class
import asyncio

@Client.on_message(filters.private & filters.command(["review"]))
async def review(bot, update):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Click Here to Review ✨', url='https://comments.bot/thread/--pwqNLA2')]])
    await update.reply_text(
        text=script.REVIEW_TXT,
        reply_markup = reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_message(filters.private & filters.command(["getsticker"]))
async def getsticker(bot, update):
    keyboard = [['.😘', '.😂', '.😃'],['.😔', '.👋', '.🆗']]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    await update.reply_text(
        text=script.GETSTICKER_TXT,
        reply_markup = reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_message(filters.private & filters.command(["joke"]))
async def print_joke():
    j = await Jokes()  # Initialise the class
    await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])

asyncio.run(print_joke())
    rm = await message.reply_text("...🤔")
    await rm.edit(f"{print_joke} \n \n **~ @KoshikKumar17**")
