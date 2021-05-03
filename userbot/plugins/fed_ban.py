# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}superfban <reply to user/userid/username>`
    FBan the person across all feds in which you are admin.

• `{i}superunfban <reply to user/userid/username>`
    Un-FBan the person across all feds in which you are admin.

Specify FBan Group and Feds to exclude in the assistant.

• `{i}fstat <username/id/reply to user>`
    Collect fed stat of the person in Rose.

• `{i}fedinfo <(fedid)>`
    Collect federation info of the given fed id, or of the fed you own, from Rose.
"""

import asyncio
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *

bot = "@MissRose_bot"


@Arcane_cmd(pattern="superfban ?(.*)")
async def _(event):
    msg = await eor(event, "Starting a Mass-FedBan...")
    fedList = []
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await arcane_bot.download_media(
                previous_message,
                "fedlist",
            )
            file = open(downloaded_file_name, encoding="utf8")
            lines = file.readlines()
            for line in lines:
                try:
                    fedList.append(line[:36])
                except BaseException:
                    pass
            arg = event.text.split(" ", maxsplit=2)
            if len(arg) > 2:
                FBAN = arg[1]
                REASON = arg[2]
            else:
                FBAN = arg[1]
                REASON = " #TBMassBanned "
        else:
            FBAN = previous_message.sender_id
            try:
                REASON = event.text.split(" ", maxsplit=1)[1]
            except BaseException:
                REASON = ""
            if REASON.strip() == "":
                REASON = " #TBMassBanned "
    else:
        arg = event.text.split(" ", maxsplit=2)
        if len(arg) > 2:
            try:
                FBAN = arg[1]
                REASON = arg[2]
            except BaseException:
                return await msg.edit("`No user designated!`")
        else:
            try:
                FBAN = arg[1]
                REASON = " #TBMassBanned "
            except BaseException:
                return await msg.edit("`No user designated!`")
    try:
        if str(FBAN) in DEVLIST:
            await msg.edit("You can't ban my dev you noob!!")
            return
        elif FBAN.startswith("@"):
            try:
                x = await arcane_bot(GetFullUserRequest(FBAN))
                uid = x.user.id
                if str(uid) in DEVLIST:
                    await msg.edit("You can't ban my dev you noob!!")
                    return
            except Exception as e:
                print(str(e))
                return await msg.edit(str(e))
    except Exception as e:
        print(str(e))
        return await msg.edit(str(e))
    if udB.get("FBAN_GROUP_ID"):
        chat = int(udB.get("FBAN_GROUP_ID"))
    else:
        chat = await event.get_chat()
    if not len(fedList):
        for a in range(3):
            async with ultroid_bot.conversation("@MissRose_bot") as bot_conv:
                await bot_conv.send_message("/start")
                await asyncio.sleep(3)
                await bot_conv.send_message("/myfeds")
                await asyncio.sleep(3)
                try:
                    response = await bot_conv.get_response()
                except asyncio.exceptions.TimeoutError:
                    return await msg.edit(
                        "`Seems like rose isn't responding, or, the plugin is misbehaving`",
                    )
                await asyncio.sleep(3)
                if "make a file" in response.text or "Looks like" in response.text:
                    await response.click(0)
                    await asyncio.sleep(3)
                    fedfile = await bot_conv.get_response()
                    await asyncio.sleep(3)
                    if fedfile.media:
                        downloaded_file_name = await arcane_bot.download_media(
                            fedfile,
                            "fedlist",
                        )
                        await asyncio.sleep(6)
                        file = open(downloaded_file_name, errors="ignore")
                        lines = file.readlines()
                        for line in lines:
                            try:
                                fedList.append(line[:36])
                            except BaseException:
                                pass
                    elif "You can only use fed commands once every 5 minutes" in (
                        await bot_conv.get_edit
                    ):
                        await msg.edit("Try again after 5 mins.")
                        return
                if len(fedList) == 0:
                    await msg.edit(
                        f"Unable to collect FedAdminList. Retrying ({a+1}/3)...",
                    )
                else:
                    break
        else:
            await msg.edit("Error")
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True
            elif In:
                tempFedId += x
        if len(fedList) == 0:
            await msg.edit("Unable to collect FedAdminList.")
            return
    await msg.edit(f"FBaning in {len(fedList)} feds.")
    try:
        await arcane_bot.send_message(chat, f"/start")
    except BaseException:
        await msg.edit("Specified FBan Group ID is incorrect.")
        return
    await asyncio.sleep(3)
    if udB.get("EXCLUDE_FED"):
        excludeFed = udB.get("EXCLUDE_FED").split(" ")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if udB.get("EXCLUDE_FED") and fed in excludeFed:
            await arcane_bot.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await arcane_bot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await arcane_bot.send_message(chat, f"/fban {FBAN} {REASON}")
        await asyncio.sleep(3)
    try:
        os.remove("fedlist")
    except Exception as e:
        print(f"Error in removing FedAdmin file.\n{str(e)}")
    await msg.edit(
        f"SuperFBan Completed.\nTotal Feds - {len(fedlist)}.\nExcluded - {exCount}.\n Affected {len(fedList) - exCount} feds.\n#TB",
    )


@admin_cmd(pattern="superunfban ?(.*)")
async def _(event):
    msg = await eor(event, "Starting a Mass-UnFedBan...")
    fedList = []
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await arcane_bot.download_media(
                previous_message,
                "fedlist",
            )
            file = open(downloaded_file_name, encoding="utf8")
            lines = file.readlines()
            for line in lines:
                try:
                    fedList.append(line[:36])
                except BaseException:
                    pass
            arg = event.text.split(" ", maxsplit=2)
            if len(arg) > 2:
                FBAN = arg[1]
                REASON = arg[2]  # rose unbans now can have reasons
            else:
                FBAN = arg[1]
                REASON = ""
        else:
            FBAN = previous_message.sender_id
            try:
                REASON = event.text.split(" ", maxsplit=1)[1]
            except BaseException:
                REASON = ""
            if REASON.strip() == "":
                REASON = ""
    else:
        arg = event.text.split(" ", maxsplit=2)
        if len(arg) > 2:
            try:
                FBAN = arg[1]
                REASON = arg[2]
            except BaseException:
                return await msg.edit("`No user designated!`")
        else:
            try:
                FBAN = arg[1]
                REASON = " #TBMassUnBanned "
            except BaseException:
                return await msg.edit("`No user designated!`")
    try:
        if str(FBAN) in DEVLIST:
            await msg.edit("You can't ban my dev you noob!!")
            return
    except Exception as e:
        print(str(e))
        return await msg.edit(str(e))
    if udB.get("FBAN_GROUP_ID"):
        chat = int(udB.get("FBAN_GROUP_ID"))
    else:
        chat = await event.get_chat()
    if not len(fedList):
        for a in range(3):
            async with arcane_bot.conversation("@MissRose_bot") as bot_conv:
                await bot_conv.send_message("/start")
                await asyncio.sleep(3)
                await bot_conv.send_message("/myfeds")
                await asyncio.sleep(3)
                try:
                    response = await bot_conv.get_response()
                except asyncio.exceptions.TimeoutError:
                    return await msg.edit(
                        "`Seems like rose isn't responding, or, the plugin is misbehaving`",
                    )
                await asyncio.sleep(3)
                if "make a file" in response.text or "Looks like" in response.text:
                    await response.click(0)
                    await asyncio.sleep(3)
                    fedfile = await bot_conv.get_response()
                    await asyncio.sleep(3)
                    if fedfile.media:
                        downloaded_file_name = await arcane_bot.download_media(
                            fedfile,
                            "fedlist",
                        )
                        await asyncio.sleep(6)
                        file = open(downloaded_file_name, errors="ignore")
                        lines = file.readlines()
                        for line in lines:
                            try:
                                fedList.append(line[:36])
                            except BaseException:
                                pass
                    elif "You can only use fed commands once every 5 minutes" in (
                        await bot_conv.get_edit
                    ):
                        await msg.edit("Try again after 5 mins.")
                        return
                if len(fedList) == 0:
                    await msg.edit(
                        f"Unable to collect FedAdminList. Retrying ({a+1}/3)...",
                    )
                else:
                    break
        else:
            await msg.edit("Error")
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True
            elif In:
                tempFedId += x
        if len(fedList) == 0:
            await msg.edit("Unable to collect FedAdminList.")
            return
    await msg.edit(f"UnFBaning in {len(fedList)} feds.")
    try:
        await arcane_bot.send_message(chat, f"/start")
    except BaseException:
        await msg.edit("Specified FBan Group ID is incorrect.")
        return
    await asyncio.sleep(3)
    if udB.get("EXCLUDE_FED"):
        excludeFed = udB.get("EXCLUDE_FED").split(" ")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if udB.get("EXCLUDE_FED") and fed in excludeFed:
            await arcane_bot.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await arcane_bot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await arcane_bot.send_message(chat, f"/unfban {FBAN} {REASON}")
        await asyncio.sleep(3)
    try:
        os.remove("fedlist")
    except Exception as e:
        print(f"Error in removing FedAdmin file.\n{str(e)}")
    await msg.edit(
        f"SuperUnFBan Completed.\nTotal Feds - {len(fedlist)}.\nExcluded - {exCount}.\n Affected {len(fedList) - exCount} feds.\n#TB",
    )


@admin_cmd(pattern="fstat ?(.*)")
async def _(event):
    ok = await eor(event, "`Checking...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
        if event.pattern_match.group(1):
            sysarg += f" {event.pattern_match.group(1)}"
    else:
        sysarg = event.pattern_match.group(1)
        user = sysarg
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her fedstat.`",
        )
        return
    else:
        async with arcane.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                audio = await conv.get_response()
                if audio.message.startswith("This command can only be used once"):
                    return await ok.edit(
                        "Oops, you can use this command only once every minute!",
                    )
                elif "Looks like" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await arcane.send_file(
                        event.chat_id,
                        audio,
                        caption=f"List of feds {user} has been banned in.\n\nCollected using Arcane.",
                        link_preview=False,
                    )
                    await ok.delete()
                else:
                    okk = await conv.get_edit()
                    await ok.edit(okk.message)
                await arcane.send_read_acknowledge(bot)
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@admin_cmd(pattern="fedinfo ?(.*)")
async def _(event):
    ok = await event.edit("`Extracting information...`")
    sysarg = event.pattern_match.group(1)
    async with arcane.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + sysarg)
            audio = await conv.get_response()
            await arcane.send_read_acknowledge(bot)
            await ok.edit(audio.text + "\n\nFedInfo Extracted by Arcane")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
