"""Ping Module for Pikabot
{i}infx"""

# Made by @Infinix for Pikabot
from . import _ping


@Infinix(outgoing=True, pattern="infx$")
async def _(event):
    await _ping(event)
