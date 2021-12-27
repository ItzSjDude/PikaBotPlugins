"""Figlet Module
{i}figlet <font name>
"""
from . import _figlet


@Infinix(outgoing=True, pattern=r"figlet ?(.*)")
@Infinix(sudo=True, pattern=r"figlet ?(.*)")
async def _(event):
    await _figlet(event)
