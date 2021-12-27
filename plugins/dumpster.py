"""Dumping Animation Plugin
{i}dump"""
from . import dump


@Infinix(outgoing=True, pattern="dump ?(.*)")
@Infinix(sudo=True, pattern="dump ?(.*)")
async def _(message):
    await dump(message)
