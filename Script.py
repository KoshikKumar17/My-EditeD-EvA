class script(object):
    START_TXT = """Hello {} ๐,
My Name is <a href=https://t.me/{}>{}</a>, I am a RoBot which can Help you to simplify your life with Telegram With <b>Multiple Features.</b>
CLICK on the Help button below know more what I can do with You.
...... ๐

<i> ๐ฅ Don't forget to give your opinion by /report .</i> 

<u>You can report Bugs, Features or suggestions or Anything you want.๐. It will help me..!</u>"""

    ABOUT1_TXT = """<b>Hey๐,
โฏ ๐ Library: <a href='https://docs.pyrogram.org'> Pyrogram 1.3.6 </a>
โฏ ๐ Language: <a href='https://python.org'> Python 3.8.7 </a>
โฏ ๐ Database: <a href='https://mongodb.com'> MongoDB </a>
โฏ ๐Bot Server: <a href='https://heroku.com'> Heroku (Free) </a>
โฏ ๐โโ๏ธMade By: <a href='tg://user?id=1162032262'> @KoshikKumar17 </a>
โฏ ๐ Thanks to: @TeamEvaMaria
โฏ Build Version: v2.5.2 [ Major ]"""

    QUOTES_TAGS = """Hehe..,
<b>Here are the Supported categories of quotes:-</b>
You can use any of them by using:- <code>/quote</code> [category]
<b>โโ This will give you a Quote of that category. โโ</b>
<b>CATEGORIES:</b>
<code>business</code>, <code>education</code>, <code>faith</code>, <code>famous-quotes</code>, <code>friendship</code>, <code>future</code>, <code>happiness</code>, <code>history</code>, <code>inspirational</code>, <code>life</code>, <code>literature</code>, <code>love</code>, <code>nature</code>, <code>politics</code>, <code>proverb</code>, <code>religion</code>, <code>science</code>, <code>success</code>, <code>technology</code>, <code>wisdom</code>"""

    CHANGELOGS_TXT = """Hey.,๐
<b>Here is the Changelogs of the Latest Update
Date:- 20th April 2022 ๐ฎ๐ณ
Changelogs:-</b>

<i>-->Updated Help message.
--> Click /start to know more.</i>
.
<b>For bugs hit /report ...
.
Thanksโค๏ธ,
@KoshikKumar17</b>"""

    HELP_TXT = """<b>Click on the Button Below to know about that module in Details.</b>
...โค๏ธ"""

    SOURCE_TXT = """Category: <b>Source  Code ๐ก</b>
..
Function: <b>Nothing.!! ๐๐</b>
.
<b>THIS BOT IS OPEN SOURCE. YOU CAN USE THAT SOURCE TO CREATE YOUR OWN PERSONAL BOT.โจ๐ฅ</b>
----------->
 <a href='https://github.com/EvamariaTG/EvaMaria'><b> โข Base Repository </b></a>
<a href='https://github.com/KoshikKumar17/My-EditeD-EvA'><b> โข Repository On Which Bot Runs </b></a>"""

    MANUELFILTER_TXT = """Category: <b>FILTERS: Manual Filter ๐ค</b>
..
Function: <b>Filter is the feature where users can set automated replies for a particular keyword ๐ and This Bot will respond whenever a keyword is found the message.โ๏ธ๐
.
It supports both Alert and URL Buttons.</b>
...
<b>How it Works ๐?</b>
.
<b>NOTE:</b>
1. Bot must be added in the Group with <b>All Admin Rights.</b>
2. ONLY Admins can add FILTERS in a chat.
3. Alert buttons have a MAX limit of 64 characters.
.
<b>Commands and Usage:</b>
โข /filter - <code>Add a filter in a chat.</code>
โโโ
Like:- /filter [keyword] [reply]
e.g:- <code>/filter hi Hi</code> will reply to every msg which contains <b>hi</b> with <b>Hi</b>...๐ฅ
<b><i><u>It must be parsed as MarkDown</u></i></b>
โโโ
โข /filters - <code>List all the filters of a chat.</code>
โข /del - <code>Delete a specific filter in chat</code> e.g:- <code>/del [keyword]</code>
โข /delall - <code>Delete all the filters in a chat (Chat owner only)</code>
"""

    BUTTON_TXT = """Category: <b>Buttons Help </b>
..
Function: <b>It will help you to parse down buttons and Text in MarkDown format.. โจ๐ค</b>
<b>How it Works ๐?</b>
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
Function: <b> In this function, Bot saves all the files in a channel to its DB and whenever a person sends any message in group, Bot will automatically detect the keywords and REPLYs with a message which contains buttons of those files.  โจ๐</b>
..
<b>How it Works ๐?</b>
.
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.
โโโ
<b>โ?๏ธI DON'T USE THIS FEATURE FOR MY BOT BECAUSE I DON'T HAVE ANY FILES TO SAVE IN IT'S DB.๐ IF I HAVE THEY ARE COPYRIGHTED. โ?๏ธ<b>
........
<i><u>This is the Best feature of this Repository. But I don't use. If you want to use this make your Own Bot with  <a href='https://github.com/EvamariaTG/EvaMaria'><b> This Repository </b></a></u></i>
โโโ"""

    CONNECTION_TXT = """Category: <b>Connections </b>
..
Function: <b>It is used to connect Bot to PM for managing filters. It helps to avoid spamming in groups.โจ๐</b>
..
<b>How it Works ๐?</b>
.....
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM.

<b>Commands and Usage:</b>
โข /connect  - <code>Connect a particular chat to your PM.</code>
โข /disconnect  - <code>Disconnect from a chat.</code>
โข /connections - <code>List all your connections.</code>"""

    EXTRAMOD_TXT = """Category: <b>Extra Modules </b>
..
Function: <b>These are the Extra features of this Bot. These features are not added by Me . These features are inherited from <a href='https://github.com/EvamariaTG/EvaMaria'><b> โข Base Repository </b></a> โจ๐</b>
..
<b>How it Works ๐?</b>
<b>NOTE:</b>
These are the Extra features of this Bot from <a href='https://github.com/EvamariaTG/EvaMaria'><b> โข Base Repository </b></a>
...
<b>Commands and Usage:</b>
โข /id - <code>Get id of a specified user.</code> /id [id/username/reply]
โข /info  - <code>Get information about a user.</code> OR /info [id/username/reply]
โข /imdb  - <code>get the film information from IMDb source.</code> /imdb pushpa
โข /search  - <code>get the film information from various sources.</code> /search pushpa"""

    ADMIN_TXT = """Category: <b>ADMIN Modules </b>
..
Function: <b>These are the COMMANDS only for ADMINS. Those whom I have added as Bot's ADMINS in heroku vars. โจ๐</b>
..
<b>How it Works ๐?</b>
..
<b>Commands and Usage:</b>
โข /logs - <code>To get the rescent errors</code>
โข /stats - <code>To get status of files in db.</code>
โข /delete - <code>To delete a specific file from db.</code>
โข /users - <code>To get list of my users and ids.</code>
โข /chats - <code>To get list of the my chats and ids </code>
โข /leave  - <code>To leave from a chat.</code>
โข /disable  -  <code>To disable a chat.</code>
โข /ban  - <code>To ban a user.</code>
โข /unban  - <code>Tk unban a user.</code>
โข /channel - <code>To get list of total connected channels</code>
โข /broadcast - <code>To broadcast a message to all users.</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ Total Users: <code>{}</code>
โ Total Chats: <code>{}</code>
โ Used Storage: <code>{}</code> ๐ผ๐๐ฑ
โ Free Storage: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    REPORTME = """Category: <b>Reporting ๐</b>
..
Function: <b>By using this command. You can contact me. Report anything of Any Type about this bot or else. ๐</b>

<b>How it Works ๐?</b>
>> Send me the message you want to report.
>> Reply that message with /report .
..
Done โ.. I will forward that message to my Owner."""

    ATTACHLINK_TXT = """Category: <b>Attach Link</b>
..
Function: <b>Attach the link with text or media.๐</b>

<b>How it Works ๐?</b>
>> Send me a <b>media or a text.</b>
>> Reply that <b>media or text</b> with a <b>link</b>
>> <b>Done โ : You will get your message with attached link.</b>
"""

    IMG2PDF_TXT = """Category: <b>Image to PDF</b>
..
Function: <b>Convert any type of image(s) to PDF, .pdf file format.๐โจ</b>

<b>How it Works ๐?</b>
>> Send an <b>Image.๐ผ๏ธ</b>. {Not as Document}
>> NOW, You have 3 options.
1๏ธโฃ.  If you want to <b>add</b> more image, Send me <b>images One by One</b>. When done send <b>/c2pdf</b>
2๏ธโฃ.  If <b>done</b> click here  or send  <b>/c2pdf</b>
3๏ธโฃ. If you want to <b>cancel or clear</b> this <b>list or queue or process</b>. Send <b>/clearpdfcache</b>
...
<i>Done โ. YOU WILL GET YOUR REPLY ON THE BASIS OF COMMAND YOU SEND <b>( /C2PDF OR /CLEARPDFCACHE)</b> ๐</i>
"""

    BOTSTSHK_TXT = """Category: <b>Bot Status (Heroku)</b>
..
Function: <b>Get This Bot's Heroku dyno status and it's uptime. ๐โจ</b>

<b>How it Works ๐?</b>
>> SEND <b> /botstatus </b>
>> You will get Dyno usage as a reply to your message.๐

Done โ.."""

    GTRANS_TXT = """Category: <b>Google Translator or GTRANS.</b>
..
Function: <b>TRANSLATE from one language other.๐โจ</b>
<i>Language should be supported by Google.</i>

<b>How it Works ๐?</b>
>> Send me the <b>text</b> you want to <b>Translate</b>.
>> REPLY that text with /tr [language code]
Language code:- <a href="https://cloud.google.com/translate/docs/languages"> <b>Click here</b> </a>
>> Done โ.. You will get the translated text.
โจ
Example: If you want to Translate that text to hindi. Then Reply that text with <code>/tr hi</code>
"""

    TTS_TXT = """Category: <b>Text to Speech</b>
..
Function: <b>Convert any type of text to speech  (Voice๐ฃ๏ธ).. #ByGoogle</b>

<b>How it Works ๐?</b>
>> Send me any type of <b>text</b> ๐.
>> <b>REPLY that text</b> with command <b>/tts</b>

<i>Done โ..... You will get your replied text as speech in an Audio File.๐โจ</i>"""

    TGRAPH_TXT = """Category: <b>Telegraph Uploader</b>
..
Function: <b>Upload any type of Media ๐ผ๏ธ to Telegraph ( telegra.ph ) ๐ค๐ฅ</b>

<b>How it Works ๐?</b>
>> Send me any type of <b>Media ( upto max 5MB) ๐ผ๏ธ</b>.
>> <b>REPLY that media</b> with command <b>/telegraph</b>.
>> Wait a bit till it uploads your media to telegra.ph

<i>Done โ..... You will get a telegra.ph link for your media.๐โจ</i>"""

    SONGDL_TXT = """Category: <b>Song Downloader</b>
..
Function: <b>Download any Song from YouTube in .mp3 or .mp4 format.๐ฅ</b>

</u></i>โผ๏ธTHIS FEATURE IS ONLY TO DOWNLOAD SONGS FROM YOUTUBE. NOT OTHER TYPE OF VIDEOS OTHERWISE,  YOU WILL GET WRONG VIDEOS โผ๏ธ</i></u>

<b>How it Works ๐?</b>
>>First choose an option from below Buttons...๐
As MP3(Audio) or As MP4(Video)"""

    YTTHUMB_TXT = """Category: <b>YouTube Thumbnail Downloader</b>
..
Function: <b>Download the Thumbnail of YouTube videos in HD Quality. ( YouTube #Shorts not supported) โจ๐ฅ</b>

<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /ytthumb </b> [youtube link]
e.g. -ยป <code> /ytthumb https://youtu.be/VYslt8bc-4Q </code>
.
Done โ... You will get your thumbnail as an image....๐ผ๏ธ"""

    YTTAGS_TXT = """Category: <b>YouTube Tags Finder</b>
..
Function: <b>Find/Search the Tags of YouTube videos in an easy way. ( YouTube #Shorts supported) ๐๐ฅ</b>

<u>โผ๏ธ This feature is for Youtubers. Because they have work of the tags. Others can ignore this.โผ๏ธ</u>

<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /yttags </b> [youtube link]
e.g. -ยป <code> /yttags https://youtu.be/VYslt8bc-4Q </code>
.
Done โ... You will get the tags of the video as a text....๐"""

    GITHUB_TXT = """Category: <b>GitHub Profile Details using api.github.com/users</b>
..
Function: <b>Get anyone's github profile details (Along with their D.P.) ๐โจ</b>

<u>Make sure to enter correct username ๐</u>

<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /github </b> [github username]
e.g. -ยป <code> /github hkrrish </code>
.
Done โ... You will get all details of that GitHub User along with their D.P."""

    QUOTES_TXT = """Category: <b>Quotes ๐</b>
..
Function: <b>Get a Quote of Specified Category/Tags each time.... ๐โจ</b>

<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /quote </b> [quote category]
e.g. -ยป <code> /quote love </code> will give you a Quote of the category (Love โค๏ธ).
.
Done โ... You will get the Quote along with category."""

    INSPIRE_TXT = """Category: <b>Inspire Me ๐</b>
..
Function: <b>Get yourself Inspired with a quote and an image... ๐ผ๏ธโจ</b>

<b>How it Works ๐?</b>
>> Send the command <b>/inspire</b>
.
Done โ.... You will get an image.๐"""

    PDFTOOLS_TXT = """Category: <b>PDF Tools</b>
..
Function: <b>Access different types of PDF functions OR help related to PDFs.๐ฅโจ</b>

<b>How it Works ๐?</b>
>> Send /pdfinfo with a Reply to PDF file to get it's information.
>> More coming soon...."""

    JOKES_TXT = """Category: <b>Joke ๐</b>
..
Function: <b>Get a Random Joke each time. ๐๐ฅโจ</b>

<b>How it Works ๐?</b>
>> Send the command <b>/joke</b> to get a joke.

."""

    SHORTLINK_TXT = """Category: <b>Link Shortener</b>
..
Function: <b>Shorten long/real links in a small link without any Wastage of Time.. ๐ค?๐ฅ</b>

</i>Currently Supported:- clck.ru , da.gd , is gd , osdb.link , ttm.sh <b>[ All are AD-FREE ]</b></i>
<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /short </b> [your long/real link]
e.g. -ยป <code> /short https://youtu.be/VYslt8bc-4Q </code>
.
Done โ... You will get your shortened  link.. ๐ That's it!"""

    UNSHORTLINK_TXT = """Category: <b>Link UnShortener</b>
..
Function: <b>UnShorten shortened links to real / long link without any Wastage of Time.. ๐๐ฅ</b>

<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /unshort </b> [your long link]
e.g. -ยป <code> /unshort https://bit.ly/BGMI_AppStore </code>
.
Done โ... You will get your real / long  link.. ๐ That's it!"""

    SONGDLMP4_TXT = """ HEHE ๐ 
<b>You have chooses as MP4(As Video)๐ฅ</b> .... Now follow the below process:
<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /video </b> [youtube song name]
e.g. -ยป <code> /video tu jaane na </code>
Will give you a song named <b> Tu Jaane Na </b> in .mp4 format with Best Quality. ๐ฅ

๐ Extra:- You can use /video or /mp4 as command.
Done โ... You will get your Song as video ๐ค?."""

    SONGDLMP3_TXT = """HEHE ๐ 
<b>You have chooses as MP3 (As Audio)๐ต</b> .... Now follow the below process:
<b>How it Works ๐?</b>
>> Send me a message in the below format:-
<b> /song </b> [youtube song name]
e.g. -ยป <code> /song tu jaane na </code>
Will give you a song named <b> Tu Jaane Na </b> as .mp3 or .m4a format with Best Quality. ๐ฅ

๐ Extra:- You can use /song or /mp3 as command.
Done โ... You will get your Song as audio ๐ค?."""

    SHTXT_TXT = """Category: <b>Share Text</b>
..
Function: <b>Get shareable link of any type of text. In the format <code>https://t.me/share/url?url=</code> ๐๐ฅ</b>

<b>How it Works ๐?</b>
>> Send me the text For which you want to generate shareable link. <b>Only texts and captions of Media are Supported..</b>
>> Reply that msg with /share or /shtxt .
....
Done โ... You will get your link.๐ค?"""
