"""Alive Plugin for Pikabot
{i}alive
"""
# Made by @Infinix. All Rights Reserved

from . import _alive


@Infinix(outgoing=True, pattern=r"alive$")
@Infinix(sudo=True, pattern=r"alive$")
async def _(event):
    await _alive(event)
