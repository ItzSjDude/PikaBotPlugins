"""Quickly make a decision
{i}decide"""

from . import decide


@Infinix(outgoing=True, pattern="decide")
@Infinix(sudo=True, pattern="decide")
async def _(event):
    await decide(event)
