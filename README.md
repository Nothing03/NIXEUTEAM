<h1 align= center><b>NIXEU MUSIC</b></h1>
<h3 align = center> A Telegram Music Bot written in Python using Pyrogram and Py-Tgcalls </h3>

<p align="center"><a href="https://t.me/NIXEU_MUSIC"><img src="https://telegra.ph//file/a71334d90daaad1baf16c.png" width="300"></a></p>

## ✨ <a name="features"></a>Features

### ⚡️ Fast & Light

Starts streaming your inputs while downloading and converting them. Also, it
doesn't make produce files.

### 👮🏻‍♀️ Safe and handy

Restricts control and sensitive commands to admins.

### 🗑 Clean and spam free

Deletes old playing trash to keep your chats clean.

### 😎 Has cool controls

Lets you switch stream mode, loop, pause, resume, mute, unmute anytime.

### 🖼 Has cool thumbnails

Response your commands with cool thumbnails on the chat.

### 😉 Streams whatever you like

You can stream audio or video files, YouTube videos with any duration,
YouTube lives, YouTube playlists and even custom live streams like radios or m3u8 links or files in
the place it is hosted!

### 📊 Streams in multiple places

Allows you to stream different things in multiple chats simultaneously. Each
chat will have its own song queue.

## 🚀 <a name="deploy"></a>Deploy

[![Deploy+On+Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/)
    

Note: `First Fork The Repo Then Click On Deploy To Heroku Button!`


## ☁️ <a name="self_host"></a>Self Host

- Legecy Method
```bash
$ git clone https://github.com/AsmSafone/MusicPlayer
$ cd MusicPlayer
$ sudo apt install git curl python3-pip ffmpeg -y
$ pip3 install -U pip
$ curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
$ sudo apt install -y nodejs
$ sudo apt install build-essential
$ sudo npm install pm2@latest -g
$ pip3 install -U -r requirements.txt
$ cp sample.env .env
# < edit .env with your own values >
$ python3 main.py
```
Or you can use this One-Liner to save your time :

```
git clone https://github.com/AsmSafone/MusicPlayer && cd MusicPlayer && sudo apt install git curl python3-pip ffmpeg -y && pip3 install -U pip && curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - && sudo apt install -y nodejs && sudo apt install build-essential && sudo npm install pm2@latest -g && pip3 install -U -r requirements.txt
```
Make sure to edit the .env file accordingly,
```
cp sample.env .env
```
Run it using,
```
python3 main.py
```

- Docker Build Method
```bash
$ git clone https://github.com/AsmSafone/MusicPlayer
$ cd MusicPlayer
$ cp sample.env .env
# < edit .env with your own values >
$ sudo docker build . -t musicplayer
$ sudo docker run musicplayer
```

## ⚒ <a name="configs"></a>Configs

- `API_ID`: Telegram app id from https://my.telegram.org/apps.
- `API_HASH`: Telegram app hash from https://my.telegram.org/apps.
- `SESSION`: Pyrogram string session. You can generate from [here](https://replit.com/@AsmSafone/genStr).
- `SUDOERS`: ID of sudo users (separate multiple ids with space).
- `BOT_TOKEN`: Telegram bot token from https://t.me/botfather. (optional)
- `QUALITY`: Custom stream quality (high/medium/low) for the userbot in vc. Default: `high`
- `PREFIX`: Bot commad prefixes (separate multiple prefix with space). Eg: `/`
- `STREAM_MODE`: An stream mode like audio or video (can change it anytime). Default: `audio`
- `ADMINS_ONLY`: Put `True` if you want to make /play commands only for admins. Default: `False`
- `SPOTIFY_CLIENT_ID`: Spotify client id get it from [here](https://developer.spotify.com/dashboard/applications). (optional)
- `SPOTIFY_CLIENT_SECRET`: Spotify client secret get it from [here](https://developer.spotify.com/dashboard/applications). (optional)


## 📄 <a name="commands"></a>Commands

Command | Description
:--- | :---
• /ping | Check if alive or not
• /start /help | Show the help for commands
• /mode  | Switch the stream mode (audio/video)
• /play [song name or youtube link] | Play a song in vc, if already playing add to queue
• /stream [radio url or stream link] | Play a live stream in vc, if already playing add to queue
• /playlist [playlist link] | Play the whole youtube playlist at once
• /skip | Skip to the next song
• /mute | Mute the current stream
• /unmute | Unmute the muted stream
• /pause | Pause the current stream
• /resume | Resume the paused stream
• /queue | Show the songs in the queue
• /shuffle | Shuflle the queued playlist
• /repeat | Enable or disable the loop mode
• /import | Import queue from exported file
• /export | Export the queue for import in future
• /stop | Leave from vc and clear the queue
• /restart | restart your music player

## 📃 <a name="license"></a>License

Music Player is licenced under the GNU Affero General Public License v3.0.
Read more [here](./LICENSE).
