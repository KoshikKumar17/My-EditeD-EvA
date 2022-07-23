<h1 align="center">
  <b><a href="https://KoshikKumar17.github.io/My-EditeD-EvA">KoshikKumar17'S Bot</a></b>
</h1>



➡️ **[~View The Bot~](https://KoshikKumar17.github.io/My-EditeD-EvA)**



[![Stars](https://img.shields.io/github/stars/KoshikKumar17/My-EditeD-EvA?style=flat-square&color=yellow)](https://github.com/KoshikKumar17/My-EditeD-EvA/stargazers)
[![Forks](https://img.shields.io/github/forks/KoshikKumar17/My-EditeD-EvA?style=flat-square&color=orange)](https://github.com/KoshikKumar17/My-EditeD-EvA/fork)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/KoshikKumar17/My-EditeD-EvA)   
[![Contributors](https://img.shields.io/github/contributors/KoshikKumar17/My-EditeD-EvA?style=flat-square&color=green)](https://github.com/KoshikKumar17/My-EditeD-EvA)
[![License](https://img.shields.io/badge/License-GPL-blue)](https://github.com/KoshikKumar17/My-EditeD-EvA/blob/main/LICENSE)

## First Thanks and Credits
As you know this is an **imported repo** from **EvaMaria.** So First Let me **thank** those **developers** who made the beautiful and awesome **base Repo** Evamaria. Also those from where **I learnt some coding**.
That's All. 

**--NO CREDITS TO ME--**

- [![EvaMaria-Devs](https://img.shields.io/static/v1?label=EvaMaria&message=devs&color=critical)](https://telegram.dog/EvaMariaDevs)
 - Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks to [SpEcHiDe](https://t.me/SpEcHlDe) for Inspiration
 - Thanks Trojanz for Heroku dyno status inspiration.
 - Thanks to Sirius and Pradeep.
 - Thanks to [PyPI](https://PyPI.org) for stuffs.
 - Thanks To Everyone In This Journey


## Features

![Features](https://telegra.ph/file/1f16236a1f9e3801abd91.jpg)

- [x] Attach links
- [x] SONGS download
- [x] Jokes
- [x] Heroku Dyno check
- [x] Translate
- [x] Text to Speech
- [x] Thoughts
- [x] YT Thumbnail Downloader
- [x] YT Tag Finder
- [x] Img to Pdf
- [x] Telegraph
- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] Reporting Admin
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] Telegram IDs and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store

## Variables


### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images or images links to show in start message. (Multiple images can be used separated by space.)
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made. (Separate multiple IDs by space.)
* `P_TTI_SHOW_OFF`: **(Use True or False)** - Users will be redirected to send /start to Bot PM  if set to True else files will be sent  directly to user's PM.
* `IMDB`: **(Use True or False)** - To disable or enable imdb data
* `SINGLE_BUTTON`: **(Use True or False)** - If set True, file name and files size will be shown in a single button instead of two separate button.
* `CUSTOM_FILE_CAPTION`: Same as IMDB template , you can **customize** the caption for files. (Available keys , **file_name, file_size, file_caption**)
 Specimen: 
```
<b>Join [Here](https://t.me/KoshikKumar17)</b> 

FILE : <code>{file_name}</code> 
Size : <i>{file_size}</i>
CAPTION: {file_caption}
```
* `LONG_IMDB_DESCRIPTION`: **(Use True or False)**  Long IMDB story line will be used if enabled.
* `SPELL_CHECK_REPLY`: **(Use True or False)** - if enabled, bot will be suggesting related movies if keyword not found in database.
* `AUTH_CHANNEL`: To enable force subscribe. Delete this var if you do not need force subscribe.
* `UPSTREAM_REPO`: If you want to use a customized fork of [My-EditeD-EvA](https://github.com/KoshikKumar17/My-EditeD-EvA), You can fill this config with github url of your fork.
* `BATCH_FILE_CAPTION`: Same as `CUSTOM_FILE_CAPTION` , use in case you want separate captions for batch files.
* `PROTECT_CONTENT`: **Use True / False** . If set to true files from bot cannot be forwarded to any chat.
* `PUBLIC_FILE_STORE`: Use **False** if you don't want your bot to be used as a filestore bot by others.
* `IMDB_TEMPLATE`: To customise IMDb Data. See code from **[Here](https://github.com/KoshikKumar17/My-EditeD-EvA/blob/V2.0/plugins/pm_filter.py#L1002) to [Here](https://github.com/KoshikKumar17/My-EditeD-EvA/blob/V2.0/plugins/pm_filter.py#L1029)** To know about available keys and Follow below example.
```
Hey {message.from_user.mention},

Here is the result for your {query}.

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : <code>{languages}</code>
👥 Cast : <code>{cast}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>

Co Powered By {message.chat.title}
...❤️...
```
* `HEROKU_API_KEY`: If you want to check your heroku account's dyno status directly from Bot.
* `COMMAND_HAND_LER`: Add a symbol to use ping command. Recommended (**,** or **!** or **.** or **/**)Default `.ping`

* Check [info.py](https://github.com/KoshikKumar17/My-EditeD-EvA/blob/V2.0/plugins/info.py) for more.


## Deploy
You can deploy this bot anywhere.

<i>**[Watch Deploying Tutorial...](https://youtu.be/1G1XwEOnxxo)**</i>

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://telegram.dog/XTZ_HerokuBot?start=S29zaGlrS3VtYXIxNy9NeS1FZGl0ZUQtRXZBIFYyLjA">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

**OR**

<a href="https://heroku.com/deploy?template=https://github.com/KoshikKumar17/My-EditeD-EvA">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/KoshikKumar17/My-EditeD-EvA
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot.
python3 bot.py
</pre>
</p>
</details>


## Commands
**All COMMANDS CAN BE USED FOLLOWING BY A '/'.**
.
Copy below text and send it to [@BotFather](https://telegram.me/botfather) to add these commands in your Bot.
```
start - Check if Up or not.
help - Get help Menu.
about - Know about the bot
botstatus - Get Bot dyno status
report - Give your report about the bot to bot owner.
tr - Reply, Long Press and Lang. Code.
song - Use /song [songname] as mp3
video - Use /video [songname] as mp4
joke - Get a Random Joke
quote - Get a Quote, /quote love
tts - Reply to text to convert to voice
short - /short [yourlink] to shorten link
github - /github [username] to fetch data from GitHub
unshort - /unshort [yourlink] to unshorten link
inspire - To get a inspirational MSG
ytthumb - To DL thumbnail of YT video
india - Get india Art
c2pdf - Get images or set of images as PDF
clearpdfcache - Delete/cancel old queued images
yttags - To find tags of YT video
telegraph - Reply to get telegra.ph link
settings - Settings of Group
link - Get shareable link of file can forward
plink - Get shareable link of file can't forward
batch - Get shareable link of multiple files (With FW)
pbatch - Get shareable link of multiple files (Without FW) 
logs - to get the rescent errors
stats - to get status of files in db.
filter - add manual filters
filters - view filters
connect - connect to PM.
disconnect - disconnect from PM
del - delete a filter
delall - delete all filters
deleteall - delete all index(autofilter)
delete - delete a specific file from index.
info - get user info
id - get tg ids.
imdb - fetch info from imdb.
users - to get list of my users and ids.
chats - to get list of the my chats and ids 
index  - to add files from a channel
leave  - to leave from a chat.
disable  -  do disable a chat.
enable - re-enable chat.
ban  - to ban a user.
unban  - to unban a user.
channel - to get list of total connected channels.
broadcast - to broadcast a message to all Bot users.
```
## Support
[![telegram badge](https://img.shields.io/badge/Telegram-Bot-30302f?style=flat&logo=telegram)](https://telegram.me/MYBOTKK_17BOT)
[![telegram badge](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://telegram.me/KOSHIKKUMAR17)

## Disclaimer
![GPL-2.0 license](./assets/LICENSE.png)

Licensed under [GPL-2.0 License](https://github.com/KoshikKumar17/My-EditeD-EvA/blob/main/LICENSE)
**Selling The Codes To Other People For Money Is Strictly Prohibited.**
