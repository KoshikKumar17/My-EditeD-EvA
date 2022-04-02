# (c) @KoshikKumar17
import os
from os import error
import pyrogram
import PyPDF2
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖🇮🇳✨ Made By ✨🇮🇳💖', url='https://t.me/KoshikKumar17')]])
A = """{} with user id:- {} used /pdfinfo command."""

DLLC = "./DOWNLOADS/PyPDF/"

@Koshik.on_message(filters.command(["pdfinfo"]))
async def info(bot, message):
     try:
         if message.reply_to_message:
              txt = await message.reply_text("**Validating PDF...🌐**", quote=True, reply_markup=BUTTONS) #VALIDATING PDF
              pdf_path = DLLC + f"{message.chat.id}.pdf" # PDF FILE PATH
              await txt.edit("**Downloading....⬇️**")
              await message.reply_to_message.download(pdf_path)  
              await txt.edit("**Downloaded File✅✨**")
              pdf = open(pdf_path,'rb')
              pdf_reader = PyPDF2.PdfFileReader(pdf) # PDF READER
              await txt.edit("**Getting Number of Pages....😎😎**")
              num_of_pages = pdf_reader.getNumPages()
              await txt.edit(f"**Found {num_of_pages} Page(s)...😇**")
              await txt.edit("**Getting PDF info...⏳**")
              info = pdf_reader.getDocumentInfo()
              await txt.edit(f"""
**Author** : {info.author}
**Creator** : {info.creator}
**Producer** : {info.producer}
**Subject** : {info.subject}
**Title** : {info.title}
**Pages** : {num_of_pages}

**@KoshikKumar17** 💖""")
              await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
              await message.reply_to_message(LOG_CHANNEL, as_copy=True) 

              os.remove(pdf_path)
         else:
             await message.reply_text("**Please Reply to a PDF File...😪😪**", quote=True)
     except Exception as error :
         await message.reply_text(f"**Oops🥴 ,** `{error}`", quote=True)
