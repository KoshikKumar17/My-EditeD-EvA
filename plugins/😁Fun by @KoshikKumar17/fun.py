import html
import random
import time
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

#sleep how many times after each edit in 'moonanimation' 
EDIT_SLEEP = 1
#edit how many times in 'moonanimation' 
EDIT_TIMES = 32


moon_ani = [
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
 ]
@Client.on_message(
    filters.command("moonani", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def moonani(_, message):
    """ .moonani"""
def moonanimation(bot, update):
    msg = update.effective_message.reply_text('🌚') 
    for x in range(EDIT_TIMES):
        msg.edit_text(moon_ani[x%32])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('🌙')
