"""Prints F with given word
{i}text"""

from . import _ftext


@Infinix(outgoing=True, pattern="ftext ?(.*)")
@Infinix(sudo=True, pattern="ftext ?(.*)")
async def _(event):
    await _ftext(event)
