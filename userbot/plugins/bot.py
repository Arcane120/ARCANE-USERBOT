# make by @LEGENDX22
# inline alive
# modify by proboy22
import asyncio
import os
from userbot.legend import BOT
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid
from userbot.utils import admin_cmd
from PIL import Image
import requests
from io import BytesIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝙰𝚁𝙲𝙰𝙽𝙴"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

pro_text=(f"✨**{BOT} 𝙸𝚂 𝚄𝙿 𝙰𝙽𝙳 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝚂𝙴𝚁𝚅𝙴 𝚈𝙾𝚄✨ **\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n⚓ About My System ⚓\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/Arcane_Bot_Support)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ARCANE BOT](https://github.com/Arcane120/ARCANE-USERBOT/License)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [ARCANE BOT](https://github.com/Arcane120/ARCANE-USERBOT)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        if query.startswith("arcane") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("✨𝚁𝙴𝙿𝙾✨", "https://github.com/Arcane120/ARCANE-USERBOT"),
                    Button.url("⚓𝙳𝙴𝙿𝙻𝙾𝚈⚓", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FArcane120%2Heroku-Setup&template=https%3A%2F%2Fgithub.com%2FArcane120%2FHeroku-Setup")],
                    [Button.url("🚨𝚂𝚃𝚁𝙸𝙽𝙶🚨", "https://replit.com/@Arcane120/ArcaneBot#main.py"),
                    Button.url("⚡𝙶𝚁𝙾𝚄𝙿⚡", "https://t.me/Arcane_Bot_Support"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="ARCANE BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="ARCANE BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@borg.on(admin_cmd(pattern=r"arcane"))
async def hehe(event):
    alive = requests.get("N/A")
    alive.raise_for_status()
    LEGENDX = BytesIO(alive.content)
    LEGENDX.seek(0)
    img = Image.open(LEGENDX)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(event.chat_id, file=sticker)

from userbot import bot


@bot.on(admin_cmd(outgoing=True, pattern="arcane"))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
