#by saminsumesh...
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

@Client.on_message(filters.command("hi", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz8Zh_ni_q5DjjojrOO81rt6zUVXcgQAC6AMAAvKJ4VeIlT8Fu-vddyME")
