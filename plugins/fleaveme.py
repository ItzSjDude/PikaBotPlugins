# Credit: @r4v4n4
"""fake Leave
{i}fleave"""

from . import _fleave


@Infinix(outgoing=True, pattern=r"fleave")
@Infinix(sudo=True, pattern=r"fleave")
async def _(event):
    await _fleave(event)
