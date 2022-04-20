class script(object):
    START_TXT = """Hello {} 👋,
My Name is <a href=https://t.me/{}>{}</a>, I am a RoBot which can Help you to simplify your life with Telegram With <b>Multiple Features.</b>
CLICK on the Help button below know more what I can do with You.
...... 💙

<i> 💥 Don't forget to give your opinion by /report .</i> 

<u>You can report Bugs, Features or suggestions or Anything you want.😉. It will help me..!</u>"""

    ABOUT1_TXT = """<b>Hey😉,
✯ 🙄 Library: <a href='https://docs.pyrogram.org'> Pyrogram 1.3.6 </a>
✯ 😛 Language: <a href='https://python.org'> Python 3.8.7 </a>
✯ 😉 Database: <a href='https://mongodb.com'> MongoDB </a>
✯ 😊Bot Server: <a href='https://heroku.com'> Heroku (Free) </a>
✯ 🙋‍♂️Made By: <a href='tg://user?id=1162032262'> @KoshikKumar17 </a>
✯ 😝 Thanks to: @TeamEvaMaria
✯ Build Version: v2.5.2 [ Major ]"""

    QUOTES_TAGS = """Hehe..,
<b>Here are the Supported categories of quotes:-</b>
You can use any of them by using:- <code>/quote</code> [category]
<b>❗❗ This will give you a Quote of that category. ❗❗</b>
<b>CATEGORIES:</b>
<code>business</code>, <code>education</code>, <code>faith</code>, <code>famous-quotes</code>, <code>friendship</code>, <code>future</code>, <code>happiness</code>, <code>history</code>, <code>inspirational</code>, <code>life</code>, <code>literature</code>, <code>love</code>, <code>nature</code>, <code>politics</code>, <code>proverb</code>, <code>religion</code>, <code>science</code>, <code>success</code>, <code>technology</code>, <code>wisdom</code>"""

    CHANGELOGS_TXT = """Hey.,🙂
<b>Here is the Changelogs of the Latest Update
Date:- 20th April 2022 🇮🇳
Changelogs:-</b>

<i>-->Updated Help message.
--> Click /start to know more.</i>
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
„„„"""

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
• /imdb  - <code>get the film information from IMDb source.</code> /imdb pushpa
• /search  - <code>get the film information from various sources.</code> /search pushpa"""

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
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code> 𝙼𝚒𝙱
★ Free Storage: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    REPORTME = """Category: <b>Reporting 💌</b>
..
Function: <b>By using this command. You can contact me. Report anything of Any Type about this bot or else. 📍</b>

<b>How it Works 🙂?</b>
>> Send me the message you want to report.
>> Reply that message with /report .
..
Done ✅.. I will forward that message to my Owner."""

    ATTACHLINK_TXT = """Category: <b>Attach Link</b>
..
Function: <b>Attach the link with text or media.📍</b>

<b>How it Works 🙂?</b>
>> Send me a <b>media or a text.</b>
>> Reply that <b>media or text</b> with a <b>link</b>
>> <b>Done ✅ : You will get your message with attached link.</b>
"""

    IMG2PDF_TXT = """Category: <b>Image to PDF</b>
..
Function: <b>Convert any type of image(s) to PDF, .pdf file format.😇✨</b>

<b>How it Works 🙂?</b>
>> Send an <b>Image.🖼️</b>. {Not as Document}
>> NOW, You have 3 options.
1️⃣.  If you want to <b>add</b> more image, Send me <b>images One by One</b>. When done send <b>/c2pdf</b>
2️⃣.  If <b>done</b> click here  or send  <b>/c2pdf</b>
3️⃣. If you want to <b>cancel or clear</b> this <b>list or queue or process</b>. Send <b>/clearpdfcache</b>
...
<i>Done ✅. YOU WILL GET YOUR REPLY ON THE BASIS OF COMMAND YOU SEND <b>( /C2PDF OR /CLEARPDFCACHE)</b> 😉</i>
"""

    BOTSTSHK_TXT = """Category: <b>Bot Status (Heroku)</b>
..
Function: <b>Get This Bot's Heroku dyno status and it's uptime. 😎✨</b>

<b>How it Works 🙂?</b>
>> SEND <b> /botstatus </b>
>> You will get Dyno usage as a reply to your message.😁

Done ✅.."""

    GTRANS_TXT = """Category: <b>Google Translator or GTRANS.</b>
..
Function: <b>TRANSLATE from one language other.😇✨</b>
<i>Language should be supported by Google.</i>

<b>How it Works 🙂?</b>
>> Send me the <b>text</b> you want to <b>Translate</b>.
>> REPLY that text with /tr [language code]
Language code:- <a href="https://cloud.google.com/translate/docs/languages"> <b>Click here</b> </a>
>> Done ✅.. You will get the translated text.
✨
Example: If you want to Translate that text to hindi. Then Reply that text with <code>/tr hi</code>
"""

    TTS_TXT = """Category: <b>Text to Speech</b>
..
Function: <b>Convert any type of text to speech  (Voice🗣️).. #ByGoogle</b>

<b>How it Works 🙂?</b>
>> Send me any type of <b>text</b> 😃.
>> <b>REPLY that text</b> with command <b>/tts</b>

<i>Done ✅..... You will get your replied text as speech in an Audio File.😉✨</i>"""

    TGRAPH_TXT = """Category: <b>Telegraph Uploader</b>
..
Function: <b>Upload any type of Media 🖼️ to Telegraph ( telegra.ph ) 🤓💥</b>

<b>How it Works 🙂?</b>
>> Send me any type of <b>Media ( upto max 5MB) 🖼️</b>.
>> <b>REPLY that media</b> with command <b>/telegraph</b>.
>> Wait a bit till it uploads your media to telegra.ph

<i>Done ✅..... You will get a telegra.ph link for your media.😜✨</i>"""

    SONGDL_TXT = """Category: <b>Song Downloader</b>
..
Function: <b>Download any Song from YouTube in .mp3 or .mp4 format.💥</b>

</u></i>‼️THIS FEATURE IS ONLY TO DOWNLOAD SONGS FROM YOUTUBE. NOT OTHER TYPE OF VIDEOS OTHERWISE,  YOU WILL GET WRONG VIDEOS ‼️</i></u>

<b>How it Works 🙂?</b>
>>First choose an option from below Buttons...😁
As MP3(Audio) or As MP4(Video)"""

    YTTHUMB_TXT = """Category: <b>YouTube Thumbnail Downloader</b>
..
Function: <b>Download the Thumbnail of YouTube videos in HD Quality. ( YouTube #Shorts not supported) ✨💥</b>

<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /ytthumb </b> [youtube link]
e.g. -» <code> /ytthumb https://youtu.be/VYslt8bc-4Q </code>
.
Done ✅... You will get your thumbnail as an image....🖼️"""

    YTTAGS_TXT = """Category: <b>YouTube Tags Finder</b>
..
Function: <b>Find/Search the Tags of YouTube videos in an easy way. ( YouTube #Shorts supported) 😁💥</b>

<u>‼️ This feature is for Youtubers. Because they have work of the tags. Others can ignore this.‼️</u>

<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /yttags </b> [youtube link]
e.g. -» <code> /yttags https://youtu.be/VYslt8bc-4Q </code>
.
Done ✅... You will get the tags of the video as a text....📝"""

    GITHUB_TXT = """Category: <b>GitHub Profile Details using api.github.com/users</b>
..
Function: <b>Get anyone's github profile details (Along with their D.P.) 😇✨</b>

<u>Make sure to enter correct username 😉</u>

<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /github </b> [github username]
e.g. -» <code> /github hkrrish </code>
.
Done ✅... You will get all details of that GitHub User along with their D.P."""

    QUOTES_TXT = """Category: <b>Quotes 💝</b>
..
Function: <b>Get a Quote of Specified Category/Tags each time.... 😘✨</b>

<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /quote </b> [quote category]
e.g. -» <code> /quote love </code> will give you a Quote of the category (Love ❤️).
.
Done ✅... You will get the Quote along with category."""

    INSPIRE_TXT = """Category: <b>Inspire Me 🙂</b>
..
Function: <b>Get yourself Inspired with a quote and an image... 🖼️✨</b>

<b>How it Works 🙂?</b>
>> Send the command <b>/inspire</b>
.
Done ✅.... You will get an image.😁"""

    PDFTOOLS_TXT = """Category: <b>PDF Tools</b>
..
Function: <b>Access different types of PDF functions OR help related to PDFs.💥✨</b>

<b>How it Works 🙂?</b>
>> Send /pdfinfo with a Reply to PDF file to get it's information.
>> More coming soon...."""

    JOKES_TXT = """Category: <b>Joke 😂</b>
..
Function: <b>Get a Random Joke each time. 😂💥✨</b>

<b>How it Works 🙂?</b>
>> Send the command <b>/joke</b> to get a joke.

."""

    SHORTLINK_TXT = """Category: <b>Link Shortener</b>
..
Function: <b>Shorten long/real links in a small link without any Wastage of Time.. 🤠💥</b>

</i>Currently Supported:- clck.ru , da.gd , is gd , osdb.link , ttm.sh <b>[ All are AD-FREE ]</b></i>
<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /short </b> [your long/real link]
e.g. -» <code> /short https://youtu.be/VYslt8bc-4Q </code>
.
Done ✅... You will get your shortened  link.. 🔗 That's it!"""

    UNSHORTLINK_TXT = """Category: <b>Link UnShortener</b>
..
Function: <b>UnShorten shortened links to real / long link without any Wastage of Time.. 😙💥</b>

<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /unshort </b> [your long link]
e.g. -» <code> /unshort https://bit.ly/BGMI_AppStore </code>
.
Done ✅... You will get your real / long  link.. 🔗 That's it!"""

    SONGDLMP4_TXT = """ HEHE 😁 
<b>You have chooses as MP4(As Video)🎥</b> .... Now follow the below process:
<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /video </b> [youtube song name]
e.g. -» <code> /video tu jaane na </code>
Will give you a song named <b> Tu Jaane Na </b> in .mp4 format with Best Quality. 💥

📍 Extra:- You can use /video or /mp4 as command.
Done ✅... You will get your Song as video 🤠."""

    SONGDLMP3_TXT = """HEHE 😁 
<b>You have chooses as MP3 (As Audio)🎵</b> .... Now follow the below process:
<b>How it Works 🙂?</b>
>> Send me a message in the below format:-
<b> /song </b> [youtube song name]
e.g. -» <code> /song tu jaane na </code>
Will give you a song named <b> Tu Jaane Na </b> as .mp3 or .m4a format with Best Quality. 💥

📍 Extra:- You can use /song or /mp3 as command.
Done ✅... You will get your Song as audio 🤠."""

    SHTXT_TXT = """Category: <b>Share Text</b>
..
Function: <b>Get shareable link of any type of text. In the format <code>https://t.me/share/url?url=</code> 😊💥</b>

<b>How it Works 🙂?</b>
>> Send me the text For which you want to generate shareable link. <b>Only texts and captions of Media are Supported..</b>
>> Reply that msg with /share or /shtxt .
....
Done ✅... You will get your link.🤠"""
