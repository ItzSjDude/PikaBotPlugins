""" Plugin for reading nd Exporting as messge on Tg
{i}reveal <reply to file>
"""
# Made By @Infinix. All rights reserved

from . import _reveal


@Infinix(pattern=r"reveal")
async def _(event):
    await _reveal(event)
