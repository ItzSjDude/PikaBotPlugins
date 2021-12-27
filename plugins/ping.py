"""Ping Module for Infxbot
{i}infx"""

# Made by @Infinix for Infxbot
from . import _ping


@Infinix(outgoing=True, pattern="infx$")
async def _(event):
    await _ping(event)
