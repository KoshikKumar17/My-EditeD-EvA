# (c) @KoshikKumar17
import os
from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

@Client.on_message(filters.private & filters.command(["review"]))
async def review(bot, update):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Click Here to Review ✨', url='https://comments.bot/thread/--pwqNLA2')]])
    await update.reply_text(
        text=script.REVIEW_TXT,
        reply_markup = reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_message(filters.private & filters.command(["getsticker"]))
async def review(bot, update):
    keyboard = [['.😘', '.😂', '.😃'],['.😔', '.👋', '.🆗']]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    await update.reply_text(
        text=script.GETSTICKER_TXT.format(message.from_user.mention),
        reply_markup = reply_markup,
        disable_web_page_preview=True,
    )
