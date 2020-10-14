# Vita Icon Downloader

## Intro
Small script written in Python to dump ps vita icons to the PC from Vita's appmeta folder using FTP.

<div style="text-align:center"><img src="https://github.com/Lvieira21/vita-dump-icons/blob/main/Assets/VitaPresenceTest.png?raw=true" /></div>

This script is intended to donwload ps vita installed app icons in order to upload to a discord rich presence app. It finds each icon0 from each appmeta game/app folder, downloads through FTP, saves it to a folder you choose under the gameID name in PNG format, and resizes it to discord app Standards.

<div style="text-align:center"><img src="https://github.com/Lvieira21/vita-dump-icons/blob/main/Assets/discordDevEx.png?raw=true" /></div>

To be used with: [Electry VitaPresence](https://github.com/Electry/VitaPresence) and [MightyV vita-presence-server](https://github.com/TheMightyV/vita-presence-the-server)

## GUI

The GUI was written using [Python Eel](https://github.com/samuelhwilliams/Eel) and currently I'm only capable of building the macOS version of the app, in one day or so I'll be building the Windows version.
<div style="text-align:center"><img src="https://github.com/Lvieira21/vita-dump-icons/blob/main/Assets/screenshot.png?raw=true" /></div>

#### Notice: in order for it to work, you need Google Chrome installed.
#### Notice 2: Windows build in the making



## Building

If, in anycase, you want to compile yourself:
```shell
git clone https://github.com/Lvieira21/vita-dump-icons.git
cd vita-dump-icons
git submodule update --init
python -m eel main.py _view --onefile --noconsole --icon "/Users/lucasvieira/Documents/Programação/PythonWorkspace/VitaIconDump/_view/_icons/psv.icns" -n 'Vita Icon Downloader
```

## Known Bugs

- If you cancel the directory selection prompt, the app hangs;


##### If you find bugs, don't hesitate to contact me.
