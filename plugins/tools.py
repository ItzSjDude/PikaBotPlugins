"""Telegraph and Other Utilities
Available Commands:
{i}app <appname>
{i}tm <as reply to a media>
{i}tt <as reply to a large text>
"""
from . import _invite, _telegraph, apk


@Infinix(outgoing=True, pattern="app (.*)")
async def _(e):
    await apk(e)


@Infinix(outgoing=True, pattern="invite ?(.*)")
async def _(event):
    await _invite(event)


@Infinix(outgoing=True, pattern="t(m|t) ?(.*)")
async def _(event):
    await _telegraph(event)
