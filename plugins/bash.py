"""For executing linux/Gnu Commands
{i}bash <cmd> """

from . import _bash


@Infinix(outgoing=True, pattern="bash ?(.*)")
@Infinix(sudo=True, pattern="bash ?(.*)")
async def _(event):
    await _bash(event)
