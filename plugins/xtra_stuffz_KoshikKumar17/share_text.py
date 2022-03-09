import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def share_link(text: str) -> str:
    return "**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(text)

@Client.on_message(filters.command(["share", "sharetext", "shtxt"]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1️⃣. You can reply **Any Messages**.✌️\n2️⃣. It doesn't support any **Media**🙄.\n\n**Any Question Ask @KoshikKumar17**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "💛 Father 💛", url=f"https://t.me/KoshikKumar17")
                    ]                
                ]
            ),
            reply_to_message_id=reply_id
        )
        return
    await message.reply_text(share_link(input_text), reply_to_message_id=reply_id)
