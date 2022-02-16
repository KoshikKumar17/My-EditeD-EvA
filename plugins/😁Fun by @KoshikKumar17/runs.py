# (c) @KoshikKumar17
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "Now you see me, now you don't.",
    "ε=ε=ε=ε=┌(;￣▽￣)┘",
    "Get back here!",
    "REEEEEEEEEEEEEEEEEE!!!!!!!",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You've got company!",
    "Chotto matte!",
    "Yare yare daze",
    "*Naruto run activated*",
    "*Nezuko run activated*",
    "Hey take responsibilty for what you just did!",
    "May the odds be ever in your favour.",
    "Run everyone, they just dropped a bomb 💣💣",
    "And they disappeared forever, never to be seen again.",
    "Legend has it, they're still running.",
    "Hasta la vista, baby.",
    "Ah, what a waste. I liked that one.",
    "As The Doctor would say... RUN!",
)
@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ .runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
