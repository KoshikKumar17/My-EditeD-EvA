# (c) @KoshikKumar17
import os , glob
from os import error
import pyrogram
import time
import math
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document

DLDICT = "./DOWNLOADS/"

@Koshik.on_message(filters.private & filters.command(["getsticker"]))
async def getstickerasfile(bot, message):  
    px = await message.reply_text("**Checking Sticker...🕵️**")
    if message.reply_to_message is False:
        await px.edit("**Not a Sticker File!!🥺**")
    else :
          if message.reply_to_message is None: 
               px =  await px.edit("**Reply to a Sticker File!...🙇🏻‍♂️**")       
          else :
               if message.reply_to_message.sticker.is_animated is False:        
                   try : 
                       tx = await message.reply_text("**Downloading...🤒**")
                       file_path = DLDICT + f"{message.chat.id}.png"
                       await message.reply_to_message.download(file_path)   
                       await tx.edit("**Successfully Downloaded...✅**")
                       await tx.edit("**Uploading...🤧**")
                       start = time.time()
                       await message.reply_document(file_path,caption="**@KoshikKumar17**")
                       await tx.delete()   
                       os.remove(file_path)
                   except Exception as error:
                       print(error)

    
@Koshik.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if not message.reply_to_message:
        return await message.reply_text("**Reply to some sticker, Brother.🙃**")
    if not message.reply_to_message.sticker:
        return await message.reply_text("**Reply to some sticker, Brother.🙃**")
       await message.reply(f"**😀The Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n **😃The Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`\n\n**@KoshikKumar17**", quote=True)
    else: 
       await message.reply("**Oops !! Not a sticker file...🤕**")


@Koshik.on_message(filters.private & filters.command(["findsticker"]))
async def findsticker(bot, message):  
  try:
       if message.reply_to_message: 
          txt = await message.reply_text("**Validating Sticker ID.....🤒**")
          stickerid = str(message.reply_to_message.text)
          chat_id = str(message.chat.id)
          await txt.delete()
          await bot.send_sticker(chat_id,f"{stickerid}")
       else:
          await message.reply_text("**Please reply to a ID to get its STICKER.**")
  except Exception as error:
        txt = await message.reply_text("**Not a Valid Sticker ID.**")
