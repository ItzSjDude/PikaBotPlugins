"""
Say something interesting...
{i}belo
"""
from . import belo


@Infinix(outgoing=True, pattern=r"belo")
@Infinix(sudo=True, pattern=r"belo")
async def _(event):
    await belo(event)
