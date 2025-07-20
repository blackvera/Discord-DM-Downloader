# Discord DM Downloader

> **Warning:** This code has been obfuscated for privacy and protection purposes, but it is fully functional.

A simple Python script to download messages from your own private Discord chat (DM) and save them as text files.

## Features
- Download all messages from a private Discord DM
- Save messages in .txt files, split into blocks of 100
- The token is never saved in the code: you enter it only at startup

## Requirements
- Python 3.8 or higher
- Libraries: `colorama` and `requests`

## Installation
1. **Download or clone this repository**
2. **Open the project folder**
3. **Run `start.bat`** (it will automatically install the required libraries and start the program)

Or, if you want to install the dependencies manually:
```sh
pip install colorama requests
```

## Usage
1. Start the program with `start.bat` (Windows) or `python main.py` (other systems)
2. Enter your Discord token when prompted (see below for how to get it)
3. Enter the DM channel ID you want to download messages from
4. Enter the folder name where you want to save the files
5. The messages will be saved as text files inside the chosen folder
6. At the end, you can choose to perform another download or close the program

## How to get your Discord token
**Warning: your token is sensitive! Do not share it with anyone.**
1. Open Discord in your browser
2. Press F12 to open the developer tools
3. Go to "Application" > "Local Storage" > `https://discord.com`
4. In the search bar, type "token" and copy the value

## How to get the DM channel ID
1. Enable developer mode in Discord (Settings > Advanced > Developer Mode)
2. Right-click on the private chat and select "Copy ID"

## Security notes
- The Discord token gives full access to your account: DO NOT share it and DO NOT publish it online.
- This script is for personal use only.

## Authors
- Nypher and Vera for Blackout Project
- https://linktr.ee/blackoutproj
