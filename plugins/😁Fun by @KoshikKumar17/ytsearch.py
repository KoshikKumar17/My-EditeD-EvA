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
            [InlineKeyboardButton(text="⭕Search Here⭕", switch_inline_query_current_chat="!yt")],
            [InlineKeyboardButton(text="↗️Search in Another Chat ↗️", switch_inline_query="!yt")]
        ]
    )
    
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func(HELP)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
            return

elif text.split()[0] == "yt":
            answers = []
            search_query = text.split(None, 1)[1]
            search_query = query.query.lower().strip().rstrip()

            if search_query == "":
                await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Type a YouTube video name...",
                    switch_pm_parameter="help",
                    cache_time=0,
                )
            else:
                search = VideosSearch(search_query, limit=50)
for result in search.result()["result"]:
                    answers.append(
                        InlineQueryResultArticle(
                            title=result["title"],
                            description="{}, {} views.".format(
                                result["duration"], result["viewCount"]["short"]
                            ),
                            input_message_content=InputTextMessageContent(
                                "https://www.youtube.com/watch?v={}".format(
                                    result["id"]
                                )
                            ),
                            thumb_url=result["thumbnails"][0]["url"],
                        )
                    )

                try:
                    await query.answer(results=answers, cache_time=0)
                except errors.QueryIdInvalid:
                    await query.answer(
                        results=answers,
                        cache_time=0,
                        switch_pm_text="Error: Search timed out",
                        switch_pm_parameter="",
                    )
