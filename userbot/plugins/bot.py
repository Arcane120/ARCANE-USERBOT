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
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝙳𝙴𝚅𝙸𝙻"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

pro_text=(f"**{BOT} IS ON FIRE **\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n🔥 About My System 🔥\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/deviluserbot)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [DEVIL BOT](https://github.com/lucifeermorningstar/Devil/License)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [DEVIL BOT](https://github.com/lucifeermorningstar/Devil)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/lucifeermorningstar/Devil"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/lucifeermorningstar/Devil/blob/master")],
                    [Button.url("String", "https://repl.it/@lucifeermorning/DevilBot#main.py"),
                    Button.url("Channel", "https://t.me/deviluserbot"),
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
                    title="DEVIL BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="DEVIL BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@borg.on(admin_cmd(pattern=r"alive"))
async def hehe(event):
    alive = requests.get("https://telegra.ph/file/8c98504c33973b8071bd3.jpg")
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


@bot.on(admin_cmd(outgoing=True, pattern="alive"))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
