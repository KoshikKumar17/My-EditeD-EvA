# (c) @KoshikKumar17
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "Aaj mere paas gaadi hai, bungla hai, paisa hai... tumhare paas kya hai?"
    "Mere paas, mere paas... Maa hai...,"
    "Rishte mein to hum tumhare baap lagte hain, naam hai Shahenshah"
    "Kaun kambakth hai jo bardasht karne ke liye peeta hai. Main toh peeta hoon ke bas saans le sakoon"
    "Main aaj bhi pheke hue paise nahin uthata"
    "Pushpa, I hate tears... "
    "Bade bade shehron mein aisi chhoti chhoti baatein hoti rehti hain, Senorita."
    "Mogambo khush hua!"
    "Taareekh pe taareekh, taareekh pe taareekh, taarekh pe taareekh."
    "Dosti ka ek usool hai, madam: no sorry, no thank you"
    "Salim tujhe marne nahi dega ... aur hum Anarkali tujhe jeene nahi denge"
   "Aapke paon dekhe, bahut haseen hai. Inhe zameen par mat utariyega, maile ho jayenge"
   "ndaaz Apna Apna"
   "ndaaz Apna Apna"
   " jahan khade hote hai line wahin se chalu hoti hai kaliyan"
    "Thapad se darr nahi lagta, pyaar se lagta hai"
)
@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ .runs"""
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
