# FIX BY TEAM DYNAMIC AMAN PANDEY      .
from telethon.tl.functions.messages import SaveDraftRequest

from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="chain$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Counting...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await event.client(
                SaveDraftRequest(
                    await event.get_input_chat(), "", reply_to_msg_id=message.id
                )
            )
        message = reply
        count += 1
    await event.edit(f"Chain length: {count}")


CMD_HELP.update(
    {
        "chain": """**Plugin :**`chain`
        
  • **Syntax : **`.chain reply to message`
  • **Function : **__Reply this command to any converstion(or message) so that it finds chain length of that message__"""
    }
)
