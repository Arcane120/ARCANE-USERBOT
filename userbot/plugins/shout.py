"""Shouts a message in MEME way
usage: .shout message
originaly from : @corsicanu_bot
"""

import sys
from telethon import events, functions
from userbot.utils import admin_cmd
import random


@borg.on(admin_cmd(pattern=r"shout"))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(' '.join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + ' ' + '  ' * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await args.edit("`"+msg+"`")
        
    
    
