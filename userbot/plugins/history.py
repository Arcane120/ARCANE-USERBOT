import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import asyncio

@bot.on(admin_cmd(pattern=("history ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit("```Reply to any user message.```")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit("```reply to text message```")
      return
   chat = "@SangMataInfo_bot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit("```Reply to actual users message.```")
      return
   await event.edit("```Processing```")
   async with borg.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
            await borg.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
         if response.text.startswith("Forward"):
            await event.edit("```This user had disabled their forward privacy... Just tag and type .sg```")
         else: 
            await event.edit(f"{response.message.message}")
CMD_HELP.update(
    {
        "history": "**Plugin : **`history`\
    \n\n**Syntax : **`.history`\
    \n**Function : **this plugin not show full history of user try .sg"
    }
)

