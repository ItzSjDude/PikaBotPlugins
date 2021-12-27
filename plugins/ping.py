"""Ping Module for Pikabot
{i}infx"""

# Made by @ItzSjDude for Pikabot
from . import _ping


@ItzSjDude(outgoing=True, pattern="infx$")
async def _(event):
    await _ping(event)
