# COPYRIGHT (C) 2021 BY LEGENDX22
"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
"""
# MADE BY LEGENDX22 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot.utils import admin_cmd as devil
from userbot import bot as DEVILBOT
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
pbot = Client("DEVIL", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "ARCANE BOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "ARCANE BOT"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ARCANE = "[ARCANE](https://t.me/Arcane_Bot_Support)"
VERSION = "3.1.5"
REPO = "[ARCANE BOT](https://github.com/Arcane120/ARCANE-USERBOT)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/Arcane_Bot_Support)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
