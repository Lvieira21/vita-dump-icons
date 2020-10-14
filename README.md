# Vita Icon Downloader

## Intro
Small script written in Python to dump ps vita icons to the PC from Vita's appmeta folder using FTP.

<div style="text-align:center"><img src="https://github.com/Lvieira21/vita-dump-icons/blob/main/Assets/VitaPresenceTest.png?raw=true" /></div>

This script is intended to donwload ps vita installed app icons in order to upload to a discord rich presence app. It finds each icon0 from each appmeta game/app folder, downloads through FTP, saves it to a folder you choose under the gameID name in PNG format, and resizes it to discord app Standards.

<div style="text-align:center"><img src="https://github.com/Lvieira21/vita-dump-icons/blob/main/Assets/discordDevEx.png?raw=true" /></div>

To be used with: [Electry VitaPresence](https://github.com/Electry/VitaPresence) and [MightyV vita-presence-server](https://github.com/TheMightyV/vita-presence-the-server)

## GUI

The GUI was written using [Materialize framework](https://materializecss.com/) and [Python Eel](https://github.com/samuelhwilliams/Eel) and currently I'm only capable of building the macOS version of the app, in one day or so I'll be building the Windows version.
<div style="text-align:center"><img src="https://github.com/Lvieira21/vita-dump-icons/blob/main/Assets/screenshot.png?raw=true" /></div>

#### Notice: in order for it to work, you need Google Chrome installed.
#### Notice 2: Windows build in the making



## Building


If in any case, you want to compile yourself, you'll need:

| Lib  | Ver  | Info  | 
|---|---|---|
|  Python | 3.8.X  |   | 
| pip  |  20.1.1 | Package Installer  | 
| pipenv  |  2020.8.13 | To create your virtual env  | 
|  Pillow |  7.2.0 | To resize images  | 
|  Eel |  0.14.0 | Python Lib to make offline GUI  | 
| tk  |  0.1.0 | Python GUI Lib used to access folders  | 

And run the commands bellow:

```shell
git clone https://github.com/Lvieira21/vita-dump-icons.git
cd vita-dump-icons
git submodule update --init
python -m eel main.py _view --onefile --noconsole --icon <ico file for windows and icns file for macOS> -n <app_name>
```

## Known Bugs

- If you cancel the directory selection prompt, the app hangs;


##### If you find bugs, don't hesitate to contact me.
