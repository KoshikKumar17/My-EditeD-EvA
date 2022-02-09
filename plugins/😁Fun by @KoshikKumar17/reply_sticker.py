# (c) @KoshikKumar17
import os
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter


@Client.on_message(filters.command("😘", COMMAND_HAND_LER) & f_onw_fliter)
async def kiss(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz6hh_mV3Lhc5piK2FdksyUx_r7QFYwACwwIAAscw4FfCkTbYQEv_rCME")

@Client.on_message(filters.command("🎶", COMMAND_HAND_LER) & f_onw_fliter)
async def music(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz9Rh_nrFKy35z76W9SRuhU8lHFqoXgAC6AMAAk6faFRaUKgjwWTmrCME")

@Client.on_message(filters.command("😂", COMMAND_HAND_LER) & f_onw_fliter)
async def laugh(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz8xh_nliel7JjMunSMIGj71GAzRZvwAC_gMAAvRk4FcD6Xj9RJhi0yME")

@Client.on_message(filters.command("😃", COMMAND_HAND_LER) & f_onw_fliter)
async def good(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz99h_oIM9Qa9Pqku9U1O6SkCwjsprgACagUAAmvb4VcvYwqSVGfp4yME")

@Client.on_message(filters.command("😔", COMMAND_HAND_LER) & f_onw_fliter)
async def sorry(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz9Bh_nl3xGapCJPjIdybBTtLRr71VQACGAMAAhF_aFRSdHzhoXs_KSME")

@Client.on_message(filters.command("🆗", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDz9Jh_nl75aWBVWGmJZalfZlEC24mmQACawIAAjawaFQmZA1Iyi7XTyME")
