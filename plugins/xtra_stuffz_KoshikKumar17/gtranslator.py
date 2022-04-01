from googletrans import Translator
from pyrogram import Client, filters
from info import LOG_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.list import list

A = """Hi, {} with user id:- {} used /tr command."""

@Client.on_message(filters.command(["tr", "translate"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "😇Language codes😇", url="https://cloud.google.com/translate/docs/languages"
                                        )
                                    ],
				    [
                                        InlineKeyboardButton(
                                            "✗ Close the Translation ✗", callback_data="close_data"
                                        )
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			except:
			   	await message.reply(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)

		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
