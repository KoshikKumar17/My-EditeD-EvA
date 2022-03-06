# (c) @KoshikKumar17

import os
from pyrogram import Client, filters
from pyrogram.types import *

CALC_TXT = "**🙋🏻‍♂️ Made with ❤️ in 🇮🇳 by @KoshikKumar17 🙇🏻**"
CALC_BTNS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DEL", callback_data="DEL"),
            InlineKeyboardButton("AC", callback_data="AC"),
            InlineKeyboardButton("(", callback_data="("),
            InlineKeyboardButton(")", callback_data=")")
        ],
        [
            InlineKeyboardButton("7", callback_data="7"),
            InlineKeyboardButton("8", callback_data="8"),
            InlineKeyboardButton("9", callback_data="9"),
            InlineKeyboardButton("÷", callback_data="/")
        ],
        [
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
            InlineKeyboardButton("6", callback_data="6"),
            InlineKeyboardButton("×", callback_data="*")
        ],
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("-", callback_data="-"),
        ],
        [
            InlineKeyboardButton(".", callback_data="."),
            InlineKeyboardButton("0", callback_data="0"),
            InlineKeyboardButton("=", callback_data="="),
            InlineKeyboardButton("+", callback_data="+"),
        ],
        [
            InlineKeyboardButton("❤️ @KoshikKumar17 ❤️", url="https://telegram.me/KoshikKumar17")
        ]
    ]
)

@Client.on_message(filters.private & filters.command(["calc", "calculator"]))
async def calculate(bot, update):
    await update.reply_text(
        text=CALC_TXT,
        reply_markup=CALC_BTNS,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_callback_query()
async def cb_data(bot, update):
        data = update.data
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            message_text = '' if CALC_TXT in message_text else message_text
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await update.message.edit_text(
                text=f"{text}\n\n{CALC_TXT}",
                disable_web_page_preview=True,
                reply_markup=CALC_BTNS
            )
        except Exception as error:
            print(error)
