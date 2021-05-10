
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import CMD_HELP



@bot.on(admin_cmd("circle ?(.*)"))
@bot.on(sudo_cmd(pattern="circle ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "Reply to any user message")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "Reply to media message")
        return
    chat = "@TelescopyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "Reply to actual users message.")
        return
    legendx22 = await edit_or_reply(event, "Trying to convert...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=397367589)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await legendx22.edit("```Please unblock @TelescopyBot and try again```")
            return
        if response.text.startswith("Forward"):
            await legendx22.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await legendx22.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
            )
            await event.client.send_read_acknowledge(conv.chat_id)

