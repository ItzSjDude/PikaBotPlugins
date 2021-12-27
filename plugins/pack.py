"""Transforms Msg into file
{i}pack <reply to msg filename.extension>

"""
# Made by @Infinix. All Rights reserved

from . import _pack


@Infinix(pattern="pack ?(.*)")
async def _(event):
    await _pack(event)
