""" Get the Bots in any chat*
Syntax: {i}gbot"""

from . import _gbot


@Infinix(outgoing=True, pattern="gbot(.*)")
@Infinix(sudo=True, pattern="gbot(.*)")
async def _(event):
    await _gbot(event)
