# COPYRIGHT © BY LEGENDX22

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))

                 MADE BY LEGENDX22
                 IDEA BY PROBOYX
                 CREDITS TEAMLEGEND
                 PLEASE KEEP CREDITS 🥺
"""



from telethon import events, Button, custom
from LEGENDX import BOT
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = LEGEND.article("LEGEND",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by LEGENDX22 and PROBOYX 🔥
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f"🔥{BOT} REPO🔥", url="https://github.com/LEGENDXOP/LEGEND-BOT"), Button.url(f"⚡{BOT} SUPPORT⚡", url="https://t.me/LEGEND_USERBOT_SUPPORT")]])
