"""

Available Commands:

.sux

.fuk

.kiss"""

from telethon import events

import asyncio

from pikabot.utils import ItzSjDude



@ItzSjDude(outgoing=True, pattern="fuck")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

   # if input_str == "fuk":

    await event.edit("fuk")

    animation_chars = [

            "👉       ✊️",

            "👉     ✊️",

            "👉  ✊️",

            "👉✊️💦"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


@ItzSjDude(outgoing=True, pattern="sux")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

    #if input_str == "sux":

    await event.edit("sux")

    animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵👼👰"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


""


from telethon import events

import asyncio





@ItzSjDude(outgoing=True, pattern="kiss")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

    #if input_str == "kiss":

    await event.edit("kiss")

    animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵💋👰"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])
