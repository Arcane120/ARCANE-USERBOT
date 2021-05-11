# COPYRIGHT TEAM DYNAMIC 2021 - 2022 
# KANG WITH CREDITS OTHERWISE YOU WILL BE FUCKED ANYTIME ANYWHERE
import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot import bot as GODBOYX
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("GODBOYX", API_ID, API_HASH).start(bot_token=token)
pbot = Client("GODBOYX", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "ARCANE BOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "ARCANE USER"
PHOTO = os.environ.get("ALIVE_PHOTO", None)
GODBOYX = "[GODBOYX](https://t.me/GODBOYX)"
VERSION = "1.1.0"
ID = 1742906647
REPO = "[Dynamic-Userbot](https://github.com/TeamDynamic/Dynamic-Userbot)"
devs = 1742906647
MASTER = f"[{NAME}](tg://user?id={ID})"
GROUP = "[SUPPORT GROUP](https://t.me/Arcane_Bot_Support)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
  run()
