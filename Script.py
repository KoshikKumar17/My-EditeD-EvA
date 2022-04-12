class script(object):
    START_TXT = """Hello {} 👋,
My Name is <a href=https://t.me/{}>{}</a>, I am a RoBot which can Help you to simplify your life with Telegram With <b>Multiple Features.</b>
CLICK on the Help button below know more what I can do with You.
...... 💙
<i> 🤘Don't forget to give your opinion by /report .</i> <u>You can report Bugs, Features or suggestions or Anything you want.😉. It will help me..!</u>"""
    ABOUT1_TXT = """<b>Hey😉,
✯ 🙄 Library: <a href='https://docs.pyrogram.org'> Pyrogram 1.3.6 </a>
✯ 😛 Language: <a href='https://python.org'> Python 3.8.7 </a>
✯ 😉 Database: <a href='https://mongodb.com'> MongoDB </a>
✯ 😊Bot Server: <a href='https://heroku.com'> Heroku (Free) </a>
✯ 🙋‍♂️Made By: <a href='tg://user?id=1162032262'> @KoshikKumar17 </a>
✯ 😝 Thanks to: @TeamEvaMaria
✯ Build Version: v2.5.1 [ Major ]"""
    QUOTES_TAGS = """Hehe..,
<b>Here are the Supported categories of quotes:-</b>
You can use any of them by using:- <code>/quote</code> {tag.name}

<b>❗❗ This will give you a Quote of that category. ❗❗</b>

<b>CATEGORIES:</b>
<code>business</code>, <code>education</code>, <code>faith</code>, <code>famous-quotes</code>, <code>friendship</code>, <code>future</code>, <code>happiness</code>, <code>history</code>, <code>inspirational</code>, <code>life</code>, <code>literature</code>, <code>love</code>, <code>nature</code>, <code>politics</code>, <code>proverb</code>, <code>religion</code>, <code>science</code>, <code>success</code>, <code>technology</code>, <code>wisdom</code>"""
    GETSTICKER_TXT = """<b>Hey Bro👋,

Choose an Emoji😜 of your choice from Below.</b>

<i>Currently only these supported.. 
I will add more soon...</i>"""

    REVIEW_TXT = """Hey Friends 👋,

Tell me your <b>opinion</b> about this bot😉

<b>It will motivate me to make this bot more user-friendly.😋

If you want to request any bugs or features comment here😉</b>
"""
    CHANGELOGS_TXT = """Hey.,🙂
<b>Here is the Changelogs of the Latest Update
Date:- 17th February 2022 > 09:00AM IST 🇮🇳
Changelogs:-</b>

<i>--> Added New commands /video , /song , .runs , /tts , /joke single .
--> Bot Updated .
--> Some Bugs Fixed .
--> Added many new things.
---> Click Menu in below left corner for more😂</i>

I can't tell more here. Please <a href='https://telegra.ph/All-Commands-Lists-Of-This-Bot-10-30'> CLICK_HERE </a> to get detailed information...
<b>For bugs hit /review ...

Thanks❤️,
@KoshikKumar17</b>"""
    COMMANDS1_TXT = """<b>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>
<a href='https://telegra.ph/All-Commands-Lists-Of-This-Bot-10-30'> 𝐂𝐋𝐈𝐂𝐊 𝐇𝐄𝐑𝐄 </a> ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ..."""
    HELP_TXT = """𝙷𝙴𝚈 {}
<b>Click on the Button Below to know about that module in Details.</b>
...❤️"""
    SOURCE_TXT = """Category: <b>Source  Code 💡</b>
..
Function: <b>Nothing.!! 😂📍</b>

<b>THIS BOT IS OPEN SOURCE. YOU CAN USE THAT SOURCE TO CREATE YOUR OWN PERSONAL BOT.✨💥</b>
----------->
 <a href='https://github.com/EvamariaTG/EvaMaria'><b> • Base Repository </b></a>
<a href='https://github.com/KoshikKumar17/My-EditeD-EvA'><b> • Repository On Which Bot Runs </b></a>"""
    MANUELFILTER_TXT = """Category: <b>FILTERS: Manual Filter 🤘</b>
..
Function: <b>Filter is the feature where users can set automated replies for a particular keyword 😇 and This Bot will respond whenever a keyword is found the message.✌️📍
.
It supports both Alert and URL Buttons.</b>
...
<b>How it Works 🙂?</b>

<b>NOTE:</b>
1. Bot must be added in the Group with <b>All Admin Rights.</b>
2. ONLY Admins can add FILTERS in a chat.
3. Alert buttons have a MAX limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>Add a filter in a chat.</code>
“““
Like:- /filter [keyword] [reply]
e.g:- <code>/filter hi Hi</code> will reply to every msg which contains <b>hi</b> with <b>Hi</b>...💥
<b><i><u>• It must be parsed as MarkDown</u></i></b>
„„„
• /filters - <code>List all the filters of a chat.</code>
• /del - <code>Delete a specific filter in chat</code> e.g:- <code>/del [keyword]</code>
• /delall - <code>Delete all the filters in a chat (Chat owner only)</code>"""
    BUTTON_TXT = """Category: <b>Buttons Help </b>
..
Function: <b>It will help you to parse down buttons and Text in MarkDown format.. ✨🤘</b>
<b>How it Works 🙂?</b>
#For_Parsing_Text_In_MD_Format

*hello* :- will result <b>hello</b>
_hello_ :- will result <i>hello</i>
[RKrishnaa](https://t.me/RKrishnaa) :- will result <a href='https://t.me/RKrishnaa'>RKrishnaa</a>
<b>For more:-</b>  Google <code>Syntax for MarkDown</code>

- This Bot supports both URL and Alert inline buttons. -

<b>NOTE:</b>
<i>1. Telegram will not allow you to send buttons without any content, so content is MANDATORY.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed in MARKDOWN format.</i>
...
<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/RKrishnaa)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an Alert message.)</code>"""
    AUTOFILTER_TXT = """Category: <b>FILTERS: Auto Filter </b>
..
Function: <b> In this function, Bot saves all the files in a channel to its DB and whenever a person sends any message in group, Bot will automatically detect the keywords and REPLYs with a message which contains buttons of those files.  ✨😇</b>
..
<b>How it Works 🙂?</b>
.
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.
“““
<b>⚠️I DON'T USE THIS FEATURE FOR MY BOT BECAUSE I DON'T HAVE ANY FILES TO SAVE IN IT'S DB.😁 IF I HAVE THEY ARE COPYRIGHTED. ⚠️<b>
........
<i><u>This is the Best feature of this Repository. But I don't use. If you want to use this make your Own Bot with  <a href='https://github.com/EvamariaTG/EvaMaria'><b> This Repository </b></a></u></i>
„„„""""
    CONNECTION_TXT = """Category: <b>Connections </b>
..
Function: <b>It is used to connect Bot to PM for managing filters. It helps to avoid spamming in groups.✨😜</b>
..
<b>How it Works 🙂?</b>
.....
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM.

<b>Commands and Usage:</b>
• /connect  - <code>Connect a particular chat to your PM.</code>
• /disconnect  - <code>Disconnect from a chat.</code>
• /connections - <code>List all your connections.</code>"""
    EXTRAMOD_TXT = """Category: <b>Extra Modules </b>
..
Function: <b>These are the Extra features of this Bot. These features are not added by Me . These features are inherited from <a href='https://github.com/EvamariaTG/EvaMaria'><b> • Base Repository </b></a> ✨😅</b>
..
<b>How it Works 🙂?</b>
<b>NOTE:</b>
These are the Extra features of this Bot from <a href='https://github.com/EvamariaTG/EvaMaria'><b> • Base Repository </b></a>
...
<b>Commands and Usage:</b>
• /id - <code>Get id of a specified user.</code> /id [id/username/reply]
• /info  - <code>Get information about a user.</code> OR /info [id/username/reply]
• /imdb  - <code>get the film information from IMDb source.</code> <b>/imdb pushpa</b>
• /search  - <code>get the film information from various sources.</code> e.g <b>/search pushpa</b>"""
    ADMIN_TXT = """Category: <b>ADMIN Modules </b>
..
Function: <b>These are the COMMANDS only for ADMINS. Those whom I have added as Bot's ADMINS in heroku vars. ✨😅</b>
..
<b>How it Works 🙂?</b>
..
<b>Commands and Usage:</b>
• /logs - <code>To get the rescent errors</code>
• /stats - <code>To get status of files in db.</code>
• /delete - <code>To delete a specific file from db.</code>
• /users - <code>To get list of my users and ids.</code>
• /chats - <code>To get list of the my chats and ids </code>
• /leave  - <code>To leave from a chat.</code>
• /disable  -  <code>To disable a chat.</code>
• /ban  - <code>To ban a user.</code>
• /unban  - <code>Tk unban a user.</code>
• /channel - <code>To get list of total connected channels</code>
• /broadcast - <code>To broadcast a message to all users.</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
