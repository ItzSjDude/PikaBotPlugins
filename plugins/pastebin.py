"""**pastebin like site**\n
{i}paste <reply to file/msg>"""

from . import _deldog


@Infinix(outgoing=True, pattern="paste ?(.*)")
async def _(event):
    await _deldog(event)
