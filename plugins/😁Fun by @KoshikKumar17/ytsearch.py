#By @FayasNoushad and 
import os
import ytthumb
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
from youtubesearchpython import VideosSearch


@Client.on_message(filters.private & filters.command("ytsearch"))
async def text(bot, update):
    
    text = "Search youtube videos using below buttons.\n\n**Made by @KoshikKumar17**"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="⭕Search Here⭕", switch_inline_query_current_chat="")],
            [InlineKeyboardButton(text="↗️Search in Another Chat ↗️", switch_inline_query="")]
        ]
    )
    
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
