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

    REVIEW_TXT = """Hey Friends 👋,

Tell me your <b>opinion</b> about this bot😉

<b>It will motivate me to make this bot more user-friendly.😋

If you want to request any bugs or features comment here😉</b>
"""

    CHANGELOGS_TXT = """Hey.,🙂
<b>Here is the Changelogs of the Latest Update
Date:- 14th April 2022 IST 🇮🇳
B.R. Ambedkar Jayanti Special 🙏🏻...
Thanks a lot to Father of Our Constitution 😊👍🇮🇳
Changelogs:-</b>

<i>--> updated Whole Ui
--> Bot Updated .
--> Some Bugs Fixed .
--> Added many new things.
---> Click /start to know more</i>
.
<b>For bugs hit /report ...
.
Thanks❤️,
@KoshikKumar17</b>"""

    HELP_TXT = """<b>Click on the Button Below to know about that module in Details.</b>
...❤️"""

    SOURCE_TXT = """Category: <b>Source  Code 💡</b>
..
Function: <b>Nothing.!! 😂📍</b>
.
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
.
<b>NOTE:</b>
1. Bot must be added in the Group with <b>All Admin Rights.</b>
2. ONLY Admins can add FILTERS in a chat.
3. Alert buttons have a MAX limit of 64 characters.
.
<b>Commands and Usage:</b>
• /filter - <code>Add a filter in a chat.</code>
“““
Like:- /filter [keyword] [reply]
e.g:- <code>/filter hi Hi</code> will reply to every msg which contains <b>hi</b> with <b>Hi</b>...💥
<b><i><u>It must be parsed as MarkDown</u></i></b>
„„„
• /filters - <code>List all the filters of a chat.</code>
• /del - <code>Delete a specific filter in chat</code> e.g:- <code>/del [keyword]</code>
• /delall - <code>Delete all the filters in a chat (Chat owner only)</code>
"""

    BUTTON_TXT = """Category: <b>Buttons Help </b>
..
Function: <b>It will help you to parse down buttons and Text in MarkDown format.. ✨🤘</b>
<b>How it Works 🙂?</b>
.
#For_Parsing_Text_In_MD_Format
.
*hello* :- will result <b>hello</b>
_hello_ :- will result <i>hello</i>
[RKrishnaa](https://t.me/RKrishnaa) :- will result <a href='https://t.me/RKrishnaa'>RKrishnaa</a>
<b>For more:-</b>  Google <code>Syntax for MarkDown</code>
.
- This Bot supports both URL and Alert inline buttons. -
.
<b>NOTE:</b>
<i>1. Telegram will not allow you to send buttons without any content, so content is MANDATORY.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed in MARKDOWN format.</i>
...
<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/RKrishnaa)</code>
.
<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an Alert message.)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
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
