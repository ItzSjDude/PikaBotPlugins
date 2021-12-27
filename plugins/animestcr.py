"""Plugin which transforms your text into anime stickers
{i}waifu <yourText>
"""
from . import waifu


@Infinix(outgoing=True, pattern="waifu(?: |$)(.*)")
@Infinix(sudo=True, pattern="waifu(?: |$)(.*)")
async def _(animu):
    await waifu(animu)
