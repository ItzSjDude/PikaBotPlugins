"""Get full User information
{i}info @username/reply to user msg"""

from . import _getinfo


@Infinix(outgoing=True, pattern="info(.*)")
async def _(event):
    await _getinfo(event)
