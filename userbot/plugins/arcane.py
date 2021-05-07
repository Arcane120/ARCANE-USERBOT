# FIX BY TEAM DYNAMIC. Aman Pandey
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime, CMD_HELP
#from . import legend
from userbot.legend import BOT
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = "https://telegra.ph/file/f71f9b1cbd6459391d422.mp4"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝙰𝚁𝙲𝙰𝙽𝙴"

global ghanti
        

@borg.on(admin_cmd(pattern=r"arcane")) 
async def amireallyalive(arcane):
   """ For .arcane command, check if the bot is running or not.  """
   tag = borg.uid
   uptm = await legend.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= f" ༒︎ {BOT} ༒︎ 𝑰𝑺 𝑼𝑷 𝑨𝑵𝑫 𝑹𝑬𝑨𝑫𝒀 𝑻𝑶 𝑺𝑬𝑹𝑽𝑬 𝒀𝑶𝑼⚓.  "
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "༆ 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 ༆\n\n"
   ALIVE_MESSAGE += "𖣔 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 𖣔 : 1.19.5\n\n"
   ALIVE_MESSAGE += "★ 𝙰𝚁𝙲𝙰𝙽𝙴 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ★ :   2.0\n\n"
   ALIVE_MESSAGE += f"𖣘 𝚄𝙿𝚃𝙸𝙼𝙴 𖣘 : {uptm}\n\n"
   ALIVE_MESSAGE += f"꧁ 𝙼𝚈 𝙱𝙾𝚂𝚂 ꧂: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
   ALIVE_MESSAGE += "☯︎ 𝙶𝚁𝙾𝚄𝙿 ☯︎ : [SUPPORT](https://t.me/Arcane_Bot_Support)\n\n"
   ALIVE_MESSAGE += f"༄ [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FArcane120%2Heroku-Setup&template=https%3A%2F%2Fgithub.com%2FArcane120%2FHeroku-Setup) ༄ 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 ❄︎[{BOT}](https://github.com/Arcane120/ARCANE-USERBOT)  ❄︎\n"   
   await arcane.delete() 
   await borg.send_file(arcane.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "arcane": "Plugin : arcane\
    \n\nSyntax : .arcane\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
