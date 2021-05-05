
from userbot.utils import admin_cmd
import asyncio
@borg.on(admin_cmd(pattern="hi"))
async def Arcane(event):
  await event.edit("HELLO MY CODE IS RUNNING")
  await asyncio.sleep(5)
  await event.reply("YEAH WORKING")
  await asyncio.sleep(5)
  await bot.send_message(event.chat_id, "HELLO THIS IS ALSO RUNNING")
  await asyncio.sleep(5)
  await bot.send_message("@arminarlert898", "HELLO VRO YOUR CODE IS WORKING")
  await asyncio.sleep(5)
  await bot.send_message(1100231654, "ID TRICK ALSO WORKING")
 
# for ultroid
import asyncio
@ultroid_cmd(pattern="hi")
async def legendx(event):
  await event.edit("HELLO MY CODE IS RUNNING")
  await asyncio.sleep(5)
  await event.reply("YEAH WORKING")
  await asyncio.sleep(5)
  await bot.send_message(event.chat_id, "HELLO THIS IS ALSO RUNNING")
  await asyncio.sleep(5)
  await bot.send_message("@arminarlert898", "HELLO VRO YOUR CODE IS WORKING")
  await asyncio.sleep(5)
  await bot.send_message(1100231654, "ID TRICK ALSO WORKING")
 

# for grand official
import asyncio
from Arcane import telethn as bot 
from Arcane.events import register
@register(pattern="/hi")
async def hehe(event):
# bots cannot use event.edit method
  await asyncio.sleep(5)
  await event.reply("YEAH WORKING")
  await asyncio.sleep(5)
  await bot.send_message(event.chat_id, "HELLO THIS IS ALSO RUNNING")
  await asyncio.sleep(5)
  await bot.send_message("@arminarlert898", "HELLO VRO YOUR CODE IS WORKING")
  await asyncio.sleep(5)
  await bot.send_message(1100231654, "ID TRICK ALSO WORKING")
