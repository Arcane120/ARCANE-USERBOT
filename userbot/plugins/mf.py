import sys
import time
import os
"""Available Commands:
.mf"""

from telethon import events, functions, __version__

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,27)
    input_str = event.pattern_match.group(1)
    if input_str == "mf":
        await event.edit(input_str)
        animation_chars = [
            "\n......................................../´¯/)\n......................................,/¯../ \n...................................../..../ \n..................................../´.¯/\n..................................../´¯/\n..................................,/¯../ \n................................../..../ \n................................./´¯./\n................................/´¯./\n..............................,/¯../\n............................./..../ \n............................/´¯/\n........................../´¯./\n........................,/¯../ \n......................./..../ \n....................../´¯/\n....................,/¯../ \n.................../..../ \n............./´¯/'...'/´¯¯`·¸ \n........../'/.../..../......./¨¯\ \n........('(...´...´.... ¯~/'...') \n.........\.................'...../ \n..........''...\.......... _.·´ \n............\..............( \n..............\.............\..."
        ]

        for i in animation_ttl:
          
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %27 ])

@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @LEGEND_USERBOT_SUPPORT""")
