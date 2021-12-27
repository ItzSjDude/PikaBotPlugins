"""Get Administrators of any Chat*
Syntax: {i}get_admin"""

from . import _gadmins


@Infinix(outgoing=True, pattern="get_ad?(m)in ?(.*)")
@Infinix(sudo=True, pattern="get_ad?(m)in ?(.*)")
async def _(event):
    await _gadmins(event)
