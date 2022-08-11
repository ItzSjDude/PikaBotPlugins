"""Alive Plugin for Infxbot
{i}alive
"""
# Made by @Infinix. All Rights Reserved

from . import _alive


@Infinix(outgoing=True, pattern=r"alive$")
@Infinix(sudo=True, pattern=r"alive$")
async def _(client, event):
    await _alive(event)
