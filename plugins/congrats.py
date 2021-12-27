"""Congrats Module
{i}congo"""

from . import _congo


@Infinix(outgoing=True, pattern="congo")
@Infinix(sudo=True, pattern="congo")
async def _(event):
    await _congo(event)
