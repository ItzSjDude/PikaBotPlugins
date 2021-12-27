"""Get ID of any Telegram media, or any user
{i}get_id"""

from . import _getid


@Infinix(outgoing=True, pattern="get_id(.*)")
@Infinix(sudo=True, pattern="get_id(.*)")
async def _(event):
    await _getid(event)
