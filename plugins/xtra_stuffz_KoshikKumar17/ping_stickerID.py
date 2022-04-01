
import time
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...🤔")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong😜😜!\n{time_taken_s:.3f} ms\n \n **~ @KoshikKumar17**")

@Client.on_message(filters.command("👋", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz8Zh_ni_q5DjjojrOO81rt6zUVXcgQAC6AMAAvKJ4VeIlT8Fu-vddyME")


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):
    p = await message.reply_text("**Processing...⏳**",quote=True)   
    if message.reply_to_message.sticker:
       await message.reply_chat_action("typing")
       await p.edit(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`\n \n**@KoshikKumar17**")
    else: 
       await p.edit("Oops !! Not a sticker file")


@Client.on_message(filters.private & filters.command(["findsticker"]))
async def findsticker(bot, message):  
  try:
       if message.reply_to_message.text: 
          txt = await message.reply_text("**Validating Sticker ID...**")
          stickerid = str(message.reply_to_message.text)
          chat_id = str(message.chat.id)
          await txt.delete()
          await message.reply_chat_action("choose_sticker")
          await bot.send_sticker(chat_id,f"{stickerid}")
       else:
          await message.reply_text("**__Please reply to a ID to get its STICKER.__**")
  except Exception as error:
          await message.reply_text(str(error))
          
