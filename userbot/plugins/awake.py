"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
MADE BY @LEGENDX22 dont kang this plugin
CREDITS = @LEGENDX22 @PROBOYX @alain_champion
Special thanks @alain_champion for this modified version
if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, devilversion, StartTime, CMD_HELP
from . import legend
from userbot.legend import BOT
from userbot.utils import admin_cmd, sudo_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Config.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = "https://telegra.ph/file/1a521001683a360053b32.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝙰𝚁𝙲𝙰𝙽𝙴"

global ghanti
        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅           
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake")) 
@borg.on(sudo_cmd(pattern="awake ?(.*)", allow_sudo=True))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   tag = borg.uid
   uptm = await legend.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= f" ⚡️ {BOT} ⚡️  IS ON 🔥 FIRE 🔥"
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "🚨 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 🚨\n\n"
   ALIVE_MESSAGE += "☎️ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ☎️ : 1.19.5\n\n"
   ALIVE_MESSAGE += "✨ 𝙰𝚁𝙲𝙰𝙽𝙴 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ✨ :   2.0\n\n"
   ALIVE_MESSAGE += f"💀 𝚄𝙿𝚃𝙸𝙼𝙴 💀 : {uptm}\n\n"
   ALIVE_MESSAGE += f"🔥 𝙼𝚈 𝙱𝙾𝚂𝚂 🔥: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
   ALIVE_MESSAGE += "⚓ 𝙶𝚁𝙾𝚄𝙿 ⚓ : [SUPPORT](https://t.me/Arcane_Bot_Support)\n\n"
   ALIVE_MESSAGE += f"😍 [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FArcane120%2Heroku-Setup&template=https%3A%2F%2Fgithub.com%2FArcane120%2FHeroku-Setup) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](https://github.com/Arcane120/ARCANE-USERBOT)  💠\n"   
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "Plugin : arcane\
    \n\nSyntax : .arcane\
    \nFunction : Do this to check me working or not.
    }
)
