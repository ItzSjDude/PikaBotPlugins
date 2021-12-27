"""Globally bans User
{i}gban <userid/username/mention> <Reason>
"""
from . import gban


@Infinix(outgoing=True, pattern="gban(?: |$)(.*)")
@Infinix(sudo=True, pattern="gban(?: |$)(.*)")
async def _(event):
    await gban(event)
