# (c) @KoshikKumar17
import os
from os import error
import pyrogram
import PyPDF2
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('๐๐ฎ๐ณโจ Made By โจ๐ฎ๐ณ๐', url='https://t.me/KoshikKumar17')]])
A = """{} with user id:- {} used /pdfinfo command."""

DLLC = "./DOWNLOADS/PyPDF/"

@Koshik.on_message(filters.command(["pdfinfo"]))
async def info(bot, message):
     try:
          if message.reply_to_message:
               txt = await message.reply_text("**Validating PDF...๐**", quote=True) #VALIDATING PDF
               pdf_path = f"{DLLC}{message.chat.id}.pdf"
               await txt.edit("**Downloading....โฌ๏ธ**")
               await message.reply_to_message.download(pdf_path)
               await txt.edit("**Downloaded Fileโโจ**")
               pdf = open(pdf_path,'rb')
               pdf_reader = PyPDF2.PdfFileReader(pdf) # PDF READER
               await txt.edit("**Getting Number of Pages....๐๐**")
               num_of_pages = pdf_reader.getNumPages()
               await txt.edit(f"**Found {num_of_pages} Page(s)...๐**")
               await txt.edit("**Getting PDF info...โณ**")
               info = pdf_reader.getDocumentInfo()
               await txt.edit(f"""
**Author** : {info.author}
**Creator** : {info.creator}
**Producer** : {info.producer}
**Subject** : {info.subject}
**Title** : {info.title}
**Pages** : {num_of_pages}

**@KoshikKumar17** ๐""")
               await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id))
               await message.reply_to_message.forward(chat_id=LOG_CHANNEL) 

               os.remove(pdf_path)
          else:
               await message.reply_text("**Please Reply to a PDF File...๐ช๐ช**", quote=True)
     except Exception as error :
         await message.reply_text(f"**Oops๐ฅด ,** `{error}`", quote=True)
