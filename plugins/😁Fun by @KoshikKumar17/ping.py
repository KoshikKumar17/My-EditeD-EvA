#by saminsumesh...
import time
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter


@Client.on_message(filters.command("hi", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz8Zh_ni_q5DjjojrOO81rt6zUVXcgQAC6AMAAvKJ4VeIlT8Fu-vddyME)


@Client.on_message(filters.command("kiss", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz6hh_mV3Lhc5piK2FdksyUx_r7QFYwACwwIAAscw4FfCkTbYQEv_rCME))

@Client.on_message(filters.command("music", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz9Rh_nrFKy35z76W9SRuhU8lHFqoXgAC6AMAAk6faFRaUKgjwWTmrCME)

@Client.on_message(filters.command("laugh", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz8xh_nliel7JjMunSMIGj71GAzRZvwAC_gMAAvRk4FcD6Xj9RJhi0yME)

@Client.on_message(filters.command("good", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz85h_nls6-mcG24RgJY1mU5xsuDp2QACxQQAAgG_aFSPjT1h-8iLFiME)

@Client.on_message(filters.command("sorry", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz9Bh_nl3xGapCJPjIdybBTtLRr71VQACGAMAAhF_aFRSdHzhoXs_KSME)

@Client.on_message(filters.command("ok", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(CAACAgUAAxkBAAEDz9Jh_nl75aWBVWGmJZalfZlEC24mmQACawIAAjawaFQmZA1Iyi7XTyME)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...🤔")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong😜😜!\n{time_taken_s:.3f} ms\n \n **~ @KoshikKumar17**")
